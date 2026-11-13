"""Typed Reddit client for the Crawlora hosted API."""

from .platform import RedditClient, AsyncRedditClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = RedditClient
AsyncClient = AsyncRedditClient
__version__ = '0.3.0'
DISPLAY_NAME = 'Reddit'
PLATFORM = 'reddit'
CONTRACT_REVISION = 'sha256:34005a8045ab32c913cc47a26b3bc48fb73f290882bf61a0abd2afa55d96d8d0'

__all__ = [
    "RedditClient", "AsyncRedditClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
