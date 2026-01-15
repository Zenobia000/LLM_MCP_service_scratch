# 第七章：Remote MCP Server 進階應用

---

## 1. 為什麼需要 Remote MCP Server？

### 本機 vs 遠端對比

| 特性 | 本機 (stdio) | 遠端 (HTTP) |
|------|-------------|------------|
| **部署位置** | 用戶電腦 | 雲端伺服器 |
| **環境需求** | Python/Node.js | 僅需網路 |
| **資料存取** | 本機檔案 | 雲端資源 |
| **團隊共享** | 困難 | 容易 |
| **維護更新** | 每台更新 | 集中管理 |

### 使用場景
- 🌍 **跨裝置使用**：手機、平板、任何瀏覽器
- 🏢 **企業部署**：統一管理工具版本
- 🔐 **敏感資源**：資料不離開企業網路
- 👥 **團隊協作**：共享自訂工具集

---

## 2. 實作 Remote MCP Server

### 2.1 使用 FastMCP 建立 HTTP Server

```python
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
import uvicorn

# 初始化 FastMCP
mcp = FastMCP("Remote MCP Server")

# 定義工具
@mcp.tool()
def get_server_time() -> str:
    """取得伺服器時間"""
    from datetime import datetime
    return datetime.now().isoformat()

# 建立 FastAPI 應用
app = FastAPI()

# 掛載 MCP 端點
@app.post("/mcp/v1/messages")
async def handle_mcp(request: dict):
    return await mcp.handle_http_request(request)

# 啟動伺服器
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 2.2 部署選項

#### A. 雲端平台部署
```yaml
# 部署到 Vercel (vercel.json)
{
  "functions": {
    "api/mcp.py": {
      "runtime": "python3.9"
    }
  }
}
```

#### B. Docker 容器化
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastmcp fastapi uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]
```

---

## 3. 客戶端連接配置

### 3.1 Claude Desktop 配置
```json
{
  "mcpServers": {
    "remote-tools": {
      "url": "https://my-mcp-server.com/mcp/v1",
      "transport": "http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### 3.2 Python Client 連接
```python
from mcp import ClientSession
import httpx

async def connect_remote():
    async with httpx.AsyncClient() as client:
        session = ClientSession(
            transport="http",
            base_url="https://my-mcp-server.com/mcp/v1"
        )
        await session.initialize()

        # 使用遠端工具
        result = await session.call_tool(
            "get_server_time",
            arguments={}
        )
        print(result)
```

---

## 4. 踩坑經驗分享

### 4.1 常見問題與解決方案

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| **CORS 錯誤** | 跨域請求被阻擋 | 設定 CORS 標頭 |
| **連線逾時** | 網路延遲或防火牆 | 增加 timeout、檢查防火牆 |
| **認證失敗** | Token 過期或格式錯誤 | 實作 Token 重新整理機制 |
| **版本不相容** | Client/Server 版本不匹配 | 版本協商機制 |

### 4.2 認證機制混亂現況

目前 MCP 規範對認證沒有統一標準，實務上常見做法：

```python
# 方案 1：Header 認證
@app.middleware("http")
async def auth_middleware(request, call_next):
    token = request.headers.get("Authorization")
    if not validate_token(token):
        return JSONResponse({"error": "Unauthorized"}, 401)
    return await call_next(request)

# 方案 2：Cloudflare Access 保護
# 使用 Cloudflare Zero Trust 做身份驗證
```

---

## 5. 實作範例：Agent as MCP Server

### 概念：將 AI Agent 包裝成 MCP Server

```python
from mcp.server.fastmcp import FastMCP
from openai import OpenAI

mcp = FastMCP("AI Assistant Server")
client = OpenAI()

@mcp.tool()
async def ask_ai_assistant(question: str) -> str:
    """
    詢問 AI 助理問題
    這個工具讓其他 Agent 可以「諮詢」這個專門的 AI
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是資料分析專家"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

@mcp.tool()
async def analyze_data(data: dict, analysis_type: str) -> dict:
    """
    執行資料分析
    將複雜的分析邏輯封裝成簡單的工具介面
    """
    # Agent 內部可以有複雜的多步驟處理
    steps = [
        "資料清理",
        "統計分析",
        "視覺化建議"
    ]

    results = {}
    for step in steps:
        # 每個步驟可能呼叫不同的 AI 模型或工具
        results[step] = await process_step(data, step)

    return results
```

### 使用場景：Agents as Tools

1. **專家 Agent**：法律顧問、醫療諮詢、財務分析
2. **流程 Agent**：多步驟工作流程自動化
3. **整合 Agent**：連接多個外部 API 的中介層

---

## 6. 最佳實踐

### 6.1 性能優化
- **快取機制**：減少重複計算
- **連線池**：重用 HTTP 連線
- **非同步處理**：使用 async/await

### 6.2 安全性考量
- **Rate Limiting**：防止濫用
- **輸入驗證**：檢查參數合法性
- **審計日誌**：記錄所有操作

### 6.3 部署建議
```yaml
# 生產環境檢查清單
✅ HTTPS 加密
✅ 認證機制
✅ 錯誤處理
✅ 監控告警
✅ 自動擴展
✅ 備份策略
```

---

## 本章小結

1. **Remote MCP Server** 解決了本機部署的限制
2. 使用 **HTTP/HTTPS** 協議實現遠端通訊
3. **認證與安全** 是部署時的首要考量
4. **Agent as MCP Server** 開啟了新的整合模式
5. 實務部署需要考慮：性能、安全、監控

👉 **下一章：安全性、生態系與未來展望**