require "json"
require "net/http"
require "uri"

module Crawlora
  module Reddit
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"reddit-comments": {"id": "reddit-comments", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1tka90t"}, {"default": "confidence", "description": "Comment order: confidence, top, new, controversial, old, or qa. Applied to the anonymous HTML request when metrics are enabled.", "enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"description": "Maximum comments returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"default": 3, "description": "Maximum flat comment depth returned in metrics mode.", "in": "query", "name": "depth", "type": "integer"}, {"default": false, "description": "Include public post and per-comment engagement metrics; costs 3 credits instead of 1", "in": "query", "name": "include_metrics", "type": "boolean"}], "path": "/reddit/comments/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"enum": ["confidence", "top", "new", "controversial", "old", "qa"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "depth", "type": "integer"}, {"in": "query", "name": "include_metrics", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "reddit-domain-posts": {"id": "reddit-domain-posts", "method": "GET", "params": [{"description": "Domain hostname, without scheme or path", "in": "path", "name": "domain", "required": true, "type": "string", "x-example": "openai.com"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/domain/{domain}/posts", "pathParams": ["domain"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-leads": {"id": "reddit-leads", "method": "GET", "params": [{"description": "What you offer, in plain language", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "crm for small teams"}, {"description": "Restrict the search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"default": "month", "description": "Time window: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum leads returned, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Minimum buying-intent score to return, 0-10, defaults to 4", "in": "query", "name": "min_score", "type": "integer"}, {"default": "auto", "description": "Classifier: auto uses the model when configured, heuristic skips it, llm requires it", "enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "path": "/reddit/leads", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "min_score", "type": "integer"}, {"enum": ["auto", "heuristic", "llm"], "in": "query", "name": "classifier", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-post": {"id": "reddit-post", "method": "GET", "params": [{"description": "Reddit post id or t3_ id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "1v8hy3q"}, {"default": false, "description": "Include public engagement metrics; costs 3 credits instead of 1", "in": "query", "name": "include_metrics", "type": "boolean"}], "path": "/reddit/post/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "include_metrics", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "reddit-search": {"id": "reddit-search", "method": "GET", "params": [{"description": "Search keywords", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "gpt"}, {"description": "Restrict search to a subreddit name, without r/", "in": "query", "name": "subreddit", "type": "string"}, {"default": "relevance", "description": "Sort: relevance, hot, new, top, or comments", "enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top/comments sorts: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "subreddit", "type": "string"}, {"enum": ["relevance", "hot", "new", "top", "comments"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-about": {"id": "reddit-subreddit-about", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum sample posts inspected, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}], "path": "/reddit/subreddit/{subreddit}/about", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-comments": {"id": "reddit-subreddit-comments", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/comments", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddit-posts": {"id": "reddit-subreddit-posts", "method": "GET", "params": [{"description": "Subreddit name, without r/", "in": "path", "name": "subreddit", "required": true, "type": "string", "x-example": "OpenAI"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddit/{subreddit}/posts", "pathParams": ["subreddit"], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-subreddits-posts": {"id": "reddit-subreddits-posts", "method": "GET", "params": [{"description": "Comma-separated subreddit names, without r/, maximum 10", "in": "query", "name": "subreddits", "required": true, "type": "string", "x-example": "OpenAI,MachineLearning"}, {"default": "hot", "description": "Sort: hot, new, top, or rising", "enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/subreddits/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "subreddits", "required": true, "type": "string"}, {"enum": ["hot", "new", "top", "rising"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-trends": {"id": "reddit-trends", "method": "GET", "params": [{"default": "hot", "description": "Sort: hot, new, rising, or top", "enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"description": "Time window for top sort: hour, day, week, month, year, or all", "enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/trends", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["hot", "new", "rising", "top"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["hour", "day", "week", "month", "year", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-comments": {"id": "reddit-user-comments", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum comments, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/comments", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "reddit-user-posts": {"id": "reddit-user-posts", "method": "GET", "params": [{"description": "Public Reddit username, without u/", "in": "path", "name": "username", "required": true, "type": "string", "x-example": "reddit"}, {"description": "Maximum posts, defaults to 25 and clamps to 100", "in": "query", "name": "limit", "type": "integer"}, {"description": "Reddit pagination token", "in": "query", "name": "after", "type": "string"}], "path": "/reddit/user/{username}/posts", "pathParams": ["username"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["reddit-comments", "reddit-domain-posts", "reddit-leads", "reddit-post", "reddit-search", "reddit-subreddit-about", "reddit-subreddit-comments", "reddit-subreddit-posts", "reddit-subreddits-posts", "reddit-trends", "reddit-user-comments", "reddit-user-posts"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-reddit-ruby/0.1.1", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-comments', params, response_type: response_type)
      end
      define_method('domain_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-domain-posts', params, response_type: response_type)
      end
      define_method('leads') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-leads', params, response_type: response_type)
      end
      define_method('post') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-post', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-search', params, response_type: response_type)
      end
      define_method('subreddit_about') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-about', params, response_type: response_type)
      end
      define_method('subreddit_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-comments', params, response_type: response_type)
      end
      define_method('subreddit_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddit-posts', params, response_type: response_type)
      end
      define_method('subreddits_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-subreddits-posts', params, response_type: response_type)
      end
      define_method('trends') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-trends', params, response_type: response_type)
      end
      define_method('user_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-user-comments', params, response_type: response_type)
      end
      define_method('user_posts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('reddit-user-posts', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
