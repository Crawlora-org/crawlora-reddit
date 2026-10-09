<?php

declare(strict_types=1);

namespace Crawlora\Reddit;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'reddit';
    public const VERSION = '0.1.1';
    public const OPERATION_COUNT = 12;
    public const OPERATION_IDS = ["reddit-comments", "reddit-domain-posts", "reddit-leads", "reddit-post", "reddit-search", "reddit-subreddit-about", "reddit-subreddit-comments", "reddit-subreddit-posts", "reddit-subreddits-posts", "reddit-trends", "reddit-user-comments", "reddit-user-posts"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"reddit-comments": {"id": "reddit-comments", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1tka90t"}, {"default": "confidence", "description": "Comment order: confidence, top, new, controversial, old, or qa. Applied to the anonymous HTML request when metrics are enabled.", "enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum comments returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"default": 3, "description": "Maximum flat comment depth returned in metrics mode.", "in": "query", "name": "depth", "type": "integer"}, {"default": false, "description": "Include public post and per-comment engagement metrics; costs 3 credits instead of 1", "in": "query", "name": "include_metrics", "type": "boolean"}], "path": "/reddit/comments/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "depth", "type": "integer"}, {"in": "query", "name": "include_metrics", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "reddit-domain-posts": {"id": "reddit-domain-posts", "method": "GET", "params": [{"description": "Domain hostname, without scheme or path", "in": "path", "name": "domain", "required": true, "type": "string", "x-example": "openai.com"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/domain/{domain}/posts", "pathParams": ["domain"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-leads": {"id": "reddit-leads", "method": "GET", "params": [{"description": "What you offer, in plain language", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "crm for small teams"}, {"description": "Restrict the search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"default": "month", "description": "Time window: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum leads returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Minimum buying-intent score to return, 0-10, defaults to 4", "in": "query", "name": "min_score", "type": "integer"}, {"default": "auto", "description": "Classifier: auto uses the model when configured, heuristic skips it, llm requires it", "enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "path": "/reddit/leads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "min_score", "type": "integer"}, {"enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-post": {"id": "reddit-post", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1v8hy3q"}, {"default": false, "description": "Include public engagement metrics; costs 3 credits instead of 1", "in": "query", "name": "include_metrics", "type": "boolean"}], "path": "/reddit/post/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "include_metrics", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "reddit-search": {"id": "reddit-search", "method": "GET", "params": [{"description": "Search keywords", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "gpt"}, {"description": "Restrict search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top/comments sorts: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-about": {"id": "reddit-subreddit-about", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum sample posts inspected, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/subreddit/{subreddit}/about", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-comments": {"id": "reddit-subreddit-comments", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/comments", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-posts": {"id": "reddit-subreddit-posts", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/posts", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-posts": {"id": "reddit-subreddits-posts", "method": "GET", "params": [{"description": "Comma-separated subreddit names, without r/, maximum 10", "in": "query", "name": "subreddits", "required": true, "type": "string", "x-example": "OpenAI,MachineLearning"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "subreddits", "required": true, "type": "string"}, {"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-trends": {"id": "reddit-trends", "method": "GET", "params": [{"default": "hot", "description": "Sort: hot, new, rising, or top", "enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/trends", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-comments": {"id": "reddit-user-comments", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/comments", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-posts": {"id": "reddit-user-posts", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/posts", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-reddit-php/0.1.1',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-comments", $params, $responseType);
    }
    public function domain_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-domain-posts", $params, $responseType);
    }
    public function leads(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-leads", $params, $responseType);
    }
    public function post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-post", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-search", $params, $responseType);
    }
    public function subreddit_about(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-about", $params, $responseType);
    }
    public function subreddit_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-comments", $params, $responseType);
    }
    public function subreddit_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddit-posts", $params, $responseType);
    }
    public function subreddits_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-subreddits-posts", $params, $responseType);
    }
    public function trends(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-trends", $params, $responseType);
    }
    public function user_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-user-comments", $params, $responseType);
    }
    public function user_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("reddit-user-posts", $params, $responseType);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId): array
    {
        if ($this->transport !== null) {
            $result = ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
