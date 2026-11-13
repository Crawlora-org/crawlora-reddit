import { RedditClient } from "../src/index.js";

const client = new RedditClient({ apiKey: "test-key" });
void client.archiveCommentsIds({"ids": "sample"});
void client.request("reddit-archive-comments-ids", {"ids": "sample"});
const streamResponse: Promise<Response> = client.request("reddit-archive-comments-ids", {"ids": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("reddit-archive-comments-ids", {"ids": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.archiveCommentsIds({"ids": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("reddit-archive-comments-ids", {"ids": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("reddit-archive-comments-ids", {"ids": "sample"}, { responseType: "text" });
void rawText;


void client.archiveCommentsSearch();
void client.request("reddit-archive-comments-search");
// @ts-expect-error The selected operation requires its documented params.
void client.archiveCommentsIds();
