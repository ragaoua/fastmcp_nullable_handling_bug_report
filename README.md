# Main files

- api.json : dummy openapi 3.0 spec. This is used to generate the MCP server.
- api.py : dummy api. This is used to expose the API.
- server.py : MCP server based on api.json
- client.py : MCP client that connects via STDIO to the MCP server to call tools

_Note : I first have tried running the API using FastAPI **then use the spec from that API**
to generate the MCP Server. The problem is this doesn't work since FastAPI generates API
that conform to the OAS 3.1 spec. Here, we want to test for OAS 3.0._

# Test

Create a python venv, source it and install the dependencies :

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the fastapi API :

```bash
fastapi dev api.py --port 8000
```

Run the fastmcp client :

```bash
python client.py
```

The client will connect to the MCP server, and try and execute the "get_item" tool.
This will return an item with a `price: null` which, even though the "price"
property has a key "nullable" set to true in `api.json`, will cause the following error :

```text
fastmcp.exceptions.ToolError: Output validation error: None is not of type 'number'
```
