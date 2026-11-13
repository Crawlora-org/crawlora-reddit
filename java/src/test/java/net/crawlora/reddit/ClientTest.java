package net.crawlora.reddit;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(39, Client.OPERATION_IDS.size());
        assertEquals(List.of("reddit-archive-comments-ids", "reddit-archive-comments-search", "reddit-archive-comments-tree", "reddit-archive-posts-ids", "reddit-archive-posts-search", "reddit-archive-subreddits-search", "reddit-archive-time-series", "reddit-comment", "reddit-comment-awards", "reddit-comments", "reddit-domain-posts", "reddit-leads", "reddit-popular", "reddit-post", "reddit-post-awards", "reddit-posts-by-ids", "reddit-search", "reddit-search-comments", "reddit-search-people", "reddit-subreddit-about", "reddit-subreddit-comments", "reddit-subreddit-flairs", "reddit-subreddit-highlights", "reddit-subreddit-leaderboard-categories", "reddit-subreddit-posts", "reddit-subreddit-rules", "reddit-subreddit-user-flairs", "reddit-subreddit-wiki", "reddit-subreddits-discover", "reddit-subreddits-posts", "reddit-subreddits-search", "reddit-subreddits-suggest", "reddit-topics", "reddit-topics-broad", "reddit-topics-search", "reddit-trends", "reddit-user-comments", "reddit-user-posts", "reddit-user-profile"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("reddit-archive-comments-tree", Map.ofEntries(Map.entry("id", "path /one"), Map.entry("parent_id", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            assertTrue(seenUri.get().contains("path%20%2Fone"), "path values should be URL encoded");
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("archiveCommentsTree", Map.class).invoke(client, Map.ofEntries(Map.entry("id", "path /one"), Map.entry("parent_id", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("reddit-archive-comments-ids", Map.ofEntries(Map.entry("ids", "sample"))));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("reddit-archive-comments-tree", Map.ofEntries(Map.entry("id", "path /one"), Map.entry("parent_id", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("reddit-archive-comments-tree", Map.ofEntries(Map.entry("id", "path /one"), Map.entry("parent_id", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("reddit-archive-comments-search", Map.ofEntries(Map.entry("sort", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("reddit-archive-comments-tree", Map.ofEntries(Map.entry("id", "path /one"), Map.entry("parent_id", "value &/one"))));
    }
}
