# Tool Implementation Example

This guide provides practical tool implementations for SEA-LION models, including working code, parsing logic, and execution frameworks. The implementations cover common patterns that you can adapt for your specific use cases.

## What's Included

This example includes the components typically needed for tool calling:

- **Tool Functions**: Working implementations for weather, time, and web search
- **Schema Definitions**: OpenAI-compatible tool schemas for model integration  
- **System Prompts**: Prompts configured for different model types (Gemma v4, Llama v3, etc.)
- **Response Parsing**: Parsing logic for both native and text-based tool calls
- **Execution Framework**: Tool execution system with error handling
- **Customization Guide**: Instructions for adapting these examples to your own tools

The three example tools (weather, time, web search) demonstrate different common patterns—external API integration, system functions, and data processing. You can use these directly or as templates when building your own tools.

### Tool Functions

#### Weather Tool Implementation

```python
async def get_weather(location, session):
    """Get weather information using Open-Meteo API."""
    if not location or not isinstance(location, str):
        raise ValueError("Invalid location")

    # Geocoding request to resolve location
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    geocode_params = {
        "name": location,
        "count": 1,
        "language": "en",
        "format": "json",
    }
    
    async with session.get(geocode_url, params=geocode_params, timeout=20) as response:
        geo_data = await response.json()
    
    results = geo_data.get("results", [])
    if not results:
        raise ValueError(f"No results found for location: {location}")
    
    first = results[0]
    latitude = first["latitude"]
    longitude = first["longitude"]
    resolved = {
        "name": first["name"],
        "country": first["country"],
        "admin1": first.get("admin1"),
        "latitude": latitude,
        "longitude": longitude,
        "timezone": first.get("timezone"),
    }

    # Weather forecast request
    forecast_url = "https://api.open-meteo.com/v1/forecast"
    forecast_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,weather_code,wind_speed_10m",
        "wind_speed_unit": "kmh",
        "timezone": "auto",
    }
    
    async with session.get(forecast_url, params=forecast_params, timeout=20) as response:
        forecast_data = await response.json()

    current = forecast_data.get("current")
    units = forecast_data.get("current_units")
    if not current:
        raise ValueError("Weather data unavailable")

    return {
        "locationQueried": location,
        "resolvedLocation": resolved,
        "current": current,
        "units": units,
        "source": "open-meteo.com",
    }
```

#### Time Tool Implementation

```python
from datetime import datetime
from zoneinfo import ZoneInfo

async def get_current_time(timezone):
    """Get current time in specified timezone."""
    if not timezone or not isinstance(timezone, str):
        raise ValueError("Invalid timezone")

    try:
        now = datetime.now()
        tz = ZoneInfo(timezone)
        time_in_timezone = now.astimezone(tz)
        
        formatted_time = time_in_timezone.strftime("%m/%d/%Y, %I:%M:%S %p %Z")
        
        return {
            "timezone": timezone,
            "currentTime": formatted_time,
            "utcTime": now.isoformat() + "Z",
            "timestamp": int(now.timestamp() * 1000)
        }
    except Exception as err:
        raise ValueError(f"Invalid timezone: {timezone}")
```

#### Web Search Tool Implementation

```python
import os

async def search_web(query, session):
    """Search web using SEARXNG (requires SEARXNG_URL environment variable)."""
    if not query or not isinstance(query, str):
        raise ValueError("Invalid search query")

    try:
        # You'll need to set up SEARXNG or use another search API
        search_url = f"{os.getenv('SEARXNG_URL')}/search"
        search_params = {
            "q": query,
            "format": "json",
            "engines": "google,duckduckgo,bing"
        }
        
        async with session.get(search_url, params=search_params, timeout=15) as response:
            search_data = await response.json()

        results = search_data.get("results", [])
        if not results:
            raise ValueError("No search results found")

        # Return top 5 results with cleaned data
        top_results = []
        for result in results[:5]:
            top_results.append({
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "content": result.get("content") or result.get("snippet", ""),
                "engine": result.get("engine", "")
            })

        return {
            "query": query,
            "resultsCount": len(results),
            "topResults": top_results,
            "source": "searxng"
        }
    except Exception as err:
        raise ValueError(f"Search failed: {str(err)}")
```
### Tool Schema Definition

```python
def build_tool_schema():
    return [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather information for a location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city or location to get weather for"
                        },
                    },
                    "required": ["location"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_time",
                "description": "Get the current time in a specified timezone.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timezone": {
                            "type": "string",
                            "description": 'The timezone to get time for (e.g., "America/New_York", "Europe/London", "Asia/Singapore")'
                        },
                    },
                    "required": ["timezone"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_web",
                "description": "Search the web for information using SEARXNG search engine.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query to look for on the web"
                        },
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
        },
    ]
```

### System Prompt Configuration

