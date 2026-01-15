# 🚀 MCP Zero to One: 模型上下文協定實戰開發

![MCP](https://img.shields.io/badge/MCP-SDK-blue) ![Python](https://img.shields.io/badge/Python-3.11%2B-green) ![License](https://img.shields.io/badge/License-MIT-orange)

歡迎來到 **「從零開始掌握 MCP」** 課程專案！本儲存庫包含了完整的教學文件、實作練習與範例代碼，旨在幫助開發者快速掌握 Model Context Protocol (MCP) 的開發技術。

## 🎯 課程目標

- **理解核心概念**：深入了解 LLM 的局限性以及 MCP 如何透過標準化協議解決 Context 整合問題。
- **掌握實作技能**：學會使用 Python SDK 開發 Tools, Resources 與 Prompts。
- **生態系整合**：能夠將自製的 MCP Server 整合至 Claude Desktop 或自定義的 Agent 應用中。
- **進階應用**：探索 Docker 部署、Remote Server 以及安全性最佳實踐。

## 📂 章節導航

| 章節 | 標題 | 內容簡介 | 關鍵資源 |
| :--- | :--- | :--- | :--- |
| **Ch01** | [為什麼需要 MCP](./01_why_mcp/) | LLM 的局限與 Agent 架構 | [Slides](./01_why_mcp/slides.md), [Agent Loop](./01_why_mcp/diagrams/agent_loop.mermaid) |
| **Ch02** | [MCP 是什麼](./02_what_is_mcp/) | 協定架構與 Before/After 對比 | [Slides](./02_what_is_mcp/slides.md), [Comparison](./02_what_is_mcp/before_after_comparison.md) |
| **Ch03** | [三大核心功能](./03_core_concepts/) | Tools, Resources, Prompts 詳解 | [Slides](./03_core_concepts/slides.md), [Schema](./03_core_concepts/schema_samples/tool_schema.json) |
| **Ch04** | [通訊協定基礎](./04_protocol_basics/) | JSON-RPC, stdio, SSE 原理 | [Slides](./04_protocol_basics/slides.md), [Sequence](./04_protocol_basics/sequence_charts/tool_execution.mermaid) |
| **Ch05** | [實作第一個 Server](./05_first_mcp_server/) | **🔥 核心實作**：Hello World 與計算機 | [Code: Basic](./05_first_mcp_server/labs/basic_tool.py), [Guide](./05_first_mcp_server/guides/inspector_guide.md) |
| **Ch06** | [Client App 整合](./06_mcp_clients/) | Claude Desktop 設定與 Python Client | [Config](./06_mcp_clients/configs/claude_desktop_config.json), [Code: Client](./06_mcp_clients/labs/client.py) |
| **Ch07** | [遠端進階應用](./07_remote_advanced/) | Docker 容器化部署 (SSE) | [Code: Remote](./07_remote_advanced/labs/remote_server.py), [Docker Guide](./07_remote_advanced/guides/docker_deploy.md) |
| **Ch08** | [安全性與未來](./08_security_future/) | 安全檢查清單與生態系展望 | [Checklist](./08_security_future/security_checklist.md), [Slides](./08_security_future/slides.md) |
| **Ch09** | [期末專案](./09_final_project/) | 打造你的個人 AI 助理工具箱 | [Project Brief](./09_final_project/project_brief.md) |

## 🛠️ 快速開始 (Quick Start)

### 1. 環境準備
本專案使用 `uv` 進行套件管理 (比 pip 快 10-100 倍)。

```bash
# 安裝 uv (如果尚未安裝)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone 專案
git clone https://github.com/Zenobia000/LLM_MCP_service_scratch.git
cd mcp-zero-to-one-course

# 初始化環境
uv sync
```

### 2. 啟動第一個 Server (Inspector 模式)
```bash
uv run mcp dev 05_first_mcp_server/labs/basic_tool.py
```

### 3. 使用 Docker 部署遠端 Server
```bash
cd 07_remote_advanced/labs
docker build -t mcp-remote-server .
docker run -d -p 8090:8000 --name my-mcp-server mcp-remote-server
```

## 📚 參考資源
- [Model Context Protocol 官方文件](https://modelcontextprotocol.io/)
- [MCP Servers Gallery](https://github.com/modelcontextprotocol/servers)

---
*Maintained by MCP Course Team. Last Updated: 2026-01-15*