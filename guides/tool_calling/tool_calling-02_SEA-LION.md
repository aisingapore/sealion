# Tool Calling Guide for SEA-LION Models

## SEA-LION Model-Specific Tool Calling Guides

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

Here's an examples that handles all three models, making use of the components provided in the [tool implementation page](./tool_examples.md):

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
    
    # Only add tools for non-reasoning models
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

### Relevant Links
 - [Gemma 3 Function Calling Example](https://www.philschmid.de/gemma-function-calling)
 - [OpenAI API Reference - `tools`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools)
 - [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)