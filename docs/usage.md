# Reddit client usage

The `@crawlora-org/reddit` and `crawlora-reddit` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Reddit locally; Crawlora is independent from and not endorsed by Reddit or its owners.

The package tracks the public API contract revision `sha256:441a9c4645a94738c644f66d38610950951f585a268d92be35900149133ce821` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 12 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `reddit` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `comments` / `comments` | `GET /reddit/comments/{id}` | `id` (path, required), `sort` (query, optional; values: `confidence`, `top`, `new`, `controversial`, `old`, `qa`), `limit` (query, optional), `depth` (query, optional), `include_metrics` (query, optional) | Get Reddit post comments |
| `domainPosts` / `domain_posts` | `GET /reddit/domain/{domain}/posts` | `domain` (path, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit domain posts |
| `leads` / `leads` | `GET /reddit/leads` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `min_score` (query, optional), `classifier` (query, optional; values: `auto`, `heuristic`, `llm`) | Find Reddit buying-intent leads |
| `post` / `post` | `GET /reddit/post/{id}` | `id` (path, required), `include_metrics` (query, optional) | Get Reddit post |
| `search` / `search` | `GET /reddit/search` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | Search Reddit posts |
| `subredditAbout` / `subreddit_about` | `GET /reddit/subreddit/{subreddit}/about` | `subreddit` (path, required), `limit` (query, optional) | Get Reddit subreddit metadata |
| `subredditComments` / `subreddit_comments` | `GET /reddit/subreddit/{subreddit}/comments` | `subreddit` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit subreddit comments |
| `subredditPosts` / `subreddit_posts` | `GET /reddit/subreddit/{subreddit}/posts` | `subreddit` (path, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit subreddit posts |
| `subredditsPosts` / `subreddits_posts` | `GET /reddit/subreddits/posts` | `subreddits` (query, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit multi-subreddit posts |
| `trends` / `trends` | `GET /reddit/trends` | `sort` (query, optional; values: `hot`, `new`, `rising`, `top`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit trends |
| `userComments` / `user_comments` | `GET /reddit/user/{username}/comments` | `username` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit user comments |
| `userPosts` / `user_posts` | `GET /reddit/user/{username}/posts` | `username` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit user posts |

## Client forms

- JavaScript: import `RedditClient` (also exported as `Client`) from `@crawlora-org/reddit`; use `new RedditClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `RedditClient` (also exported as `Client`) from `crawlora_reddit`; use `with RedditClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncRedditClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
