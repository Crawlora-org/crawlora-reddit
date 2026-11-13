package net.crawlora.reddit;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Reddit endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 39;
    public static final List<String> OPERATION_IDS = List.of(
            "reddit-archive-comments-ids",
            "reddit-archive-comments-search",
            "reddit-archive-comments-tree",
            "reddit-archive-posts-ids",
            "reddit-archive-posts-search",
            "reddit-archive-subreddits-search",
            "reddit-archive-time-series",
            "reddit-comment",
            "reddit-comment-awards",
            "reddit-comments",
            "reddit-domain-posts",
            "reddit-leads",
            "reddit-popular",
            "reddit-post",
            "reddit-post-awards",
            "reddit-posts-by-ids",
            "reddit-search",
            "reddit-search-comments",
            "reddit-search-people",
            "reddit-subreddit-about",
            "reddit-subreddit-comments",
            "reddit-subreddit-flairs",
            "reddit-subreddit-highlights",
            "reddit-subreddit-leaderboard-categories",
            "reddit-subreddit-posts",
            "reddit-subreddit-rules",
            "reddit-subreddit-user-flairs",
            "reddit-subreddit-wiki",
            "reddit-subreddits-discover",
            "reddit-subreddits-posts",
            "reddit-subreddits-search",
            "reddit-subreddits-suggest",
            "reddit-topics",
            "reddit-topics-broad",
            "reddit-topics-search",
            "reddit-trends",
            "reddit-user-comments",
            "reddit-user-posts",
            "reddit-user-profile"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("reddit-archive-comments-ids", new Operation("reddit-archive-comments-ids", "GET", "/reddit/archive/comments/ids", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-archive-comments-search", new Operation("reddit-archive-comments-search", "GET", "/reddit/archive/comments/search", Map.ofEntries(Map.entry("author", new Param("author", "query", false, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("query", new Param("query", "query", false, "string", List.of(), "csv")), Map.entry("link_id", new Param("link_id", "query", false, "string", List.of(), "csv")), Map.entry("parent_id", new Param("parent_id", "query", false, "string", List.of(), "csv")), Map.entry("created_after", new Param("created_after", "query", false, "string", List.of(), "csv")), Map.entry("created_before", new Param("created_before", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-archive-comments-tree", new Operation("reddit-archive-comments-tree", "GET", "/reddit/archive/comments/{id}/tree", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("parent_id", new Param("parent_id", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("start_breadth", new Param("start_breadth", "query", false, "integer", List.of(), "csv")), Map.entry("start_depth", new Param("start_depth", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-archive-posts-ids", new Operation("reddit-archive-posts-ids", "GET", "/reddit/archive/posts/ids", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-archive-posts-search", new Operation("reddit-archive-posts-search", "GET", "/reddit/archive/posts/search", Map.ofEntries(Map.entry("query", new Param("query", "query", false, "string", List.of(), "csv")), Map.entry("author", new Param("author", "query", false, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("url", new Param("url", "query", false, "string", List.of(), "csv")), Map.entry("url_exact", new Param("url_exact", "query", false, "boolean", List.of(), "csv")), Map.entry("created_after", new Param("created_after", "query", false, "string", List.of(), "csv")), Map.entry("created_before", new Param("created_before", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-archive-subreddits-search", new Operation("reddit-archive-subreddits-search", "GET", "/reddit/archive/subreddits/search", Map.ofEntries(Map.entry("query", new Param("query", "query", true, "string", List.of(), "csv")), Map.entry("min_subscribers", new Param("min_subscribers", "query", false, "integer", List.of(), "csv")), Map.entry("max_subscribers", new Param("max_subscribers", "query", false, "integer", List.of(), "csv")), Map.entry("over_18", new Param("over_18", "query", false, "boolean", List.of(), "csv")), Map.entry("sort_by", new Param("sort_by", "query", false, "string", List.of("created_utc", "subscribers", "subreddit"), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("asc", "desc"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-archive-time-series", new Operation("reddit-archive-time-series", "GET", "/reddit/archive/time-series", Map.ofEntries(Map.entry("metric", new Param("metric", "query", true, "string", List.of("posts_count", "comments_count", "posts_score_sum", "comments_score_sum", "posts_retrieval_delay_seconds_sum", "comments_retrieval_delay_seconds_sum", "subreddit_subscribers"), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("precision", new Param("precision", "query", true, "string", List.of("year", "quarter", "month", "week", "day", "hour", "minute"), "csv")), Map.entry("created_after", new Param("created_after", "query", true, "string", List.of(), "csv")), Map.entry("created_before", new Param("created_before", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-comment", new Operation("reddit-comment", "GET", "/reddit/comment/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-comment-awards", new Operation("reddit-comment-awards", "GET", "/reddit/comment/{id}/awards", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-comments", new Operation("reddit-comments", "GET", "/reddit/comments/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("confidence", "top", "new", "controversial", "old", "qa"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("depth", new Param("depth", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-domain-posts", new Operation("reddit-domain-posts", "GET", "/reddit/domain/{domain}/posts", Map.ofEntries(Map.entry("domain", new Param("domain", "path", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top", "rising"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-leads", new Operation("reddit-leads", "GET", "/reddit/leads", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("relevance", "hot", "new", "top", "comments"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("min_score", new Param("min_score", "query", false, "integer", List.of(), "csv")), Map.entry("classifier", new Param("classifier", "query", false, "string", List.of("auto", "heuristic", "llm"), "csv"))), List.of("application/json")));
        operations.put("reddit-popular", new Operation("reddit-popular", "GET", "/reddit/popular", Map.ofEntries(Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "top"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-post", new Operation("reddit-post", "GET", "/reddit/post/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-post-awards", new Operation("reddit-post-awards", "GET", "/reddit/post/{id}/awards", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-posts-by-ids", new Operation("reddit-posts-by-ids", "GET", "/reddit/posts/ids", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-search", new Operation("reddit-search", "GET", "/reddit/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("relevance", "hot", "new", "top", "comments"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-search-comments", new Operation("reddit-search-comments", "GET", "/reddit/search/comments", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("relevance", "hot", "new", "top", "comments"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-search-people", new Operation("reddit-search-people", "GET", "/reddit/search/people", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("relevance", "hot", "new", "top", "comments"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-about", new Operation("reddit-subreddit-about", "GET", "/reddit/subreddit/{subreddit}/about", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-comments", new Operation("reddit-subreddit-comments", "GET", "/reddit/subreddit/{subreddit}/comments", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-flairs", new Operation("reddit-subreddit-flairs", "GET", "/reddit/subreddit/{subreddit}/flairs", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-highlights", new Operation("reddit-subreddit-highlights", "GET", "/reddit/subreddit/{subreddit}/highlights", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-leaderboard-categories", new Operation("reddit-subreddit-leaderboard-categories", "GET", "/reddit/subreddit/{subreddit}/leaderboard/categories", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-posts", new Operation("reddit-subreddit-posts", "GET", "/reddit/subreddit/{subreddit}/posts", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top", "rising", "controversial"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-rules", new Operation("reddit-subreddit-rules", "GET", "/reddit/subreddit/{subreddit}/rules", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-user-flairs", new Operation("reddit-subreddit-user-flairs", "GET", "/reddit/subreddit/{subreddit}/user-flairs", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-wiki", new Operation("reddit-subreddit-wiki", "GET", "/reddit/subreddit/{subreddit}/wiki", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddits-discover", new Operation("reddit-subreddits-discover", "GET", "/reddit/subreddits/discover", Map.ofEntries(Map.entry("feed", new Param("feed", "query", false, "string", List.of("popular", "new", "default"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddits-posts", new Operation("reddit-subreddits-posts", "GET", "/reddit/subreddits/posts", Map.ofEntries(Map.entry("subreddits", new Param("subreddits", "query", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top", "rising"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddits-search", new Operation("reddit-subreddits-search", "GET", "/reddit/subreddits/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddits-suggest", new Operation("reddit-subreddits-suggest", "GET", "/reddit/subreddits/suggest", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-topics", new Operation("reddit-topics", "GET", "/reddit/topics", Map.ofEntries(Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-topics-broad", new Operation("reddit-topics-broad", "GET", "/reddit/topics/broad", Map.of(), List.of("application/json")));
        operations.put("reddit-topics-search", new Operation("reddit-topics-search", "GET", "/reddit/topics/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-trends", new Operation("reddit-trends", "GET", "/reddit/trends", Map.ofEntries(Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "rising", "top"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-user-comments", new Operation("reddit-user-comments", "GET", "/reddit/user/{username}/comments", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-user-posts", new Operation("reddit-user-posts", "GET", "/reddit/user/{username}/posts", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-user-profile", new Operation("reddit-user-profile", "GET", "/reddit/user/{username}/profile", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Reddit operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object archiveCommentsIds(Map<String, ?> params) { return request("reddit-archive-comments-ids", params); }
    public Object archiveCommentsSearch(Map<String, ?> params) { return request("reddit-archive-comments-search", params); }
    public Object archiveCommentsTree(Map<String, ?> params) { return request("reddit-archive-comments-tree", params); }
    public Object archivePostsIds(Map<String, ?> params) { return request("reddit-archive-posts-ids", params); }
    public Object archivePostsSearch(Map<String, ?> params) { return request("reddit-archive-posts-search", params); }
    public Object archiveSubredditsSearch(Map<String, ?> params) { return request("reddit-archive-subreddits-search", params); }
    public Object archiveTimeSeries(Map<String, ?> params) { return request("reddit-archive-time-series", params); }
    public Object comment(Map<String, ?> params) { return request("reddit-comment", params); }
    public Object commentAwards(Map<String, ?> params) { return request("reddit-comment-awards", params); }
    public Object comments(Map<String, ?> params) { return request("reddit-comments", params); }
    public Object domainPosts(Map<String, ?> params) { return request("reddit-domain-posts", params); }
    public Object leads(Map<String, ?> params) { return request("reddit-leads", params); }
    public Object popular(Map<String, ?> params) { return request("reddit-popular", params); }
    public Object post(Map<String, ?> params) { return request("reddit-post", params); }
    public Object postAwards(Map<String, ?> params) { return request("reddit-post-awards", params); }
    public Object postsByIds(Map<String, ?> params) { return request("reddit-posts-by-ids", params); }
    public Object search(Map<String, ?> params) { return request("reddit-search", params); }
    public Object searchComments(Map<String, ?> params) { return request("reddit-search-comments", params); }
    public Object searchPeople(Map<String, ?> params) { return request("reddit-search-people", params); }
    public Object subredditAbout(Map<String, ?> params) { return request("reddit-subreddit-about", params); }
    public Object subredditComments(Map<String, ?> params) { return request("reddit-subreddit-comments", params); }
    public Object subredditFlairs(Map<String, ?> params) { return request("reddit-subreddit-flairs", params); }
    public Object subredditHighlights(Map<String, ?> params) { return request("reddit-subreddit-highlights", params); }
    public Object subredditLeaderboardCategories(Map<String, ?> params) { return request("reddit-subreddit-leaderboard-categories", params); }
    public Object subredditPosts(Map<String, ?> params) { return request("reddit-subreddit-posts", params); }
    public Object subredditRules(Map<String, ?> params) { return request("reddit-subreddit-rules", params); }
    public Object subredditUserFlairs(Map<String, ?> params) { return request("reddit-subreddit-user-flairs", params); }
    public Object subredditWiki(Map<String, ?> params) { return request("reddit-subreddit-wiki", params); }
    public Object subredditsDiscover(Map<String, ?> params) { return request("reddit-subreddits-discover", params); }
    public Object subredditsPosts(Map<String, ?> params) { return request("reddit-subreddits-posts", params); }
    public Object subredditsSearch(Map<String, ?> params) { return request("reddit-subreddits-search", params); }
    public Object subredditsSuggest(Map<String, ?> params) { return request("reddit-subreddits-suggest", params); }
    public Object topics(Map<String, ?> params) { return request("reddit-topics", params); }
    public Object topicsBroad(Map<String, ?> params) { return request("reddit-topics-broad", params); }
    public Object topicsSearch(Map<String, ?> params) { return request("reddit-topics-search", params); }
    public Object trends(Map<String, ?> params) { return request("reddit-trends", params); }
    public Object userComments(Map<String, ?> params) { return request("reddit-user-comments", params); }
    public Object userPosts(Map<String, ?> params) { return request("reddit-user-posts", params); }
    public Object userProfile(Map<String, ?> params) { return request("reddit-user-profile", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
