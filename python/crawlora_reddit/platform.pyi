from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelRedditUserPostsResponseDoc = TypedDict('ModelRedditUserPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditUserPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditUserPostsResponse = TypedDict('ModelRedditUserPostsResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'source': NotRequired[ModelRedditSourceDetail],
    'username': NotRequired[str],
}, total=False)

ModelRedditSourceDetail = TypedDict('ModelRedditSourceDetail', {
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelRedditPost = TypedDict('ModelRedditPost', {
    'author': NotRequired[ModelRedditAuthor],
    'award_count': NotRequired[int],
    'comment_count': NotRequired[int],
    'created': NotRequired[str],
    'created_utc': NotRequired[int],
    'domain': NotRequired[str],
    'estimated_downvotes': NotRequired[int],
    'estimated_upvotes': NotRequired[int],
    'flair': NotRequired[str],
    'id': NotRequired[str],
    'is_self': NotRequired[bool],
    'is_video': NotRequired[bool],
    'locked': NotRequired[bool],
    'name': NotRequired[str],
    'over_18': NotRequired[bool],
    'permalink': NotRequired[str],
    'score': NotRequired[int],
    'selftext': NotRequired[str],
    'source_feed_url': NotRequired[str],
    'stickied': NotRequired[bool],
    'subreddit': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'upvote_ratio': NotRequired[float],
    'url': NotRequired[str],
    'vote_counts_estimated': NotRequired[bool],
}, total=False)

ModelRedditAuthor = TypedDict('ModelRedditAuthor', {
    'name': NotRequired[str],
    'profile_url': NotRequired[str],
}, total=False)

ModelRedditPagination = TypedDict('ModelRedditPagination', {
    'after': NotRequired[str],
    'limit': NotRequired[int],
}, total=False)

ModelRedditUserCommentsResponseDoc = TypedDict('ModelRedditUserCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditUserCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditUserCommentsResponse = TypedDict('ModelRedditUserCommentsResponse', {
    'comments': NotRequired[list[ModelRedditComment]],
    'pagination': NotRequired[ModelRedditPagination],
    'source': NotRequired[ModelRedditSourceDetail],
    'username': NotRequired[str],
}, total=False)

ModelRedditComment = TypedDict('ModelRedditComment', {
    'author': NotRequired[ModelRedditAuthor],
    'award_count': NotRequired[int],
    'body': NotRequired[str],
    'created': NotRequired[str],
    'created_utc': NotRequired[int],
    'depth': NotRequired[int],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'parent_id': NotRequired[str],
    'permalink': NotRequired[str],
    'replies': NotRequired[list[ModelRedditComment]],
    'score': NotRequired[int],
}, total=False)

ModelRedditTrendsResponseDoc = TypedDict('ModelRedditTrendsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditTrendsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditTrendsResponse = TypedDict('ModelRedditTrendsResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'time': NotRequired[str],
}, total=False)

ModelRedditMultiSubredditPostsResponseDoc = TypedDict('ModelRedditMultiSubredditPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditMultiSubredditPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditMultiSubredditPostsResponse = TypedDict('ModelRedditMultiSubredditPostsResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddits': NotRequired[list[str]],
    'time': NotRequired[str],
}, total=False)

ModelRedditSubredditPostsResponseDoc = TypedDict('ModelRedditSubredditPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditPostsResponse = TypedDict('ModelRedditSubredditPostsResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
    'time': NotRequired[str],
}, total=False)

