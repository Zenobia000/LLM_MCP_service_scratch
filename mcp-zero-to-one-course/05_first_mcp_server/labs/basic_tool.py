"""
Lab 1: 第一個 MCP Server 工具
檔案路徑: 05_first_mcp_server/labs/basic_tool.py

【如何執行】
請勿直接執行此檔案 (如 python basic_tool.py)，因為它需要 JSON-RPC 通訊。
請使用以下指令啟動 Inspector 進行測試：
👉 uv run mcp dev 05_first_mcp_server/labs/basic_tool.py

這個練習將引導你使用 FastMCP SDK 建立兩個基礎工具：
1. add: 數字加法器
2. echo: 訊息回傳器
"""

from mcp.server.fastmcp import FastMCP

# 1. 初始化 FastMCP
# 名稱會顯示在 MCP Inspector 和 Client App 中
mcp = FastMCP("My First MCP Server")

# 2. 定義一個簡單的工具
# 使用 @mcp.tool() 裝飾器將函數轉換為 MCP Tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    將兩個整數相加。
    
    這是 Tool 的說明 (Description)，LLM 會讀取這段文字來判斷何時該使用此工具。
    """
    return a + b

# 3. 定義一個帶有預設值的工具
@mcp.tool()
def say_hello(name: str = "陌生人") -> str:
    """
    向某人打招呼。
    """
    return f"你好, {name}! 歡迎來到 MCP 的世界。"

# 4. 程式執行入口
if __name__ == "__main__":
    # 當直接執行此檔案時，啟動 Server
    # 預設使用 stdio 通訊模式
    mcp.run()