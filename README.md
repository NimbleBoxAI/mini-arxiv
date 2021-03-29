# mini-arxiv

#### arxiv-sanity for NBX Dashboard.

[Arxiv-Sanity](https://github.com/karpathy/arxiv-sanity-preserver) can show recent papers, this is for NBX dashboard and implments the following `apis`:

#### `get_latest_papers(n_return = 10)`
```
Get a json-able dictionary of the latest 10 pages not of any particular author category.

Args:
    n_return (int): number of latest papers to return.
```

#### `get_papers_with_fuzzy_string_match(user_query, n_return = 10)`
```
Performs fuzzy matching to get paper string from the user query. Sorted by fuzzy scores.

Args:
    user_query (str): String from the user
    n_return (int): number of latest papers to return.
```

#### `get_papers_by_authors(author, n_return = 10)`
```
Returns a json-able dictionary for the author searched.

Args:
    author (str): string shared by the user
    n_return (int): number of latest papers to return.
```

#### `get_paper_by_category(category, n_return = 10)`
```
Returns a json-able dictionary for papers in a certain category.

Args:
    category (str): paper category either arxiv code or complete string
        of the category
    n_return (int): number of latest papers to return.
```

## Files

There are two files:
- `miniarxiv.py`: The file that has the above mentioned APIs
- `prepare.py`: prepares the dataset, expected to be run as a CRON job
