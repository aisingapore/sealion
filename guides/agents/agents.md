# Agents

SEA-LION models can be used as intelligent agents capable of tool-calling, multi-step reasoning, and complex task execution. The SEA-LION v3 family, such as `aisingapore/Llama-SEA-LION-v3-70B-IT`, can be utilized for agent-based applications with tool-calling capabilities.

Agents built with SEA-LION can:
- Execute complex, multi-step workflows
- Integrate with external tools and APIs
- Perform real-time information retrieval
- Handle specialized tasks like translation, calculation, and web search
- Chain multiple operations together intelligently

## Available Frameworks

The following guides provide technical how-tos for building SEA-LION agents using different frameworks:

### [Strands Agents SDK](./strands_sdk.md)
Learn how to build powerful agents using AWS's Strands Agents SDK, including:
- Basic agent setup using in-built tools
- Custom tool development
- Using agents as tools
- Multi-tool agent example

### [Google Agent Development Kit](./google_adk.md)
Develop and deploy agents with Google ADK:
- Basic agent setup with custom tools and agent-as-a-tool
- Custom tool development
- Using agents as tools
- Running multi-tool agent via in-built web interface/CLI


## Recommended Models

For optimal agent performance, we recommend using the following SEA-LION models:

- **`aisingapore/Llama-SEA-LION-v3-70B-IT`/`aisingapore/Llama-SEA-LION-v3-8B-IT`** - Suitable for tool-calling, long context tasks or creative response.
- **`aisingapore/Gemma-SEA-LION-v3-9B-IT`** - Suitable for tool-calling, smaller tasks with succinct response. 
- **`aisingapore/Llama-SEA-LION-v3.5-70B-R`/`aisingapore/Llama-SEA-LION-v3.5-8B-R`** - Display reasoning process.

## Key Features

**Tool Integration**: SEA-LION agents can seamlessly integrate with both built-in tools (calculations, time queries) and custom tools (web search, translation, APIs).

**Multi-Agent Systems**: Agents can be composed together in multiple ways. Specialized agents serving as tools, running in sequential workflow, or passing to each other in a loop.

**Streaming Responses**: Built-in support for real-time streaming responses for better user experience.

**Flexible Configuration**: Easy environment-based configuration for different deployment scenarios.