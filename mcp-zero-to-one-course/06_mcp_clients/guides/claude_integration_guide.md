# Claude Desktop MCP 整合與驗證指南

本指南將引導您如何在 Claude Desktop App 中設定並驗證我們實作的 MCP Server (Lab 1 & Lab 2)。

## 1. 設定設定檔 (Configuration)

請依照您的作業系統，找到並編輯 `claude_desktop_config.json`。

### 檔案位置
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
  (即 `C:\Users\<User>\AppData\Roaming\Claude\claude_desktop_config.json`)

### 填入內容
請將以下 JSON 貼入，並務必將 `<PATH_TO_PROJECT>` 替換為您的專案**絕對路徑**。

```json
{
  "mcpServers": {
    "course-lab1": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/username/projects/mcp-zero-to-one-course", 
        "run",
        "05_first_mcp_server/labs/basic_tool.py"
      ]
    },
    "course-lab2": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/username/projects/mcp-zero-to-one-course",
        "run",
        "05_first_mcp_server/labs/resources_prompts.py"
      ]
    }
  }
}
```
> **注意**：Windows 使用者請確保路徑格式正確，例如 `"C:/Users/Name/Documents/..."` (使用正斜線 `/` 或雙反斜線 `\\`)。

---

## 2. 驗證連線 (Verification)

設定完成後，請執行以下步驟：

1.  **完全關閉** Claude Desktop App (確認工作列/選單列圖示已消失)。
2.  **重新開啟** Claude Desktop App。
3.  觀察介面右上角或是輸入框下方，是否出現一個 **🔌 插頭圖示** (或類似的工具圖示)。
    - 若看到插頭圖示，點擊它。
    - 您應該能看到 `course-lab1` 和 `course-lab2` 顯示為 **Connected (綠燈)**。
    - 展開後能看到 `add`, `say_hello`, `save_note` 等工具清單。

**❌ 如果看到紅燈或沒有圖示：**
- 檢查 `claude_desktop_config.log` (通常在設定檔同目錄下的 logs 資料夾)。
- 常見錯誤：路徑打錯、`uv` 沒有安裝在 PATH 中。

---

## 3. 實戰測試 (Testing)

現在，您可以直接對著 Claude 說話來測試這些工具：

### 測試 Tools (Lab 1)
> **User**: "請幫我計算 1234 加 5678 等於多少？"
> **Claude**: (思考中... 呼叫 `add` 工具) -> "答案是 6912。"

> **User**: "請用 MCP 向我打個招呼。"
> **Claude**: (呼叫 `say_hello`) -> "你好！歡迎來到 MCP 的世界。"

### 測試 Resources (Lab 2)
> **User**: "請讀取 project readme 的內容告訴我這個專案在做什麼。"
> **Claude**: (讀取 `note://project/readme` 資源) -> "這是一個關於 MCP 開發的秘密專案..."

### 測試 Prompts (Lab 2)
1. 點擊輸入框附近的 **Prompts (提示詞)** 按鈕。
2. 選擇 `review_project`。
3. 填入參數 (例如專案名稱 "Apollo")。
4. Claude 會自動載入預設好的提示詞模板，開始進行專案審查。

---

## 🎉 恭喜！
如果您成功完成了上述測試，代表您已經掌握了將自製 MCP Server 整合進頂級 AI 模型的技能！
