from mcp.server.fastmcp import FastMCP
import os
import requests
import urllib.parse
import anyio

# Create the MCP server
mcp = FastMCP("Wolfram Alpha Integration")

def get_wolfram_app_id():
    """Get Wolfram Alpha AppID from environment variable"""
    app_id = os.getenv("WOLFRAM_APP_ID")
    if not app_id:
        raise ValueError("WOLFRAM_APP_ID environment variable not set")
    return app_id

@mcp.tool()
async def wolfram_alpha_query(query: str):
    """Query Wolfram Alpha LLM API for scientific and factual information"""
    return await anyio.to_thread.run_sync(perform_query, query)

def perform_query(query):
    app_id = get_wolfram_app_id()
    url = "https://www.wolframalpha.com/api/v1/llm-api"
    params = {
        "input": query,
        "appid": app_id
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error querying Wolfram Alpha: {str(e)}"

if __name__ == "__main__":
    mcp.run()

