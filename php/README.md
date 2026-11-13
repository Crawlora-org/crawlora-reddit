# Crawlora Reddit API client for PHP (`crawlora/reddit`)

This PHP package calls Crawlora's hosted Reddit API at `https://api.crawlora.net/api/v1`. It exposes 39 endpoints covering search, post and comment details, subreddit feeds, user history, domain listings, trends, and leads. It does not call or scrape Reddit directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/reddit
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Reddit\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("reddit-search", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 39 API operations.

## Supported Reddit API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-reddit). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md).