```python
def build_system_message():
    return {
        "role": "system",
        "content": (
            "You are a helpful assistant with access to weather information, time checking, and web search capabilities. "
            "\n\nYou have three tools available: get_weather, get_time, and search_web. "
            "\n\nIMPORTANT: When you need to use a tool, you MUST wrap the function call in a tool_code code block using the exact format specified below:"
            "\n\nFOR WEATHER:\n```tool_code\nget_weather(location=\"City Name\")\n```"
            "\n\nFOR TIME:\n```tool_code\nget_time(timezone=\"Timezone\")\n```"
            "\n\nFOR WEB SEARCH:\n```tool_code\nsearch_web(query=\"search terms\")\n```"
            "\n\nCRITICAL REQUIREMENTS:"
            "\n- Always wrap tool calls in ```tool_code code blocks"
            "\n- Use the EXACT function call syntax shown above"
            "\n- Always use double quotes around parameter values"
            "\n- Do NOT use JSON format or any other format"
            "\n- When a user asks for weather, time, or current information, you MUST use the appropriate tool"
            "\n- Do NOT try to answer from your knowledge alone for these requests"
            "\n\nAfter receiving tool results, provide a helpful response based on the actual data returned."
        )
    }
```

### Response Parsing

```python
def parse_tool_calls_from_text(content):
    """Parse tool calls from text content using regex patterns."""
    if not content or not isinstance(content, str):
        return None
    
    # Extract content from tool_code blocks
    tool_code_pattern = r'```tool_code\s*([\s\S]*?)\s*```'
    tool_code_matches = re.findall(tool_code_pattern, content)
    
    search_content = '\n'.join(tool_code_matches) if tool_code_matches else content
    
    # Define regex patterns for different tool calls
    patterns = [
        (r'get_weather\s*\(\s*location\s*=\s*[\'"]([^\'"]+)[\'"]\s*\)', "get_weather", "location"),
        (r'get_time\s*\(\s*timezone\s*=\s*[\'"]([^\'"]+)[\'"]\s*\)', "get_time", "timezone"),
        (r'search_web\s*\(\s*query\s*=\s*[\'"]([^\'"]+)[\'"]\s*\)', "search_web", "query"),
    ]
    
    results = []
    for pattern, func_name, param_name in patterns:
        matches = re.findall(pattern, search_content)
        for i, match in enumerate(matches):
            results.append({
                "id": f"text_parsed_{func_name}_{i}",
                "function": {
                    "name": func_name,
                    "arguments": json.dumps({param_name: match})
                }
            })
    
    return results if results else None
```

### Tool Execution Framework

```python
async def execute_tool_calls(tool_calls, session):
    """Execute the tool calls and return results."""
    results = []
    
    for call in tool_calls:
        name = call.get("function", {}).get("name")
        args = call.get("function", {}).get("arguments")
        try:
            args = json.loads(args) if isinstance(args, str) else args
        except json.JSONDecodeError:
            args = {}

        try:
            if name == "get_weather":
                location = args.get("location")
                result = await get_weather(location, session)
            elif name == "get_time":
                timezone = args.get("timezone")
                result = await get_current_time(timezone)
            elif name == "search_web":
                query = args.get("query")
                result = await search_web(query, session)
            else:
                result = {"error": f"Unknown tool: {name}"}

            results.append({
                "tool_call_id": call.get("id"),
                "role": "user",
                "name": name,
                "content": json.dumps(result)
            })
        except Exception as err:
            error_result = {"name": name, "error": str(err)}
            results.append({
                "tool_call_id": call.get("id"),
                "role": "user", 
                "name": name,
                "content": json.dumps(error_result)
            })
    
    return results
```

### Customizing Tools for Your Application

The example tools above demonstrate different types of functionality:

- **get_weather**: External API integration with error handling
- **get_time**: System/library function usage with timezone handling  
- **search_web**: Complex data processing and result formatting

To create your own tools:

1. **Define your function**: Create an async function that takes parameters and returns structured data
2. **Add error handling**: Always validate inputs and handle exceptions gracefully
3. **Update the tool schema**: Define the function signature for the model
4. **Modify the execution framework**: Add your function to the `execute_tool_calls` function
5. **Update system prompts**: Include your tool in the system message (for Gemma v4)

Example of a custom tool:

```python
# Custom database query tool
async def query_database(table, filters):
    """Query database with filters."""
    if not table or not isinstance(table, str):
        raise ValueError("Invalid table name")
    
    # Your database logic here
    # This is just an example structure
    try:
        # connection = await get_db_connection()
        # results = await connection.fetch(f"SELECT * FROM {table} WHERE {filters}")
        results = [{"id": 1, "name": "example"}]  # placeholder
        
        return {
            "table": table,
            "filters": filters,
            "results": results,
            "count": len(results)
        }
    except Exception as err:
        raise ValueError(f"Database query failed: {str(err)}")

# Add to tool schema
{
    "type": "function",
    "function": {
        "name": "query_database",
        "description": "Query a database table with optional filters.",
        "parameters": {
            "type": "object",
            "properties": {
                "table": {"type": "string", "description": "The table name to query"},
                "filters": {"type": "string", "description": "SQL WHERE clause filters"}
            },
            "required": ["table"],
            "additionalProperties": False,
        },
    },
}
```