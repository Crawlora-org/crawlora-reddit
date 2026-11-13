# Crawlora Reddit API client for Java

The official Java client for Crawlora's hosted Reddit API. It exposes 39 endpoints covering search, post and comment details, subreddit feeds, user history, domain listings, trends, and leads. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-reddit</artifactId>
  <version>0.3.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-java-console) to get an API key.

```java
import net.crawlora.reddit.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("q", "open source")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Reddit API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/reddit/archive/comments/ids` | `reddit-archive-comments-ids` | Look up archived Reddit comments by ids |
| `GET` | `/reddit/archive/comments/search` | `reddit-archive-comments-search` | Search archived Reddit comments |
| `GET` | `/reddit/archive/comments/{id}/tree` | `reddit-archive-comments-tree` | Get an archived Reddit comment tree |
| `GET` | `/reddit/archive/posts/ids` | `reddit-archive-posts-ids` | Look up archived Reddit posts by ids |
| `GET` | `/reddit/archive/posts/search` | `reddit-archive-posts-search` | Search archived Reddit posts |
| `GET` | `/reddit/archive/subreddits/search` | `reddit-archive-subreddits-search` | Search Reddit's archived subreddit directory |
| `GET` | `/reddit/archive/time-series` | `reddit-archive-time-series` | Get historical Reddit archive time series |
| `GET` | `/reddit/comment/{id}` | `reddit-comment` | Get a Reddit comment |
| `GET` | `/reddit/comment/{id}/awards` | `reddit-comment-awards` | Get Reddit comment awards |
| `GET` | `/reddit/comments/{id}` | `reddit-comments` | Get Reddit post comments |
| `GET` | `/reddit/domain/{domain}/posts` | `reddit-domain-posts` | List Reddit domain posts |
| `GET` | `/reddit/leads` | `reddit-leads` | Find Reddit buying-intent leads |
| `GET` | `/reddit/popular` | `reddit-popular` | List Reddit popular posts |
| `GET` | `/reddit/post/{id}` | `reddit-post` | Get Reddit post |
| `GET` | `/reddit/post/{id}/awards` | `reddit-post-awards` | Get Reddit post awards |
| `GET` | `/reddit/posts/ids` | `reddit-posts-by-ids` | Get Reddit posts by ids |
| `GET` | `/reddit/search` | `reddit-search` | Search Reddit posts |
| `GET` | `/reddit/search/comments` | `reddit-search-comments` | Search Reddit comments |
| `GET` | `/reddit/search/people` | `reddit-search-people` | Search Reddit people |
| `GET` | `/reddit/subreddit/{subreddit}/about` | `reddit-subreddit-about` | Get Reddit subreddit metadata |
| `GET` | `/reddit/subreddit/{subreddit}/comments` | `reddit-subreddit-comments` | List Reddit subreddit comments |
| `GET` | `/reddit/subreddit/{subreddit}/flairs` | `reddit-subreddit-flairs` | List Reddit community post flairs |
| `GET` | `/reddit/subreddit/{subreddit}/highlights` | `reddit-subreddit-highlights` | List Reddit community highlights |
| `GET` | `/reddit/subreddit/{subreddit}/leaderboard/categories` | `reddit-subreddit-leaderboard-categories` | List Reddit community leaderboard categories |
| `GET` | `/reddit/subreddit/{subreddit}/posts` | `reddit-subreddit-posts` | List Reddit subreddit posts |
| `GET` | `/reddit/subreddit/{subreddit}/rules` | `reddit-subreddit-rules` | Get Reddit community rules |
| `GET` | `/reddit/subreddit/{subreddit}/user-flairs` | `reddit-subreddit-user-flairs` | List Reddit community user flairs |
| `GET` | `/reddit/subreddit/{subreddit}/wiki` | `reddit-subreddit-wiki` | Get Reddit community wiki |
| `GET` | `/reddit/subreddits/discover` | `reddit-subreddits-discover` | List Reddit community discovery feeds |
| `GET` | `/reddit/subreddits/posts` | `reddit-subreddits-posts` | List Reddit multi-subreddit posts |
| `GET` | `/reddit/subreddits/search` | `reddit-subreddits-search` | Search Reddit communities |
| `GET` | `/reddit/subreddits/suggest` | `reddit-subreddits-suggest` | Suggest Reddit communities |
| `GET` | `/reddit/topics` | `reddit-topics` | List Reddit taxonomy topics |
| `GET` | `/reddit/topics/broad` | `reddit-topics-broad` | List Reddit broad topics |
| `GET` | `/reddit/topics/search` | `reddit-topics-search` | Search Reddit topics |
| `GET` | `/reddit/trends` | `reddit-trends` | List Reddit trends |
| `GET` | `/reddit/user/{username}/comments` | `reddit-user-comments` | List Reddit user comments |
| `GET` | `/reddit/user/{username}/posts` | `reddit-user-posts` | List Reddit user posts |
| `GET` | `/reddit/user/{username}/profile` | `reddit-user-profile` | Get a Reddit user profile |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-reddit)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-java-api-docs)
