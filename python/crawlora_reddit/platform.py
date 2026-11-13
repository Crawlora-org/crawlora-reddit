"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class RedditClient(CrawloraClient):
    """Synchronous Reddit API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-reddit-python/0.3.0')
        super().__init__(*args, **kwargs)

    def archive_comments_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-comments-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    def archive_comments_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-comments-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def archive_comments_tree(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-comments-tree', params, response_type=response_type, timeout=timeout, headers=headers)

    def archive_posts_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-posts-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    def archive_posts_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-posts-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def archive_subreddits_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-subreddits-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def archive_time_series(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-archive-time-series', params, response_type=response_type, timeout=timeout, headers=headers)

    def comment(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-comment', params, response_type=response_type, timeout=timeout, headers=headers)

    def comment_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-comment-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    def comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def domain_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-domain-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def leads(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-leads', params, response_type=response_type, timeout=timeout, headers=headers)

    def popular(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-popular', params, response_type=response_type, timeout=timeout, headers=headers)

    def post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def post_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-post-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    def posts_by_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-posts-by-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-search-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_people(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-search-people', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_about(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-about', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_flairs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-flairs', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_highlights(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-highlights', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_leaderboard_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-leaderboard-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_rules(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-rules', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_user_flairs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-user-flairs', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddit_wiki(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-wiki', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddits_discover(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddits-discover', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddits_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddits-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddits_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddits-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddits_suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddits-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

    def topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    def topics_broad(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-topics-broad', params, response_type=response_type, timeout=timeout, headers=headers)

    def topics_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-topics-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def trends(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-trends', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-user-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-user-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-user-profile', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncRedditClient(AsyncCrawloraClient):
    """Asynchronous Reddit API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-reddit-python/0.3.0')
        super().__init__(*args, **kwargs)

    async def archive_comments_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-comments-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    async def archive_comments_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-comments-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def archive_comments_tree(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-comments-tree', params, response_type=response_type, timeout=timeout, headers=headers)

    async def archive_posts_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-posts-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    async def archive_posts_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-posts-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def archive_subreddits_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-subreddits-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def archive_time_series(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-archive-time-series', params, response_type=response_type, timeout=timeout, headers=headers)

    async def comment(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-comment', params, response_type=response_type, timeout=timeout, headers=headers)

    async def comment_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-comment-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    async def comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def domain_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-domain-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leads(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-leads', params, response_type=response_type, timeout=timeout, headers=headers)

    async def popular(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-popular', params, response_type=response_type, timeout=timeout, headers=headers)

    async def post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def post_awards(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-post-awards', params, response_type=response_type, timeout=timeout, headers=headers)

    async def posts_by_ids(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-posts-by-ids', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-search-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_people(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-search-people', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_about(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-about', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_flairs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-flairs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_highlights(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-highlights', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_leaderboard_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-leaderboard-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_rules(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-rules', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_user_flairs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-user-flairs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddit_wiki(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-wiki', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddits_discover(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddits-discover', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddits_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddits-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddits_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddits-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddits_suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddits-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

    async def topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def topics_broad(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-topics-broad', params, response_type=response_type, timeout=timeout, headers=headers)

    async def topics_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-topics-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trends(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-trends', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-user-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-user-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-user-profile', params, response_type=response_type, timeout=timeout, headers=headers)