ModelRedditSubredditCommentsResponseDoc = TypedDict('ModelRedditSubredditCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditCommentsResponse = TypedDict('ModelRedditSubredditCommentsResponse', {
    'comments': NotRequired[list[ModelRedditComment]],
    'pagination': NotRequired[ModelRedditPagination],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditSubredditAboutResponseDoc = TypedDict('ModelRedditSubredditAboutResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditAboutResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditAboutResponse = TypedDict('ModelRedditSubredditAboutResponse', {
    'display_name': NotRequired[str],
    'feed_url': NotRequired[str],
    'latest_post_created': NotRequired[str],
    'latest_post_created_utc': NotRequired[int],
    'public_url': NotRequired[str],
    'recent_post_count': NotRequired[int],
    'sample_posts': NotRequired[list[ModelRedditPost]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelRedditSearchResponseDoc = TypedDict('ModelRedditSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSearchResponse = TypedDict('ModelRedditSearchResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
    'time': NotRequired[str],
}, total=False)

ModelRedditPostResponseDoc = TypedDict('ModelRedditPostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditPostResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditPostResponse = TypedDict('ModelRedditPostResponse', {
    'metrics_source': NotRequired[ModelRedditSourceDetail],
    'post': NotRequired[ModelRedditPost],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

ModelRedditLeadsResponseDoc = TypedDict('ModelRedditLeadsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditleadsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditleadsResponse = TypedDict('ModelRedditleadsResponse', {
    'classifier': NotRequired[str],
    'degraded': NotRequired[bool],
    'leads': NotRequired[list[ModelRedditleadsLead]],
    'min_score': NotRequired[int],
    'model': NotRequired[str],
    'query': NotRequired[str],
    'stats': NotRequired[ModelRedditleadsStats],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditleadsStats = TypedDict('ModelRedditleadsStats', {
    'classified': NotRequired[int],
    'prefiltered': NotRequired[int],
    'returned': NotRequired[int],
    'scanned': NotRequired[int],
}, total=False)

ModelRedditleadsLead = TypedDict('ModelRedditleadsLead', {
    'author': NotRequired[str],
    'comment_count': NotRequired[int],
    'created': NotRequired[str],
    'permalink': NotRequired[str],
    'post_score': NotRequired[int],
    'reason': NotRequired[str],
    'score': NotRequired[int],
    'signals': NotRequired[list[ModelRedditleadsSignal]],
    'subreddit': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelRedditleadsSignal = TypedDict('ModelRedditleadsSignal', {
    'id': NotRequired[str],
    'label': NotRequired[str],
}, total=False)

ModelRedditDomainPostsResponseDoc = TypedDict('ModelRedditDomainPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditDomainPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditDomainPostsResponse = TypedDict('ModelRedditDomainPostsResponse', {
    'domain': NotRequired[str],
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'time': NotRequired[str],
}, total=False)

ModelRedditCommentsResponseDoc = TypedDict('ModelRedditCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditCommentsResponse = TypedDict('ModelRedditCommentsResponse', {
    'comments': NotRequired[list[ModelRedditComment]],
    'metrics_source': NotRequired[ModelRedditSourceDetail],
    'post': NotRequired[ModelRedditPost],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

RedditCommentsResponse = ModelRedditCommentsResponseDoc
RedditCommentsParams = TypedDict('RedditCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditDomainPostsResponse = ModelRedditDomainPostsResponseDoc
RedditDomainPostsParams = TypedDict('RedditDomainPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'domain': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditLeadsResponse = ModelRedditLeadsResponseDoc
RedditLeadsParams = TypedDict('RedditLeadsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'min_score': NotRequired[int],
    'classifier': NotRequired[Literal['auto', 'heuristic', 'llm']],
}, total=False)

RedditPostResponse = ModelRedditPostResponseDoc
RedditPostParams = TypedDict('RedditPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditSearchResponse = ModelRedditSearchResponseDoc
RedditSearchParams = TypedDict('RedditSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditAboutResponse = ModelRedditSubredditAboutResponseDoc
RedditSubredditAboutParams = TypedDict('RedditSubredditAboutParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
}, total=False)

RedditSubredditCommentsResponse = ModelRedditSubredditCommentsResponseDoc
RedditSubredditCommentsParams = TypedDict('RedditSubredditCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditPostsResponse = ModelRedditSubredditPostsResponseDoc
RedditSubredditPostsParams = TypedDict('RedditSubredditPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsPostsResponse = ModelRedditMultiSubredditPostsResponseDoc
RedditSubredditsPostsParams = TypedDict('RedditSubredditsPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddits': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTrendsResponse = ModelRedditTrendsResponseDoc
RedditTrendsParams = TypedDict('RedditTrendsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sort': NotRequired[Literal['hot', 'new', 'rising', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserCommentsResponse = ModelRedditUserCommentsResponseDoc
RedditUserCommentsParams = TypedDict('RedditUserCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserPostsResponse = ModelRedditUserPostsResponseDoc
RedditUserPostsParams = TypedDict('RedditUserPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

class RedditGroup:
    @overload
    def comments(self, **params: Unpack[RedditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def comments(self, **params: Unpack[RedditCommentsTextResponseParams]) -> str: ...
    @overload
    def comments(self, **params: Unpack[RedditCommentsDefaultParams]) -> RedditCommentsResponse: ...
    @overload
    def domain_posts(self, **params: Unpack[RedditDomainPostsStreamParams]) -> BinaryIO: ...
    @overload
    def domain_posts(self, **params: Unpack[RedditDomainPostsTextResponseParams]) -> str: ...
    @overload
    def domain_posts(self, **params: Unpack[RedditDomainPostsDefaultParams]) -> RedditDomainPostsResponse: ...
    @overload
    def leads(self, **params: Unpack[RedditLeadsStreamParams]) -> BinaryIO: ...
    @overload
    def leads(self, **params: Unpack[RedditLeadsTextResponseParams]) -> str: ...
    @overload
    def leads(self, **params: Unpack[RedditLeadsDefaultParams]) -> RedditLeadsResponse: ...
    @overload
    def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    def subreddit_about(self, **params: Unpack[RedditSubredditAboutStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_about(self, **params: Unpack[RedditSubredditAboutTextResponseParams]) -> str: ...
    @overload
    def subreddit_about(self, **params: Unpack[RedditSubredditAboutDefaultParams]) -> RedditSubredditAboutResponse: ...
    @overload
    def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsTextResponseParams]) -> str: ...
    @overload
    def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsDefaultParams]) -> RedditSubredditCommentsResponse: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    def trends(self, **params: Unpack[RedditTrendsStreamParams]) -> BinaryIO: ...
    @overload
    def trends(self, **params: Unpack[RedditTrendsTextResponseParams]) -> str: ...
    @overload
    def trends(self, **params: Unpack[RedditTrendsDefaultParams]) -> RedditTrendsResponse: ...
    @overload
    def user_comments(self, **params: Unpack[RedditUserCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def user_comments(self, **params: Unpack[RedditUserCommentsTextResponseParams]) -> str: ...
    @overload
    def user_comments(self, **params: Unpack[RedditUserCommentsDefaultParams]) -> RedditUserCommentsResponse: ...
    @overload
    def user_posts(self, **params: Unpack[RedditUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    def user_posts(self, **params: Unpack[RedditUserPostsTextResponseParams]) -> str: ...
    @overload
    def user_posts(self, **params: Unpack[RedditUserPostsDefaultParams]) -> RedditUserPostsResponse: ...

OperationId = Literal[
    'reddit-comments',
    'reddit-domain-posts',
    'reddit-leads',
    'reddit-post',
    'reddit-search',
    'reddit-subreddit-about',
    'reddit-subreddit-comments',
    'reddit-subreddit-posts',
    'reddit-subreddits-posts',
    'reddit-trends',
    'reddit-user-comments',
    'reddit-user-posts',
]

class CrawloraClient:
    reddit: RedditGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-comments'],
        params: RedditCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-domain-posts'],
        params: RedditDomainPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditDomainPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-leads'],
        params: RedditLeadsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditLeadsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-post'],
        params: RedditPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-search'],
        params: RedditSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-about'],
        params: RedditSubredditAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditAboutResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-comments'],
        params: RedditSubredditCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-posts'],
        params: RedditSubredditPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddits-posts'],
        params: RedditSubredditsPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-trends'],
        params: RedditTrendsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTrendsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-user-comments'],
        params: RedditUserCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditUserCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-user-posts'],
        params: RedditUserPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditUserPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-comments'],
        params: RedditCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-domain-posts'],
        params: RedditDomainPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditDomainPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-leads'],
        params: RedditLeadsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditLeadsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-post'],
        params: RedditPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-search'],
        params: RedditSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-about'],
        params: RedditSubredditAboutParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditAboutResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-comments'],
        params: RedditSubredditCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-posts'],
        params: RedditSubredditPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddits-posts'],
        params: RedditSubredditsPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-trends'],
        params: RedditTrendsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTrendsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-user-comments'],
        params: RedditUserCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditUserCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-user-posts'],
        params: RedditUserPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditUserPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class RedditClient(CrawloraClient):
    def __enter__(self) -> RedditClient: ...
    @overload
    def comments(self, **params: Unpack[RedditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def comments(self, **params: Unpack[RedditCommentsTextResponseParams]) -> str: ...
    @overload
    def comments(self, **params: Unpack[RedditCommentsDefaultParams]) -> RedditCommentsResponse: ...
    @overload
    def domain_posts(self, **params: Unpack[RedditDomainPostsStreamParams]) -> BinaryIO: ...
    @overload
    def domain_posts(self, **params: Unpack[RedditDomainPostsTextResponseParams]) -> str: ...
    @overload
    def domain_posts(self, **params: Unpack[RedditDomainPostsDefaultParams]) -> RedditDomainPostsResponse: ...
    @overload
    def leads(self, **params: Unpack[RedditLeadsStreamParams]) -> BinaryIO: ...
    @overload
    def leads(self, **params: Unpack[RedditLeadsTextResponseParams]) -> str: ...
    @overload
    def leads(self, **params: Unpack[RedditLeadsDefaultParams]) -> RedditLeadsResponse: ...
    @overload
    def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    def subreddit_about(self, **params: Unpack[RedditSubredditAboutStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_about(self, **params: Unpack[RedditSubredditAboutTextResponseParams]) -> str: ...
    @overload
    def subreddit_about(self, **params: Unpack[RedditSubredditAboutDefaultParams]) -> RedditSubredditAboutResponse: ...
    @overload
    def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsTextResponseParams]) -> str: ...
    @overload
    def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsDefaultParams]) -> RedditSubredditCommentsResponse: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    def trends(self, **params: Unpack[RedditTrendsStreamParams]) -> BinaryIO: ...
    @overload
    def trends(self, **params: Unpack[RedditTrendsTextResponseParams]) -> str: ...
    @overload
    def trends(self, **params: Unpack[RedditTrendsDefaultParams]) -> RedditTrendsResponse: ...
    @overload
    def user_comments(self, **params: Unpack[RedditUserCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def user_comments(self, **params: Unpack[RedditUserCommentsTextResponseParams]) -> str: ...
    @overload
    def user_comments(self, **params: Unpack[RedditUserCommentsDefaultParams]) -> RedditUserCommentsResponse: ...
    @overload
    def user_posts(self, **params: Unpack[RedditUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    def user_posts(self, **params: Unpack[RedditUserPostsTextResponseParams]) -> str: ...
    @overload
    def user_posts(self, **params: Unpack[RedditUserPostsDefaultParams]) -> RedditUserPostsResponse: ...

class AsyncRedditClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncRedditClient: ...
    reddit: _AsyncRedditGroup
    @overload
    async def comments(self, **params: Unpack[RedditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def comments(self, **params: Unpack[RedditCommentsTextResponseParams]) -> str: ...
    @overload
    async def comments(self, **params: Unpack[RedditCommentsDefaultParams]) -> RedditCommentsResponse: ...
    @overload
    async def domain_posts(self, **params: Unpack[RedditDomainPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def domain_posts(self, **params: Unpack[RedditDomainPostsTextResponseParams]) -> str: ...
    @overload
    async def domain_posts(self, **params: Unpack[RedditDomainPostsDefaultParams]) -> RedditDomainPostsResponse: ...
    @overload
    async def leads(self, **params: Unpack[RedditLeadsStreamParams]) -> BinaryIO: ...
    @overload
    async def leads(self, **params: Unpack[RedditLeadsTextResponseParams]) -> str: ...
    @overload
    async def leads(self, **params: Unpack[RedditLeadsDefaultParams]) -> RedditLeadsResponse: ...
    @overload
    async def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    async def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    async def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    async def subreddit_about(self, **params: Unpack[RedditSubredditAboutStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_about(self, **params: Unpack[RedditSubredditAboutTextResponseParams]) -> str: ...
    @overload
    async def subreddit_about(self, **params: Unpack[RedditSubredditAboutDefaultParams]) -> RedditSubredditAboutResponse: ...
    @overload
    async def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsDefaultParams]) -> RedditSubredditCommentsResponse: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    async def trends(self, **params: Unpack[RedditTrendsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends(self, **params: Unpack[RedditTrendsTextResponseParams]) -> str: ...
    @overload
    async def trends(self, **params: Unpack[RedditTrendsDefaultParams]) -> RedditTrendsResponse: ...
    @overload
    async def user_comments(self, **params: Unpack[RedditUserCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_comments(self, **params: Unpack[RedditUserCommentsTextResponseParams]) -> str: ...
    @overload
    async def user_comments(self, **params: Unpack[RedditUserCommentsDefaultParams]) -> RedditUserCommentsResponse: ...
    @overload
    async def user_posts(self, **params: Unpack[RedditUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_posts(self, **params: Unpack[RedditUserPostsTextResponseParams]) -> str: ...
    @overload
    async def user_posts(self, **params: Unpack[RedditUserPostsDefaultParams]) -> RedditUserPostsResponse: ...

class _AsyncRedditGroup:
    @overload
    async def comments(self, **params: Unpack[RedditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def comments(self, **params: Unpack[RedditCommentsTextResponseParams]) -> str: ...
    @overload
    async def comments(self, **params: Unpack[RedditCommentsDefaultParams]) -> RedditCommentsResponse: ...
    @overload
    async def domain_posts(self, **params: Unpack[RedditDomainPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def domain_posts(self, **params: Unpack[RedditDomainPostsTextResponseParams]) -> str: ...
    @overload
    async def domain_posts(self, **params: Unpack[RedditDomainPostsDefaultParams]) -> RedditDomainPostsResponse: ...
    @overload
    async def leads(self, **params: Unpack[RedditLeadsStreamParams]) -> BinaryIO: ...
    @overload
    async def leads(self, **params: Unpack[RedditLeadsTextResponseParams]) -> str: ...
    @overload
    async def leads(self, **params: Unpack[RedditLeadsDefaultParams]) -> RedditLeadsResponse: ...
    @overload
    async def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    async def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    async def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    async def subreddit_about(self, **params: Unpack[RedditSubredditAboutStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_about(self, **params: Unpack[RedditSubredditAboutTextResponseParams]) -> str: ...
    @overload
    async def subreddit_about(self, **params: Unpack[RedditSubredditAboutDefaultParams]) -> RedditSubredditAboutResponse: ...
    @overload
    async def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_comments(self, **params: Unpack[RedditSubredditCommentsDefaultParams]) -> RedditSubredditCommentsResponse: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    async def trends(self, **params: Unpack[RedditTrendsStreamParams]) -> BinaryIO: ...
    @overload
    async def trends(self, **params: Unpack[RedditTrendsTextResponseParams]) -> str: ...
    @overload
    async def trends(self, **params: Unpack[RedditTrendsDefaultParams]) -> RedditTrendsResponse: ...
    @overload
    async def user_comments(self, **params: Unpack[RedditUserCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_comments(self, **params: Unpack[RedditUserCommentsTextResponseParams]) -> str: ...
    @overload
    async def user_comments(self, **params: Unpack[RedditUserCommentsDefaultParams]) -> RedditUserCommentsResponse: ...
    @overload
    async def user_posts(self, **params: Unpack[RedditUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_posts(self, **params: Unpack[RedditUserPostsTextResponseParams]) -> str: ...
    @overload
    async def user_posts(self, **params: Unpack[RedditUserPostsDefaultParams]) -> RedditUserPostsResponse: ...

RedditCommentsDefaultParams = TypedDict('RedditCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditCommentsTextResponseParams = TypedDict('RedditCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditCommentsStreamParams = TypedDict('RedditCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditDomainPostsDefaultParams = TypedDict('RedditDomainPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'domain': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditDomainPostsTextResponseParams = TypedDict('RedditDomainPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'domain': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditDomainPostsStreamParams = TypedDict('RedditDomainPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'domain': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditLeadsDefaultParams = TypedDict('RedditLeadsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'min_score': NotRequired[int],
    'classifier': NotRequired[Literal['auto', 'heuristic', 'llm']],
}, total=False)

RedditLeadsTextResponseParams = TypedDict('RedditLeadsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'min_score': NotRequired[int],
    'classifier': NotRequired[Literal['auto', 'heuristic', 'llm']],
}, total=False)

RedditLeadsStreamParams = TypedDict('RedditLeadsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'min_score': NotRequired[int],
    'classifier': NotRequired[Literal['auto', 'heuristic', 'llm']],
}, total=False)

RedditPostDefaultParams = TypedDict('RedditPostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditPostTextResponseParams = TypedDict('RedditPostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditPostStreamParams = TypedDict('RedditPostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'include_metrics': NotRequired[bool],
}, total=False)

RedditSearchDefaultParams = TypedDict('RedditSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSearchTextResponseParams = TypedDict('RedditSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSearchStreamParams = TypedDict('RedditSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'subreddit': NotRequired[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditAboutDefaultParams = TypedDict('RedditSubredditAboutDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
}, total=False)

RedditSubredditAboutTextResponseParams = TypedDict('RedditSubredditAboutTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
}, total=False)

RedditSubredditAboutStreamParams = TypedDict('RedditSubredditAboutStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
}, total=False)

RedditSubredditCommentsDefaultParams = TypedDict('RedditSubredditCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditCommentsTextResponseParams = TypedDict('RedditSubredditCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditCommentsStreamParams = TypedDict('RedditSubredditCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditPostsDefaultParams = TypedDict('RedditSubredditPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditPostsTextResponseParams = TypedDict('RedditSubredditPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditPostsStreamParams = TypedDict('RedditSubredditPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsPostsDefaultParams = TypedDict('RedditSubredditsPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddits': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsPostsTextResponseParams = TypedDict('RedditSubredditsPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddits': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsPostsStreamParams = TypedDict('RedditSubredditsPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddits': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTrendsDefaultParams = TypedDict('RedditTrendsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sort': NotRequired[Literal['hot', 'new', 'rising', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTrendsTextResponseParams = TypedDict('RedditTrendsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sort': NotRequired[Literal['hot', 'new', 'rising', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTrendsStreamParams = TypedDict('RedditTrendsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sort': NotRequired[Literal['hot', 'new', 'rising', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserCommentsDefaultParams = TypedDict('RedditUserCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserCommentsTextResponseParams = TypedDict('RedditUserCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserCommentsStreamParams = TypedDict('RedditUserCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserPostsDefaultParams = TypedDict('RedditUserPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserPostsTextResponseParams = TypedDict('RedditUserPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditUserPostsStreamParams = TypedDict('RedditUserPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)
