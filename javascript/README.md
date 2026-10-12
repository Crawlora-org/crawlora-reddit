# @crawlora-org/reddit — Reddit API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Reddit API.
It exposes 12 API endpoints for search, post and comment details, subreddit feeds, user history, domain listings, trends, and leads through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-javascript-homepage). It does not run a browser or scrape Reddit locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Reddit or its owners.

## Install

```sh
npm install @crawlora-org/reddit
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=reddit-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { RedditClient } from "@crawlora-org/reddit";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new RedditClient({ apiKey });
const result1 = await client.search({ q: "open source" });
console.log(result1);
const result2 = await client.subredditPosts({ subreddit: "technology" });
console.log(result2);
```

The client also exports `Client` as an alias for `RedditClient`. Operation
methods are available directly in camelCase and through the `reddit`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-reddit/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Reddit API endpoints

This package exposes each route below as a direct method and through the `reddit` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-reddit/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
