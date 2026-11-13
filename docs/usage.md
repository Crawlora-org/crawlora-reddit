# Reddit API endpoint reference and client usage

This reference lists all 39 public Reddit API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/reddit`, `crawlora-reddit`, and `crawlora-reddit` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Reddit locally; Crawlora is independent from and not endorsed by Reddit or its owners.

The package tracks the public API contract revision `sha256:34005a8045ab32c913cc47a26b3bc48fb73f290882bf61a0abd2afa55d96d8d0` bundled with release `0.3.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

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
| `archiveCommentsIds` | `archive_comments_ids` | `reddit.archive_comments_ids` | `GET /reddit/archive/comments/ids` | `ids` (query, required) | Look up archived Reddit comments by ids |
| `archiveCommentsSearch` | `archive_comments_search` | `reddit.archive_comments_search` | `GET /reddit/archive/comments/search` | `author` (query, optional), `subreddit` (query, optional), `query` (query, optional), `link_id` (query, optional), `parent_id` (query, optional), `created_after` (query, optional), `created_before` (query, optional), `sort` (query, optional; values: `asc`, `desc`), `limit` (query, optional) | Search archived Reddit comments |
| `archiveCommentsTree` | `archive_comments_tree` | `reddit.archive_comments_tree` | `GET /reddit/archive/comments/{id}/tree` | `id` (path, required), `parent_id` (query, optional), `limit` (query, optional), `start_breadth` (query, optional), `start_depth` (query, optional) | Get an archived Reddit comment tree |
| `archivePostsIds` | `archive_posts_ids` | `reddit.archive_posts_ids` | `GET /reddit/archive/posts/ids` | `ids` (query, required) | Look up archived Reddit posts by ids |
| `archivePostsSearch` | `archive_posts_search` | `reddit.archive_posts_search` | `GET /reddit/archive/posts/search` | `query` (query, optional), `author` (query, optional), `subreddit` (query, optional), `url` (query, optional), `url_exact` (query, optional), `created_after` (query, optional), `created_before` (query, optional), `sort` (query, optional; values: `asc`, `desc`), `limit` (query, optional) | Search archived Reddit posts |
| `archiveSubredditsSearch` | `archive_subreddits_search` | `reddit.archive_subreddits_search` | `GET /reddit/archive/subreddits/search` | `query` (query, required), `min_subscribers` (query, optional), `max_subscribers` (query, optional), `over_18` (query, optional), `sort_by` (query, optional; values: `created_utc`, `subscribers`, `subreddit`), `sort` (query, optional; values: `asc`, `desc`), `limit` (query, optional) | Search Reddit's archived subreddit directory |
| `archiveTimeSeries` | `archive_time_series` | `reddit.archive_time_series` | `GET /reddit/archive/time-series` | `metric` (query, required; values: `posts_count`, `comments_count`, `posts_score_sum`, `comments_score_sum`, `posts_retrieval_delay_seconds_sum`, `comments_retrieval_delay_seconds_sum`, `subreddit_subscribers`), `subreddit` (query, optional), `precision` (query, required; values: `year`, `quarter`, `month`, `week`, `day`, `hour`, `minute`), `created_after` (query, required), `created_before` (query, required) | Get historical Reddit archive time series |
| `comment` | `comment` | `reddit.comment` | `GET /reddit/comment/{id}` | `id` (path, required) | Get a Reddit comment |
| `commentAwards` | `comment_awards` | `reddit.comment_awards` | `GET /reddit/comment/{id}/awards` | `id` (path, required) | Get Reddit comment awards |
| `comments` | `comments` | `reddit.comments` | `GET /reddit/comments/{id}` | `id` (path, required), `sort` (query, optional; values: `confidence`, `top`, `new`, `controversial`, `old`, `qa`), `limit` (query, optional), `depth` (query, optional) | Get Reddit post comments |
| `domainPosts` | `domain_posts` | `reddit.domain_posts` | `GET /reddit/domain/{domain}/posts` | `domain` (path, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit domain posts |
| `leads` | `leads` | `reddit.leads` | `GET /reddit/leads` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `min_score` (query, optional), `classifier` (query, optional; values: `auto`, `heuristic`, `llm`) | Find Reddit buying-intent leads |
| `popular` | `popular` | `reddit.popular` | `GET /reddit/popular` | `sort` (query, optional; values: `hot`, `top`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit popular posts |
| `post` | `post` | `reddit.post` | `GET /reddit/post/{id}` | `id` (path, required) | Get Reddit post |
| `postAwards` | `post_awards` | `reddit.post_awards` | `GET /reddit/post/{id}/awards` | `id` (path, required) | Get Reddit post awards |
| `postsByIds` | `posts_by_ids` | `reddit.posts_by_ids` | `GET /reddit/posts/ids` | `ids` (query, required) | Get Reddit posts by ids |
| `search` | `search` | `reddit.search` | `GET /reddit/search` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | Search Reddit posts |
| `searchComments` | `search_comments` | `reddit.search_comments` | `GET /reddit/search/comments` | `q` (query, required), `subreddit` (query, optional), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | Search Reddit comments |
| `searchPeople` | `search_people` | `reddit.search_people` | `GET /reddit/search/people` | `q` (query, required), `sort` (query, optional; values: `relevance`, `hot`, `new`, `top`, `comments`), `limit` (query, optional), `after` (query, optional) | Search Reddit people |
| `subredditAbout` | `subreddit_about` | `reddit.subreddit_about` | `GET /reddit/subreddit/{subreddit}/about` | `subreddit` (path, required), `limit` (query, optional) | Get Reddit subreddit metadata |
| `subredditComments` | `subreddit_comments` | `reddit.subreddit_comments` | `GET /reddit/subreddit/{subreddit}/comments` | `subreddit` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit subreddit comments |
| `subredditFlairs` | `subreddit_flairs` | `reddit.subreddit_flairs` | `GET /reddit/subreddit/{subreddit}/flairs` | `subreddit` (path, required) | List Reddit community post flairs |
| `subredditHighlights` | `subreddit_highlights` | `reddit.subreddit_highlights` | `GET /reddit/subreddit/{subreddit}/highlights` | `subreddit` (path, required) | List Reddit community highlights |
| `subredditLeaderboardCategories` | `subreddit_leaderboard_categories` | `reddit.subreddit_leaderboard_categories` | `GET /reddit/subreddit/{subreddit}/leaderboard/categories` | `subreddit` (path, required) | List Reddit community leaderboard categories |
| `subredditPosts` | `subreddit_posts` | `reddit.subreddit_posts` | `GET /reddit/subreddit/{subreddit}/posts` | `subreddit` (path, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`, `controversial`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit subreddit posts |
| `subredditRules` | `subreddit_rules` | `reddit.subreddit_rules` | `GET /reddit/subreddit/{subreddit}/rules` | `subreddit` (path, required) | Get Reddit community rules |
| `subredditsDiscover` | `subreddits_discover` | `reddit.subreddits_discover` | `GET /reddit/subreddits/discover` | `feed` (query, optional; values: `popular`, `new`, `default`), `limit` (query, optional), `after` (query, optional) | List Reddit community discovery feeds |
| `subredditsPosts` | `subreddits_posts` | `reddit.subreddits_posts` | `GET /reddit/subreddits/posts` | `subreddits` (query, required), `sort` (query, optional; values: `hot`, `new`, `top`, `rising`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit multi-subreddit posts |
| `subredditsSearch` | `subreddits_search` | `reddit.subreddits_search` | `GET /reddit/subreddits/search` | `q` (query, required), `limit` (query, optional), `after` (query, optional) | Search Reddit communities |
| `subredditsSuggest` | `subreddits_suggest` | `reddit.subreddits_suggest` | `GET /reddit/subreddits/suggest` | `q` (query, required) | Suggest Reddit communities |
| `subredditUserFlairs` | `subreddit_user_flairs` | `reddit.subreddit_user_flairs` | `GET /reddit/subreddit/{subreddit}/user-flairs` | `subreddit` (path, required) | List Reddit community user flairs |
| `subredditWiki` | `subreddit_wiki` | `reddit.subreddit_wiki` | `GET /reddit/subreddit/{subreddit}/wiki` | `subreddit` (path, required), `page` (query, optional) | Get Reddit community wiki |
| `topics` | `topics` | `reddit.topics` | `GET /reddit/topics` | `limit` (query, optional), `after` (query, optional) | List Reddit taxonomy topics |
| `topicsBroad` | `topics_broad` | `reddit.topics_broad` | `GET /reddit/topics/broad` | — | List Reddit broad topics |
| `topicsSearch` | `topics_search` | `reddit.topics_search` | `GET /reddit/topics/search` | `q` (query, required) | Search Reddit topics |
| `trends` | `trends` | `reddit.trends` | `GET /reddit/trends` | `sort` (query, optional; values: `hot`, `new`, `rising`, `top`), `time` (query, optional; values: `hour`, `day`, `week`, `month`, `year`, `all`), `limit` (query, optional), `after` (query, optional) | List Reddit trends |
| `userComments` | `user_comments` | `reddit.user_comments` | `GET /reddit/user/{username}/comments` | `username` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit user comments |
| `userPosts` | `user_posts` | `reddit.user_posts` | `GET /reddit/user/{username}/posts` | `username` (path, required), `limit` (query, optional), `after` (query, optional) | List Reddit user posts |
| `userProfile` | `user_profile` | `reddit.user_profile` | `GET /reddit/user/{username}/profile` | `username` (path, required) | Get a Reddit user profile |

## Client forms

- JavaScript: import `RedditClient` (also exported as `Client`) from `@crawlora-org/reddit`; use `new RedditClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `RedditClient` (also exported as `Client`) from `crawlora_reddit`; use `with RedditClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncRedditClient`, used with `async with` and `await`.
- Rust: add `crawlora-reddit` with Cargo; import `Client` and the generated operation parameter struct, then call `client.reddit.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-reddit/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
