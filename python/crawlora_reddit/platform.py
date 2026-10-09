"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class RedditClient(CrawloraClient):
    """Synchronous Reddit API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-reddit-python/0.1.1')
        super().__init__(*args, **kwargs)

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

    def post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-search', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def subreddit_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddit-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def subreddits_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('reddit-subreddits-posts', params, response_type=response_type, timeout=timeout, headers=headers)

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

class AsyncRedditClient(AsyncCrawloraClient):
    """Asynchronous Reddit API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-reddit-python/0.1.1')
        super().__init__(*args, **kwargs)

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

    async def post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-search', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def subreddit_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddit-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def subreddits_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('reddit-subreddits-posts', params, response_type=response_type, timeout=timeout, headers=headers)

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
