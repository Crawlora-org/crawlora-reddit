require "json"
require "net/http"
require "uri"

module Crawlora
  module Reddit
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"reddit-archive-comments-ids": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-comments-ids", "method": "GET", "params": [{"description": "Comma-separated Reddit comment ids (1-1,000); optional t1_ prefixes are accepted", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "c60n05h,abc123"}], "path": "/reddit/archive/comments/ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-archive-comments-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-comments-search", "method": "GET", "params": [{"description": "Public Reddit username filter", "in": "query", "name": "author", "type": "string"}, {"description": "Subreddit name filter", "in": "query", "name": "subreddit", "type": "string"}, {"description": "Full-text search within comment bodies; requires author, subreddit, link_id, or parent_id", "in": "query", "name": "query", "type": "string"}, {"description": "Reddit post id to scope comments", "in": "query", "name": "link_id", "type": "string"}, {"description": "Parent comment id; an explicitly empty value selects top-level comments", "in": "query", "name": "parent_id", "type": "string"}, {"description": "Creation-time lower bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_after", "type": "string"}, {"description": "Creation-time upper bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_before", "type": "string"}, {"default": "desc", "description": "Sort by creation time", "enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/archive/comments/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "author", "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "link_id", "type": "string"}, {"in": "query", "name": "parent_id", "type": "string"}, {"in": "query", "name": "created_after", "type": "string"}, {"in": "query", "name": "created_before", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-comments-tree": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-comments-tree", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "7cff0b"}, {"description": "Parent comment id; an explicitly empty value selects top-level comments", "in": "query", "name": "parent_id", "type": "string"}, {"description": "Maximum archive comment nodes to expand, defaults to 50 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Initial breadth, defaults to 2 and must be between 0 and 8", "in": "query", "name": "start_breadth", "type": "integer"}, {"description": "Initial depth, defaults to 3 and must be between 0 and 8", "in": "query", "name": "start_depth", "type": "integer"}], "path": "/reddit/archive/comments/{id}/tree", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "parent_id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "start_breadth", "type": "integer"}, {"in": "query", "name": "start_depth", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-posts-ids": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-posts-ids", "method": "GET", "params": [{"description": "Comma-separated Reddit post ids (1-1,000); optional t3_ prefixes are accepted", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "1wwa2ff,z1c9z"}], "path": "/reddit/archive/posts/ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-archive-posts-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-posts-search", "method": "GET", "params": [{"description": "Text search across archived post titles and selftext", "in": "query", "name": "query", "type": "string"}, {"description": "Public Reddit username filter", "in": "query", "name": "author", "type": "string"}, {"description": "Subreddit name filter", "in": "query", "name": "subreddit", "type": "string"}, {"description": "Linked URL prefix filter", "in": "query", "name": "url", "type": "string"}, {"description": "Require an exact URL match; requires url", "in": "query", "name": "url_exact", "type": "boolean"}, {"description": "Creation-time lower bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_after", "type": "string"}, {"description": "Creation-time upper bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_before", "type": "string"}, {"default": "desc", "description": "Sort by creation time", "enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/archive/posts/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "author", "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "url_exact", "type": "boolean"}, {"in": "query", "name": "created_after", "type": "string"}, {"in": "query", "name": "created_before", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-subreddits-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-subreddits-search", "method": "GET", "params": [{"description": "Subreddit name prefix, with or without r/", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Minimum archived subscriber count", "in": "query", "name": "min_subscribers", "type": "integer"}, {"description": "Maximum archived subscriber count", "in": "query", "name": "max_subscribers", "type": "integer"}, {"description": "Filter by archived NSFW status", "in": "query", "name": "over_18", "type": "boolean"}, {"default": "subscribers", "description": "Sort field", "enum": ["created_utc", "subscribers", "subreddit"], "in": "query", "name": "sort_by", "type": "string"}, {"default": "desc", "description": "Sort direction", "enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum subreddits, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/archive/subreddits/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "min_subscribers", "type": "integer"}, {"in": "query", "name": "max_subscribers", "type": "integer"}, {"in": "query", "name": "over_18", "type": "boolean"}, {"enum": ["created_utc", "subscribers", "subreddit"], "in": "query", "name": "sort_by", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-time-series": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-time-series", "method": "GET", "params": [{"description": "Archive metric", "enum": ["posts_count", "comments_count", "posts_score_sum", "comments_score_sum", "posts_retrieval_delay_seconds_sum", "comments_retrieval_delay_seconds_sum", "subreddit_subscribers"], "in": "query", "name": "metric", "required": true, "type": "string", "x-example": "posts_count"}, {"description": "Optional subreddit scope; required for subreddit_subscribers, and unsupported for retrieval-delay metrics", "in": "query", "name": "subreddit", "type": "string", "x-example": "OpenAI"}, {"description": "Time bucket precision", "enum": ["year", "quarter", "month", "week", "day", "hour", "minute"], "in": "query", "name": "precision", "required": true, "type": "string", "x-example": "year"}, {"description": "Absolute start time: epoch seconds/milliseconds or ISO 8601", "in": "query", "name": "created_after", "required": true, "type": "string", "x-example": "2024-01-01"}, {"description": "Absolute end time: epoch seconds/milliseconds or ISO 8601", "in": "query", "name": "created_before", "required": true, "type": "string", "x-example": "2025-01-01"}], "path": "/reddit/archive/time-series", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["posts_count", "comments_count", "posts_score_sum", "comments_score_sum", "posts_retrieval_delay_seconds_sum", "comments_retrieval_delay_seconds_sum", "subreddit_subscribers"], "in": "query", "name": "metric", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["year", "quarter", "month", "week", "day", "hour", "minute"], "in": "query", "name": "precision", "required": true, "type": "string"}, {"in": "query", "name": "created_after", "required": true, "type": "string"}, {"in": "query", "name": "created_before", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-comment": {"bodyParam": null, "bodyRequired": false, "id": "reddit-comment", "method": "GET", "params": [{"description": "Comment id with or without t1_, or a comment URL", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "p8402di"}], "path": "/reddit/comment/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-comment-awards": {"bodyParam": null, "bodyRequired": false, "id": "reddit-comment-awards", "method": "GET", "params": [{"description": "Comment id with or without t1_, or a comment URL", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "19shpw8bwhfnn"}], "path": "/reddit/comment/{id}/awards", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-comments", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1tka90t"}, {"default": "confidence", "description": "Comment order: confidence, top, new, controversial, old, or qa.", "enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum comments returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"default": 3, "description": "Maximum flat comment depth returned.", "in": "query", "name": "depth", "type": "integer"}], "path": "/reddit/comments/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "depth", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-domain-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-domain-posts", "method": "GET", "params": [{"description": "Domain hostname, without scheme or path", "in": "path", "name": "domain", "required": true, "type": "string", "x-example": "openai.com"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/domain/{domain}/posts", "pathParams": ["domain"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-leads": {"bodyParam": null, "bodyRequired": false, "id": "reddit-leads", "method": "GET", "params": [{"description": "What you offer, in plain language", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "crm for small teams"}, {"description": "Restrict the search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"default": "month", "description": "Time window: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum leads returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Minimum buying-intent score to return, 0-10, defaults to 4", "in": "query", "name": "min_score", "type": "integer"}, {"default": "auto", "description": "Classifier: auto uses the model when configured, heuristic skips it, llm requires it", "enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "path": "/reddit/leads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "min_score", "type": "integer"}, {"enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-popular": {"bodyParam": null, "bodyRequired": false, "id": "reddit-popular", "method": "GET", "params": [{"default": "hot", "description": "Sort order: hot or top", "enum": ["hot", "top"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/popular", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "top"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-post": {"bodyParam": null, "bodyRequired": false, "id": "reddit-post", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1v8hy3q"}], "path": "/reddit/post/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-post-awards": {"bodyParam": null, "bodyRequired": false, "id": "reddit-post-awards", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1v8hy3q"}], "path": "/reddit/post/{id}/awards", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-posts-by-ids": {"bodyParam": null, "bodyRequired": false, "id": "reddit-posts-by-ids", "method": "GET", "params": [{"description": "Comma-separated post ids, with or without the t3_ prefix (maximum 100)", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "1v8hy3q,1tka90t"}], "path": "/reddit/posts/ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-search", "method": "GET", "params": [{"description": "Search keywords", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "gpt"}, {"description": "Restrict search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top/comments sorts: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-search-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-search-comments", "method": "GET", "params": [{"description": "Search keywords", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang generics"}, {"description": "Restrict search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top/comments sorts: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Opaque app pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search/comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-search-people": {"bodyParam": null, "bodyRequired": false, "id": "reddit-search-people", "method": "GET", "params": [{"description": "Username or profile keyword", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "spez"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum people, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Opaque app pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search/people", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-about": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-about", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum sample posts inspected, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/subreddit/{subreddit}/about", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-comments", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/comments", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-flairs": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-flairs", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/flairs", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-highlights": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-highlights", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/highlights", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-leaderboard-categories": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-leaderboard-categories", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/leaderboard/categories", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-posts", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"default": "hot", "description": "Sort: hot, new, top, rising, or controversial", "enum": ["hot", "new", "top", "rising", "controversial"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/posts", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising", "controversial"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-rules": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-rules", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/rules", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-user-flairs": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-user-flairs", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "nba"}], "path": "/reddit/subreddit/{subreddit}/user-flairs", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-wiki": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-wiki", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}, {"description": "Wiki page path, defaults to index", "in": "query", "name": "page", "type": "string", "x-example": "index"}], "path": "/reddit/subreddit/{subreddit}/wiki", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-discover": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-discover", "method": "GET", "params": [{"default": "popular", "description": "Community feed: popular, new, or default", "enum": ["popular", "new", "default"], "in": "query", "name": "feed", "type": "string"}, {"description": "Maximum communities, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/discover", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["popular", "new", "default"], "in": "query", "name": "feed", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-posts", "method": "GET", "params": [{"description": "Comma-separated subreddit names, without r/, maximum 10", "in": "query", "name": "subreddits", "required": true, "type": "string", "x-example": "OpenAI,MachineLearning"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "subreddits", "required": true, "type": "string"}, {"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-search", "method": "GET", "params": [{"description": "Community name search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang"}, {"description": "Maximum communities, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-suggest": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-suggest", "method": "GET", "params": [{"description": "Community name or prefix", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddits/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-topics": {"bodyParam": null, "bodyRequired": false, "id": "reddit-topics", "method": "GET", "params": [{"description": "Maximum topics, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Opaque app pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/topics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-topics-broad": {"bodyParam": null, "bodyRequired": false, "id": "reddit-topics-broad", "method": "GET", "params": [], "path": "/reddit/topics/broad", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-topics-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-topics-search", "method": "GET", "params": [{"description": "Topic search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/topics/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-trends": {"bodyParam": null, "bodyRequired": false, "id": "reddit-trends", "method": "GET", "params": [{"default": "hot", "description": "Sort: hot, new, rising, or top", "enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/trends", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-user-comments", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/comments", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-user-posts", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/posts", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-profile": {"bodyParam": null, "bodyRequired": false, "id": "reddit-user-profile", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "spez"}], "path": "/reddit/user/{username}/profile", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["reddit-archive-comments-ids", "reddit-archive-comments-search", "reddit-archive-comments-tree", "reddit-archive-posts-ids", "reddit-archive-posts-search", "reddit-archive-subreddits-search", "reddit-archive-time-series", "reddit-comment", "reddit-comment-awards", "reddit-comments", "reddit-domain-posts", "reddit-leads", "reddit-popular", "reddit-post", "reddit-post-awards", "reddit-posts-by-ids", "reddit-search", "reddit-search-comments", "reddit-search-people", "reddit-subreddit-about", "reddit-subreddit-comments", "reddit-subreddit-flairs", "reddit-subreddit-highlights", "reddit-subreddit-leaderboard-categories", "reddit-subreddit-posts", "reddit-subreddit-rules", "reddit-subreddit-user-flairs", "reddit-subreddit-wiki", "reddit-subreddits-discover", "reddit-subreddits-posts", "reddit-subreddits-search", "reddit-subreddits-suggest", "reddit-topics", "reddit-topics-broad", "reddit-topics-search", "reddit-trends", "reddit-user-comments", "reddit-user-posts", "reddit-user-profile"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-reddit-ruby/0.3.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('archive_comments_ids') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-comments-ids', params, response_type: response_type)
      end
      define_method('archive_comments_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-comments-search', params, response_type: response_type)
      end
      define_method('archive_comments_tree') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-comments-tree', params, response_type: response_type)
      end
      define_method('archive_posts_ids') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-posts-ids', params, response_type: response_type)
      end
      define_method('archive_posts_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-posts-search', params, response_type: response_type)
      end
      define_method('archive_subreddits_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-subreddits-search', params, response_type: response_type)
      end
      define_method('archive_time_series') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-archive-time-series', params, response_type: response_type)
      end
      define_method('comment') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-comment', params, response_type: response_type)
      end
      define_method('comment_awards') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-comment-awards', params, response_type: response_type)
      end
      define_method('comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-comments', params, response_type: response_type)
      end
      define_method('domain_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-domain-posts', params, response_type: response_type)
      end
      define_method('leads') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-leads', params, response_type: response_type)
      end
      define_method('popular') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-popular', params, response_type: response_type)
      end
      define_method('post') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-post', params, response_type: response_type)
      end
      define_method('post_awards') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-post-awards', params, response_type: response_type)
      end
      define_method('posts_by_ids') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-posts-by-ids', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-search', params, response_type: response_type)
      end
      define_method('search_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-search-comments', params, response_type: response_type)
      end
      define_method('search_people') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-search-people', params, response_type: response_type)
      end
      define_method('subreddit_about') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-about', params, response_type: response_type)
      end
      define_method('subreddit_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-comments', params, response_type: response_type)
      end
      define_method('subreddit_flairs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-flairs', params, response_type: response_type)
      end
      define_method('subreddit_highlights') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-highlights', params, response_type: response_type)
      end
      define_method('subreddit_leaderboard_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-leaderboard-categories', params, response_type: response_type)
      end
      define_method('subreddit_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-posts', params, response_type: response_type)
      end
      define_method('subreddit_rules') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-rules', params, response_type: response_type)
      end
      define_method('subreddit_user_flairs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-user-flairs', params, response_type: response_type)
      end
      define_method('subreddit_wiki') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-wiki', params, response_type: response_type)
      end
      define_method('subreddits_discover') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddits-discover', params, response_type: response_type)
      end
      define_method('subreddits_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddits-posts', params, response_type: response_type)
      end
      define_method('subreddits_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddits-search', params, response_type: response_type)
      end
      define_method('subreddits_suggest') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddits-suggest', params, response_type: response_type)
      end
      define_method('topics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-topics', params, response_type: response_type)
      end
      define_method('topics_broad') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-topics-broad', params, response_type: response_type)
      end
      define_method('topics_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-topics-search', params, response_type: response_type)
      end
      define_method('trends') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-trends', params, response_type: response_type)
      end
      define_method('user_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-user-comments', params, response_type: response_type)
      end
      define_method('user_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-user-posts', params, response_type: response_type)
      end
      define_method('user_profile') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-user-profile', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
