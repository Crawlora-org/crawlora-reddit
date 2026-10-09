import { RedditClient } from "../src/index.js";

const client = new RedditClient({ apiKey: "test-key" });
void client.comments({"id": "sample"});
void client.request("reddit-comments", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("reddit-comments", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("reddit-comments", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.comments({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("reddit-comments", {"id": "sample", "sort": "confidence", "limit": 1, "depth": 1, "include_metrics": true}, { responseType: "text" });
const rawText: Promise<string> = client.request("reddit-comments", {"id": "sample"}, { responseType: "text" });
void rawText;


void client.trends();
void client.request("reddit-trends");
// @ts-expect-error The selected operation requires its documented params.
void client.comments();
