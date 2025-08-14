# Wolfram Alpha MCP Server

This is an MCP (Model Context Protocol) server that provides access to the Wolfram Alpha LLM API, enabling AI assistants to query Wolfram Alpha for scientific and factual information.

## Features

- Query Wolfram Alpha's LLM API for scientific and factual information
- Asynchronous operation using anyio for better performance
- Easy integration with MCP-compatible AI assistants

## Prerequisites

1. Python 3.8 or higher
2. A Wolfram Alpha App ID (free to obtain at [wolframalpha.com](https://www.wolframalpha.com/))

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd wolfram-alpha-mcp-server
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The server requires a Wolfram Alpha App ID to function. You can obtain one by:

1. Visiting [wolframalpha.com](https://www.wolframalpha.com/)
2. Creating a free account or signing in
3. Generating an App ID for the LLM API

Once you have your App ID, you'll need to set it as an environment variable.

## Usage

### Running the Server

Run the server with your Wolfram Alpha App ID:

```bash
WOLFRAM_APP_ID=your_app_id_here python server.py
```

### Integrating with an MCP Client

To use this server with an MCP-compatible client, add the following to your MCP configuration:

```json
{
  "mcpServers": {
    "wolfram-alpha": {
      "command": "python",
      "args": [
        "/path/to/server.py"
      ],
      "env": {
        "WOLFRAM_APP_ID": "YOUR_APP_ID"
      }
    }
  }
}
```

Replace `/path/to/server.py` with the actual path to your server.py file and `YOUR_APP_ID` with your actual Wolfram Alpha App ID.

## How It Works

The server exposes a single tool:

- `wolfram_alpha_query(query: str)`: Sends a query to the Wolfram Alpha LLM API and returns the result

When an AI assistant calls this tool, the server will:
1. Take the query string
2. Send it to Wolfram Alpha's LLM API
3. Return the response to the assistant

## Example Queries

The Wolfram Alpha LLM API is particularly good at answering:
- Scientific questions ("What is the speed of light?")
- Mathematical problems ("Solve x^2 + 2x + 1 = 0")
- Factual information ("Population of Tokyo")
- Unit conversions ("Convert 100°F to Celsius")
- Chemical data ("Molecular weight of caffeine")

