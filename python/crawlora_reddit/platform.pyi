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

ModelRedditUserProfileResponseDoc = TypedDict('ModelRedditUserProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditUserProfileResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditUserProfileResponse = TypedDict('ModelRedditUserProfileResponse', {
    'accepts_chats': NotRequired[bool],
    'accepts_followers': NotRequired[bool],
    'banner_url': NotRequired[str],
    'comment_count': NotRequired[int],
    'created': NotRequired[str],
    'created_utc': NotRequired[int],
    'display_name': NotRequired[str],
    'icon_url': NotRequired[str],
    'is_employee': NotRequired[bool],
    'is_gilded': NotRequired[bool],
    'karma': NotRequired[int],
    'name': NotRequired[str],
    'over_18': NotRequired[bool],
    'post_count': NotRequired[int],
    'public_description': NotRequired[str],
    'public_url': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'title': NotRequired[str],
    'trophy_count': NotRequired[int],
    'username': NotRequired[str],
}, total=False)

ModelRedditSourceDetail = TypedDict('ModelRedditSourceDetail', {
    'type': NotRequired[str],
    'url': NotRequired[str],
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

ModelRedditPost = TypedDict('ModelRedditPost', {
    'author': NotRequired[ModelRedditAuthor],
    'award_count': NotRequired[int],
    'comment_count': NotRequired[int],
    'created': NotRequired[str],
    'created_utc': NotRequired[int],
    'crosspost_count': NotRequired[int],
    'distinguished': NotRequired[str],
    'domain': NotRequired[str],
    'edited': NotRequired[str],
    'edited_utc': NotRequired[int],
    'estimated_downvotes': NotRequired[int],
    'estimated_upvotes': NotRequired[int],
    'flair': NotRequired[str],
    'id': NotRequired[str],
    'is_archived': NotRequired[bool],
    'is_contest_mode': NotRequired[bool],
    'is_crosspostable': NotRequired[bool],
    'is_original_content': NotRequired[bool],
    'is_score_hidden': NotRequired[bool],
    'is_self': NotRequired[bool],
    'is_spoiler': NotRequired[bool],
    'is_video': NotRequired[bool],
    'language_code': NotRequired[str],
    'locked': NotRequired[bool],
    'name': NotRequired[str],
    'over_18': NotRequired[bool],
    'permalink': NotRequired[str],
    'score': NotRequired[int],
    'selftext': NotRequired[str],
    'source_feed_url': NotRequired[str],
    'stickied': NotRequired[bool],
    'subreddit': NotRequired[str],
    'suggested_comment_sort': NotRequired[str],
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
    'distinguished': NotRequired[str],
    'edited': NotRequired[str],
    'edited_utc': NotRequired[int],
    'id': NotRequired[str],
    'is_archived': NotRequired[bool],
    'is_locked': NotRequired[bool],
    'is_op': NotRequired[bool],
    'is_score_hidden': NotRequired[bool],
    'is_stickied': NotRequired[bool],
    'name': NotRequired[str],
    'parent_id': NotRequired[str],
    'permalink': NotRequired[str],
    'post_id': NotRequired[str],
    'post_title': NotRequired[str],
    'replies': NotRequired[list[ModelRedditComment]],
    'score': NotRequired[int],
    'subreddit': NotRequired[str],
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

ModelRedditTopicSearchResponseDoc = TypedDict('ModelRedditTopicSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditTopicSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditTopicSearchResponse = TypedDict('ModelRedditTopicSearchResponse', {
    'query': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'topics': NotRequired[list[ModelRedditTopic]],
}, total=False)

ModelRedditTopic = TypedDict('ModelRedditTopic', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'parents': NotRequired[list[str]],
    'title': NotRequired[str],
    'topic_type': NotRequired[str],
}, total=False)

ModelRedditBroadTopicsResponseDoc = TypedDict('ModelRedditBroadTopicsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditBroadTopicsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditBroadTopicsResponse = TypedDict('ModelRedditBroadTopicsResponse', {
    'source': NotRequired[ModelRedditSourceDetail],
    'topics': NotRequired[list[ModelRedditBroadTopic]],
}, total=False)

ModelRedditBroadTopic = TypedDict('ModelRedditBroadTopic', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'is_preselected': NotRequired[bool],
}, total=False)

ModelRedditTopicsResponseDoc = TypedDict('ModelRedditTopicsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditTopicsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditTopicsResponse = TypedDict('ModelRedditTopicsResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'source': NotRequired[ModelRedditSourceDetail],
    'topics': NotRequired[list[ModelRedditTopic]],
}, total=False)

ModelRedditSubredditSuggestResponseDoc = TypedDict('ModelRedditSubredditSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditSuggestResponse = TypedDict('ModelRedditSubredditSuggestResponse', {
    'query': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddits': NotRequired[list[ModelRedditCommunity]],
}, total=False)

ModelRedditCommunity = TypedDict('ModelRedditCommunity', {
    'banner_url': NotRequired[str],
    'created': NotRequired[str],
    'created_utc': NotRequired[int],
    'display_name': NotRequired[str],
    'icon_url': NotRequired[str],
    'is_quarantined': NotRequired[bool],
    'name': NotRequired[str],
    'over_18': NotRequired[bool],
    'public_description': NotRequired[str],
    'public_url': NotRequired[str],
    'subreddit': NotRequired[str],
    'subreddit_type': NotRequired[str],
    'subscribers': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelRedditSubredditSearchResponseDoc = TypedDict('ModelRedditSubredditSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditSearchResponse = TypedDict('ModelRedditSubredditSearchResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'query': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddits': NotRequired[list[ModelRedditCommunity]],
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
    'warnings': NotRequired[list[str]],
}, total=False)

ModelRedditSubredditsDiscoverResponseDoc = TypedDict('ModelRedditSubredditsDiscoverResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditsDiscoverResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditsDiscoverResponse = TypedDict('ModelRedditSubredditsDiscoverResponse', {
    'feed': NotRequired[str],
    'pagination': NotRequired[ModelRedditPagination],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddits': NotRequired[list[ModelRedditCommunity]],
}, total=False)

