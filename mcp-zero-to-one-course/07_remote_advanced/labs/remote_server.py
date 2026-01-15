"""
Lab 4: 遠端 MCP Server (SSE 模式)
檔案路徑: 07_remote_advanced/labs/remote_server.py
"""

from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP
mcp = FastMCP("Remote Calculator")

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """乘法運算"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """除法運算"""
    if b == 0:
        raise ValueError("除數不能為零")
    return a / b

# 注意：我們不再需要 if __name__ == "__main__": mcp.run()
# 因為我們會直接透過 uvicorn 存取 mcp.sse_app