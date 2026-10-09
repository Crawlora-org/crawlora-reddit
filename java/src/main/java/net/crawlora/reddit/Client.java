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
    public static final int OPERATION_COUNT = 12;
    public static final List<String> OPERATION_IDS = List.of(
            "reddit-comments",
            "reddit-domain-posts",
            "reddit-leads",
            "reddit-post",
            "reddit-search",
            "reddit-subreddit-about",
            "reddit-subreddit-comments",
            "reddit-subreddit-posts",
            "reddit-subreddits-posts",
            "reddit-trends",
            "reddit-user-comments",
            "reddit-user-posts"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("reddit-comments", new Operation("reddit-comments", "GET", "/reddit/comments/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("confidence", "top", "new", "controversial", "old", "qa"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("depth", new Param("depth", "query", false, "integer", List.of(), "csv")), Map.entry("include_metrics", new Param("include_metrics", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-domain-posts", new Operation("reddit-domain-posts", "GET", "/reddit/domain/{domain}/posts", Map.ofEntries(Map.entry("domain", new Param("domain", "path", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top", "rising"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-leads", new Operation("reddit-leads", "GET", "/reddit/leads", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("relevance", "hot", "new", "top", "comments"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("min_score", new Param("min_score", "query", false, "integer", List.of(), "csv")), Map.entry("classifier", new Param("classifier", "query", false, "string", List.of("auto", "heuristic", "llm"), "csv"))), List.of("application/json")));
        operations.put("reddit-post", new Operation("reddit-post", "GET", "/reddit/post/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("include_metrics", new Param("include_metrics", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-search", new Operation("reddit-search", "GET", "/reddit/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("subreddit", new Param("subreddit", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("relevance", "hot", "new", "top", "comments"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-about", new Operation("reddit-subreddit-about", "GET", "/reddit/subreddit/{subreddit}/about", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-comments", new Operation("reddit-subreddit-comments", "GET", "/reddit/subreddit/{subreddit}/comments", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddit-posts", new Operation("reddit-subreddit-posts", "GET", "/reddit/subreddit/{subreddit}/posts", Map.ofEntries(Map.entry("subreddit", new Param("subreddit", "path", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top", "rising"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-subreddits-posts", new Operation("reddit-subreddits-posts", "GET", "/reddit/subreddits/posts", Map.ofEntries(Map.entry("subreddits", new Param("subreddits", "query", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "top", "rising"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-trends", new Operation("reddit-trends", "GET", "/reddit/trends", Map.ofEntries(Map.entry("sort", new Param("sort", "query", false, "string", List.of("hot", "new", "rising", "top"), "csv")), Map.entry("time", new Param("time", "query", false, "string", List.of("hour", "day", "week", "month", "year", "all"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-user-comments", new Operation("reddit-user-comments", "GET", "/reddit/user/{username}/comments", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("reddit-user-posts", new Operation("reddit-user-posts", "GET", "/reddit/user/{username}/posts", Map.ofEntries(Map.entry("username", new Param("username", "path", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("after", new Param("after", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
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
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
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
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
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

    public Object comments(Map<String, ?> params) { return request("reddit-comments", params); }
    public Object domainPosts(Map<String, ?> params) { return request("reddit-domain-posts", params); }
    public Object leads(Map<String, ?> params) { return request("reddit-leads", params); }
    public Object post(Map<String, ?> params) { return request("reddit-post", params); }
    public Object search(Map<String, ?> params) { return request("reddit-search", params); }
    public Object subredditAbout(Map<String, ?> params) { return request("reddit-subreddit-about", params); }
    public Object subredditComments(Map<String, ?> params) { return request("reddit-subreddit-comments", params); }
    public Object subredditPosts(Map<String, ?> params) { return request("reddit-subreddit-posts", params); }
    public Object subredditsPosts(Map<String, ?> params) { return request("reddit-subreddits-posts", params); }
    public Object trends(Map<String, ?> params) { return request("reddit-trends", params); }
    public Object userComments(Map<String, ?> params) { return request("reddit-user-comments", params); }
    public Object userPosts(Map<String, ?> params) { return request("reddit-user-posts", params); }

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