ModelRedditSubredditWikiResponseDoc = TypedDict('ModelRedditSubredditWikiResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditWikiResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditWikiResponse = TypedDict('ModelRedditSubredditWikiResponse', {
    'page': NotRequired[str],
    'page_content': NotRequired[ModelRedditWikiPageContent],
    'page_tree': NotRequired[list[ModelRedditWikiPageNode]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditWikiPageNode = TypedDict('ModelRedditWikiPageNode', {
    'depth': NotRequired[int],
    'name': NotRequired[str],
    'page_present': NotRequired[bool],
    'parent': NotRequired[str],
    'path': NotRequired[str],
}, total=False)

ModelRedditWikiPageContent = TypedDict('ModelRedditWikiPageContent', {
    'content_html': NotRequired[str],
    'content_markdown': NotRequired[str],
    'content_richtext': NotRequired[str],
    'is_revisable': NotRequired[bool],
    'name': NotRequired[str],
    'revision_count': NotRequired[int],
    'status': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelRedditUserFlairsResponseDoc = TypedDict('ModelRedditUserFlairsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditUserFlairsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditUserFlairsResponse = TypedDict('ModelRedditUserFlairsResponse', {
    'flairs': NotRequired[list[ModelRedditFlairTemplate]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditFlairTemplate = TypedDict('ModelRedditFlairTemplate', {
    'allowable_content': NotRequired[str],
    'background_color': NotRequired[str],
    'id': NotRequired[str],
    'is_editable': NotRequired[bool],
    'is_mod_only': NotRequired[bool],
    'max_emojis': NotRequired[int],
    'richtext': NotRequired[str],
    'text': NotRequired[str],
    'text_color': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelRedditSubredditRulesResponseDoc = TypedDict('ModelRedditSubredditRulesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditRulesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditRulesResponse = TypedDict('ModelRedditSubredditRulesResponse', {
    'rules': NotRequired[list[ModelRedditSubredditRule]],
    'site_rules': NotRequired[list[ModelRedditSiteRule]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditSiteRule = TypedDict('ModelRedditSiteRule', {
    'text': NotRequired[str],
}, total=False)

ModelRedditSubredditRule = TypedDict('ModelRedditSubredditRule', {
    'content_html': NotRequired[str],
    'description': NotRequired[str],
    'name': NotRequired[str],
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

ModelRedditLeaderboardCategoriesResponseDoc = TypedDict('ModelRedditLeaderboardCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditLeaderboardCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditLeaderboardCategoriesResponse = TypedDict('ModelRedditLeaderboardCategoriesResponse', {
    'categories': NotRequired[list[ModelRedditLeaderboardCategory]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditLeaderboardCategory = TypedDict('ModelRedditLeaderboardCategory', {
    'deeplink_url': NotRequired[str],
    'description': NotRequired[str],
    'footer_text': NotRequired[str],
    'id': NotRequired[str],
    'is_active': NotRequired[bool],
    'last_updated_label': NotRequired[str],
    'name': NotRequired[str],
    'periods': NotRequired[list[ModelRedditLeaderboardPeriod]],
    'update_interval_label': NotRequired[str],
}, total=False)

ModelRedditLeaderboardPeriod = TypedDict('ModelRedditLeaderboardPeriod', {
    'id': NotRequired[str],
    'is_active': NotRequired[bool],
    'name': NotRequired[str],
}, total=False)

ModelRedditSubredditHighlightsResponseDoc = TypedDict('ModelRedditSubredditHighlightsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditHighlightsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditHighlightsResponse = TypedDict('ModelRedditSubredditHighlightsResponse', {
    'highlights': NotRequired[list[ModelRedditHighlight]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditHighlight = TypedDict('ModelRedditHighlight', {
    'expires_at': NotRequired[str],
    'label': NotRequired[str],
    'post': NotRequired[ModelRedditPost],
}, total=False)

ModelRedditSubredditFlairsResponseDoc = TypedDict('ModelRedditSubredditFlairsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSubredditFlairsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSubredditFlairsResponse = TypedDict('ModelRedditSubredditFlairsResponse', {
    'flairs': NotRequired[list[ModelRedditFlairTemplate]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
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
    'allowed_post_types': NotRequired[list[str]],
    'banner_url': NotRequired[str],
    'community_leaderboard_enabled': NotRequired[bool],
    'created': NotRequired[str],
    'created_utc': NotRequired[int],
    'display_name': NotRequired[str],
    'feed_url': NotRequired[str],
    'icon_url': NotRequired[str],
    'is_crossposting_allowed': NotRequired[bool],
    'is_quarantined': NotRequired[bool],
    'is_spoiler_available': NotRequired[bool],
    'latest_post_created': NotRequired[str],
    'latest_post_created_utc': NotRequired[int],
    'over_18': NotRequired[bool],
    'primary_color': NotRequired[str],
    'public_description': NotRequired[str],
    'public_url': NotRequired[str],
    'recent_post_count': NotRequired[int],
    'sample_posts': NotRequired[list[ModelRedditPost]],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
    'subscribers': NotRequired[int],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'weekly_active_users': NotRequired[int],
    'weekly_contributions': NotRequired[int],
}, total=False)

ModelRedditSearchPeopleResponseDoc = TypedDict('ModelRedditSearchPeopleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSearchPeopleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSearchPeopleResponse = TypedDict('ModelRedditSearchPeopleResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'people': NotRequired[list[ModelRedditPerson]],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

ModelRedditPerson = TypedDict('ModelRedditPerson', {
    'accepts_followers': NotRequired[bool],
    'display_name': NotRequired[str],
    'icon_url': NotRequired[str],
    'karma': NotRequired[int],
    'name': NotRequired[str],
    'over_18': NotRequired[bool],
    'public_url': NotRequired[str],
    'username': NotRequired[str],
}, total=False)

ModelRedditSearchCommentsResponseDoc = TypedDict('ModelRedditSearchCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditSearchCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditSearchCommentsResponse = TypedDict('ModelRedditSearchCommentsResponse', {
    'comments': NotRequired[list[ModelRedditComment]],
    'pagination': NotRequired[ModelRedditPagination],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
    'time': NotRequired[str],
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

ModelRedditPostsByIdsResponseDoc = TypedDict('ModelRedditPostsByIdsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditPostsByIdsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditPostsByIdsResponse = TypedDict('ModelRedditPostsByIdsResponse', {
    'missing_ids': NotRequired[list[str]],
    'posts': NotRequired[list[ModelRedditPost]],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

ModelRedditPostAwardsResponseDoc = TypedDict('ModelRedditPostAwardsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditPostAwardsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditPostAwardsResponse = TypedDict('ModelRedditPostAwardsResponse', {
    'awards': NotRequired[list[ModelRedditPostAwarding]],
    'post_id': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

ModelRedditPostAwarding = TypedDict('ModelRedditPostAwarding', {
    'award': NotRequired[ModelRedditAward],
    'gold_count': NotRequired[int],
    'total': NotRequired[int],
}, total=False)

ModelRedditAward = TypedDict('ModelRedditAward', {
    'description': NotRequired[str],
    'icon_url': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'tags': NotRequired[list[str]],
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

ModelRedditPopularResponseDoc = TypedDict('ModelRedditPopularResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditPopularResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditPopularResponse = TypedDict('ModelRedditPopularResponse', {
    'pagination': NotRequired[ModelRedditPagination],
    'posts': NotRequired[list[ModelRedditPost]],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'time': NotRequired[str],
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

ModelRedditCommentAwardsResponseDoc = TypedDict('ModelRedditCommentAwardsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditCommentAwardsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditCommentAwardsResponse = TypedDict('ModelRedditCommentAwardsResponse', {
    'awards': NotRequired[list[ModelRedditPostAwarding]],
    'comment_id': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

ModelRedditCommentDetailResponseDoc = TypedDict('ModelRedditCommentDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditCommentDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditCommentDetailResponse = TypedDict('ModelRedditCommentDetailResponse', {
    'comment': NotRequired[ModelRedditComment],
    'source': NotRequired[ModelRedditSourceDetail],
}, total=False)

ModelRedditArchiveTimeSeriesResponseDoc = TypedDict('ModelRedditArchiveTimeSeriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchiveTimeSeriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchiveTimeSeriesResponse = TypedDict('ModelRedditArchiveTimeSeriesResponse', {
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'metric': NotRequired[str],
    'points': NotRequired[list[ModelRedditArchiveTimeSeriesPoint]],
    'precision': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditArchiveTimeSeriesPoint = TypedDict('ModelRedditArchiveTimeSeriesPoint', {
    'date': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelRedditArchiveSubredditsSearchResponseDoc = TypedDict('ModelRedditArchiveSubredditsSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchiveSubredditsSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchiveSubredditsSearchResponse = TypedDict('ModelRedditArchiveSubredditsSearchResponse', {
    'limit': NotRequired[int],
    'max_subscribers': NotRequired[int],
    'min_subscribers': NotRequired[int],
    'over_18': NotRequired[bool],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'sort_by': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddits': NotRequired[list[ModelRedditArchiveSubreddit]],
}, total=False)

ModelRedditArchiveSubreddit = TypedDict('ModelRedditArchiveSubreddit', {
    'created_utc': NotRequired[int],
    'display_name': NotRequired[str],
    'id': NotRequired[str],
    'over_18': NotRequired[bool],
    'retrieved_on': NotRequired[int],
    'subscribers': NotRequired[int],
}, total=False)

ModelRedditArchivePostsSearchResponseDoc = TypedDict('ModelRedditArchivePostsSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchivePostsSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchivePostsSearchResponse = TypedDict('ModelRedditArchivePostsSearchResponse', {
    'author': NotRequired[str],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'limit': NotRequired[int],
    'posts': NotRequired[list[ModelRedditArchivePost]],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
    'url': NotRequired[str],
    'url_exact': NotRequired[bool],
}, total=False)

ModelRedditArchivePost = TypedDict('ModelRedditArchivePost', {
    'author': NotRequired[str],
    'author_flair_text': NotRequired[str],
    'author_fullname': NotRequired[str],
    'created_utc': NotRequired[int],
    'crosspost_parent': NotRequired[str],
    'distinguished': NotRequired[str],
    'id': NotRequired[str],
    'link_flair_text': NotRequired[str],
    'num_comments': NotRequired[int],
    'over_18': NotRequired[bool],
    'post_hint': NotRequired[str],
    'removed_by_category': NotRequired[str],
    'retrieved_on': NotRequired[int],
    'score': NotRequired[int],
    'selftext': NotRequired[str],
    'spoiler': NotRequired[bool],
    'subreddit': NotRequired[str],
    'subreddit_id': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelRedditArchivePostsIdsResponseDoc = TypedDict('ModelRedditArchivePostsIdsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchivePostsIdsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchivePostsIdsResponse = TypedDict('ModelRedditArchivePostsIdsResponse', {
    'missing_ids': NotRequired[list[str]],
    'posts': NotRequired[list[ModelRedditArchivePost]],
    'requested_count': NotRequired[int],
    'returned_count': NotRequired[int],
    'source': NotRequired[ModelRedditArchiveBatchSource],
}, total=False)

ModelRedditArchiveBatchSource = TypedDict('ModelRedditArchiveBatchSource', {
    'requests': NotRequired[int],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentsTreeResponseDoc = TypedDict('ModelRedditArchiveCommentsTreeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchiveCommentsTreeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentsTreeResponse = TypedDict('ModelRedditArchiveCommentsTreeResponse', {
    'comments': NotRequired[list[ModelRedditArchiveCommentTreeEntry]],
    'limit': NotRequired[int],
    'parent_id': NotRequired[str],
    'post_id': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'start_breadth': NotRequired[int],
    'start_depth': NotRequired[int],
}, total=False)

ModelRedditArchiveCommentTreeEntry = TypedDict('ModelRedditArchiveCommentTreeEntry', {
    'comment': NotRequired[ModelRedditArchiveCommentTreeNode],
    'kind': NotRequired[Literal['t1', 'more']],
    'more': NotRequired[ModelRedditArchiveMoreComments],
}, total=False)

ModelRedditArchiveMoreComments = TypedDict('ModelRedditArchiveMoreComments', {
    'children': NotRequired[list[str]],
    'count': NotRequired[int],
    'depth': NotRequired[int],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'parent_id': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentTreeNode = TypedDict('ModelRedditArchiveCommentTreeNode', {
    'comment': NotRequired[ModelRedditArchiveComment],
    'replies': NotRequired[list[ModelRedditArchiveCommentTreeEntry]],
}, total=False)

ModelRedditArchiveComment = TypedDict('ModelRedditArchiveComment', {
    'author': NotRequired[str],
    'author_flair_text': NotRequired[str],
    'author_fullname': NotRequired[str],
    'body': NotRequired[str],
    'created_utc': NotRequired[int],
    'depth': NotRequired[int],
    'distinguished': NotRequired[str],
    'id': NotRequired[str],
    'link_id': NotRequired[str],
    'name': NotRequired[str],
    'parent_id': NotRequired[str],
    'permalink': NotRequired[str],
    'removed_by_category': NotRequired[str],
    'retrieved_on': NotRequired[int],
    'score': NotRequired[int],
    'subreddit': NotRequired[str],
    'subreddit_id': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentsSearchResponseDoc = TypedDict('ModelRedditArchiveCommentsSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchiveCommentsSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentsSearchResponse = TypedDict('ModelRedditArchiveCommentsSearchResponse', {
    'author': NotRequired[str],
    'comments': NotRequired[list[ModelRedditArchiveComment]],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'limit': NotRequired[int],
    'link_id': NotRequired[str],
    'parent_id': NotRequired[str],
    'query': NotRequired[str],
    'sort': NotRequired[str],
    'source': NotRequired[ModelRedditSourceDetail],
    'subreddit': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentsIdsResponseDoc = TypedDict('ModelRedditArchiveCommentsIdsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelRedditArchiveCommentsIdsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelRedditArchiveCommentsIdsResponse = TypedDict('ModelRedditArchiveCommentsIdsResponse', {
    'comments': NotRequired[list[ModelRedditArchiveComment]],
    'missing_ids': NotRequired[list[str]],
    'requested_count': NotRequired[int],
    'returned_count': NotRequired[int],
    'source': NotRequired[ModelRedditArchiveBatchSource],
}, total=False)

RedditArchiveCommentsIdsResponse = ModelRedditArchiveCommentsIdsResponseDoc
RedditArchiveCommentsIdsParams = TypedDict('RedditArchiveCommentsIdsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

RedditArchiveCommentsSearchResponse = ModelRedditArchiveCommentsSearchResponseDoc
RedditArchiveCommentsSearchParams = TypedDict('RedditArchiveCommentsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'query': NotRequired[str],
    'link_id': NotRequired[str],
    'parent_id': NotRequired[str],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveCommentsTreeResponse = ModelRedditArchiveCommentsTreeResponseDoc
RedditArchiveCommentsTreeParams = TypedDict('RedditArchiveCommentsTreeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'parent_id': NotRequired[str],
    'limit': NotRequired[int],
    'start_breadth': NotRequired[int],
    'start_depth': NotRequired[int],
}, total=False)

RedditArchivePostsIdsResponse = ModelRedditArchivePostsIdsResponseDoc
RedditArchivePostsIdsParams = TypedDict('RedditArchivePostsIdsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

RedditArchivePostsSearchResponse = ModelRedditArchivePostsSearchResponseDoc
RedditArchivePostsSearchParams = TypedDict('RedditArchivePostsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': NotRequired[str],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'url': NotRequired[str],
    'url_exact': NotRequired[bool],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveSubredditsSearchResponse = ModelRedditArchiveSubredditsSearchResponseDoc
RedditArchiveSubredditsSearchParams = TypedDict('RedditArchiveSubredditsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'min_subscribers': NotRequired[int],
    'max_subscribers': NotRequired[int],
    'over_18': NotRequired[bool],
    'sort_by': NotRequired[Literal['created_utc', 'subscribers', 'subreddit']],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveTimeSeriesResponse = ModelRedditArchiveTimeSeriesResponseDoc
RedditArchiveTimeSeriesParams = TypedDict('RedditArchiveTimeSeriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'metric': Required[Literal['posts_count', 'comments_count', 'posts_score_sum', 'comments_score_sum', 'posts_retrieval_delay_seconds_sum', 'comments_retrieval_delay_seconds_sum', 'subreddit_subscribers']],
    'subreddit': NotRequired[str],
    'precision': Required[Literal['year', 'quarter', 'month', 'week', 'day', 'hour', 'minute']],
    'created_after': Required[str],
    'created_before': Required[str],
}, total=False)

RedditCommentResponse = ModelRedditCommentDetailResponseDoc
RedditCommentParams = TypedDict('RedditCommentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

RedditCommentAwardsResponse = ModelRedditCommentAwardsResponseDoc
RedditCommentAwardsParams = TypedDict('RedditCommentAwardsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
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

RedditPopularResponse = ModelRedditPopularResponseDoc
RedditPopularParams = TypedDict('RedditPopularParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sort': NotRequired[Literal['hot', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditPostResponse = ModelRedditPostResponseDoc
RedditPostParams = TypedDict('RedditPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

RedditPostAwardsResponse = ModelRedditPostAwardsResponseDoc
RedditPostAwardsParams = TypedDict('RedditPostAwardsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

RedditPostsByIdsResponse = ModelRedditPostsByIdsResponseDoc
RedditPostsByIdsParams = TypedDict('RedditPostsByIdsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
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

RedditSearchCommentsResponse = ModelRedditSearchCommentsResponseDoc
RedditSearchCommentsParams = TypedDict('RedditSearchCommentsParams', {
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

RedditSearchPeopleResponse = ModelRedditSearchPeopleResponseDoc
RedditSearchPeopleParams = TypedDict('RedditSearchPeopleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
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

RedditSubredditFlairsResponse = ModelRedditSubredditFlairsResponseDoc
RedditSubredditFlairsParams = TypedDict('RedditSubredditFlairsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditHighlightsResponse = ModelRedditSubredditHighlightsResponseDoc
RedditSubredditHighlightsParams = TypedDict('RedditSubredditHighlightsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditLeaderboardCategoriesResponse = ModelRedditLeaderboardCategoriesResponseDoc
RedditSubredditLeaderboardCategoriesParams = TypedDict('RedditSubredditLeaderboardCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditPostsResponse = ModelRedditSubredditPostsResponseDoc
RedditSubredditPostsParams = TypedDict('RedditSubredditPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising', 'controversial']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditRulesResponse = ModelRedditSubredditRulesResponseDoc
RedditSubredditRulesParams = TypedDict('RedditSubredditRulesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditUserFlairsResponse = ModelRedditUserFlairsResponseDoc
RedditSubredditUserFlairsParams = TypedDict('RedditSubredditUserFlairsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditWikiResponse = ModelRedditSubredditWikiResponseDoc
RedditSubredditWikiParams = TypedDict('RedditSubredditWikiParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'subreddit': Required[str],
    'page': NotRequired[str],
}, total=False)

RedditSubredditsDiscoverResponse = ModelRedditSubredditsDiscoverResponseDoc
RedditSubredditsDiscoverParams = TypedDict('RedditSubredditsDiscoverParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'feed': NotRequired[Literal['popular', 'new', 'default']],
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

RedditSubredditsSearchResponse = ModelRedditSubredditSearchResponseDoc
RedditSubredditsSearchParams = TypedDict('RedditSubredditsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsSuggestResponse = ModelRedditSubredditSuggestResponseDoc
RedditSubredditsSuggestParams = TypedDict('RedditSubredditsSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

RedditTopicsResponse = ModelRedditTopicsResponseDoc
RedditTopicsParams = TypedDict('RedditTopicsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTopicsBroadResponse = ModelRedditBroadTopicsResponseDoc
RedditTopicsBroadParams = TypedDict('RedditTopicsBroadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

RedditTopicsSearchResponse = ModelRedditTopicSearchResponseDoc
RedditTopicsSearchParams = TypedDict('RedditTopicsSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
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

RedditUserProfileResponse = ModelRedditUserProfileResponseDoc
RedditUserProfileParams = TypedDict('RedditUserProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

class RedditGroup:
    @overload
    def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsStreamParams]) -> BinaryIO: ...
    @overload
    def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsTextResponseParams]) -> str: ...
    @overload
    def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsDefaultParams]) -> RedditArchiveCommentsIdsResponse: ...
    @overload
    def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchTextResponseParams]) -> str: ...
    @overload
    def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchDefaultParams]) -> RedditArchiveCommentsSearchResponse: ...
    @overload
    def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeStreamParams]) -> BinaryIO: ...
    @overload
    def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeTextResponseParams]) -> str: ...
    @overload
    def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeDefaultParams]) -> RedditArchiveCommentsTreeResponse: ...
    @overload
    def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsStreamParams]) -> BinaryIO: ...
    @overload
    def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsTextResponseParams]) -> str: ...
    @overload
    def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsDefaultParams]) -> RedditArchivePostsIdsResponse: ...
    @overload
    def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchTextResponseParams]) -> str: ...
    @overload
    def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchDefaultParams]) -> RedditArchivePostsSearchResponse: ...
    @overload
    def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchDefaultParams]) -> RedditArchiveSubredditsSearchResponse: ...
    @overload
    def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesStreamParams]) -> BinaryIO: ...
    @overload
    def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesTextResponseParams]) -> str: ...
    @overload
    def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesDefaultParams]) -> RedditArchiveTimeSeriesResponse: ...
    @overload
    def comment(self, **params: Unpack[RedditCommentStreamParams]) -> BinaryIO: ...
    @overload
    def comment(self, **params: Unpack[RedditCommentTextResponseParams]) -> str: ...
    @overload
    def comment(self, **params: Unpack[RedditCommentDefaultParams]) -> RedditCommentResponse: ...
    @overload
    def comment_awards(self, **params: Unpack[RedditCommentAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def comment_awards(self, **params: Unpack[RedditCommentAwardsTextResponseParams]) -> str: ...
    @overload
    def comment_awards(self, **params: Unpack[RedditCommentAwardsDefaultParams]) -> RedditCommentAwardsResponse: ...
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
    def popular(self, **params: Unpack[RedditPopularStreamParams]) -> BinaryIO: ...
    @overload
    def popular(self, **params: Unpack[RedditPopularTextResponseParams]) -> str: ...
    @overload
    def popular(self, **params: Unpack[RedditPopularDefaultParams]) -> RedditPopularResponse: ...
    @overload
    def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    def post_awards(self, **params: Unpack[RedditPostAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def post_awards(self, **params: Unpack[RedditPostAwardsTextResponseParams]) -> str: ...
    @overload
    def post_awards(self, **params: Unpack[RedditPostAwardsDefaultParams]) -> RedditPostAwardsResponse: ...
    @overload
    def posts_by_ids(self, **params: Unpack[RedditPostsByIdsStreamParams]) -> BinaryIO: ...
    @overload
    def posts_by_ids(self, **params: Unpack[RedditPostsByIdsTextResponseParams]) -> str: ...
    @overload
    def posts_by_ids(self, **params: Unpack[RedditPostsByIdsDefaultParams]) -> RedditPostsByIdsResponse: ...
    @overload
    def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    def search_comments(self, **params: Unpack[RedditSearchCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def search_comments(self, **params: Unpack[RedditSearchCommentsTextResponseParams]) -> str: ...
    @overload
    def search_comments(self, **params: Unpack[RedditSearchCommentsDefaultParams]) -> RedditSearchCommentsResponse: ...
    @overload
    def search_people(self, **params: Unpack[RedditSearchPeopleStreamParams]) -> BinaryIO: ...
    @overload
    def search_people(self, **params: Unpack[RedditSearchPeopleTextResponseParams]) -> str: ...
    @overload
    def search_people(self, **params: Unpack[RedditSearchPeopleDefaultParams]) -> RedditSearchPeopleResponse: ...
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
    def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsTextResponseParams]) -> str: ...
    @overload
    def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsDefaultParams]) -> RedditSubredditFlairsResponse: ...
    @overload
    def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsTextResponseParams]) -> str: ...
    @overload
    def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsDefaultParams]) -> RedditSubredditHighlightsResponse: ...
    @overload
    def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesTextResponseParams]) -> str: ...
    @overload
    def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesDefaultParams]) -> RedditSubredditLeaderboardCategoriesResponse: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    def subreddit_rules(self, **params: Unpack[RedditSubredditRulesStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_rules(self, **params: Unpack[RedditSubredditRulesTextResponseParams]) -> str: ...
    @overload
    def subreddit_rules(self, **params: Unpack[RedditSubredditRulesDefaultParams]) -> RedditSubredditRulesResponse: ...
    @overload
    def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsTextResponseParams]) -> str: ...
    @overload
    def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsDefaultParams]) -> RedditSubredditUserFlairsResponse: ...
    @overload
    def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiTextResponseParams]) -> str: ...
    @overload
    def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiDefaultParams]) -> RedditSubredditWikiResponse: ...
    @overload
    def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverTextResponseParams]) -> str: ...
    @overload
    def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverDefaultParams]) -> RedditSubredditsDiscoverResponse: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    def subreddits_search(self, **params: Unpack[RedditSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_search(self, **params: Unpack[RedditSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    def subreddits_search(self, **params: Unpack[RedditSubredditsSearchDefaultParams]) -> RedditSubredditsSearchResponse: ...
    @overload
    def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestTextResponseParams]) -> str: ...
    @overload
    def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestDefaultParams]) -> RedditSubredditsSuggestResponse: ...
    @overload
    def topics(self, **params: Unpack[RedditTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def topics(self, **params: Unpack[RedditTopicsTextResponseParams]) -> str: ...
    @overload
    def topics(self, **params: Unpack[RedditTopicsDefaultParams]) -> RedditTopicsResponse: ...
    @overload
    def topics_broad(self, **params: Unpack[RedditTopicsBroadStreamParams]) -> BinaryIO: ...
    @overload
    def topics_broad(self, **params: Unpack[RedditTopicsBroadTextResponseParams]) -> str: ...
    @overload
    def topics_broad(self, **params: Unpack[RedditTopicsBroadDefaultParams]) -> RedditTopicsBroadResponse: ...
    @overload
    def topics_search(self, **params: Unpack[RedditTopicsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def topics_search(self, **params: Unpack[RedditTopicsSearchTextResponseParams]) -> str: ...
    @overload
    def topics_search(self, **params: Unpack[RedditTopicsSearchDefaultParams]) -> RedditTopicsSearchResponse: ...
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
    @overload
    def user_profile(self, **params: Unpack[RedditUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    def user_profile(self, **params: Unpack[RedditUserProfileTextResponseParams]) -> str: ...
    @overload
    def user_profile(self, **params: Unpack[RedditUserProfileDefaultParams]) -> RedditUserProfileResponse: ...

OperationId = Literal[
    'reddit-archive-comments-ids',
    'reddit-archive-comments-search',
    'reddit-archive-comments-tree',
    'reddit-archive-posts-ids',
    'reddit-archive-posts-search',
    'reddit-archive-subreddits-search',
    'reddit-archive-time-series',
    'reddit-comment',
    'reddit-comment-awards',
    'reddit-comments',
    'reddit-domain-posts',
    'reddit-leads',
    'reddit-popular',
    'reddit-post',
    'reddit-post-awards',
    'reddit-posts-by-ids',
    'reddit-search',
    'reddit-search-comments',
    'reddit-search-people',
    'reddit-subreddit-about',
    'reddit-subreddit-comments',
    'reddit-subreddit-flairs',
    'reddit-subreddit-highlights',
    'reddit-subreddit-leaderboard-categories',
    'reddit-subreddit-posts',
    'reddit-subreddit-rules',
    'reddit-subreddit-user-flairs',
    'reddit-subreddit-wiki',
    'reddit-subreddits-discover',
    'reddit-subreddits-posts',
    'reddit-subreddits-search',
    'reddit-subreddits-suggest',
    'reddit-topics',
    'reddit-topics-broad',
    'reddit-topics-search',
    'reddit-trends',
    'reddit-user-comments',
    'reddit-user-posts',
    'reddit-user-profile',
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
        operation_id: Literal['reddit-archive-comments-ids'],
        params: RedditArchiveCommentsIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveCommentsIdsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-archive-comments-search'],
        params: RedditArchiveCommentsSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveCommentsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-archive-comments-tree'],
        params: RedditArchiveCommentsTreeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveCommentsTreeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-archive-posts-ids'],
        params: RedditArchivePostsIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchivePostsIdsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-archive-posts-search'],
        params: RedditArchivePostsSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchivePostsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-archive-subreddits-search'],
        params: RedditArchiveSubredditsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveSubredditsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-archive-time-series'],
        params: RedditArchiveTimeSeriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveTimeSeriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-comment'],
        params: RedditCommentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditCommentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-comment-awards'],
        params: RedditCommentAwardsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditCommentAwardsResponse: ...
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
        operation_id: Literal['reddit-popular'],
        params: RedditPopularParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPopularResponse: ...
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
        operation_id: Literal['reddit-post-awards'],
        params: RedditPostAwardsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPostAwardsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-posts-by-ids'],
        params: RedditPostsByIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPostsByIdsResponse: ...
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
        operation_id: Literal['reddit-search-comments'],
        params: RedditSearchCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSearchCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-search-people'],
        params: RedditSearchPeopleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSearchPeopleResponse: ...
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
        operation_id: Literal['reddit-subreddit-flairs'],
        params: RedditSubredditFlairsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditFlairsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-highlights'],
        params: RedditSubredditHighlightsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditHighlightsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-leaderboard-categories'],
        params: RedditSubredditLeaderboardCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditLeaderboardCategoriesResponse: ...
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
        operation_id: Literal['reddit-subreddit-rules'],
        params: RedditSubredditRulesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditRulesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-user-flairs'],
        params: RedditSubredditUserFlairsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditUserFlairsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddit-wiki'],
        params: RedditSubredditWikiParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditWikiResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddits-discover'],
        params: RedditSubredditsDiscoverParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsDiscoverResponse: ...
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
        operation_id: Literal['reddit-subreddits-search'],
        params: RedditSubredditsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-subreddits-suggest'],
        params: RedditSubredditsSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-topics'],
        params: RedditTopicsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTopicsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-topics-broad'],
        params: RedditTopicsBroadParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTopicsBroadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['reddit-topics-search'],
        params: RedditTopicsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTopicsSearchResponse: ...
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
        operation_id: Literal['reddit-user-profile'],
        params: RedditUserProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditUserProfileResponse: ...
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
        operation_id: Literal['reddit-archive-comments-ids'],
        params: RedditArchiveCommentsIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveCommentsIdsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-archive-comments-search'],
        params: RedditArchiveCommentsSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveCommentsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-archive-comments-tree'],
        params: RedditArchiveCommentsTreeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveCommentsTreeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-archive-posts-ids'],
        params: RedditArchivePostsIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchivePostsIdsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-archive-posts-search'],
        params: RedditArchivePostsSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchivePostsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-archive-subreddits-search'],
        params: RedditArchiveSubredditsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveSubredditsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-archive-time-series'],
        params: RedditArchiveTimeSeriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditArchiveTimeSeriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-comment'],
        params: RedditCommentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditCommentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-comment-awards'],
        params: RedditCommentAwardsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditCommentAwardsResponse: ...
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
        operation_id: Literal['reddit-popular'],
        params: RedditPopularParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPopularResponse: ...
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
        operation_id: Literal['reddit-post-awards'],
        params: RedditPostAwardsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPostAwardsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-posts-by-ids'],
        params: RedditPostsByIdsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditPostsByIdsResponse: ...
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
        operation_id: Literal['reddit-search-comments'],
        params: RedditSearchCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSearchCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-search-people'],
        params: RedditSearchPeopleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSearchPeopleResponse: ...
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
        operation_id: Literal['reddit-subreddit-flairs'],
        params: RedditSubredditFlairsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditFlairsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-highlights'],
        params: RedditSubredditHighlightsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditHighlightsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-leaderboard-categories'],
        params: RedditSubredditLeaderboardCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditLeaderboardCategoriesResponse: ...
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
        operation_id: Literal['reddit-subreddit-rules'],
        params: RedditSubredditRulesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditRulesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-user-flairs'],
        params: RedditSubredditUserFlairsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditUserFlairsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddit-wiki'],
        params: RedditSubredditWikiParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditWikiResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddits-discover'],
        params: RedditSubredditsDiscoverParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsDiscoverResponse: ...
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
        operation_id: Literal['reddit-subreddits-search'],
        params: RedditSubredditsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-subreddits-suggest'],
        params: RedditSubredditsSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditSubredditsSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-topics'],
        params: RedditTopicsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTopicsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-topics-broad'],
        params: RedditTopicsBroadParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTopicsBroadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['reddit-topics-search'],
        params: RedditTopicsSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditTopicsSearchResponse: ...
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
        operation_id: Literal['reddit-user-profile'],
        params: RedditUserProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> RedditUserProfileResponse: ...
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
    def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsStreamParams]) -> BinaryIO: ...
    @overload
    def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsTextResponseParams]) -> str: ...
    @overload
    def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsDefaultParams]) -> RedditArchiveCommentsIdsResponse: ...
    @overload
    def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchTextResponseParams]) -> str: ...
    @overload
    def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchDefaultParams]) -> RedditArchiveCommentsSearchResponse: ...
    @overload
    def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeStreamParams]) -> BinaryIO: ...
    @overload
    def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeTextResponseParams]) -> str: ...
    @overload
    def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeDefaultParams]) -> RedditArchiveCommentsTreeResponse: ...
    @overload
    def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsStreamParams]) -> BinaryIO: ...
    @overload
    def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsTextResponseParams]) -> str: ...
    @overload
    def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsDefaultParams]) -> RedditArchivePostsIdsResponse: ...
    @overload
    def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchTextResponseParams]) -> str: ...
    @overload
    def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchDefaultParams]) -> RedditArchivePostsSearchResponse: ...
    @overload
    def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchDefaultParams]) -> RedditArchiveSubredditsSearchResponse: ...
    @overload
    def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesStreamParams]) -> BinaryIO: ...
    @overload
    def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesTextResponseParams]) -> str: ...
    @overload
    def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesDefaultParams]) -> RedditArchiveTimeSeriesResponse: ...
    @overload
    def comment(self, **params: Unpack[RedditCommentStreamParams]) -> BinaryIO: ...
    @overload
    def comment(self, **params: Unpack[RedditCommentTextResponseParams]) -> str: ...
    @overload
    def comment(self, **params: Unpack[RedditCommentDefaultParams]) -> RedditCommentResponse: ...
    @overload
    def comment_awards(self, **params: Unpack[RedditCommentAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def comment_awards(self, **params: Unpack[RedditCommentAwardsTextResponseParams]) -> str: ...
    @overload
    def comment_awards(self, **params: Unpack[RedditCommentAwardsDefaultParams]) -> RedditCommentAwardsResponse: ...
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
    def popular(self, **params: Unpack[RedditPopularStreamParams]) -> BinaryIO: ...
    @overload
    def popular(self, **params: Unpack[RedditPopularTextResponseParams]) -> str: ...
    @overload
    def popular(self, **params: Unpack[RedditPopularDefaultParams]) -> RedditPopularResponse: ...
    @overload
    def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    def post_awards(self, **params: Unpack[RedditPostAwardsStreamParams]) -> BinaryIO: ...
    @overload
    def post_awards(self, **params: Unpack[RedditPostAwardsTextResponseParams]) -> str: ...
    @overload
    def post_awards(self, **params: Unpack[RedditPostAwardsDefaultParams]) -> RedditPostAwardsResponse: ...
    @overload
    def posts_by_ids(self, **params: Unpack[RedditPostsByIdsStreamParams]) -> BinaryIO: ...
    @overload
    def posts_by_ids(self, **params: Unpack[RedditPostsByIdsTextResponseParams]) -> str: ...
    @overload
    def posts_by_ids(self, **params: Unpack[RedditPostsByIdsDefaultParams]) -> RedditPostsByIdsResponse: ...
    @overload
    def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    def search_comments(self, **params: Unpack[RedditSearchCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def search_comments(self, **params: Unpack[RedditSearchCommentsTextResponseParams]) -> str: ...
    @overload
    def search_comments(self, **params: Unpack[RedditSearchCommentsDefaultParams]) -> RedditSearchCommentsResponse: ...
    @overload
    def search_people(self, **params: Unpack[RedditSearchPeopleStreamParams]) -> BinaryIO: ...
    @overload
    def search_people(self, **params: Unpack[RedditSearchPeopleTextResponseParams]) -> str: ...
    @overload
    def search_people(self, **params: Unpack[RedditSearchPeopleDefaultParams]) -> RedditSearchPeopleResponse: ...
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
    def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsTextResponseParams]) -> str: ...
    @overload
    def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsDefaultParams]) -> RedditSubredditFlairsResponse: ...
    @overload
    def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsTextResponseParams]) -> str: ...
    @overload
    def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsDefaultParams]) -> RedditSubredditHighlightsResponse: ...
    @overload
    def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesTextResponseParams]) -> str: ...
    @overload
    def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesDefaultParams]) -> RedditSubredditLeaderboardCategoriesResponse: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    def subreddit_rules(self, **params: Unpack[RedditSubredditRulesStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_rules(self, **params: Unpack[RedditSubredditRulesTextResponseParams]) -> str: ...
    @overload
    def subreddit_rules(self, **params: Unpack[RedditSubredditRulesDefaultParams]) -> RedditSubredditRulesResponse: ...
    @overload
    def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsTextResponseParams]) -> str: ...
    @overload
    def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsDefaultParams]) -> RedditSubredditUserFlairsResponse: ...
    @overload
    def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiStreamParams]) -> BinaryIO: ...
    @overload
    def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiTextResponseParams]) -> str: ...
    @overload
    def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiDefaultParams]) -> RedditSubredditWikiResponse: ...
    @overload
    def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverTextResponseParams]) -> str: ...
    @overload
    def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverDefaultParams]) -> RedditSubredditsDiscoverResponse: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    def subreddits_search(self, **params: Unpack[RedditSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_search(self, **params: Unpack[RedditSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    def subreddits_search(self, **params: Unpack[RedditSubredditsSearchDefaultParams]) -> RedditSubredditsSearchResponse: ...
    @overload
    def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestTextResponseParams]) -> str: ...
    @overload
    def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestDefaultParams]) -> RedditSubredditsSuggestResponse: ...
    @overload
    def topics(self, **params: Unpack[RedditTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def topics(self, **params: Unpack[RedditTopicsTextResponseParams]) -> str: ...
    @overload
    def topics(self, **params: Unpack[RedditTopicsDefaultParams]) -> RedditTopicsResponse: ...
    @overload
    def topics_broad(self, **params: Unpack[RedditTopicsBroadStreamParams]) -> BinaryIO: ...
    @overload
    def topics_broad(self, **params: Unpack[RedditTopicsBroadTextResponseParams]) -> str: ...
    @overload
    def topics_broad(self, **params: Unpack[RedditTopicsBroadDefaultParams]) -> RedditTopicsBroadResponse: ...
    @overload
    def topics_search(self, **params: Unpack[RedditTopicsSearchStreamParams]) -> BinaryIO: ...
    @overload
    def topics_search(self, **params: Unpack[RedditTopicsSearchTextResponseParams]) -> str: ...
    @overload
    def topics_search(self, **params: Unpack[RedditTopicsSearchDefaultParams]) -> RedditTopicsSearchResponse: ...
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
    @overload
    def user_profile(self, **params: Unpack[RedditUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    def user_profile(self, **params: Unpack[RedditUserProfileTextResponseParams]) -> str: ...
    @overload
    def user_profile(self, **params: Unpack[RedditUserProfileDefaultParams]) -> RedditUserProfileResponse: ...

class AsyncRedditClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncRedditClient: ...
    reddit: _AsyncRedditGroup
    @overload
    async def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsTextResponseParams]) -> str: ...
    @overload
    async def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsDefaultParams]) -> RedditArchiveCommentsIdsResponse: ...
    @overload
    async def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchTextResponseParams]) -> str: ...
    @overload
    async def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchDefaultParams]) -> RedditArchiveCommentsSearchResponse: ...
    @overload
    async def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeTextResponseParams]) -> str: ...
    @overload
    async def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeDefaultParams]) -> RedditArchiveCommentsTreeResponse: ...
    @overload
    async def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsTextResponseParams]) -> str: ...
    @overload
    async def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsDefaultParams]) -> RedditArchivePostsIdsResponse: ...
    @overload
    async def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchTextResponseParams]) -> str: ...
    @overload
    async def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchDefaultParams]) -> RedditArchivePostsSearchResponse: ...
    @overload
    async def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    async def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchDefaultParams]) -> RedditArchiveSubredditsSearchResponse: ...
    @overload
    async def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesTextResponseParams]) -> str: ...
    @overload
    async def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesDefaultParams]) -> RedditArchiveTimeSeriesResponse: ...
    @overload
    async def comment(self, **params: Unpack[RedditCommentStreamParams]) -> BinaryIO: ...
    @overload
    async def comment(self, **params: Unpack[RedditCommentTextResponseParams]) -> str: ...
    @overload
    async def comment(self, **params: Unpack[RedditCommentDefaultParams]) -> RedditCommentResponse: ...
    @overload
    async def comment_awards(self, **params: Unpack[RedditCommentAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def comment_awards(self, **params: Unpack[RedditCommentAwardsTextResponseParams]) -> str: ...
    @overload
    async def comment_awards(self, **params: Unpack[RedditCommentAwardsDefaultParams]) -> RedditCommentAwardsResponse: ...
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
    async def popular(self, **params: Unpack[RedditPopularStreamParams]) -> BinaryIO: ...
    @overload
    async def popular(self, **params: Unpack[RedditPopularTextResponseParams]) -> str: ...
    @overload
    async def popular(self, **params: Unpack[RedditPopularDefaultParams]) -> RedditPopularResponse: ...
    @overload
    async def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    async def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    async def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    async def post_awards(self, **params: Unpack[RedditPostAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def post_awards(self, **params: Unpack[RedditPostAwardsTextResponseParams]) -> str: ...
    @overload
    async def post_awards(self, **params: Unpack[RedditPostAwardsDefaultParams]) -> RedditPostAwardsResponse: ...
    @overload
    async def posts_by_ids(self, **params: Unpack[RedditPostsByIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def posts_by_ids(self, **params: Unpack[RedditPostsByIdsTextResponseParams]) -> str: ...
    @overload
    async def posts_by_ids(self, **params: Unpack[RedditPostsByIdsDefaultParams]) -> RedditPostsByIdsResponse: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    async def search_comments(self, **params: Unpack[RedditSearchCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_comments(self, **params: Unpack[RedditSearchCommentsTextResponseParams]) -> str: ...
    @overload
    async def search_comments(self, **params: Unpack[RedditSearchCommentsDefaultParams]) -> RedditSearchCommentsResponse: ...
    @overload
    async def search_people(self, **params: Unpack[RedditSearchPeopleStreamParams]) -> BinaryIO: ...
    @overload
    async def search_people(self, **params: Unpack[RedditSearchPeopleTextResponseParams]) -> str: ...
    @overload
    async def search_people(self, **params: Unpack[RedditSearchPeopleDefaultParams]) -> RedditSearchPeopleResponse: ...
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
    async def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsDefaultParams]) -> RedditSubredditFlairsResponse: ...
    @overload
    async def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsDefaultParams]) -> RedditSubredditHighlightsResponse: ...
    @overload
    async def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesTextResponseParams]) -> str: ...
    @overload
    async def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesDefaultParams]) -> RedditSubredditLeaderboardCategoriesResponse: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    async def subreddit_rules(self, **params: Unpack[RedditSubredditRulesStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_rules(self, **params: Unpack[RedditSubredditRulesTextResponseParams]) -> str: ...
    @overload
    async def subreddit_rules(self, **params: Unpack[RedditSubredditRulesDefaultParams]) -> RedditSubredditRulesResponse: ...
    @overload
    async def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsDefaultParams]) -> RedditSubredditUserFlairsResponse: ...
    @overload
    async def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiTextResponseParams]) -> str: ...
    @overload
    async def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiDefaultParams]) -> RedditSubredditWikiResponse: ...
    @overload
    async def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverTextResponseParams]) -> str: ...
    @overload
    async def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverDefaultParams]) -> RedditSubredditsDiscoverResponse: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    async def subreddits_search(self, **params: Unpack[RedditSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_search(self, **params: Unpack[RedditSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    async def subreddits_search(self, **params: Unpack[RedditSubredditsSearchDefaultParams]) -> RedditSubredditsSearchResponse: ...
    @overload
    async def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestTextResponseParams]) -> str: ...
    @overload
    async def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestDefaultParams]) -> RedditSubredditsSuggestResponse: ...
    @overload
    async def topics(self, **params: Unpack[RedditTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def topics(self, **params: Unpack[RedditTopicsTextResponseParams]) -> str: ...
    @overload
    async def topics(self, **params: Unpack[RedditTopicsDefaultParams]) -> RedditTopicsResponse: ...
    @overload
    async def topics_broad(self, **params: Unpack[RedditTopicsBroadStreamParams]) -> BinaryIO: ...
    @overload
    async def topics_broad(self, **params: Unpack[RedditTopicsBroadTextResponseParams]) -> str: ...
    @overload
    async def topics_broad(self, **params: Unpack[RedditTopicsBroadDefaultParams]) -> RedditTopicsBroadResponse: ...
    @overload
    async def topics_search(self, **params: Unpack[RedditTopicsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def topics_search(self, **params: Unpack[RedditTopicsSearchTextResponseParams]) -> str: ...
    @overload
    async def topics_search(self, **params: Unpack[RedditTopicsSearchDefaultParams]) -> RedditTopicsSearchResponse: ...
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
    @overload
    async def user_profile(self, **params: Unpack[RedditUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def user_profile(self, **params: Unpack[RedditUserProfileTextResponseParams]) -> str: ...
    @overload
    async def user_profile(self, **params: Unpack[RedditUserProfileDefaultParams]) -> RedditUserProfileResponse: ...

class _AsyncRedditGroup:
    @overload
    async def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsTextResponseParams]) -> str: ...
    @overload
    async def archive_comments_ids(self, **params: Unpack[RedditArchiveCommentsIdsDefaultParams]) -> RedditArchiveCommentsIdsResponse: ...
    @overload
    async def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchTextResponseParams]) -> str: ...
    @overload
    async def archive_comments_search(self, **params: Unpack[RedditArchiveCommentsSearchDefaultParams]) -> RedditArchiveCommentsSearchResponse: ...
    @overload
    async def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeTextResponseParams]) -> str: ...
    @overload
    async def archive_comments_tree(self, **params: Unpack[RedditArchiveCommentsTreeDefaultParams]) -> RedditArchiveCommentsTreeResponse: ...
    @overload
    async def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsTextResponseParams]) -> str: ...
    @overload
    async def archive_posts_ids(self, **params: Unpack[RedditArchivePostsIdsDefaultParams]) -> RedditArchivePostsIdsResponse: ...
    @overload
    async def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchTextResponseParams]) -> str: ...
    @overload
    async def archive_posts_search(self, **params: Unpack[RedditArchivePostsSearchDefaultParams]) -> RedditArchivePostsSearchResponse: ...
    @overload
    async def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    async def archive_subreddits_search(self, **params: Unpack[RedditArchiveSubredditsSearchDefaultParams]) -> RedditArchiveSubredditsSearchResponse: ...
    @overload
    async def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesStreamParams]) -> BinaryIO: ...
    @overload
    async def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesTextResponseParams]) -> str: ...
    @overload
    async def archive_time_series(self, **params: Unpack[RedditArchiveTimeSeriesDefaultParams]) -> RedditArchiveTimeSeriesResponse: ...
    @overload
    async def comment(self, **params: Unpack[RedditCommentStreamParams]) -> BinaryIO: ...
    @overload
    async def comment(self, **params: Unpack[RedditCommentTextResponseParams]) -> str: ...
    @overload
    async def comment(self, **params: Unpack[RedditCommentDefaultParams]) -> RedditCommentResponse: ...
    @overload
    async def comment_awards(self, **params: Unpack[RedditCommentAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def comment_awards(self, **params: Unpack[RedditCommentAwardsTextResponseParams]) -> str: ...
    @overload
    async def comment_awards(self, **params: Unpack[RedditCommentAwardsDefaultParams]) -> RedditCommentAwardsResponse: ...
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
    async def popular(self, **params: Unpack[RedditPopularStreamParams]) -> BinaryIO: ...
    @overload
    async def popular(self, **params: Unpack[RedditPopularTextResponseParams]) -> str: ...
    @overload
    async def popular(self, **params: Unpack[RedditPopularDefaultParams]) -> RedditPopularResponse: ...
    @overload
    async def post(self, **params: Unpack[RedditPostStreamParams]) -> BinaryIO: ...
    @overload
    async def post(self, **params: Unpack[RedditPostTextResponseParams]) -> str: ...
    @overload
    async def post(self, **params: Unpack[RedditPostDefaultParams]) -> RedditPostResponse: ...
    @overload
    async def post_awards(self, **params: Unpack[RedditPostAwardsStreamParams]) -> BinaryIO: ...
    @overload
    async def post_awards(self, **params: Unpack[RedditPostAwardsTextResponseParams]) -> str: ...
    @overload
    async def post_awards(self, **params: Unpack[RedditPostAwardsDefaultParams]) -> RedditPostAwardsResponse: ...
    @overload
    async def posts_by_ids(self, **params: Unpack[RedditPostsByIdsStreamParams]) -> BinaryIO: ...
    @overload
    async def posts_by_ids(self, **params: Unpack[RedditPostsByIdsTextResponseParams]) -> str: ...
    @overload
    async def posts_by_ids(self, **params: Unpack[RedditPostsByIdsDefaultParams]) -> RedditPostsByIdsResponse: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[RedditSearchDefaultParams]) -> RedditSearchResponse: ...
    @overload
    async def search_comments(self, **params: Unpack[RedditSearchCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def search_comments(self, **params: Unpack[RedditSearchCommentsTextResponseParams]) -> str: ...
    @overload
    async def search_comments(self, **params: Unpack[RedditSearchCommentsDefaultParams]) -> RedditSearchCommentsResponse: ...
    @overload
    async def search_people(self, **params: Unpack[RedditSearchPeopleStreamParams]) -> BinaryIO: ...
    @overload
    async def search_people(self, **params: Unpack[RedditSearchPeopleTextResponseParams]) -> str: ...
    @overload
    async def search_people(self, **params: Unpack[RedditSearchPeopleDefaultParams]) -> RedditSearchPeopleResponse: ...
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
    async def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_flairs(self, **params: Unpack[RedditSubredditFlairsDefaultParams]) -> RedditSubredditFlairsResponse: ...
    @overload
    async def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_highlights(self, **params: Unpack[RedditSubredditHighlightsDefaultParams]) -> RedditSubredditHighlightsResponse: ...
    @overload
    async def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesTextResponseParams]) -> str: ...
    @overload
    async def subreddit_leaderboard_categories(self, **params: Unpack[RedditSubredditLeaderboardCategoriesDefaultParams]) -> RedditSubredditLeaderboardCategoriesResponse: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_posts(self, **params: Unpack[RedditSubredditPostsDefaultParams]) -> RedditSubredditPostsResponse: ...
    @overload
    async def subreddit_rules(self, **params: Unpack[RedditSubredditRulesStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_rules(self, **params: Unpack[RedditSubredditRulesTextResponseParams]) -> str: ...
    @overload
    async def subreddit_rules(self, **params: Unpack[RedditSubredditRulesDefaultParams]) -> RedditSubredditRulesResponse: ...
    @overload
    async def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsTextResponseParams]) -> str: ...
    @overload
    async def subreddit_user_flairs(self, **params: Unpack[RedditSubredditUserFlairsDefaultParams]) -> RedditSubredditUserFlairsResponse: ...
    @overload
    async def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiTextResponseParams]) -> str: ...
    @overload
    async def subreddit_wiki(self, **params: Unpack[RedditSubredditWikiDefaultParams]) -> RedditSubredditWikiResponse: ...
    @overload
    async def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverTextResponseParams]) -> str: ...
    @overload
    async def subreddits_discover(self, **params: Unpack[RedditSubredditsDiscoverDefaultParams]) -> RedditSubredditsDiscoverResponse: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsTextResponseParams]) -> str: ...
    @overload
    async def subreddits_posts(self, **params: Unpack[RedditSubredditsPostsDefaultParams]) -> RedditSubredditsPostsResponse: ...
    @overload
    async def subreddits_search(self, **params: Unpack[RedditSubredditsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_search(self, **params: Unpack[RedditSubredditsSearchTextResponseParams]) -> str: ...
    @overload
    async def subreddits_search(self, **params: Unpack[RedditSubredditsSearchDefaultParams]) -> RedditSubredditsSearchResponse: ...
    @overload
    async def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestTextResponseParams]) -> str: ...
    @overload
    async def subreddits_suggest(self, **params: Unpack[RedditSubredditsSuggestDefaultParams]) -> RedditSubredditsSuggestResponse: ...
    @overload
    async def topics(self, **params: Unpack[RedditTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def topics(self, **params: Unpack[RedditTopicsTextResponseParams]) -> str: ...
    @overload
    async def topics(self, **params: Unpack[RedditTopicsDefaultParams]) -> RedditTopicsResponse: ...
    @overload
    async def topics_broad(self, **params: Unpack[RedditTopicsBroadStreamParams]) -> BinaryIO: ...
    @overload
    async def topics_broad(self, **params: Unpack[RedditTopicsBroadTextResponseParams]) -> str: ...
    @overload
    async def topics_broad(self, **params: Unpack[RedditTopicsBroadDefaultParams]) -> RedditTopicsBroadResponse: ...
    @overload
    async def topics_search(self, **params: Unpack[RedditTopicsSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def topics_search(self, **params: Unpack[RedditTopicsSearchTextResponseParams]) -> str: ...
    @overload
    async def topics_search(self, **params: Unpack[RedditTopicsSearchDefaultParams]) -> RedditTopicsSearchResponse: ...
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
    @overload
    async def user_profile(self, **params: Unpack[RedditUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def user_profile(self, **params: Unpack[RedditUserProfileTextResponseParams]) -> str: ...
    @overload
    async def user_profile(self, **params: Unpack[RedditUserProfileDefaultParams]) -> RedditUserProfileResponse: ...

RedditArchiveCommentsIdsDefaultParams = TypedDict('RedditArchiveCommentsIdsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

RedditArchiveCommentsIdsTextResponseParams = TypedDict('RedditArchiveCommentsIdsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

RedditArchiveCommentsIdsStreamParams = TypedDict('RedditArchiveCommentsIdsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

RedditArchiveCommentsSearchDefaultParams = TypedDict('RedditArchiveCommentsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'query': NotRequired[str],
    'link_id': NotRequired[str],
    'parent_id': NotRequired[str],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveCommentsSearchTextResponseParams = TypedDict('RedditArchiveCommentsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'query': NotRequired[str],
    'link_id': NotRequired[str],
    'parent_id': NotRequired[str],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveCommentsSearchStreamParams = TypedDict('RedditArchiveCommentsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'query': NotRequired[str],
    'link_id': NotRequired[str],
    'parent_id': NotRequired[str],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveCommentsTreeDefaultParams = TypedDict('RedditArchiveCommentsTreeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'parent_id': NotRequired[str],
    'limit': NotRequired[int],
    'start_breadth': NotRequired[int],
    'start_depth': NotRequired[int],
}, total=False)

RedditArchiveCommentsTreeTextResponseParams = TypedDict('RedditArchiveCommentsTreeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'parent_id': NotRequired[str],
    'limit': NotRequired[int],
    'start_breadth': NotRequired[int],
    'start_depth': NotRequired[int],
}, total=False)

RedditArchiveCommentsTreeStreamParams = TypedDict('RedditArchiveCommentsTreeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'parent_id': NotRequired[str],
    'limit': NotRequired[int],
    'start_breadth': NotRequired[int],
    'start_depth': NotRequired[int],
}, total=False)

RedditArchivePostsIdsDefaultParams = TypedDict('RedditArchivePostsIdsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

RedditArchivePostsIdsTextResponseParams = TypedDict('RedditArchivePostsIdsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

RedditArchivePostsIdsStreamParams = TypedDict('RedditArchivePostsIdsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

RedditArchivePostsSearchDefaultParams = TypedDict('RedditArchivePostsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': NotRequired[str],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'url': NotRequired[str],
    'url_exact': NotRequired[bool],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchivePostsSearchTextResponseParams = TypedDict('RedditArchivePostsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': NotRequired[str],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'url': NotRequired[str],
    'url_exact': NotRequired[bool],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchivePostsSearchStreamParams = TypedDict('RedditArchivePostsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': NotRequired[str],
    'author': NotRequired[str],
    'subreddit': NotRequired[str],
    'url': NotRequired[str],
    'url_exact': NotRequired[bool],
    'created_after': NotRequired[str],
    'created_before': NotRequired[str],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveSubredditsSearchDefaultParams = TypedDict('RedditArchiveSubredditsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': Required[str],
    'min_subscribers': NotRequired[int],
    'max_subscribers': NotRequired[int],
    'over_18': NotRequired[bool],
    'sort_by': NotRequired[Literal['created_utc', 'subscribers', 'subreddit']],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveSubredditsSearchTextResponseParams = TypedDict('RedditArchiveSubredditsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': Required[str],
    'min_subscribers': NotRequired[int],
    'max_subscribers': NotRequired[int],
    'over_18': NotRequired[bool],
    'sort_by': NotRequired[Literal['created_utc', 'subscribers', 'subreddit']],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveSubredditsSearchStreamParams = TypedDict('RedditArchiveSubredditsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': Required[str],
    'min_subscribers': NotRequired[int],
    'max_subscribers': NotRequired[int],
    'over_18': NotRequired[bool],
    'sort_by': NotRequired[Literal['created_utc', 'subscribers', 'subreddit']],
    'sort': NotRequired[Literal['asc', 'desc']],
    'limit': NotRequired[int],
}, total=False)

RedditArchiveTimeSeriesDefaultParams = TypedDict('RedditArchiveTimeSeriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'metric': Required[Literal['posts_count', 'comments_count', 'posts_score_sum', 'comments_score_sum', 'posts_retrieval_delay_seconds_sum', 'comments_retrieval_delay_seconds_sum', 'subreddit_subscribers']],
    'subreddit': NotRequired[str],
    'precision': Required[Literal['year', 'quarter', 'month', 'week', 'day', 'hour', 'minute']],
    'created_after': Required[str],
    'created_before': Required[str],
}, total=False)

RedditArchiveTimeSeriesTextResponseParams = TypedDict('RedditArchiveTimeSeriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'metric': Required[Literal['posts_count', 'comments_count', 'posts_score_sum', 'comments_score_sum', 'posts_retrieval_delay_seconds_sum', 'comments_retrieval_delay_seconds_sum', 'subreddit_subscribers']],
    'subreddit': NotRequired[str],
    'precision': Required[Literal['year', 'quarter', 'month', 'week', 'day', 'hour', 'minute']],
    'created_after': Required[str],
    'created_before': Required[str],
}, total=False)

RedditArchiveTimeSeriesStreamParams = TypedDict('RedditArchiveTimeSeriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'metric': Required[Literal['posts_count', 'comments_count', 'posts_score_sum', 'comments_score_sum', 'posts_retrieval_delay_seconds_sum', 'comments_retrieval_delay_seconds_sum', 'subreddit_subscribers']],
    'subreddit': NotRequired[str],
    'precision': Required[Literal['year', 'quarter', 'month', 'week', 'day', 'hour', 'minute']],
    'created_after': Required[str],
    'created_before': Required[str],
}, total=False)

RedditCommentDefaultParams = TypedDict('RedditCommentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

RedditCommentTextResponseParams = TypedDict('RedditCommentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

RedditCommentStreamParams = TypedDict('RedditCommentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

RedditCommentAwardsDefaultParams = TypedDict('RedditCommentAwardsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

RedditCommentAwardsTextResponseParams = TypedDict('RedditCommentAwardsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

RedditCommentAwardsStreamParams = TypedDict('RedditCommentAwardsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

RedditCommentsDefaultParams = TypedDict('RedditCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
}, total=False)

RedditCommentsTextResponseParams = TypedDict('RedditCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
}, total=False)

RedditCommentsStreamParams = TypedDict('RedditCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'sort': NotRequired[Literal['confidence', 'top', 'new', 'controversial', 'old', 'qa']],
    'limit': NotRequired[int],
    'depth': NotRequired[int],
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

RedditPopularDefaultParams = TypedDict('RedditPopularDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sort': NotRequired[Literal['hot', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditPopularTextResponseParams = TypedDict('RedditPopularTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sort': NotRequired[Literal['hot', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditPopularStreamParams = TypedDict('RedditPopularStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sort': NotRequired[Literal['hot', 'top']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditPostDefaultParams = TypedDict('RedditPostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

RedditPostTextResponseParams = TypedDict('RedditPostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

RedditPostStreamParams = TypedDict('RedditPostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

RedditPostAwardsDefaultParams = TypedDict('RedditPostAwardsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

RedditPostAwardsTextResponseParams = TypedDict('RedditPostAwardsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

RedditPostAwardsStreamParams = TypedDict('RedditPostAwardsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

RedditPostsByIdsDefaultParams = TypedDict('RedditPostsByIdsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

RedditPostsByIdsTextResponseParams = TypedDict('RedditPostsByIdsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

RedditPostsByIdsStreamParams = TypedDict('RedditPostsByIdsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
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

RedditSearchCommentsDefaultParams = TypedDict('RedditSearchCommentsDefaultParams', {
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

RedditSearchCommentsTextResponseParams = TypedDict('RedditSearchCommentsTextResponseParams', {
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

RedditSearchCommentsStreamParams = TypedDict('RedditSearchCommentsStreamParams', {
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

RedditSearchPeopleDefaultParams = TypedDict('RedditSearchPeopleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSearchPeopleTextResponseParams = TypedDict('RedditSearchPeopleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSearchPeopleStreamParams = TypedDict('RedditSearchPeopleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'sort': NotRequired[Literal['relevance', 'hot', 'new', 'top', 'comments']],
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

RedditSubredditFlairsDefaultParams = TypedDict('RedditSubredditFlairsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditFlairsTextResponseParams = TypedDict('RedditSubredditFlairsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditFlairsStreamParams = TypedDict('RedditSubredditFlairsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditHighlightsDefaultParams = TypedDict('RedditSubredditHighlightsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditHighlightsTextResponseParams = TypedDict('RedditSubredditHighlightsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditHighlightsStreamParams = TypedDict('RedditSubredditHighlightsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditLeaderboardCategoriesDefaultParams = TypedDict('RedditSubredditLeaderboardCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditLeaderboardCategoriesTextResponseParams = TypedDict('RedditSubredditLeaderboardCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditLeaderboardCategoriesStreamParams = TypedDict('RedditSubredditLeaderboardCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditPostsDefaultParams = TypedDict('RedditSubredditPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising', 'controversial']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditPostsTextResponseParams = TypedDict('RedditSubredditPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising', 'controversial']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditPostsStreamParams = TypedDict('RedditSubredditPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
    'sort': NotRequired[Literal['hot', 'new', 'top', 'rising', 'controversial']],
    'time': NotRequired[Literal['hour', 'day', 'week', 'month', 'year', 'all']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditRulesDefaultParams = TypedDict('RedditSubredditRulesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditRulesTextResponseParams = TypedDict('RedditSubredditRulesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditRulesStreamParams = TypedDict('RedditSubredditRulesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditUserFlairsDefaultParams = TypedDict('RedditSubredditUserFlairsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditUserFlairsTextResponseParams = TypedDict('RedditSubredditUserFlairsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditUserFlairsStreamParams = TypedDict('RedditSubredditUserFlairsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
}, total=False)

RedditSubredditWikiDefaultParams = TypedDict('RedditSubredditWikiDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'subreddit': Required[str],
    'page': NotRequired[str],
}, total=False)

RedditSubredditWikiTextResponseParams = TypedDict('RedditSubredditWikiTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'subreddit': Required[str],
    'page': NotRequired[str],
}, total=False)

RedditSubredditWikiStreamParams = TypedDict('RedditSubredditWikiStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'subreddit': Required[str],
    'page': NotRequired[str],
}, total=False)

RedditSubredditsDiscoverDefaultParams = TypedDict('RedditSubredditsDiscoverDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'feed': NotRequired[Literal['popular', 'new', 'default']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsDiscoverTextResponseParams = TypedDict('RedditSubredditsDiscoverTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'feed': NotRequired[Literal['popular', 'new', 'default']],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsDiscoverStreamParams = TypedDict('RedditSubredditsDiscoverStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'feed': NotRequired[Literal['popular', 'new', 'default']],
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

RedditSubredditsSearchDefaultParams = TypedDict('RedditSubredditsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsSearchTextResponseParams = TypedDict('RedditSubredditsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsSearchStreamParams = TypedDict('RedditSubredditsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditSubredditsSuggestDefaultParams = TypedDict('RedditSubredditsSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

RedditSubredditsSuggestTextResponseParams = TypedDict('RedditSubredditsSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

RedditSubredditsSuggestStreamParams = TypedDict('RedditSubredditsSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
}, total=False)

RedditTopicsDefaultParams = TypedDict('RedditTopicsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTopicsTextResponseParams = TypedDict('RedditTopicsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTopicsStreamParams = TypedDict('RedditTopicsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'limit': NotRequired[int],
    'after': NotRequired[str],
}, total=False)

RedditTopicsBroadDefaultParams = TypedDict('RedditTopicsBroadDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

RedditTopicsBroadTextResponseParams = TypedDict('RedditTopicsBroadTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

RedditTopicsBroadStreamParams = TypedDict('RedditTopicsBroadStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

RedditTopicsSearchDefaultParams = TypedDict('RedditTopicsSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

RedditTopicsSearchTextResponseParams = TypedDict('RedditTopicsSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

RedditTopicsSearchStreamParams = TypedDict('RedditTopicsSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
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

RedditUserProfileDefaultParams = TypedDict('RedditUserProfileDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

RedditUserProfileTextResponseParams = TypedDict('RedditUserProfileTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

RedditUserProfileStreamParams = TypedDict('RedditUserProfileStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)
