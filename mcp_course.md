# MCP 應用開發完整教學課程規劃

## 課程總覽

**課程名稱**：從零開始掌握 MCP — 模型上下文協定應用開發實戰

**課程目標**：讓學習者理解 MCP 的核心概念、設計原理與實務應用，能夠獨立開發 MCP Server 並整合至 AI 應用中。

**課程時長**：約 12-16 小時（可拆分為 8 堂課）

---

## 第一章：為什麼需要 MCP？（第一性原理）

### 1.1 從 LLM 的本質談起
- **核心問題**：LLM 是被關在房間裡的天才 [4]
- 大模型的限制：無法主動學習、無法存取即時資訊、無法操作外部世界
- **關鍵洞察**：Raw Intelligence ≠ Intelligent Software Systems [7]

### 1.2 Agent 的誕生：讓 LLM 能「做事」
- Agent 的本質：LLM + Tools + Loop [5][6]
- 簡單示意：
  ```
  目標 → LLM 思考 → 選擇工具 → 執行 → 回傳結果 → 繼續思考 → 完成任務
  ```
- **教學重點**：先讓學員理解「工具」對 LLM 的重要性

### 1.3 Context Engineering 的重要性
- 兩大關鍵要素：
  1. 🔧 工具整合
  2. 📦 正確的上下文 [7]
- **思考題**：如果每個工具都要自己寫整合，會發生什麼問題？

---

## 第二章：MCP 是什麼？（概念建立）

### 2.1 MCP 的定位與願景
- 標準化協議：模型如何取得 Context 的統一方式 [8]
- 類比說明：就像 USB 統一了各種設備的連接方式

### 2.2 Before vs After MCP
- **Before**：每個 API 都要寫 function schema + 實作 [10]
- **After**：
  - 啟動時：Client 向 Server 查詢工具清單 [11]
  - 執行時：透過標準化方式呼叫工具 [12]

### 2.3 MCP 的四方共贏
| 角色 | 好處 |
|------|------|
| AI App 開發者 | 銜接任何 MCP server 超簡單 |
| 工具廠商 | 建構一次，所有 Client 都能用 |
| AI App 用戶 | App 具備擴充能力 |
| 企業 | Agent 團隊與 Tool 團隊可分工 |

[13]

---

## 第三章：MCP 的三大核心功能

### 3.1 Tools — 給模型用的工具 ⭐ 最重要
- 設計目的：讓 LLM 透過 function calling 使用 [16]
- **簡單範例**：產生隨機數字的工具
- **教學重點**：理解 Tool = Function Schema + 實作

### 3.2 Resources — 給 App 用的資料
- 設計目的：讓 Client App 取得資料 [18]
- 類比：就像網頁的 GET 請求
- **思考題**：為什麼不直接用 Tool 提供資料？
  - 答案：用途不同，Resources 是給 App 決定如何使用

### 3.3 Prompts — 給用戶用的提示詞模板
- 設計目的：提供預設的高品質 prompt template [19]
- 應用場景：資料分析、摘要生成等複雜任務

### 3.4 三者的關係圖解
```
MCP Server 提供
    ├── Tools → 給 LLM 使用
    ├── Resources → 給 Client App 使用
    └── Prompts → 給用戶選擇使用
```
[15]

---

## 第四章：MCP 的通訊方式（技術基礎）

### 4.1 三種傳輸協議總覽
| 類型 | 協議 | 適用場景 |
|------|------|----------|
| 本機 | stdio | 大部分情況 |
| 遠端 | HTTP+SSE | 舊版遠端 |
| 遠端 | Streamable HTTP | 新版遠端（推薦）|

[22]

### 4.2 本機模式：stdio 詳解
- 運作原理：透過 child process 的標準輸入輸出溝通 [23]
- 優點：簡單、可用本機資源
- 缺點：需要本機環境能正確執行

### 4.3 遠端模式：HTTP 協議
- SSE 版本：需維持持續連線 [24]
- Streamable HTTP：可 Stateless，部署更容易 [25]

### 4.4 實作考量
- **教學重點**：先從 stdio 開始學習，熟悉後再進階到遠端

---

## 第五章：動手做第一個 MCP Server

### 5.1 開發環境準備
- 安裝 Python SDK [16]
- 安裝 MCP Inspector 除錯工具 [26]

