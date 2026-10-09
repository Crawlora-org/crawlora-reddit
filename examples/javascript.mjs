import { RedditClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new RedditClient({ apiKey });

  const search = await client.search({ q: "open source" });
  console.log("search", search);
  const subredditPosts = await client.subredditPosts({ subreddit: "technology" });
  console.log("subredditPosts", subredditPosts);
