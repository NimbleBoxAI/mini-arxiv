import os
import json
import pickle
import numpy as np
import fastapi as fa
from time import time
from uuid import uuid4
from pydantic import BaseModel
from typing import Dict, Optional
from rapidfuzz import fuzz, process

from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class MiniArxiv():
  def __init__(self, db):
    self.db = db
    with open(db, "rb") as f:
      self.data = pickle.load(f)

    self.prepare_data()

  def prepare_data(self):
    # method to prepare the data and create multiple indexes that can be queried
    # we don't want a full SQL, but this is the next best thing
    
    author_wise_papers = {} # {author: [paper#1_id, paper#2_id]}
    title_wise_papers = {} # {paper_title: paper_id}
    for _id in self.data:
      x = self.data[_id] # get the actual object
      for auth in x["authors"]:
        author_wise_papers.setdefault(auth, [])
        author_wise_papers[auth].append(_id)
      title_wise_papers[x["title"].lower().strip()] = _id

    self.author_wise_papers = author_wise_papers
    self.title_wise_papers = title_wise_papers
    self.titles_list = np.array(list(title_wise_papers.keys())) # convert to array for faster indexing
    self.sorted_ids = sorted(list(self.data.keys()))[::-1] # reverse the array

    # we are using tf-idf ans fuzzy matching with KNN
    # from: https://gist.github.com/audhiaprilliant/a86a4488d5a029cfae27bfa28efc8b7b
    self.vectorizer = TfidfVectorizer(ngram_range = (1, 4))
    X = self.vectorizer.fit_transform(self.titles_list)
    self.nbrs = NearestNeighbors(n_neighbors = 1, metric = 'cosine').fit(X)


  def get_latest_papers(self, n_return = 10):
    matches_data = [self.data[x] for x in self.sorted_ids[:n_return]]
    return matches_data


  def get_papers_with_fuzzy_string_match(self, raw_str, n_return = 10):
    raw_str = raw_str.lower().strip()

    # perform tf-idf nn
    input_vec = self.vectorizer.transform([raw_str])
    distances, indices = self.nbrs.kneighbors(input_vec, n_neighbors = n_return)
    papers = self.titles_list[indices[0]]
    
    # fuzyy nn
    matches = process.extract(raw_str, papers, scorer=fuzz.QRatio, limit=n_return)
    
    # get final data
    matches_data = [
      self.data[self.title_wise_papers[x[0]]]
      for x in matches
    ] # correct text is x[0], get id from self.title_wise_papers, get data using id
    return matches_data

###### global constants ######
app = fa.FastAPI()
miniarxiv = MiniArxiv("./mini-arxiv.p")

###### Models ######
# https://fastapi.tiangolo.com/tutorial/response-model/

class MiniArxivBaseResponse(BaseModel):
  # model for asking things to NALA API
  user_string: Optional[str] = None
  options: Optional[list] = None
  n_return: Optional[int] = 10


@app.get("/papers", response_model=MiniArxivBaseResponse)
async def get_papers_with_fuzzy_string_match(request: fa.Request, server_req: MiniArxivBaseResponse):
  """API for getting latest papers"""
  papers = miniarxiv.get_latest_papers(server_req.n_return)
  return MiniArxivBaseResponse(options = papers)


@app.get("/papermatch", response_model=MiniArxivBaseResponse)
async def get_papers_with_fuzzy_string_match(request: fa.Request, server_req: MiniArxivBaseResponse):
  """API for getting searches for papers"""
  papers = miniarxiv.get_papers_with_fuzzy_string_match(server_req.user_string, server_req.n_return)
  return MiniArxivBaseResponse(options = papers)