### 5.2 Hello MCP：最簡單的 Tool
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("我的第一個 MCP Server")

@mcp.tool()
def say_hello(name: str) -> str:
    """跟某人打招呼"""
    return f"你好，{name}！"
```
- **教學重點**：理解裝飾器、參數定義、docstring 的作用

### 5.3 使用 MCP Inspector 測試
- 啟動 Inspector
- 連接到你的 MCP Server
- 測試 Tool 是否正常運作 [26]

### 5.4 加入 Resources 與 Prompts
- 實作一個簡單的 Resource
- 實作一個 Prompt Template
- **教學重點**：體驗三種功能的差異

---

## 第六章：在 Client App 中使用 MCP

### 6.1 常見的 MCP Client 介紹
- Claude Desktop App
- ChatWise
- Cursor / Windsurf Editor
- 自行開發的 Agent 程式 [9]

### 6.2 實作：在 Claude Desktop 安裝 MCP Server
- 設定 `claude_desktop_config.json`
- 啟動並測試
- **教學重點**：理解設定檔的結構與意義

### 6.3 實作：用 Python 開發 MCP Client
- 使用官方 Python SDK [28]
- 連接 MCP Server
- 取得 Tools 並整合到 Agent [29][30]

### 6.4 使用 OpenAI Agents SDK 整合
- 更簡潔的整合方式 [31]
- **教學重點**：理解不同整合方式的優缺點

---

## 第七章：Remote MCP Server 進階應用

### 7.1 為什麼需要 Remote MCP Server？
- 跨裝置使用
- 不需要本機環境
- 團隊共享工具

### 7.2 實作：建立 Remote MCP Server
- 使用 SSE 協議
- 使用 Streamable HTTP 協議

### 7.3 踩坑經驗分享
- Client 支援度問題 [32]
- 認證機制的混亂現況 [33]
- 解決方案：使用 Cloudflare proxy [32]

### 7.4 實作範例：Agent as MCP Server
- 將一個 Agent 包裝成 MCP Server [38]
- 讓其他 Agent 可以「對話」這個 Agent
- **教學重點**：理解 Agents as Tools 的概念 [35][36]

---

## 第八章：安全性、生態系與未來展望

### 8.1 MCP 的安全性考量
| 風險類型 | 說明 |
|----------|------|
| 程式執行攻擊 | 惡意 MCP Server 執行惡意程式碼 |
| 命名攻擊 | 冒充合法工具名稱 |
| 工具中毒 | 在 description 中注入惡意 prompt |
| 工具過多 | 名稱衝突、影響 LLM 性能 |

[42]

### 8.2 解決方案與最佳實踐
- 只安裝可信任來源的 MCP Server
- 設計工具搜尋機制
- 逐層揭露工具 [42]

### 8.3 MCP 生態系現況
- 快速發展中的生態系 [14]
- 推薦的 MCP Servers [27]

### 8.4 未來發展藍圖
- **MCP Registry**：統一的 metadata 服務 [43]
- **Server Discovery**：`.well-known/mcp` 標準化 [44]
- **Sampling 功能**：Server 請求 Client 進行推論 [34]

### 8.5 延伸學習資源
- 官方文件與課程推薦 [45]

---

## 課程總結與實戰專案

### 綜合練習：打造你的 AI 助理工具箱
1. 設計 3-5 個實用的 Tools
2. 建立 MCP Server 並部署
3. 整合到你選擇的 Client App
4. 分享與討論

### 學習成果檢核
- [ ] 理解 MCP 解決什麼問題
- [ ] 能開發 MCP Server（Tools / Resources / Prompts）
- [ ] 能在 Client App 中使用 MCP Server
- [ ] 理解 Local vs Remote 的差異
- [ ] 了解安全性考量與最佳實踐

---

## 附錄

### A. 常用 MCP Servers 清單 [27]
### B. 開發環境設定指南
### C. 常見問題 FAQ
### D. 延伸閱讀資源 [45][46]

---

## 課程設計理念

| 原則 | 說明 |
|------|------|
| **第一性原理** | 從「為什麼」開始，建立正確心智模型 |
| **循序漸進** | 概念 → 原理 → 實作 → 進階 → 整合 |
| **重理解輕堆砌** | 範例簡單明瞭，聚焦在「用途」而非程式碼細節 |
| **實務導向** | 包含踩坑經驗、安全考量、生態系現況 |