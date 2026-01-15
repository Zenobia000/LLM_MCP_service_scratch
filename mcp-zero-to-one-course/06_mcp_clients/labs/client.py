"""
Lab 3: 實作自定義 Python Client
檔案路徑: 06_mcp_clients/labs/client.py

本練習將展示如何撰寫程式碼來充當 Client，主動連接並呼叫 MCP Server。
這也是打造自己的 AI Agent 的第一步。
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 設定我們要連接的 Server 參數
# 這裡我們連接 Lab 1 的 basic_tool.py
server_params = StdioServerParameters(
    command="uv",
    args=[
        "run",
        "/home/os-sunnie.gd.weng/python_workstation/side-project/LLM_mcp_service_zero_to_one/mcp-zero-to-one-course/05_first_mcp_server/labs/basic_tool.py"
    ],
    env=None
)

async def run():
    print("🚀 正在連接 MCP Server...")
    
    # 使用 context manager 建立 stdio 連線
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 1. 初始化 (Handshake)
            await session.initialize()
            print("✅ 連接成功！")

            # 2. 列出可用工具
            tools = await session.list_tools()
            print(f"\n📋 發現 {len(tools.tools)} 個工具：")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # 3. 呼叫工具 (add)
            print("\n🔢 正在測試 'add' 工具 (10 + 25)...")
            result = await session.call_tool("add", arguments={"a": 10, "b": 25})
            
            # 顯示結果
            # 結果通常是一個 TextContent 物件列表
            print(f"👉 結果：{result.content[0].text}")

            # 4. 呼叫工具 (say_hello)
            print("\n👋 正在測試 'say_hello' 工具...")
            result = await session.call_tool("say_hello", arguments={"name": "學員"})
            print(f"👉 結果：{result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(run())