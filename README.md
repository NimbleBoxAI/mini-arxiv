# mini-arxiv

Usage:

```
uvicorn main:app --reload --port=8123 [debug]
uvicorn main:app --port=8123 [prod]

# to get response
curl -X GET http://127.0.0.1:8123/papers -d "{\"n_return\": 3}" 
```

#### arxiv-sanity for NBX Dashboard.

[Arxiv-Sanity](https://github.com/karpathy/arxiv-sanity-preserver) can show recent papers, this is for NBX dashboard and implments the following `apis`:

#### `/papers`
```
API for getting latest papers
```

#### `/papermatch`
```
Performs tf-ids + fuzzy NN matching to get papers from the user query.
```

#### [WIP] `get_papers_by_authors(author, n_return = 10)`
```
Returns a json-able dictionary for the author searched.

Args:
    author (str): string shared by the user
    n_return (int): number of latest papers to return.
```

#### [WIP] `get_paper_by_category(category, n_return = 10)`
```
Returns a json-able dictionary for papers in a certain category.

Args:
    category (str): paper category either arxiv code or complete string
        of the category
    n_return (int): number of latest papers to return.
```

## Files

There are two files:
- `main.py`: The file that has the above mentioned APIs
- `prepare.py`: prepares the dataset, expected to be run as a CRON job
