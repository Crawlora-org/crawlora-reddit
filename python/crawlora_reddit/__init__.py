"""Typed Reddit client for the Crawlora hosted API."""

from .platform import RedditClient, AsyncRedditClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = RedditClient
AsyncClient = AsyncRedditClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Reddit'
PLATFORM = 'reddit'
CONTRACT_REVISION = 'sha256:441a9c4645a94738c644f66d38610950951f585a268d92be35900149133ce821'

__all__ = [
    "RedditClient", "AsyncRedditClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
