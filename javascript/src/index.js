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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-reddit-js/0.3.0" });
    this["archiveCommentsIds"] = (...args) => this.request("reddit-archive-comments-ids", ...args);
    this["archiveCommentsSearch"] = (...args) => this.request("reddit-archive-comments-search", ...args);
    this["archiveCommentsTree"] = (...args) => this.request("reddit-archive-comments-tree", ...args);
    this["archivePostsIds"] = (...args) => this.request("reddit-archive-posts-ids", ...args);
    this["archivePostsSearch"] = (...args) => this.request("reddit-archive-posts-search", ...args);
    this["archiveSubredditsSearch"] = (...args) => this.request("reddit-archive-subreddits-search", ...args);
    this["archiveTimeSeries"] = (...args) => this.request("reddit-archive-time-series", ...args);
    this["comment"] = (...args) => this.request("reddit-comment", ...args);
    this["commentAwards"] = (...args) => this.request("reddit-comment-awards", ...args);
    this["comments"] = (...args) => this.request("reddit-comments", ...args);
    this["domainPosts"] = (...args) => this.request("reddit-domain-posts", ...args);
    this["leads"] = (...args) => this.request("reddit-leads", ...args);
    this["popular"] = (...args) => this.request("reddit-popular", ...args);
    this["post"] = (...args) => this.request("reddit-post", ...args);
    this["postAwards"] = (...args) => this.request("reddit-post-awards", ...args);
    this["postsByIds"] = (...args) => this.request("reddit-posts-by-ids", ...args);
    this["search"] = (...args) => this.request("reddit-search", ...args);
    this["searchComments"] = (...args) => this.request("reddit-search-comments", ...args);
    this["searchPeople"] = (...args) => this.request("reddit-search-people", ...args);
    this["subredditAbout"] = (...args) => this.request("reddit-subreddit-about", ...args);
    this["subredditComments"] = (...args) => this.request("reddit-subreddit-comments", ...args);
    this["subredditFlairs"] = (...args) => this.request("reddit-subreddit-flairs", ...args);
    this["subredditHighlights"] = (...args) => this.request("reddit-subreddit-highlights", ...args);
    this["subredditLeaderboardCategories"] = (...args) => this.request("reddit-subreddit-leaderboard-categories", ...args);
    this["subredditPosts"] = (...args) => this.request("reddit-subreddit-posts", ...args);
    this["subredditRules"] = (...args) => this.request("reddit-subreddit-rules", ...args);
    this["subredditUserFlairs"] = (...args) => this.request("reddit-subreddit-user-flairs", ...args);
    this["subredditWiki"] = (...args) => this.request("reddit-subreddit-wiki", ...args);
    this["subredditsDiscover"] = (...args) => this.request("reddit-subreddits-discover", ...args);
    this["subredditsPosts"] = (...args) => this.request("reddit-subreddits-posts", ...args);
    this["subredditsSearch"] = (...args) => this.request("reddit-subreddits-search", ...args);
    this["subredditsSuggest"] = (...args) => this.request("reddit-subreddits-suggest", ...args);
    this["topics"] = (...args) => this.request("reddit-topics", ...args);
    this["topicsBroad"] = (...args) => this.request("reddit-topics-broad", ...args);
    this["topicsSearch"] = (...args) => this.request("reddit-topics-search", ...args);
    this["trends"] = (...args) => this.request("reddit-trends", ...args);
    this["userComments"] = (...args) => this.request("reddit-user-comments", ...args);
    this["userPosts"] = (...args) => this.request("reddit-user-posts", ...args);
    this["userProfile"] = (...args) => this.request("reddit-user-profile", ...args);
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
export const VERSION = "0.3.0";
export default RedditClient;
