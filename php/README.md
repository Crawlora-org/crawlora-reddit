# Crawlora Reddit API client for PHP (`crawlora/reddit`)

This PHP package calls Crawlora's hosted Reddit API at `https://api.crawlora.net/api/v1`. It exposes 12 endpoints covering search, post and comment details, subreddit feeds, user history, domain listings, trends, and leads. It does not call or scrape Reddit directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

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

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 12 API operations.

## Supported Reddit API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/reddit/comments/{id}` | `reddit-comments` | Get Reddit post comments |
| `GET` | `/reddit/domain/{domain}/posts` | `reddit-domain-posts` | List Reddit domain posts |
| `GET` | `/reddit/leads` | `reddit-leads` | Find Reddit buying-intent leads |
| `GET` | `/reddit/post/{id}` | `reddit-post` | Get Reddit post |
| `GET` | `/reddit/search` | `reddit-search` | Search Reddit posts |
| `GET` | `/reddit/subreddit/{subreddit}/about` | `reddit-subreddit-about` | Get Reddit subreddit metadata |
| `GET` | `/reddit/subreddit/{subreddit}/comments` | `reddit-subreddit-comments` | List Reddit subreddit comments |
| `GET` | `/reddit/subreddit/{subreddit}/posts` | `reddit-subreddit-posts` | List Reddit subreddit posts |
| `GET` | `/reddit/subreddits/posts` | `reddit-subreddits-posts` | List Reddit multi-subreddit posts |
| `GET` | `/reddit/trends` | `reddit-trends` | List Reddit trends |
| `GET` | `/reddit/user/{username}/comments` | `reddit-user-comments` | List Reddit user comments |
| `GET` | `/reddit/user/{username}/posts` | `reddit-user-posts` | List Reddit user posts |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-reddit). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md).
