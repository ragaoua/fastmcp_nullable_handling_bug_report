from fastmcp import FastMCP
import json
import httpx

api_url = "http://127.0.0.1:8000"

api_spec = None
with open("./api.json", "r") as f:
    api_spec = json.loads(f.read())
client = httpx.AsyncClient(base_url=api_url)

server = FastMCP.from_openapi(
    openapi_spec=api_spec,
    client=client,
)

server.run()
