# 從零開始掌握 MCP — 模型上下文協定應用開發實戰
(Model Context Protocol: Zero to One)

歡迎來到 MCP 實戰開發課程！本課程旨在帶領開發者從第一性原理出發，理解為什麼 AI 需要 MCP，並透過實作掌握開發 MCP Server 與 Client 的核心技能。

## 🎯 課程目標

- **理解核心概念**：深入了解 LLM 的局限性以及 MCP 如何透過標準化協議解決 Context 整合問題。
- **掌握實作技能**：學會使用 Python SDK 開發 Tools, Resources 與 Prompts。
- **生態系整合**：能夠將自製的 MCP Server 整合至 Claude Desktop 或自定義的 Agent 應用中。
- **進階應用**：探索 Remote Server、安全最佳實踐以及 "Agent as a Tool" 的設計模式。

## 🛠️ 開發環境需求

在開始之前，請確保您的環境符合以下要求：

- **作業系統**: Linux / macOS / Windows (WSL2)
- **Python 版本**: Python 3.10 或更高版本
- **套件管理**: 本課程全面使用 [uv](https://docs.astral.sh/uv/) (極速 Python 套件管理器)
- **開發工具**:
  - VS Code / Cursor / Windsurf
  - [Claude Desktop App](https://claude.ai/download) (用於測試整合)

## 📚 課程清單

| 章節 | 資料夾 | 課程標題 | 學習重點 | 核心交付物 |
| :--- | :--- | :--- | :--- | :--- |
| **01** | `01_why_mcp/` | **為什麼需要 MCP** | LLM 的本質局限、Agent Loop 原理、Context Engineering | 觀念簡報、概念圖解 |
| **02** | `02_what_is_mcp/` | **MCP 是什麼** | 標準化協定介紹、Before/After 比較、生態系四方共贏 | 觀念簡報、對照表 |
| **03** | `03_core_concepts/` | **三大核心功能** | Tools (工具)、Resources (資源)、Prompts (提示詞) 的定義與區別 | 架構圖、JSON Schema 範例 |
| **04** | `04_protocol_basics/` | **通訊協定基礎** | stdio vs HTTP/SSE、JSON-RPC 訊息流、握手過程 | 時序圖 (Sequence Diagrams) |
| **05** | `05_first_mcp_server/` | **動手做第一個 Server** | 環境建置、FastMCP 實作、使用 MCP Inspector 除錯 | `hello_mcp.py`、除錯指南 |
| **06** | `06_mcp_clients/` | **Client App 整合** | Claude Desktop 設定檔詳解、Python Client SDK 實作 | `config.json`、自製 Client |
| **07** | `07_remote_advanced/` | **遠端進階應用** | 建立 Remote SSE Server、Agent as a Tool 模式 | 遠端部署範例、Agent 互通實作 |
| **08** | `08_security_future/` | **安全性與未來展望** | 安全風險 (Injection, Spoofing)、MCP Registry、Roadmap | 安全檢查表、參考資源 |
| **09** | `09_final_project/` | **綜合實戰專案** | 期末專案：打造個人 AI 助理工具箱 | 完整專案原始碼 |

## 🚀 快速開始

1. **安裝 uv** (如果尚未安裝)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone 本專案**
   ```bash
   git clone <repository-url>
   cd mcp-zero-to-one-course
   ```

3. **同步環境與依賴**
   ```bash
   uv sync
   ```

4. **執行 Lab 範例**
   ```bash
   uv run 05_first_mcp_server/labs/basic_tool.py
   ```

5. **進入章節目錄開始學習**
   請依照章節順序，進入對應資料夾閱讀教材並執行 Lab 練習。

---

## 🔗 相關資源

- [Model Context Protocol 官方文件](https://modelcontextprotocol.io/)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [MCP Servers Gallery](https://github.com/modelcontextprotocol/servers)

---
*Created for the "MCP Zero to One" Course. Updated: 2026-01-15*
