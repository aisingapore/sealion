# Strands Agents SDK

This guide demonstrates how to use SEA-LION models as intelligent agents using AWS's Strands Agent SDK. The examples show how to build both general-purpose agents with multiple tools and specialized single-purpose agents.

## Prerequisites

- Python 3.10+
- AWS Strands Agents SDK installed ([Quickstart](https://strandsagents.com/0.1.x/user-guide/quickstart/))
- [SEA-LION API](https://docs.sea-lion.ai/guides/inferencing/api) or [Bedrock](https://docs.sea-lion.ai/guides/inferencing/amazon_bedrock) access
- Environment variables configured

The sample code in this guide will be configuring the model via SEA-LION API, which follows [an OpenAI-compatible format](https://strandsagents.com/0.1.x/user-guide/concepts/model-providers/openai/).
Strands Agent ADK is also compatible with other model providers. For configuring SEA-LION in Strands SDK via Bedrock, you may refer to [this page](https://strandsagents.com/0.1.x/user-guide/concepts/model-providers/amazon-bedrock/). For setting up of SEA-LION in Bedrock, refer to [this link](https://docs.sea-lion.ai/guides/inferencing/amazon_bedrock).

## Environment Setup

Create a `.env` file with your configuration:

```env
API_KEY=your-api-key-here
API_BASE_URL=https://api.sea-lion.ai/v1
MODEL=aisingapore/Llama-SEA-LION-v3-70B-IT

# Environment variable for custom tool
SEARXNG_URL=https://your-searxng-instance-url-here
```

## Basic Agent Setup

Here's how to create a basic SEA-LION agent with tool-calling capabilities:

**`agent.py`**
```python
import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.openai import OpenAIModel
from strands_tools import calculator, current_time

load_dotenv()

# Configure the SEA-LION model
model = OpenAIModel(
    client_args={
        "api_key": os.environ.get("API_KEY"),
        "base_url": os.environ.get("API_BASE_URL"),
    },
    model_id=os.environ.get("MODEL", "aisingapore/Llama-SEA-LION-v3-70B-IT"),
    params={
        "max_tokens": 1000,
        "stream": True,
    },
)

# Initialize the agent
agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant who answers questions in a concise and informative manner. You can use tools to assist with calculations and current time queries.",
    tools=[current_time, calculator]
)

# Use the agent
demo_prompts = [
    "What is the current time in Singapore?",
    "What is sixty five + 34?"
]

for prompt in demo_prompts:
    agent(prompt)
```
Refer to [the documentation](https://strandsagents.com/0.1.x/user-guide/concepts/tools/example-tools-package/) for more examples of in-built tools.

## Custom Tool Development

You can create custom tools for your agents. <br>
Here's an example of custom web search tool using [a locally-deployed SearXNG search engine](https://docs.searxng.org/admin/installation-docker.html):

**`tools.py`**
```python
import os
import requests

from dotenv import load_dotenv
from strands import tool
from typing import Optional, List, Dict, Any
from urllib.parse import urljoin

load_dotenv()

@tool
def searxng_search(
    query: str,
    categories: Optional[List[str]] = None,
    engines: Optional[List[str]] = None,
    language: Optional[str] = None,
    pageno: int = 1,
    time_range: Optional[str] = None,
    format: str = "json",
    safesearch: int = 1,
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Send a search query to a SearXNG search engine.
    
    Args:
        query: The search query string
        categories: List of search categories (e.g., ["general", "images"])
        engines: List of specific engines to use (e.g., ["google", "bing"])
        language: Language code (e.g., "en", "de")
        pageno: Page number for pagination (default: 1)
        time_range: Time range filter ("day", "month", "year")
        format: Output format ("json", "csv", "rss")
        safesearch: Safe search level (0=off, 1=moderate, 2=strict)
        timeout: Request timeout in seconds
    
    Returns:
        Dictionary containing search results
    """
    
    search_url = urljoin(os.getenv("SEARXNG_URL", "http://localhost:8080"), '/search')
    
    params = {
        'q': query,
        'pageno': pageno,
        'format': format,
        'safesearch': safesearch
    }
    
    # Add optional parameters
    if categories:
        params['categories'] = ','.join(categories)
    if engines:
        params['engines'] = ','.join(engines)
    if language:
        params['language'] = language
    if time_range:
        params['time_range'] = time_range
    
    try:
        response = requests.get(search_url, params=params, timeout=timeout)
        response.raise_for_status()
        
        if format == 'json':
            return response.json()
        else:
            return {'raw_response': response.text, 'status_code': response.status_code}
            
    except requests.RequestException as e:
        raise requests.RequestException(f"SearXNG search failed: {str(e)}")
```

## Agent as a Tool

Create a specialized agent that can be used as a tool by other agents:

**`translate_agent.py`**
```python
import os
import sys

from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.openai import OpenAIModel

load_dotenv()

# Use a smaller model for specialized tasks
translation_model = OpenAIModel(
    client_args={
        "api_key": os.environ.get("API_KEY"),
        "base_url": os.environ.get("API_BASE_URL"),
    },
    model_id="aisingapore/Gemma-SEA-LION-v3-9B-IT",
    params={
        "max_tokens": 1000,
        "stream": True,
    },
)

@tool
def translator(input_text: str, target_language: str) -> str:
    """
    Translates the input text to the target language.
    
    Args:
        input_text (str): The text to translate.
        target_language (str): The language to translate to (e.g. "English").
        
    Returns:
        str: The translated text.
    """
    TRANSLATOR_PROMPT = f"""
    You are a translation engine. Your sole purpose is to translate text.

    - If the input is not in {target_language}, translate it to {target_language}.
    - If language is not specified or unclear, default to English.

    You must only output the translated text. Do not include any additional explanations, notes, formatting, or any other text besides the translated content.
    """
    
    try:
        agent = Agent(
            model=translation_model,
            system_prompt=TRANSLATOR_PROMPT,
            tools=[]  # No tools needed for translation
        )
        response = agent(input_text)
        return response
    except Exception as e:
        return f"Translation failed: {str(e)}"

# Usage example
if __name__ == "__main__":
    try:
        print("🤖 Strands Translator Agent CLI")
        language = input("Enter the target language (e.g. English): ").strip()

        if not language:
            language = "English"
        print(f"Target language set to: {language}")
        print("Type your text below. Type 'quit', 'exit', or press Ctrl+C to exit.")

        # Initialize the agent
        
        while True:
            try:
                
                # Get user input
                user_input = input("\nUser: ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye! 👋")
                    break
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Get agent response
                print("Translation: ", end="", flush=True)
                translator(user_input,language)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except EOFError:
                print("\nGoodbye! 👋")
                break

    except Exception as e:
        print(f"An error occurred initializing the agent: {e}")
        sys.exit(1)
```

## Multi-Tool Agent Example

Combine multiple tools for a comprehensive agent, making use of Strands tools, custom tools and agents as tools:

**`agent_multi.py`**
```python
import os

from dotenv import load_dotenv
from strands import Agent
from strands.models.openai import OpenAIModel
from strands_tools import calculator, current_time

# Import your custom tools from your tools.py script, or place in this script with @tools decorator
from .tools import searxng_search

# Import your specialised agent from your agent's script, or place in this script with @tools decorator
from .translate_agent import translator

load_dotenv()
# Configure model
model = OpenAIModel(
    client_args={
        "api_key": os.environ.get("API_KEY"),
        "base_url": os.environ.get("API_BASE_URL"),
    },
    model_id=os.environ.get("MODEL", "aisingapore/Llama-SEA-LION-v3-70B-IT"),
    params={
        "max_tokens": 1000,
        "stream": True,
    },
)

# Create comprehensive agent
agent = Agent(
    model=model,
    system_prompt="""You are a helpful assistant who answers questions in a concise and informative manner. 
    You can use tools to assist with calculations, current time queries, web search, and translation. 
    For current_time, you can specify a timezone in the format 'Asia/Singapore'. 
    For searxng_search, make sure to provide the links to user as well. 
    If you need more information, ask the user for clarification.""",
    tools=[current_time, calculator, searxng_search, translator]
)

# Interactive CLI
def main():
    print("🤖 SEA-LION Agent CLI")
    print("Type your questions below. Type 'quit' to exit.")
    
    while True:
        try:
            user_input = input("\nUser: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye! 👋")
                break
            
            if not user_input:
                continue
            
            print("Agent: ", end="", flush=True)
            agent(user_input)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()
```

## Best Practices

### Model Selection
- Use `aisingapore/Llama-SEA-LION-v3-70B-IT` for complex reasoning and tool-calling
- Use `aisingapore/Gemma-SEA-LION-v3-9B-IT` for specialized, single-purpose agents

### Agent Configuration
- Use clear, descriptive names for your agents
- Provide specific instructions about tool usage guidelines
- Include examples when tools have specific parameter formats
- Clearly define the agent's role and capabilities

### Session Management
- Agent conversation history can be accessed via the `agent.messages` property
- To handle long-context conversations, `SlidingWindowConversationManager` can be configured
- More information and examples on conversation/state/session management available [here](https://strandsagents.com/0.1.x/user-guide/concepts/agents/sessions-state/)

### Tool Documentation
Always provide clear docstrings for custom tools, including:
- Purpose and functionality
- Parameter descriptions with types
- Return value format
- Usage examples
- Exception handling

## Troubleshooting

**Common Issues:**

1. **Tool not being called**: Ensure your system prompt mentions the tool and its use cases
2. **API connection errors**: Verify your API_KEY and API_BASE_URL in the `.env` file
3. **Timeout issues**: Adjust the timeout parameters in your tools
4. **Memory usage**: Use streaming responses for better performance with large outputs

**Performance Tips:**

- Use appropriate model sizes for your use case
- Implement proper error handling and fallbacks
- Monitor token usage to optimize costs

**Strands Agents SDK Specific**

- Configuring specialised agents as tools allows for them to do focused singular tasks. For using agents in a workflow or loop, consider other multi-agents systems in Strands SDK like [Workflow](https://strandsagents.com/0.1.x/user-guide/concepts/multi-agent/workflow/) or [Graph](https://strandsagents.com/0.1.x/user-guide/concepts/multi-agent/graph/)