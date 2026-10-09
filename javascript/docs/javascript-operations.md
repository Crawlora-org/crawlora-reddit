# Crawlora Reddit JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `12`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reddit | `reddit.comments` | `reddit-comments` | `GET /reddit/comments/{id}` | `id` (path string required)<br>`sort` (query "confidence" \| "top" \| "new" \| "controversial" \| "old" \| "qa")<br>`limit` (query number)<br>`depth` (query number)<br>`include_metrics` (query boolean) | `ApiKeyAuth` | `RedditCommentsResponse` |  |
| reddit | `reddit.domainPosts` | `reddit-domain-posts` | `GET /reddit/domain/{domain}/posts` | `domain` (path string required)<br>`sort` (query "hot" \| "new" \| "top" \| "rising")<br>`time` (query "hour" \| "day" \| "week" \| "month" \| "year" \| "all")<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditDomainPostsResponse` |  |
| reddit | `reddit.leads` | `reddit-leads` | `GET /reddit/leads` | `q` (query string required)<br>`subreddit` (query string)<br>`sort` (query "relevance" \| "hot" \| "new" \| "top" \| "comments")<br>`time` (query "hour" \| "day" \| "week" \| "month" \| "year" \| "all")<br>`limit` (query number)<br>`min_score` (query number)<br>`classifier` (query "auto" \| "heuristic" \| "llm") | `ApiKeyAuth` | `RedditLeadsResponse` |  |
| reddit | `reddit.post` | `reddit-post` | `GET /reddit/post/{id}` | `id` (path string required)<br>`include_metrics` (query boolean) | `ApiKeyAuth` | `RedditPostResponse` |  |
| reddit | `reddit.search` | `reddit-search` | `GET /reddit/search` | `q` (query string required)<br>`subreddit` (query string)<br>`sort` (query "relevance" \| "hot" \| "new" \| "top" \| "comments")<br>`time` (query "hour" \| "day" \| "week" \| "month" \| "year" \| "all")<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditSearchResponse` |  |
| reddit | `reddit.subredditAbout` | `reddit-subreddit-about` | `GET /reddit/subreddit/{subreddit}/about` | `subreddit` (path string required)<br>`limit` (query number) | `ApiKeyAuth` | `RedditSubredditAboutResponse` |  |
| reddit | `reddit.subredditComments` | `reddit-subreddit-comments` | `GET /reddit/subreddit/{subreddit}/comments` | `subreddit` (path string required)<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditSubredditCommentsResponse` |  |
| reddit | `reddit.subredditPosts` | `reddit-subreddit-posts` | `GET /reddit/subreddit/{subreddit}/posts` | `subreddit` (path string required)<br>`sort` (query "hot" \| "new" \| "top" \| "rising")<br>`time` (query "hour" \| "day" \| "week" \| "month" \| "year" \| "all")<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditSubredditPostsResponse` |  |
| reddit | `reddit.subredditsPosts` | `reddit-subreddits-posts` | `GET /reddit/subreddits/posts` | `subreddits` (query string required)<br>`sort` (query "hot" \| "new" \| "top" \| "rising")<br>`time` (query "hour" \| "day" \| "week" \| "month" \| "year" \| "all")<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditSubredditsPostsResponse` |  |
| reddit | `reddit.trends` | `reddit-trends` | `GET /reddit/trends` | `sort` (query "hot" \| "new" \| "rising" \| "top")<br>`time` (query "hour" \| "day" \| "week" \| "month" \| "year" \| "all")<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditTrendsResponse` |  |
| reddit | `reddit.userComments` | `reddit-user-comments` | `GET /reddit/user/{username}/comments` | `username` (path string required)<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditUserCommentsResponse` |  |
| reddit | `reddit.userPosts` | `reddit-user-posts` | `GET /reddit/user/{username}/posts` | `username` (path string required)<br>`limit` (query number)<br>`after` (query string) | `ApiKeyAuth` | `RedditUserPostsResponse` |  |
