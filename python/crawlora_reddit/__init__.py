"""Typed Reddit client for the Crawlora hosted API."""

from .platform import RedditClient, AsyncRedditClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = RedditClient
AsyncClient = AsyncRedditClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Reddit'
PLATFORM = 'reddit'
CONTRACT_REVISION = 'sha256:11f2ddb0c3c61724bf46ac537a74910bf241c72ada328691f88369a8aac9e4e1'

__all__ = [
    "RedditClient", "AsyncRedditClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
