# code for loading the arxiv pages for nimblebox dashboard
#
# implements the following function:
# get_latest_papers(n_papers)
# get_papers_with_fuzzy_string_match(user_query)
# get_papers_by_authors(author)
# get_paper_by_category(category)
#
# @yashbonde - 29th March, 2021

def get_latest_papers(n_papers):
  """
  Get a json-able dictionary of the latest 10 pages not of any particular author category.
  Args:
    n_return (int): number of latest papers to return.
  """
  pass


def get_papers_with_fuzzy_string_match(user_query):
  """
  Performs fuzzy matching to get paper string from the user query. Sorted by fuzzy scores.
  Args:
    user_query (str): String from the user
    n_return (int): number of latest papers to return.
  """
  pass

def get_papers_by_authors(author):
  """
  Returns a json-able dictionary for the author searched.
  Args:
    author (str): string shared by the user
    n_return (int): number of latest papers to return.
  """
  pass

def get_paper_by_category(category):
  """
  Returns a json-able dictionary for papers in a certain category.
  Args:
    category (str): paper category either arxiv code or complete string
      of the category
    n_return (int): number of latest papers to return.
  """
  pass


