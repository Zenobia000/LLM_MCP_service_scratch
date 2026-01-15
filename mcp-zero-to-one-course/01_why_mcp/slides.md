# 第一章：為什麼需要 MCP？(Why MCP?)

---

## 1. 核心問題：LLM 的本質局限

### 🧠 "天才在密室" (Genius in a Locked Room)
想像一個智商極高的人（LLM），被關在一個完全封閉的房間裡。

*   **知識截止 (Knowledge Cutoff)**：他讀過的書只到 2023 年。
*   **與世隔絕 (Isolation)**：他沒有網路，無法 Google 搜尋。
*   **無行動力 (No Agency)**：他無法幫你訂披薩，只能寫下訂披薩的步驟。

> **結論**：Raw Intelligence (原始智力) ≠ Capable Assistant (能幹的助理)。

---

## 2. 解決方案：給模型「雙手」 (Tools)

為了讓 LLM 有用，我們發明了 **Agent (代理人)** 架構。

### Agent 的基本公式
```
Agent = LLM + Tools + Runtime Loop
```

![Agent Loop Diagram](./diagrams/agent_loop.mermaid)

1.  **使用者**：「幫我查詢台北現在的天氣。」
2.  **LLM 思考**：「我不知道。但我有一個叫 `get_weather` 的工具。」
3.  **執行 (Runtime)**：程式呼叫氣象 API。
4.  **回饋 (Feedback)**：API 回傳 `{temp: 25, loc: "Taipei"}`。
5.  **LLM 回答**：「台北現在 25 度。」

---

## 3. 災難的開始：整合地獄 (Integration Hell)

在 MCP 出現之前，連接每一個工具都是一場惡夢。

### 🚫 The "Spaghetti" Reality (義大利麵現狀)
*   **Google Drive** 需要接一次...
*   **Slack** 需要接一次...
*   **PostgreSQL** 需要接一次...

而且，每一個 AI 應用 (Claude, ChatGPT, LangChain) 的接口定義 **都不一樣**！

*   開發者要維護 N 個工具 x M 個平台 = **N x M 的複雜度**。

---

## 4. Context Engineering (上下文工程)

我們需要的不是寫更多的 Python Glue Code (膠水程式碼)，而是需要一種標準化的方式來提供 Context。

### 什麼是 Context？
*   **檔案內容** (Project Docs)
*   **資料庫紀錄** (User Data)
*   **即時狀態** (System Logs)

### MCP 的願景
讓 **「提供 Context」** 變得像 **「插入 USB 隨身碟」** 一樣簡單。
*   不管你是接滑鼠、鍵盤還是印表機 (Tools)，USB 接口都是一樣的。
*   不管你是接 Windows, Mac 還是 Linux (Clients)，USB 接口也是一樣的。

---

## 5. 本章小結

1.  LLM 本身是被隔離的，需要 **Tools** 才能與世界互動。
2.  傳統的工具整合方式導致了 **N x M** 的維護成本。
3.  我們需要一個 **通用標準** 來連接 AI 模型與資料來源。
4.  這就是 **MCP (Model Context Protocol)** 誕生的原因。

👉 **下一章：MCP 到底是什麼？(技術架構解析)**