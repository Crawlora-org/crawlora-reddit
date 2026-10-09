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
  comments(params: OperationParamsMap["reddit-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  domainPosts(params: OperationParamsMap["reddit-domain-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leads(params: OperationParamsMap["reddit-leads"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  post(params: OperationParamsMap["reddit-post"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["reddit-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditAbout(params: OperationParamsMap["reddit-subreddit-about"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditComments(params: OperationParamsMap["reddit-subreddit-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditPosts(params: OperationParamsMap["reddit-subreddit-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  subredditsPosts(params: OperationParamsMap["reddit-subreddits-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trends(params?: OperationParamsMap["reddit-trends"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userComments(params: OperationParamsMap["reddit-user-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userPosts(params: OperationParamsMap["reddit-user-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  comments(params: OperationParamsMap["reddit-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  domainPosts(params: OperationParamsMap["reddit-domain-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leads(params: OperationParamsMap["reddit-leads"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  post(params: OperationParamsMap["reddit-post"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["reddit-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditAbout(params: OperationParamsMap["reddit-subreddit-about"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditComments(params: OperationParamsMap["reddit-subreddit-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditPosts(params: OperationParamsMap["reddit-subreddit-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  subredditsPosts(params: OperationParamsMap["reddit-subreddits-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trends(params?: OperationParamsMap["reddit-trends"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userComments(params: OperationParamsMap["reddit-user-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userPosts(params: OperationParamsMap["reddit-user-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  comments(...args: OperationRequestArgs<"reddit-comments">): Promise<OperationResponseMap["reddit-comments"]>;
  domainPosts(...args: OperationRequestArgs<"reddit-domain-posts">): Promise<OperationResponseMap["reddit-domain-posts"]>;
  leads(...args: OperationRequestArgs<"reddit-leads">): Promise<OperationResponseMap["reddit-leads"]>;
  post(...args: OperationRequestArgs<"reddit-post">): Promise<OperationResponseMap["reddit-post"]>;
  search(...args: OperationRequestArgs<"reddit-search">): Promise<OperationResponseMap["reddit-search"]>;
  subredditAbout(...args: OperationRequestArgs<"reddit-subreddit-about">): Promise<OperationResponseMap["reddit-subreddit-about"]>;
  subredditComments(...args: OperationRequestArgs<"reddit-subreddit-comments">): Promise<OperationResponseMap["reddit-subreddit-comments"]>;
  subredditPosts(...args: OperationRequestArgs<"reddit-subreddit-posts">): Promise<OperationResponseMap["reddit-subreddit-posts"]>;
  subredditsPosts(...args: OperationRequestArgs<"reddit-subreddits-posts">): Promise<OperationResponseMap["reddit-subreddits-posts"]>;
  trends(...args: OperationRequestArgs<"reddit-trends">): Promise<OperationResponseMap["reddit-trends"]>;
  userComments(...args: OperationRequestArgs<"reddit-user-comments">): Promise<OperationResponseMap["reddit-user-comments"]>;
  userPosts(...args: OperationRequestArgs<"reddit-user-posts">): Promise<OperationResponseMap["reddit-user-posts"]>;
}
export { RedditClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default RedditClient;
