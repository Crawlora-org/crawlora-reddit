import os

from crawlora_reddit import RedditClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with RedditClient(api_key=api_key) as client:
    search = client.search(q='open source')
    print('search', search)
    subreddit_posts = client.subreddit_posts(subreddit='technology')
    print('subreddit_posts', subreddit_posts)
