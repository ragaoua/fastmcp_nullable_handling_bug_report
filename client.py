from fastmcp import Client
import json
import asyncio


# Use jq to pretty print them
def pretty_print_tool(tool):
    print(
        json.dumps(
            {
                "name": tool.name,
                "inputSchema": tool.inputSchema,
                "outputSchema": tool.outputSchema,
            },
            indent=4,
        )
    )


async def main():
    async with Client("./server.py") as mcp:
        tools = await mcp.list_tools()

        # for tool in tools:
        #     pretty_print_tool(tool)

        tool = next(t for t in tools if t.name == "get_item")

        res = await mcp.call_tool(name=tool.name)
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
