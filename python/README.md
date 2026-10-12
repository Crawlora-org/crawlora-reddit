# crawlora-reddit — Reddit API client for Python

Python client for Crawlora's hosted Reddit API. It exposes 12 API endpoints covering search, post and comment details, subreddit feeds, user history, domain listings, trends, and leads. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-python-homepage); the package does not run a browser or scrape
Reddit locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Reddit or its owners.

## Install

```sh
python -m pip install crawlora-reddit
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_reddit import RedditClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with RedditClient(api_key=api_key) as client:
    result_1 = client.search(q='open source')
    print(result_1)
    result_2 = client.subreddit_posts(subreddit='technology')
    print(result_2)
```

The package also exports `Client` as an alias for `RedditClient`. Operation
methods are available directly in snake_case and through the `reddit`
group. The async package client is `AsyncRedditClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-reddit/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_reddit import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(q='open source')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-reddit/blob/main/examples/python.py) for a complete usage example.

## Supported Reddit API endpoints

This package exposes every route below through direct snake_case methods and the `reddit` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/reddit/comments/{id}` | `reddit-comments` | Get Reddit post comments |
| `GET` | `/reddit/domain/{domain}/posts` | `reddit-domain-posts` | List Reddit domain posts |
| `GET` | `/reddit/leads` | `reddit-leads` | Find Reddit buying-intent leads |
| `GET` | `/reddit/post/{id}` | `reddit-post` | Get Reddit post |
| `GET` | `/reddit/search` | `reddit-search` | Search Reddit posts |
| `GET` | `/reddit/subreddit/{subreddit}/about` | `reddit-subreddit-about` | Get Reddit subreddit metadata |
| `GET` | `/reddit/subreddit/{subreddit}/comments` | `reddit-subreddit-comments` | List Reddit subreddit comments |
| `GET` | `/reddit/subreddit/{subreddit}/posts` | `reddit-subreddit-posts` | List Reddit subreddit posts |
| `GET` | `/reddit/subreddits/posts` | `reddit-subreddits-posts` | List Reddit multi-subreddit posts |
| `GET` | `/reddit/trends` | `reddit-trends` | List Reddit trends |
| `GET` | `/reddit/user/{username}/comments` | `reddit-user-comments` | List Reddit user comments |
| `GET` | `/reddit/user/{username}/posts` | `reddit-user-posts` | List Reddit user posts |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
