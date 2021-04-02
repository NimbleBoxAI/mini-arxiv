# mini-arxiv

Usage:

```
uvicorn main:app --reload --port=8123 [debug]
uvicorn main:app --port=8123 [prod]

# to get response
curl --location --request GET 'http://127.0.0.1:8123/papers' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "n_return": 5
}'

curl --location --request GET 'http://127.0.0.1:8123/papermatch' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "user_string": "BERT",
    "n_return": 5
}'
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

#### `/categorymatch`
```
Returns a json-able dictionary for papers in a certain category.
```

**NOTE**: The input will be the complete category string as given in the `./taxonomy` file. Eg. send `{"user_string": "Artificial Intelligence"}` and not `cs.AI`. Provide the category as an option to the user.

## Files

There are two files:
- `main.py`: The file that has the above mentioned APIs
- `prepare.py`: prepares the dataset, expected to be run as a CRON job sometime post midnight PST, that's when the papers hit arxiv servers.
