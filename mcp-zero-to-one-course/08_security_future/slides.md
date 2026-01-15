# 第八章：安全性、生態系與未來展望

---

## 1. MCP 的安全性挑戰

當你賦予 AI 模型「執行動作」的權利時，安全就成為首要任務。

### 🚨 常見風險
1.  **提示詞注入 (Prompt Injection)**：攻擊者透過 Tool 的回傳結果，誘導模型執行惡意指令。
2.  **工具中毒 (Tool Poisoning)**：惡意 Server 在描述中寫入誤導性資訊。
3.  **過度授權 (Over-privileged)**：Server 權限過大（例如可以刪除硬碟所有檔案）。

---

## 2. 最佳實踐：如何開發安全的 Server

*   **最小權限原則 (Principle of Least Privilege)**：
    *   不要給 `rm -rf /`，只給 `delete_file(filename)` 並限制在特定資料夾。
*   **輸入驗證 (Input Validation)**：
    *   永遠不要相信模型傳入的參數。使用 Pydantic 進行嚴格的型別與範圍檢查。
*   **人類介入 (Human-in-the-loop)**：
    *   對於敏感操作（如匯款、發信），Client 應要求用戶點擊確認。

---

## 3. MCP 生態系現況

目前社群已貢獻了大量的開源 Server，你可以直接使用：

*   **官方目錄 (MCP Gallery)**：包含 Google Drive, Slack, GitHub, SQLite 等。
*   **部署平台**：Smithery.ai 等平台讓部署 MCP 變得更簡單。

---

## 4. 未來發展藍圖 (Roadmap)

1.  **MCP Registry**：像 NPM 一樣的統一註冊表，方便搜尋與安裝。
2.  **Sampling API**：讓 Server 可以反過來要求 Client 進行推論（主動詢問模型）。
3.  **更強的認證機制**：標準化 OAuth2 等安全認證流程。

---

## 5. 結語：AI 應用程式的新範式

MCP 不僅是一個技術協定，它代表了 **「AI 應用解耦」** 的未來。
*   模型專注於思考 (Intelligence)。
*   Server 專注於資料與執行 (Capabilities)。

👉 **接下來：挑戰你的期末實戰專案！**