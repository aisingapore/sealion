# Tool Calling Guide for SEA-LION Models

## Introduction to Tool Calling

Tool calling is a powerful feature that enables Large Language Models (LLMs) to interact with external functions and APIs, extending their capabilities beyond text generation. SEA-LION models support tool calling with different implementations depending on the model version.

Tool calling allows models to:
- Access real-time information (weather, time, web search)
- Perform calculations and data processing  
- Interact with external systems and APIs
- Execute specific functions based on user requests

This guide covers tool calling implementation for the SEA-LION model variants hosted on [SEA-LION API](../inferencing/api.md), each with distinct behaviors and requirements.
For demonstration purposes, the tools suggested in the [tool implementation page](./tool_examples.md) will be used in the sample code snippets.

#### <u>[Tool Implementation Example](./tool_examples.md)</u>
 - [Tool Functions](./tool_examples.md#tool-functions)
 - [Tool Schema Definition](./tool_examples.md#tool-schema-definition)
 - [System Prompt](./tool_examples.md#system-prompt-configuration)
 - [Response Parsing](./tool_examples.md#response-parsing)
 - [Tool Execution](./tool_examples.md#tool-execution-framework)
 - [Customizing Tools](./tool_examples.md#customizing-tools-for-your-application)

## Model-Specific Tool Calling Guides

### Gemma-SEA-LION-v4-27B-IT

**Key Characteristics:**
- Uses text-based tool calling format
- Requires parsing tool calls from response content  
- Does not utilize standard `tool_calls` parameter
- Follows system prompt instructions for tool call formatting

Following the Gemma 3 chat template, Gemma-SEA-LION-v4-27B-IT does not parse the [`tools` parameter](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools), hence it is recommended to handle tool-calling via the parsing of the model's message response, similar to [this example](https://www.philschmid.de/gemma-function-calling) by Google DeepMind engineer Philipp Schmid.

When `tool_choice` is configured to enforce usage of a specific tool, the `tool_calls` parameter will be returned, but this removes flexibility from the LLM on determining whether tool call is required.

#### API Request Configuration

```python
# For Gemma-SEA-LION-v4-27B-IT, DO NOT include tools in request
request_data = {
    "model": "aisingapore/Gemma-SEA-LION-v4-27B-IT",
    "messages": messages,
    "temperature": 0,
    # Note: No tools or tool_choice parameters
}
```

If enforcing tool call:

```python
# For models that support native tool calling, include tools and enforce specific tool
request_data = {
    "model": "aisingapore/Gemma-SEA-LION-v4-27B-IT",
    "messages": messages,
    "temperature": 0,
    "tools": build_tool_schema(),
    "tool_choice": {
        "type": "function",
        "function": {"name": "get_current_weather"}  # Force use of specific tool
    }
}

# Alternative: Force any tool call (not a specific one)
request_data_any_tool = {
    "model": "aisingapore/Gemma-SEA-LION-v4-27B-IT", 
    "messages": messages,
    "temperature": 0,
    "tools": build_tool_schema(),
    "tool_choice": "required"  # Force model to use any available tool
}
```

#### Example Response (Tool-calling not enforced)

```json
{
  "choices": [{
    "message": {
      "content": "```tool_code\nget_time(timezone=\"Asia/Singapore\")\n```",
      "role": "assistant"
    }
  }]
}
```

### Llama-SEA-LION-v3-70B-IT

**Key Characteristics:**
- Supports standard OpenAI-style function calling
- Uses `tool_calls` parameter in responses
- Requires tools configuration in API request
- Works with `tool_choice: "auto"` setting

#### API Request Configuration

```python
# For Llama-SEA-LION-v3-70B-IT, include tools and tool_choice
request_data = {
    "model": "aisingapore/Llama-SEA-LION-v3-70B-IT",
    "messages": messages,
    "temperature": 0,
    "tools": build_tool_schema(),
    "tool_choice": "auto"
}
```

#### Response Handling

```python
def extract_tool_calls(data):
    """Extract tool calls from the response data."""
    choice = data.get("choices", [{}])[0] if data.get("choices") else {}
    return choice.get("message", {}).get("tool_calls")

# Usage
tool_calls = extract_tool_calls(response_data)
if tool_calls:
    # Execute tool calls directly
    tool_results = await execute_tool_calls(tool_calls, session)
```

#### Example Response

```json
{
  "choices": [{
    "message": {
      "content": null,
      "role": "assistant",
      "tool_calls": [{
        "function": {
          "arguments": "{\"timezone\": \"Asia/Singapore\"}",
          "name": "get_time"
        },
        "id": "chatcmpl-tool-920019c71dd14d96a262ec798b778ccd",
        "type": "function"
      }]
    }
  }]
}
```

### Llama-SEA-LION-v3.5-70B-R

**Key Characteristics:**
- Reasoning model without tool calling capability
- Tool-calling can be done via parsing from message response
- Similar to Gemma-SEA-LION-v4-27B-IT using tool-calling via message content
- Recommend not adding `tools`, `tool_choice` in API call

#### API Request Configuration

```python
# For reasoning models, do NOT include tools to avoid errors
def is_reasoning_model(model_name):
    return model_name.endswith('-R')

# Request configuration
if is_reasoning_model(api_config["model"]):
    request_data = {
        "model": "aisingapore/Llama-SEA-LION-v3.5-70B-R",
        "messages": messages,
        "temperature": 0,
        # No tools or tool_choice parameters
    }
else:
    request_data = {
        "model": api_config["model"],
        "messages": messages,
        "temperature": 0,
        "tools": tools,
        "tool_choice": "auto"
    }
```

## Implementation Example

Here's a complete implementation that handles all three model types:

```python
async def process_user_message(user_message, messages, api_config, session):
    """Process a user message and handle tool calls for different model types."""
    messages.append({"role": "user", "content": user_message})
    tools = build_tool_schema()
    
    # Check model type
    is_reasoning_model = api_config["model"].endswith('-R')
    
    # Configure request based on model type
    request_data = {
        "model": api_config["model"],
        "messages": messages,
        "temperature": 0,
    }
    
    # Only add tools for non-reasoning models (except Gemma v4)
    if not is_reasoning_model:
        request_data["tools"] = tools
        request_data["tool_choice"] = "auto"
    
    headers = {"Authorization": f"Bearer {api_config['api_key']}"}
    
    async with session.post(
        api_config["api_url"],
        json=request_data,
        headers=headers,
        timeout=30
    ) as response:
        data = await response.json()
    
    assistant_message = data.get("choices", [{}])[0].get("message")
    if not assistant_message:
        return
        
    messages.append(assistant_message)
    
    # Handle tool calls based on model type
    tool_calls = extract_tool_calls(data)
    if not tool_calls:
        # Tool call not found, parse tool call from message content
        message_content = assistant_message.get("content", "")
        if is_reasoning_model:
            # Check for tool call only in non-reasoning content to prevent excess calls
            message_content = message_content.split("</think>")[1].strip()
        tool_calls = parse_tool_calls_from_text(message_content)
    
    if tool_calls:
        # Execute tools and get final response
        tool_results = await execute_tool_calls(tool_calls, session)
        messages.extend(tool_results)
        
        # Get final response with tool results
        final_response = await session.post(
            api_config["api_url"],
            json={"model": api_config["model"], "messages": messages, "temperature": 0},
            headers=headers,
            timeout=30
        )
        final_data = await final_response.json()
        
        final_message = final_data.get("choices", [{}])[0].get("message")
        if final_message:
            print(final_message["content"])
            messages.append(final_message)
    else:
        # No tool calls, show direct response
        print(assistant_message.get("content", ""))
```

## Points to Take Note Of

### Model-Specific Considerations

1. **Gemma-SEA-LION-v4-27B-IT**:
   - Typically uses text parsing instead of standard tool calling
   - System prompt should explicitly define tool call format
   - `tools` parameter in API requests is only utilized when `tool_choice` is set to `"required"` or specific tool is enforced
   - Tool calls are wrapped in ```tool_code blocks
   - Regex patterns needed for extraction

2. **Llama-SEA-LION-v3-70B-IT**:
   - Fully supports OpenAI-style tool calling
   - Uses `tools` and `tool_choice` in API requests
   - Returns structured `tool_calls` in response
   - Reliable for production tool calling applications

3. **Llama-SEA-LION-v3.5-70B-R**:
   - Reasoning model without tool calling capability
   - Tool-calling can be done via parsing from message response
   - Can reason about tool usage
   - Take note to parse from message content after reasoning segment, to prevent multiple redundant tool calls
   - Best used for complex reasoning tasks

### General Best Practices

1. **Error Handling**: Always implement proper error handling for tool execution failures and API timeouts.

2. **Model Detection**: Use model name suffixes to determine the appropriate tool calling approach:
   ```python
   is_reasoning_model = model_name.endswith('-R')
   ```

3. **Timeout Management**: Set appropriate timeouts for both LLM API calls and tool execution

4. **Response Validation**: Always validate tool call responses before processing:
   ```python
   if not tool_calls or not isinstance(tool_calls, list):
       # Handle no tool calls case
   ```

5. **Conversation Flow**: Maintain proper conversation history by adding all messages (user, assistant, tool results) to the messages array.
    - Gemma 3 chat template enforces the alternating of `user` and `assistant` in message history, hence in the example function `execute_tool_calls`, the role returned is `user` and not `tool` for the tool result

6. **Platform Considerations**: Some models may behave differently on different platforms (e.g., Ollama vs cloud APIs). Test your implementation on your target platform.

7. **Token Efficiency**: The text-based approach may use more tokens than standard function calling. Monitor usage accordingly.

### Security Considerations

- Validate all tool parameters before execution
- Implement rate limiting for external API calls
- Sanitize user inputs that will be passed to tools
- Consider implementing tool execution sandboxing for production environments

### Performance Optimization

- Cache tool results where appropriate (e.g., weather data for short periods)
- Implement parallel tool execution when multiple tools are called
- Use connection pooling for HTTP requests in tool implementations
- Consider implementing tool call batching for efficiency

### Relevant Links
 - [Gemma 3 Function Calling Example](https://www.philschmid.de/gemma-function-calling)
 - [OpenAI API Reference - `tools`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools)
 - [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)