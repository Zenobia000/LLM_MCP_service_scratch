# ⚡ uv 極速 Python 套件管理指南

## 為什麼選擇 uv？
在本課程中，我們捨棄傳統的 `pip` + `venv` 組合，改用 Rust 編寫的 `uv`。
- **速度快**：安裝套件比 pip 快 10-100 倍。
- **省心**：自動管理 `.venv`，不需要手動 activate/deactivate。
- **專案制**：類似 Node.js 的 `package.json` (使用 `pyproject.toml`)，確保每個人環境一致。

---

## 🚀 核心指令速查

### 1. 專案初始化與安裝
當你第一次下載本專案時，只需執行：
```bash
# 就像 npm install
uv sync
```
這會讀取 `pyproject.toml` 並自動建立 `.venv` 資料夾，安裝所有必要的套件。

### 2. 執行程式 (最重要的指令) ⭐
**忘記 `python script.py` 吧！** 請習慣使用 `uv run`：

```bash
# 執行 Python 腳本 (自動使用虛擬環境)
uv run labs/basic_tool.py

# 執行模組或工具
uv run mcp dev labs/basic_tool.py
```
`uv run` 會確保程式是在正確的隔離環境中執行，即使你沒有手動 activate 虛擬環境。

### 3. 安裝新套件
如果你想在課程中加入新的庫 (例如 `requests` 或 `pandas`)：
```bash
# 安裝並自動寫入 pyproject.toml
uv add requests pandas

# 安裝開發專用的工具 (如 pytest, ruff)
uv add --dev pytest ruff
```

### 4. 移除套件
```bash
uv remove requests
```

---

## 🛠️ MCP 開發專用流程

### 開發模式 (Debug)
開發 MCP Server 時，我們使用官方的 Inspector 工具。透過 `uv` 執行非常簡單：

```bash
# 語法：uv run mcp dev <你的檔案路徑>
uv run mcp dev 05_first_mcp_server/labs/basic_tool.py
```

### 整合至 Claude Desktop
在設定 `claude_desktop_config.json` 時，我們需要告訴 Claude 使用這個專案的環境。

**推薦設定法 (絕對路徑)**：
```json
{
  "mcpServers": {
    "my-course-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/你的/完整路徑/mcp-zero-to-one-course",
        "run",
        "05_first_mcp_server/labs/basic_tool.py"
      ]
    }
  }
}
```
這樣設定的好處是：**你不需要指定 Python 的絕對路徑**，只要 `uv` 在你的 PATH 裡，它就會自動找到正確的環境。

---

## 💻 IDE 設定 (VS Code / Cursor)

為了讓編輯器能正確讀取套件 (解決 "ImportError" 警告)：

1. 開啟 VS Code / Cursor。
2. 按下 `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)。
3. 搜尋 **"Python: Select Interpreter"**。
4. 選擇專案目錄下的 `.venv`：
   `./.venv/bin/python` (或是顯示為 `Python 3.x (venv)`)

---

## ❓ 常見問題 (FAQ)

**Q: 我需要手動 `source .venv/bin/activate` 嗎？**
A: **不需要**。只要使用 `uv run`，它會暫時性地為該指令載入環境。這更安全，因為你不會忘記自己在哪個環境裡。

**Q: `uv pip install` 和 `uv add` 有什麼不同？**
A: 
- `uv add`：會更新 `pyproject.toml` (推薦用於專案開發)。
- `uv pip install`：僅安裝到環境，不記錄依賴 (適合臨時測試)。

**Q: 我把 `.venv` 刪掉了怎麼辦？**
A: 別慌，執行 `uv sync`，它會秒速重建回來。
