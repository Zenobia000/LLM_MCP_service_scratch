# Docker 部署指南 (Remote MCP Server)

本指南將教您如何將 MCP Server 打包成 Docker 容器，實現真正的「隨處執行」。

## 1. 建置映像檔 (Build Image)

請在 `07_remote_advanced/labs` 目錄下執行：

```bash
# 進入目錄
cd 07_remote_advanced/labs

# 建置映像檔，命名為 mcp-remote-server
docker build -t mcp-remote-server .
```

## 2. 啟動容器 (Run Container)

```bash
# 啟動容器，將容器的 8000 端口映射到本機的 8090 端口
# 如果 8090 已被佔用，可以更換為其他端口 (例如 8091:8000)
docker run -d -p 8090:8000 --name my-mcp-server mcp-remote-server
```

## 3. 驗證服務

您可以使用 `curl` 或瀏覽器測試 Server 是否活著：

```bash
curl http://localhost:8090/sse
```
如果連線成功（通常會卡住等待事件），代表 Server 已正常運作。

## 4. 如何讓 Claude 連接 Docker 中的 Server？

由於 Docker 容器內的 Server 是透過 HTTP 暴露的，我們需要在 `claude_desktop_config.json` 中使用 `sse` 類型的設定，而不是 `command`。

### 修改 Claude 設定檔
```json
{
  "mcpServers": {
    "docker-server": {
      "url": "http://localhost:8090/sse"
    }
  }
}
```

> **注意**：目前 Claude Desktop 對 SSE 的支援仍在演進中，部分版本可能需要透過 `mcp-proxy` 才能連接 HTTP Server。
