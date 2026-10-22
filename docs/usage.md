# Reddit API endpoint reference and client usage

This reference lists all 12 public Reddit API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/reddit`, `crawlora-reddit`, and `crawlora-reddit` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Reddit locally; Crawlora is independent from and not endorsed by Reddit or its owners.

The package tracks the public API contract revision `sha256:11f2ddb0c3c61724bf46ac537a74910bf241c72ada328691f88369a8aac9e4e1` bundled with release `0.2.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `reddit`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `comments` | `comments` | `reddit.comments` | `GET /reddit/comments/{id}` | `id` (path, required), `sort` (query, optional; values: `confidence`, `top`, `new`, `controversial`, `old`, `qa`), `limit` (query, optional), `depth` (query, optional), `include_metrics` (query, optional) | Get Reddit post comments |
| `domainPosts` | `domain_posts` | `reddit.domain_posts` | `GET /reddit/domain/{domain}/posts` | `domain` (path, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit domain posts |
| `leads` | `leads` | `reddit.leads` | `GET /reddit/leads` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `min_score` (query, optional), `classifier` (query, optional; values: `auto`, `heuristic`, `llm`) | Find Reddit buying-intent leads |
| `post` | `post` | `reddit.post` | `GET /reddit/post/{id}` | `id` (path, required), `include_metrics` (query, optional) | Get Reddit post |
| `search` | `search` | `reddit.search` | `GET /reddit/search` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | Search Reddit posts |
| `subredditAbout` | `subreddit_about` | `reddit.subreddit_about` | `GET /reddit/subreddit/{subreddit}/about` | `subreddit` (path, required), `limit` (query, optional) | Get Reddit subreddit metadata |
| `subredditComments` | `subreddit_comments` | `reddit.subreddit_comments` | `GET /reddit/subreddit/{subreddit}/comments` | `subreddit` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit subreddit comments |
| `subredditPosts` | `subreddit_posts` | `reddit.subreddit_posts` | `GET /reddit/subreddit/{subreddit}/posts` | `subreddit` (path, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit subreddit posts |
| `subredditsPosts` | `subreddits_posts` | `reddit.subreddits_posts` | `GET /reddit/subreddits/posts` | `subreddits` (query, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit multi-subreddit posts |
| `trends` | `trends` | `reddit.trends` | `GET /reddit/trends` | `sort` (query, optional; values: `hot`, `new`, `rising`, `top`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit trends |
| `userComments` | `user_comments` | `reddit.user_comments` | `GET /reddit/user/{username}/comments` | `username` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit user comments |
| `userPosts` | `user_posts` | `reddit.user_posts` | `GET /reddit/user/{username}/posts` | `username` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit user posts |

## Client forms

- JavaScript: import `RedditClient` (also exported as `Client`) from `@crawlora-org/reddit`; use `new RedditClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `RedditClient` (also exported as `Client`) from `crawlora_reddit`; use `with RedditClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncRedditClient`, used with `async with` and `await`.
- Rust: add `crawlora-reddit` with Cargo; import `Client` and the generated operation parameter struct, then call `client.reddit.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-reddit/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
