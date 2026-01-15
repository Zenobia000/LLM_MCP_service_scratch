# 第 5 章：動手做第一個 MCP Server

在本章節中，我們將學習如何從零開始建立一個 MCP Server。

## 🎯 學習目標
1. 熟悉 `uv` 開發流程。
2. 實作一個簡單的 MCP Tool。
3. 使用 MCP Inspector 進行除錯。

## 🛠️ 開發流程

### 1. 安裝環境
我們在專案根目錄已經初始化了 `uv` 環境，請確保您已執行過：
```bash
uv sync
```

### 2. 撰寫程式碼
請參考 `labs/basic_tool.py`。我們使用 `FastMCP` 來快速建立 Server：

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyFirstServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b
```

### 3. 使用 uv 執行與除錯
您可以使用以下指令啟動 **MCP Inspector**，它會自動開啟網頁界面供您測試工具：

```bash
uv run mcp dev labs/basic_tool.py
```

> **注意**：`mcp dev` 是除錯時的最佳夥伴，它能即時重載代碼。

## 🧪 練習內容
- [ ] 完成 `labs/basic_tool.py` 中的加法工具。
- [ ] 試著加入一個會回傳當前時間的 Tool。