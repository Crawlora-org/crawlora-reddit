import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class RedditClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-reddit-js/0.1.1" });
    this["comments"] = (...args) => this.request("reddit-comments", ...args);
    this["domainPosts"] = (...args) => this.request("reddit-domain-posts", ...args);
    this["leads"] = (...args) => this.request("reddit-leads", ...args);
    this["post"] = (...args) => this.request("reddit-post", ...args);
    this["search"] = (...args) => this.request("reddit-search", ...args);
    this["subredditAbout"] = (...args) => this.request("reddit-subreddit-about", ...args);
    this["subredditComments"] = (...args) => this.request("reddit-subreddit-comments", ...args);
    this["subredditPosts"] = (...args) => this.request("reddit-subreddit-posts", ...args);
    this["subredditsPosts"] = (...args) => this.request("reddit-subreddits-posts", ...args);
    this["trends"] = (...args) => this.request("reddit-trends", ...args);
    this["userComments"] = (...args) => this.request("reddit-user-comments", ...args);
    this["userPosts"] = (...args) => this.request("reddit-user-posts", ...args);
  }
}

export { RedditClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.1";
export default RedditClient;
