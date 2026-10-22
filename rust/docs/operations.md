# Crawlora Reddit Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `12`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reddit | `reddit.comments` | `reddit-comments` | `GET /reddit/comments/{id}` | `id` (path String required)<br>`sort` (query String enum{confidence, top, new, controversial, old, qa})<br>`limit` (query i64)<br>`depth` (query i64)<br>`include_metrics` (query bool) | `ApiKeyAuth` | `RedditCommentsResponse` |  |
| reddit | `reddit.domain_posts` | `reddit-domain-posts` | `GET /reddit/domain/{domain}/posts` | `domain` (path String required)<br>`sort` (query String enum{hot, new, top, rising})<br>`time` (query String enum{hour, day, week, month, year, all})<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditDomainPostsResponse` |  |
| reddit | `reddit.leads` | `reddit-leads` | `GET /reddit/leads` | `q` (query String required)<br>`subreddit` (query String)<br>`sort` (query String enum{relevance, hot, new, top, comments})<br>`time` (query String enum{hour, day, week, month, year, all})<br>`limit` (query i64)<br>`min_score` (query i64)<br>`classifier` (query String enum{auto, heuristic, llm}) | `ApiKeyAuth` | `RedditLeadsResponse` |  |
| reddit | `reddit.post` | `reddit-post` | `GET /reddit/post/{id}` | `id` (path String required)<br>`include_metrics` (query bool) | `ApiKeyAuth` | `RedditPostResponse` |  |
| reddit | `reddit.search` | `reddit-search` | `GET /reddit/search` | `q` (query String required)<br>`subreddit` (query String)<br>`sort` (query String enum{relevance, hot, new, top, comments})<br>`time` (query String enum{hour, day, week, month, year, all})<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditSearchResponse` |  |
| reddit | `reddit.subreddit_about` | `reddit-subreddit-about` | `GET /reddit/subreddit/{subreddit}/about` | `subreddit` (path String required)<br>`limit` (query i64) | `ApiKeyAuth` | `RedditSubredditAboutResponse` |  |
| reddit | `reddit.subreddit_comments` | `reddit-subreddit-comments` | `GET /reddit/subreddit/{subreddit}/comments` | `subreddit` (path String required)<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditSubredditCommentsResponse` |  |
| reddit | `reddit.subreddit_posts` | `reddit-subreddit-posts` | `GET /reddit/subreddit/{subreddit}/posts` | `subreddit` (path String required)<br>`sort` (query String enum{hot, new, top, rising})<br>`time` (query String enum{hour, day, week, month, year, all})<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditSubredditPostsResponse` |  |
| reddit | `reddit.subreddits_posts` | `reddit-subreddits-posts` | `GET /reddit/subreddits/posts` | `subreddits` (query String required)<br>`sort` (query String enum{hot, new, top, rising})<br>`time` (query String enum{hour, day, week, month, year, all})<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditSubredditsPostsResponse` |  |
| reddit | `reddit.trends` | `reddit-trends` | `GET /reddit/trends` | `sort` (query String enum{hot, new, rising, top})<br>`time` (query String enum{hour, day, week, month, year, all})<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditTrendsResponse` |  |
| reddit | `reddit.user_comments` | `reddit-user-comments` | `GET /reddit/user/{username}/comments` | `username` (path String required)<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditUserCommentsResponse` |  |
| reddit | `reddit.user_posts` | `reddit-user-posts` | `GET /reddit/user/{username}/posts` | `username` (path String required)<br>`limit` (query i64)<br>`after` (query String) | `ApiKeyAuth` | `RedditUserPostsResponse` |  |
