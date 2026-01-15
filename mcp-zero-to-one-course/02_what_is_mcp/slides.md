# 第二章：MCP 到底是什麼？(What is MCP?)

---

## 1. MCP 的定義

**Model Context Protocol (MCP)** 是一個開放標準，它讓開發者能夠建立安全的、可重用的連接器，將資料與工具提供給 AI 模型。

*   **官方口號**：The open standard for connecting AI models to data sources.
*   **核心本質**：它不是一個 AI 模型，而是一個 **「通訊協定」** (如同 HTTP 或 USB)。

---

## 2. 核心架構：Client-Server 模型

MCP 採用經典的 **客戶端-伺服器** 架構：

### 🖥️ MCP Server (提供者)
*   **職責**：暴露資料與工具。
*   **範例**：一個能讀取本地檔案的 Server、一個能查詢資料庫的 Server。
*   **技術**：使用 Python 或 TypeScript 撰寫。

### 📱 MCP Client (使用者)
*   **職責**：連接 Server 並將獲取的內容餵給 LLM。
*   **範例**：Claude Desktop, Cursor, IDE 插件, 或你自製的 AI App。

---

## 3. 前後對比：為什麼 MCP 是革命性的？

### ❌ Before MCP (碎片化)
每個 App 都要為每個工具寫專屬的代碼。
*   Claude ←(自定義代碼)→ GitHub
*   ChatGPT ←(自定義代碼)→ GitHub
*   Cursor ←(自定義代碼)→ GitHub

### ✅ After MCP (標準化)
工具只需要寫一次，所有 Client 都能用。
*   **GitHub MCP Server** ←(標準協定)→ **任何 MCP Client** (Claude, Cursor, etc.)

---

## 4. MCP 的四方共贏生態系

| 參與者 | 獲得的好處 |
| :--- | :--- |
| **AI App 開發者** | 不需要寫整合代碼，直接連接現成的 MCP Server 即可獲取功能。 |
| **工具/資料供應商** | 只要開發一次 MCP Server，就能讓所有 AI 使用者存取你的服務。 |
| **企業 IT** | 可以在本地部署 MCP Server，安全地控制哪些資料可以被 AI 存取。 |
| **最終使用者** | 可以在同一個 AI 介面中使用各種不同的工具，大幅提升生產力。 |

---

## 5. 總結

1.  MCP 是連接模型與資料的 **開放標準**。
2.  它解耦了 **「工具實作」** 與 **「模型應用」**。
3.  它是 AI 生態系中的 **「基礎設施」**，目標是達成工具的隨插即用。

👉 **下一章：MCP 的三大法寶 (Tools, Resources, Prompts)**