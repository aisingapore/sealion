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


### Relevant Links
 - [Gemma 3 Function Calling Example](https://www.philschmid.de/gemma-function-calling)
 - [OpenAI API Reference - `tools`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools)
 - [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)