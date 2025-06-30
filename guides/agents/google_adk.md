# Google ADK Agents

This guide demonstrates how to use SEA-LION models as intelligent agents using Google's Agent Development Kit (ADK). The examples show how to build both general-purpose agents with multiple tools and specialized single-purpose agents.

## Prerequisites

- Python 3.9+
- Google ADK installed ([Quickstart](https://google.github.io/adk-docs/get-started/quickstart/))
- [SEA-LION API](https://docs.sea-lion.ai/guides/inferencing/api) or [Google Vertex AI](https://docs.sea-lion.ai/guides/inferencing/vertex_ai) access
- Environment variables configured

The sample code in this guide will be configuring the model via SEA-LION API through LiteLLM, which follows [an OpenAI-compatible format](https://google.github.io/adk-docs/agents/models/#using-openai-provider).
Google ADK is also compatible with other model providers including Google's own Vertex AI. For configuring SEA-LION in Google ADK, you may refer to [this page](https://google.github.io/adk-docs/agents/models/#vertex-ai). [Click here for instructions on deploying SEA-LION in Vertex AI.](https://docs.sea-lion.ai/guides/inferencing/vertex_ai)

## Environment Setup

Create a `.env` file with your configuration:

```env
## For using SEA-LION API, uncomment if needed
OPENAI_API_KEY=your-sea-lion-api-key-here
OPENAI_API_BASE=https://api.sea-lion.ai/v1
MODEL=aisingapore/Llama-SEA-LION-v3-70B-IT

## For using Google Vertex AI, uncomment if needed
# GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
# GOOGLE_CLOUD_LOCATION="YOUR_VERTEX_AI_LOCATION" # e.g., us-central1
GOOGLE_GENAI_USE_VERTEXAI=TRUE # Set to TRUE if NOT using Google AI Studio, due to function declaration issue: https://github.com/google/adk-python/issues/26#issuecomment-2911749485

# Environment variable for custom tool
SEARXNG_URL=https://your-searxng-instance-url-here
```

## Project Structure

```
parent_folder/
    adk_agent/
        __init__.py
        agent.py
        .env
        tools.py
        translator.py
        chat-cli.py
```

## Basic Agent Setup

Here's how to create a basic SEA-LION agent with tool-calling capabilities:

**`agent.py`**
```python
import os
import sys

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool

from .tools import searxng_search
from .translator import root_agent as translator

load_dotenv()

try:
   root_agent = Agent(
      name="root_agent",
      model=LiteLlm(
         model=f"openai/{os.getenv('MODEL', 'aisingapore/Llama-SEA-LION-v3-70B-IT')}"
      ),
      description="Agent to answer questions using search and translation tools.",
      instruction="You are a helpful assistant who answers questions in a concise and informative manner. " \
      "You can use tools to assist with searches (`searxng_search`) and translations (`translator`). "\
      "If using `searxng_search`, make sure to provide the links you use at the end of your response, if not already provided",
      tools=[searxng_search, AgentTool(agent=translator)],
   )
except Exception as e:
   print(f"An error occurred while creating the root agent: {e}")
   sys.exit(1)
```

**`__init__.py`**
```python
from . import agent
```

## Custom Tool Development

You can create custom tools for your agents.<br>
Here's an example of custom web search tool using [a locally-deployed SearXNG search engine](https://docs.searxng.org/admin/installation-docker.html):

**`tools.py`**
```python
import requests
from dotenv import load_dotenv
import os
from typing import Optional, List, Dict, Any
from urllib.parse import urljoin

load_dotenv()
SEARXNG_URL = os.getenv("SEARXNG_URL", "http://localhost:8080")

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
    Quick local set up for SearXNG via Docker can be found at
    https://docs.searxng.org/admin/installation-docker.html
    
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
    
    Raises:
        requests.RequestException: If the request fails
        ValueError: If the response is not valid JSON (when format="json")
    """
    
    # Prepare the search endpoint URL
    search_url = urljoin(SEARXNG_URL, '/search')
    
    # Build parameters
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
    
    # Make the request
    try:
        response = requests.get(search_url, params=params, timeout=timeout)
        response.raise_for_status()
        
        if format == 'json':
            return response.json()
        else:
            return {'raw_response': response.text, 'status_code': response.status_code}
            
    except requests.RequestException as e:
        raise requests.RequestException(f"SearXNG search failed: {str(e)}")
    except ValueError as e:
        if format == 'json':
            raise ValueError(f"Invalid JSON response from SearXNG: {str(e)}")
        raise
```

## Agent as a Tool

Create a specialized agent that can be used as a tool by other agents:

**`translator.py`**
```python
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

TRANSLATOR_PROMPT = """
You are a translation engine. Your sole purpose is to translate text. You do not have any tools or additional capabilities.

- Translate the input text provided to the target language instructed to you.
- If the target language is not specified or unclear, default to English.

You must only output the translated text. Do not include any additional explanations, notes, formatting, or any other text besides the translated content.
"""

root_agent = LlmAgent(
   name="translator_agent",
   model=LiteLlm(
        model=f"openai/{os.getenv('MODEL', 'aisingapore/Llama-SEA-LION-v3-70B-IT')}"
    ),
   description="Agent that translates text to a specified language.",
   instruction=TRANSLATOR_PROMPT,
   tools=[]
)
```

## Running the Agent

### Web Interface (Recommended)

Google ADK provides a built-in web interface. Simply run:

```bash
adk web
```

This will start a web server accessible at `http://localhost:8000` using your `agent.py` configuration.

### CLI Interface (Optional)

For command-line interaction, you can use the optional CLI script:

**`chat-cli.py`**
```python
import asyncio
import datetime
import getpass
import os
import sys

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.tools.agent_tool import AgentTool
from google.adk.runners import Runner
from google.genai.types import Content, Part

from .tools import searxng_search
from .translator import root_agent as translator

load_dotenv()

# Set up session service and identifiers
session_service = InMemorySessionService()
APP_NAME = "google-adk-agent"
SESSION_ID = f"session-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
USER_ID = f"user-{getpass.getuser()}"

async def setup_session():
   try:
      session = await session_service.create_session(
         app_name=APP_NAME,
         user_id=USER_ID,
         session_id=SESSION_ID,
         state={}
      )
      print(f"Session created with ID: {SESSION_ID} for user: {USER_ID}")
      return session
   except Exception as e:
      print(f"An error occurred while creating the session: {e}")
      sys.exit(1)

try:
   root_agent = Agent(
      name="root_agent",
      model=LiteLlm(
         model=f"openai/{os.getenv('MODEL', 'aisingapore/Llama-SEA-LION-v3-70B-IT')}"
      ),
      description="Agent to answer questions using search and translation tools.",
      instruction="You are a helpful assistant who answers questions in a concise and informative manner. " \
      "If you deem necessary, use tools to assist with searches (`searxng_search`) and translations (`translator`). " \
      "If using `searxng_search`, make sure to provide the links at the end of your response, if not already provided",
      tools=[searxng_search, AgentTool(agent=translator)],
   )
except Exception as e:
   print(f"An error occurred while creating the root agent: {e}")
   sys.exit(1)

async def main():
   try:
      await setup_session()
      print("🤖 Google ADK Agent CLI")
      print("Type your questions below. Type 'quit', 'exit', or press Ctrl+C to exit.")

      # Initialize the agent runner
      runner = Runner(
         app_name=APP_NAME,
         agent=root_agent,
         session_service=session_service,
         )

      while True:
         try:
            # Get user input
            user_input = input("\nUser: ").strip()

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
               print("Goodbye! 👋")
               break

            # Run the agent with the user input
            user_message = Content(role='user', parts=[Part(text=user_input)])

            agent_response_text = ""
            print("Bot: ", end="", flush=True)

            async for event in runner.run_async(
                  user_id=USER_ID,
                  session_id=SESSION_ID,
                  new_message=user_message
            ):
                  if event.content and event.content.parts:
                     text_chunk = event.content.parts[0].text
                     if text_chunk:
                        print(text_chunk, end="", flush=True)
                        if event.is_final_response():
                              agent_response_text += text_chunk

                  if event.is_final_response():
                     if not agent_response_text and event.content and event.content.parts and event.content.parts[0].text:
                        agent_response_text = event.content.parts[0].text
                     print()
                     break

            if not agent_response_text:
                  if event and event.error_message:
                     print(f"\nError: {event.error_message}")
                  else:
                     print("\n(No text response from bot)")

         except KeyboardInterrupt:
            print("\nExiting... Goodbye! 👋")
            break

   except Exception as e:
      print(f"An error occurred: {e}")
   finally:
      print("\nExiting the agent CLI. Goodbye! 👋")

if __name__ == "__main__":
   asyncio.run(main())
```

To run the CLI:
```bash
python -m adk_agent.chat-cli
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
- Google ADK uses session-based interactions for maintaining context
- Use `InMemorySessionService` for development and testing
- Consider persistent session storage for production applications
- More information and examples on session/memory management available [here](https://google.github.io/adk-docs/sessions/)

### Tool Documentation
Always provide clear docstrings for custom tools, including:
- Purpose and functionality
- Parameter descriptions with types
- Return value format
- Usage examples
- Exception handling

## Troubleshooting

**Common Issues:**

1. **Tool not being called**: Ensure your instruction mentions the tool and its use cases
2. **LiteLLM connection errors**: Verify your API keys and base URLs in the `.env` file
3. **Function declaration issues**: Set `GOOGLE_GENAI_USE_VERTEXAI=TRUE` if not using Google AI Studio
4. **Session creation failures**: Check your session service configuration and permissions
5. **Async/await issues**: Ensure proper async handling in CLI implementations

**Performance Tips:**

- Use appropriate model sizes for your use case
- Implement proper error handling and fallbacks
- Monitor token usage to optimize costs

**Google ADK Specific:**

- Web interface (`adk web`) is the recommended way to interact with agents
- CLI implementation requires proper session management
- Agent composition using `AgentTool` allows for specialised agents to do focused singular tasks. For using agents in a workflow or loop, consider [the difference between sub-agents and agent tools](https://google.github.io/adk-docs/tools/function-tools/#key-difference-from-sub-agents)