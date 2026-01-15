"""
Lab 2: Resources 與 Prompts 的實作
檔案路徑: 05_first_mcp_server/labs/resources_prompts.py

本練習將展示如何定義 Resources 與 Prompts，並配合一個 Tool。
情境：建立一個「專案筆記助手」。
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Notes Assistant")

# --- 1. Resources (資源) ---
# Resources 就像是暴露給模型的檔案或資料庫內容
# 我們使用 URI 格式來標識資源
@mcp.resource("note://project/readme")
def get_readme() -> str:
    """
    提供專案的讀我檔案內容作為背景資料。
    """
    return """
    # Project X
    這是一個使用 MCP 技術開發的秘密專案。
    目前進度：10%
    負責人：MCP 課程學員
    """

# --- 2. Prompts (提示詞模板) ---
# Prompts 協助用戶快速構建對話
@mcp.prompt()
def review_project(name: str) -> str:
    """
    建立一個審查專案進度的提示詞。
    """
    return f"請根據專案 {name} 的資料，分析目前的開發瓶頸並給予建議。"

# --- 3. Tools (工具) ---
# 配合一個可以用來「儲存」新筆記的工具
@mcp.tool()
def save_note(content: str) -> str:
    """
    儲存一條新的專案筆記。
    """
    # 這裡僅作模擬演示
    print(f"DEBUG: 儲存筆記 -> {content}")
    return "筆記已成功儲存！"

if __name__ == "__main__":
    mcp.run()
