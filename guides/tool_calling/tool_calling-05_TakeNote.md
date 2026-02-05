# Tool Calling Guide for SEA-LION Models

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