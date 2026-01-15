# MCP Inspector 使用指南

## 什麼是 MCP Inspector?
它是官方提供的網頁版除錯工具，讓你在不用寫 Client 程式碼的情況下，直接測試 Server 的功能。

## 如何啟動
在專案根目錄執行：
```bash
uv run mcp dev <你的檔案路徑>
```

## 介面功能介紹
1. **Tools Tab**: 列出所有可用工具，並提供表單讓你填寫參數並執行。
2. **Resources Tab**: 瀏覽並讀取 Server 提供的資源內容。
3. **Prompts Tab**: 測試 Prompt 模板生成的結果。
4. **Logs**: 查看 Server 的標準輸出 (print) 與錯誤訊息。

## 常見問題
- **Q: 為什麼顯示連線失敗？**
  - A: 檢查你的 Python 腳本是否有語法錯誤，或者是否忘記呼叫 `mcp.run()`。
