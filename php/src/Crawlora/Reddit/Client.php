<?php

declare(strict_types=1);

namespace Crawlora\Reddit;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'reddit';
    public const VERSION = '0.3.0';
    public const OPERATION_COUNT = 39;
    public const OPERATION_IDS = ["reddit-archive-comments-ids", "reddit-archive-comments-search", "reddit-archive-comments-tree", "reddit-archive-posts-ids", "reddit-archive-posts-search", "reddit-archive-subreddits-search", "reddit-archive-time-series", "reddit-comment", "reddit-comment-awards", "reddit-comments", "reddit-domain-posts", "reddit-leads", "reddit-popular", "reddit-post", "reddit-post-awards", "reddit-posts-by-ids", "reddit-search", "reddit-search-comments", "reddit-search-people", "reddit-subreddit-about", "reddit-subreddit-comments", "reddit-subreddit-flairs", "reddit-subreddit-highlights", "reddit-subreddit-leaderboard-categories", "reddit-subreddit-posts", "reddit-subreddit-rules", "reddit-subreddit-user-flairs", "reddit-subreddit-wiki", "reddit-subreddits-discover", "reddit-subreddits-posts", "reddit-subreddits-search", "reddit-subreddits-suggest", "reddit-topics", "reddit-topics-broad", "reddit-topics-search", "reddit-trends", "reddit-user-comments", "reddit-user-posts", "reddit-user-profile"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"reddit-archive-comments-ids": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-comments-ids", "method": "GET", "params": [{"description": "Comma-separated Reddit comment ids (1-1,000); optional t1_ prefixes are accepted", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "c60n05h,abc123"}], "path": "/reddit/archive/comments/ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-archive-comments-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-comments-search", "method": "GET", "params": [{"description": "Public Reddit username filter", "in": "query", "name": "author", "type": "string"}, {"description": "Subreddit name filter", "in": "query", "name": "subreddit", "type": "string"}, {"description": "Full-text search within comment bodies; requires author, subreddit, link_id, or parent_id", "in": "query", "name": "query", "type": "string"}, {"description": "Reddit post id to scope comments", "in": "query", "name": "link_id", "type": "string"}, {"description": "Parent comment id; an explicitly empty value selects top-level comments", "in": "query", "name": "parent_id", "type": "string"}, {"description": "Creation-time lower bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_after", "type": "string"}, {"description": "Creation-time upper bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_before", "type": "string"}, {"default": "desc", "description": "Sort by creation time", "enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/archive/comments/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "author", "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "link_id", "type": "string"}, {"in": "query", "name": "parent_id", "type": "string"}, {"in": "query", "name": "created_after", "type": "string"}, {"in": "query", "name": "created_before", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-comments-tree": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-comments-tree", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "7cff0b"}, {"description": "Parent comment id; an explicitly empty value selects top-level comments", "in": "query", "name": "parent_id", "type": "string"}, {"description": "Maximum archive comment nodes to expand, defaults to 50 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Initial breadth, defaults to 2 and must be between 0 and 8", "in": "query", "name": "start_breadth", "type": "integer"}, {"description": "Initial depth, defaults to 3 and must be between 0 and 8", "in": "query", "name": "start_depth", "type": "integer"}], "path": "/reddit/archive/comments/{id}/tree", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "parent_id", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "start_breadth", "type": "integer"}, {"in": "query", "name": "start_depth", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-posts-ids": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-posts-ids", "method": "GET", "params": [{"description": "Comma-separated Reddit post ids (1-1,000); optional t3_ prefixes are accepted", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "1wwa2ff,z1c9z"}], "path": "/reddit/archive/posts/ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-archive-posts-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-posts-search", "method": "GET", "params": [{"description": "Text search across archived post titles and selftext", "in": "query", "name": "query", "type": "string"}, {"description": "Public Reddit username filter", "in": "query", "name": "author", "type": "string"}, {"description": "Subreddit name filter", "in": "query", "name": "subreddit", "type": "string"}, {"description": "Linked URL prefix filter", "in": "query", "name": "url", "type": "string"}, {"description": "Require an exact URL match; requires url", "in": "query", "name": "url_exact", "type": "boolean"}, {"description": "Creation-time lower bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_after", "type": "string"}, {"description": "Creation-time upper bound; accepts epoch seconds or milliseconds, ISO 8601 dates, or relative offsets such as 1year, 2d, or 5min", "in": "query", "name": "created_before", "type": "string"}, {"default": "desc", "description": "Sort by creation time", "enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/archive/posts/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"in": "query", "name": "author", "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"in": "query", "name": "url", "type": "string"}, {"in": "query", "name": "url_exact", "type": "boolean"}, {"in": "query", "name": "created_after", "type": "string"}, {"in": "query", "name": "created_before", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-subreddits-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-subreddits-search", "method": "GET", "params": [{"description": "Subreddit name prefix, with or without r/", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Minimum archived subscriber count", "in": "query", "name": "min_subscribers", "type": "integer"}, {"description": "Maximum archived subscriber count", "in": "query", "name": "max_subscribers", "type": "integer"}, {"description": "Filter by archived NSFW status", "in": "query", "name": "over_18", "type": "boolean"}, {"default": "subscribers", "description": "Sort field", "enum": ["created_utc", "subscribers", "subreddit"], "in": "query", "name": "sort_by", "type": "string"}, {"default": "desc", "description": "Sort direction", "enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum subreddits, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/archive/subreddits/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "min_subscribers", "type": "integer"}, {"in": "query", "name": "max_subscribers", "type": "integer"}, {"in": "query", "name": "over_18", "type": "boolean"}, {"enum": ["created_utc", "subscribers", "subreddit"], "in": "query", "name": "sort_by", "type": "string"}, {"enum": ["asc", "desc"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-archive-time-series": {"bodyParam": null, "bodyRequired": false, "id": "reddit-archive-time-series", "method": "GET", "params": [{"description": "Archive metric", "enum": ["posts_count", "comments_count", "posts_score_sum", "comments_score_sum", "posts_retrieval_delay_seconds_sum", "comments_retrieval_delay_seconds_sum", "subreddit_subscribers"], "in": "query", "name": "metric", "required": true, "type": "string", "x-example": "posts_count"}, {"description": "Optional subreddit scope; required for subreddit_subscribers, and unsupported for retrieval-delay metrics", "in": "query", "name": "subreddit", "type": "string", "x-example": "OpenAI"}, {"description": "Time bucket precision", "enum": ["year", "quarter", "month", "week", "day", "hour", "minute"], "in": "query", "name": "precision", "required": true, "type": "string", "x-example": "year"}, {"description": "Absolute start time: epoch seconds/milliseconds or ISO 8601", "in": "query", "name": "created_after", "required": true, "type": "string", "x-example": "2024-01-01"}, {"description": "Absolute end time: epoch seconds/milliseconds or ISO 8601", "in": "query", "name": "created_before", "required": true, "type": "string", "x-example": "2025-01-01"}], "path": "/reddit/archive/time-series", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["posts_count", "comments_count", "posts_score_sum", "comments_score_sum", "posts_retrieval_delay_seconds_sum", "comments_retrieval_delay_seconds_sum", "subreddit_subscribers"], "in": "query", "name": "metric", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["year", "quarter", "month", "week", "day", "hour", "minute"], "in": "query", "name": "precision", "required": true, "type": "string"}, {"in": "query", "name": "created_after", "required": true, "type": "string"}, {"in": "query", "name": "created_before", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-comment": {"bodyParam": null, "bodyRequired": false, "id": "reddit-comment", "method": "GET", "params": [{"description": "Comment id with or without t1_, or a comment URL", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "p8402di"}], "path": "/reddit/comment/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-comment-awards": {"bodyParam": null, "bodyRequired": false, "id": "reddit-comment-awards", "method": "GET", "params": [{"description": "Comment id with or without t1_, or a comment URL", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "19shpw8bwhfnn"}], "path": "/reddit/comment/{id}/awards", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-comments", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1tka90t"}, {"default": "confidence", "description": "Comment order: confidence, top, new, controversial, old, or qa.", "enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum comments returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"default": 3, "description": "Maximum flat comment depth returned.", "in": "query", "name": "depth", "type": "integer"}], "path": "/reddit/comments/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "depth", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-domain-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-domain-posts", "method": "GET", "params": [{"description": "Domain hostname, without scheme or path", "in": "path", "name": "domain", "required": true, "type": "string", "x-example": "openai.com"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/domain/{domain}/posts", "pathParams": ["domain"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-leads": {"bodyParam": null, "bodyRequired": false, "id": "reddit-leads", "method": "GET", "params": [{"description": "What you offer, in plain language", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "crm for small teams"}, {"description": "Restrict the search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"default": "month", "description": "Time window: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum leads returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Minimum buying-intent score to return, 0-10, defaults to 4", "in": "query", "name": "min_score", "type": "integer"}, {"default": "auto", "description": "Classifier: auto uses the model when configured, heuristic skips it, llm requires it", "enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "path": "/reddit/leads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "min_score", "type": "integer"}, {"enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-popular": {"bodyParam": null, "bodyRequired": false, "id": "reddit-popular", "method": "GET", "params": [{"default": "hot", "description": "Sort order: hot or top", "enum": ["hot", "top"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/popular", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "top"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-post": {"bodyParam": null, "bodyRequired": false, "id": "reddit-post", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1v8hy3q"}], "path": "/reddit/post/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-post-awards": {"bodyParam": null, "bodyRequired": false, "id": "reddit-post-awards", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1v8hy3q"}], "path": "/reddit/post/{id}/awards", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-posts-by-ids": {"bodyParam": null, "bodyRequired": false, "id": "reddit-posts-by-ids", "method": "GET", "params": [{"description": "Comma-separated post ids, with or without the t3_ prefix (maximum 100)", "in": "query", "name": "ids", "required": true, "type": "string", "x-example": "1v8hy3q,1tka90t"}], "path": "/reddit/posts/ids", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-search", "method": "GET", "params": [{"description": "Search keywords", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "gpt"}, {"description": "Restrict search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top/comments sorts: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-search-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-search-comments", "method": "GET", "params": [{"description": "Search keywords", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang generics"}, {"description": "Restrict search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top/comments sorts: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Opaque app pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search/comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-search-people": {"bodyParam": null, "bodyRequired": false, "id": "reddit-search-people", "method": "GET", "params": [{"description": "Username or profile keyword", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "spez"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum people, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Opaque app pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search/people", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-about": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-about", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum sample posts inspected, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/subreddit/{subreddit}/about", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-comments", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/comments", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-flairs": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-flairs", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/flairs", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-highlights": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-highlights", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/highlights", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-leaderboard-categories": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-leaderboard-categories", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/leaderboard/categories", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-posts", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"default": "hot", "description": "Sort: hot, new, top, rising, or controversial", "enum": ["hot", "new", "top", "rising", "controversial"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/posts", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising", "controversial"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-rules": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-rules", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddit/{subreddit}/rules", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-user-flairs": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-user-flairs", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "nba"}], "path": "/reddit/subreddit/{subreddit}/user-flairs", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-subreddit-wiki": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddit-wiki", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "golang"}, {"description": "Wiki page path, defaults to index", "in": "query", "name": "page", "type": "string", "x-example": "index"}], "path": "/reddit/subreddit/{subreddit}/wiki", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-discover": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-discover", "method": "GET", "params": [{"default": "popular", "description": "Community feed: popular, new, or default", "enum": ["popular", "new", "default"], "in": "query", "name": "feed", "type": "string"}, {"description": "Maximum communities, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/discover", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["popular", "new", "default"], "in": "query", "name": "feed", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-posts", "method": "GET", "params": [{"description": "Comma-separated subreddit names, without r/, maximum 10", "in": "query", "name": "subreddits", "required": true, "type": "string", "x-example": "OpenAI,MachineLearning"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "subreddits", "required": true, "type": "string"}, {"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-search", "method": "GET", "params": [{"description": "Community name search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang"}, {"description": "Maximum communities, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-suggest": {"bodyParam": null, "bodyRequired": false, "id": "reddit-subreddits-suggest", "method": "GET", "params": [{"description": "Community name or prefix", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/subreddits/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-topics": {"bodyParam": null, "bodyRequired": false, "id": "reddit-topics", "method": "GET", "params": [{"description": "Maximum topics, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Opaque app pagination cursor from a previous response", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/topics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-topics-broad": {"bodyParam": null, "bodyRequired": false, "id": "reddit-topics-broad", "method": "GET", "params": [], "path": "/reddit/topics/broad", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "reddit-topics-search": {"bodyParam": null, "bodyRequired": false, "id": "reddit-topics-search", "method": "GET", "params": [{"description": "Topic search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "golang"}], "path": "/reddit/topics/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-trends": {"bodyParam": null, "bodyRequired": false, "id": "reddit-trends", "method": "GET", "params": [{"default": "hot", "description": "Sort: hot, new, rising, or top", "enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/trends", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-comments": {"bodyParam": null, "bodyRequired": false, "id": "reddit-user-comments", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/comments", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-posts": {"bodyParam": null, "bodyRequired": false, "id": "reddit-user-posts", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/posts", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-profile": {"bodyParam": null, "bodyRequired": false, "id": "reddit-user-profile", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "spez"}], "path": "/reddit/user/{username}/profile", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-reddit-php/0.3.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function archive_comments_ids(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-comments-ids", $params, $responseType);
    }
    public function archive_comments_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-comments-search", $params, $responseType);
    }
    public function archive_comments_tree(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-comments-tree", $params, $responseType);
    }
    public function archive_posts_ids(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-posts-ids", $params, $responseType);
    }
    public function archive_posts_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-posts-search", $params, $responseType);
    }
    public function archive_subreddits_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-subreddits-search", $params, $responseType);
    }
    public function archive_time_series(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-archive-time-series", $params, $responseType);
    }
    public function comment(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-comment", $params, $responseType);
    }
    public function comment_awards(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-comment-awards", $params, $responseType);
    }
    public function comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-comments", $params, $responseType);
    }
    public function domain_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-domain-posts", $params, $responseType);
    }
    public function leads(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-leads", $params, $responseType);
    }
    public function popular(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-popular", $params, $responseType);
    }
    public function post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-post", $params, $responseType);
    }
    public function post_awards(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-post-awards", $params, $responseType);
    }
    public function posts_by_ids(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-posts-by-ids", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-search", $params, $responseType);
    }
    public function search_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-search-comments", $params, $responseType);
    }
    public function search_people(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-search-people", $params, $responseType);
    }
    public function subreddit_about(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-about", $params, $responseType);
    }
    public function subreddit_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-comments", $params, $responseType);
    }
    public function subreddit_flairs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-flairs", $params, $responseType);
    }
    public function subreddit_highlights(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-highlights", $params, $responseType);
    }
    public function subreddit_leaderboard_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-leaderboard-categories", $params, $responseType);
    }
    public function subreddit_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-posts", $params, $responseType);
    }
    public function subreddit_rules(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-rules", $params, $responseType);
    }
    public function subreddit_user_flairs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-user-flairs", $params, $responseType);
    }
    public function subreddit_wiki(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-wiki", $params, $responseType);
    }
    public function subreddits_discover(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddits-discover", $params, $responseType);
    }
    public function subreddits_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddits-posts", $params, $responseType);
    }
    public function subreddits_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddits-search", $params, $responseType);
    }
    public function subreddits_suggest(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddits-suggest", $params, $responseType);
    }
    public function topics(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-topics", $params, $responseType);
    }
    public function topics_broad(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-topics-broad", $params, $responseType);
    }
    public function topics_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-topics-search", $params, $responseType);
    }
    public function trends(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-trends", $params, $responseType);
    }
    public function user_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-user-comments", $params, $responseType);
    }
    public function user_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-user-posts", $params, $responseType);
    }
    public function user_profile(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-user-profile", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
