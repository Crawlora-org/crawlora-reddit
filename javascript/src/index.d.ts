import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class RedditClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archiveCommentsIds(params: OperationParamsMap["reddit-archive-comments-ids"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archiveCommentsSearch(params?: OperationParamsMap["reddit-archive-comments-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archiveCommentsTree(params: OperationParamsMap["reddit-archive-comments-tree"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archivePostsIds(params: OperationParamsMap["reddit-archive-posts-ids"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archivePostsSearch(params?: OperationParamsMap["reddit-archive-posts-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archiveSubredditsSearch(params: OperationParamsMap["reddit-archive-subreddits-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archiveTimeSeries(params: OperationParamsMap["reddit-archive-time-series"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  comment(params: OperationParamsMap["reddit-comment"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  commentAwards(params: OperationParamsMap["reddit-comment-awards"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  comments(params: OperationParamsMap["reddit-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  domainPosts(params: OperationParamsMap["reddit-domain-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leads(params: OperationParamsMap["reddit-leads"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  popular(params?: OperationParamsMap["reddit-popular"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  post(params: OperationParamsMap["reddit-post"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  postAwards(params: OperationParamsMap["reddit-post-awards"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  postsByIds(params: OperationParamsMap["reddit-posts-by-ids"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["reddit-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchComments(params: OperationParamsMap["reddit-search-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchPeople(params: OperationParamsMap["reddit-search-people"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditAbout(params: OperationParamsMap["reddit-subreddit-about"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditComments(params: OperationParamsMap["reddit-subreddit-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditFlairs(params: OperationParamsMap["reddit-subreddit-flairs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditHighlights(params: OperationParamsMap["reddit-subreddit-highlights"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditLeaderboardCategories(params: OperationParamsMap["reddit-subreddit-leaderboard-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditPosts(params: OperationParamsMap["reddit-subreddit-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditRules(params: OperationParamsMap["reddit-subreddit-rules"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditUserFlairs(params: OperationParamsMap["reddit-subreddit-user-flairs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditWiki(params: OperationParamsMap["reddit-subreddit-wiki"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditsDiscover(params?: OperationParamsMap["reddit-subreddits-discover"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditsPosts(params: OperationParamsMap["reddit-subreddits-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditsSearch(params: OperationParamsMap["reddit-subreddits-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditsSuggest(params: OperationParamsMap["reddit-subreddits-suggest"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topics(params?: OperationParamsMap["reddit-topics"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topicsBroad(params?: OperationParamsMap["reddit-topics-broad"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topicsSearch(params: OperationParamsMap["reddit-topics-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trends(params?: OperationParamsMap["reddit-trends"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userComments(params: OperationParamsMap["reddit-user-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userPosts(params: OperationParamsMap["reddit-user-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userProfile(params: OperationParamsMap["reddit-user-profile"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archiveCommentsIds(params: OperationParamsMap["reddit-archive-comments-ids"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archiveCommentsSearch(params?: OperationParamsMap["reddit-archive-comments-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archiveCommentsTree(params: OperationParamsMap["reddit-archive-comments-tree"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archivePostsIds(params: OperationParamsMap["reddit-archive-posts-ids"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archivePostsSearch(params?: OperationParamsMap["reddit-archive-posts-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archiveSubredditsSearch(params: OperationParamsMap["reddit-archive-subreddits-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archiveTimeSeries(params: OperationParamsMap["reddit-archive-time-series"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  comment(params: OperationParamsMap["reddit-comment"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  commentAwards(params: OperationParamsMap["reddit-comment-awards"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  comments(params: OperationParamsMap["reddit-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  domainPosts(params: OperationParamsMap["reddit-domain-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leads(params: OperationParamsMap["reddit-leads"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  popular(params?: OperationParamsMap["reddit-popular"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  post(params: OperationParamsMap["reddit-post"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  postAwards(params: OperationParamsMap["reddit-post-awards"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  postsByIds(params: OperationParamsMap["reddit-posts-by-ids"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["reddit-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchComments(params: OperationParamsMap["reddit-search-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchPeople(params: OperationParamsMap["reddit-search-people"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditAbout(params: OperationParamsMap["reddit-subreddit-about"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditComments(params: OperationParamsMap["reddit-subreddit-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditFlairs(params: OperationParamsMap["reddit-subreddit-flairs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditHighlights(params: OperationParamsMap["reddit-subreddit-highlights"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditLeaderboardCategories(params: OperationParamsMap["reddit-subreddit-leaderboard-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditPosts(params: OperationParamsMap["reddit-subreddit-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditRules(params: OperationParamsMap["reddit-subreddit-rules"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditUserFlairs(params: OperationParamsMap["reddit-subreddit-user-flairs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditWiki(params: OperationParamsMap["reddit-subreddit-wiki"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditsDiscover(params?: OperationParamsMap["reddit-subreddits-discover"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditsPosts(params: OperationParamsMap["reddit-subreddits-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditsSearch(params: OperationParamsMap["reddit-subreddits-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditsSuggest(params: OperationParamsMap["reddit-subreddits-suggest"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topics(params?: OperationParamsMap["reddit-topics"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topicsBroad(params?: OperationParamsMap["reddit-topics-broad"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topicsSearch(params: OperationParamsMap["reddit-topics-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trends(params?: OperationParamsMap["reddit-trends"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userComments(params: OperationParamsMap["reddit-user-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userPosts(params: OperationParamsMap["reddit-user-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userProfile(params: OperationParamsMap["reddit-user-profile"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  archiveCommentsIds(...args: OperationRequestArgs<"reddit-archive-comments-ids">): Promise<OperationResponseMap["reddit-archive-comments-ids"]>;
  archiveCommentsSearch(...args: OperationRequestArgs<"reddit-archive-comments-search">): Promise<OperationResponseMap["reddit-archive-comments-search"]>;
  archiveCommentsTree(...args: OperationRequestArgs<"reddit-archive-comments-tree">): Promise<OperationResponseMap["reddit-archive-comments-tree"]>;
  archivePostsIds(...args: OperationRequestArgs<"reddit-archive-posts-ids">): Promise<OperationResponseMap["reddit-archive-posts-ids"]>;
  archivePostsSearch(...args: OperationRequestArgs<"reddit-archive-posts-search">): Promise<OperationResponseMap["reddit-archive-posts-search"]>;
  archiveSubredditsSearch(...args: OperationRequestArgs<"reddit-archive-subreddits-search">): Promise<OperationResponseMap["reddit-archive-subreddits-search"]>;
  archiveTimeSeries(...args: OperationRequestArgs<"reddit-archive-time-series">): Promise<OperationResponseMap["reddit-archive-time-series"]>;
  comment(...args: OperationRequestArgs<"reddit-comment">): Promise<OperationResponseMap["reddit-comment"]>;
  commentAwards(...args: OperationRequestArgs<"reddit-comment-awards">): Promise<OperationResponseMap["reddit-comment-awards"]>;
  comments(...args: OperationRequestArgs<"reddit-comments">): Promise<OperationResponseMap["reddit-comments"]>;
  domainPosts(...args: OperationRequestArgs<"reddit-domain-posts">): Promise<OperationResponseMap["reddit-domain-posts"]>;
  leads(...args: OperationRequestArgs<"reddit-leads">): Promise<OperationResponseMap["reddit-leads"]>;
  popular(...args: OperationRequestArgs<"reddit-popular">): Promise<OperationResponseMap["reddit-popular"]>;
  post(...args: OperationRequestArgs<"reddit-post">): Promise<OperationResponseMap["reddit-post"]>;
  postAwards(...args: OperationRequestArgs<"reddit-post-awards">): Promise<OperationResponseMap["reddit-post-awards"]>;
  postsByIds(...args: OperationRequestArgs<"reddit-posts-by-ids">): Promise<OperationResponseMap["reddit-posts-by-ids"]>;
  search(...args: OperationRequestArgs<"reddit-search">): Promise<OperationResponseMap["reddit-search"]>;
  searchComments(...args: OperationRequestArgs<"reddit-search-comments">): Promise<OperationResponseMap["reddit-search-comments"]>;
  searchPeople(...args: OperationRequestArgs<"reddit-search-people">): Promise<OperationResponseMap["reddit-search-people"]>;
  subredditAbout(...args: OperationRequestArgs<"reddit-subreddit-about">): Promise<OperationResponseMap["reddit-subreddit-about"]>;
  subredditComments(...args: OperationRequestArgs<"reddit-subreddit-comments">): Promise<OperationResponseMap["reddit-subreddit-comments"]>;
  subredditFlairs(...args: OperationRequestArgs<"reddit-subreddit-flairs">): Promise<OperationResponseMap["reddit-subreddit-flairs"]>;
  subredditHighlights(...args: OperationRequestArgs<"reddit-subreddit-highlights">): Promise<OperationResponseMap["reddit-subreddit-highlights"]>;
  subredditLeaderboardCategories(...args: OperationRequestArgs<"reddit-subreddit-leaderboard-categories">): Promise<OperationResponseMap["reddit-subreddit-leaderboard-categories"]>;
  subredditPosts(...args: OperationRequestArgs<"reddit-subreddit-posts">): Promise<OperationResponseMap["reddit-subreddit-posts"]>;
  subredditRules(...args: OperationRequestArgs<"reddit-subreddit-rules">): Promise<OperationResponseMap["reddit-subreddit-rules"]>;
  subredditUserFlairs(...args: OperationRequestArgs<"reddit-subreddit-user-flairs">): Promise<OperationResponseMap["reddit-subreddit-user-flairs"]>;
  subredditWiki(...args: OperationRequestArgs<"reddit-subreddit-wiki">): Promise<OperationResponseMap["reddit-subreddit-wiki"]>;
  subredditsDiscover(...args: OperationRequestArgs<"reddit-subreddits-discover">): Promise<OperationResponseMap["reddit-subreddits-discover"]>;
  subredditsPosts(...args: OperationRequestArgs<"reddit-subreddits-posts">): Promise<OperationResponseMap["reddit-subreddits-posts"]>;
  subredditsSearch(...args: OperationRequestArgs<"reddit-subreddits-search">): Promise<OperationResponseMap["reddit-subreddits-search"]>;
  subredditsSuggest(...args: OperationRequestArgs<"reddit-subreddits-suggest">): Promise<OperationResponseMap["reddit-subreddits-suggest"]>;
  topics(...args: OperationRequestArgs<"reddit-topics">): Promise<OperationResponseMap["reddit-topics"]>;
  topicsBroad(...args: OperationRequestArgs<"reddit-topics-broad">): Promise<OperationResponseMap["reddit-topics-broad"]>;
  topicsSearch(...args: OperationRequestArgs<"reddit-topics-search">): Promise<OperationResponseMap["reddit-topics-search"]>;
  trends(...args: OperationRequestArgs<"reddit-trends">): Promise<OperationResponseMap["reddit-trends"]>;
  userComments(...args: OperationRequestArgs<"reddit-user-comments">): Promise<OperationResponseMap["reddit-user-comments"]>;
  userPosts(...args: OperationRequestArgs<"reddit-user-posts">): Promise<OperationResponseMap["reddit-user-posts"]>;
  userProfile(...args: OperationRequestArgs<"reddit-user-profile">): Promise<OperationResponseMap["reddit-user-profile"]>;
}
export { RedditClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default RedditClient;
