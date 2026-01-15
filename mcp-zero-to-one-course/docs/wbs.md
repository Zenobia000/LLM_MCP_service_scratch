# 📅 MCP 課程開發工作分解結構 (WBS)

## 1.0 專案初始化 (Project Initialization) [已完成]
- [x] 1.1 建立目錄結構
- [x] 1.2 初始化 uv 環境與依賴
- [x] 1.3 撰寫 README.md 與 uv 使用指南

## 2.0 第一階段：核心觀念教材 (Phase 1: Concepts)
- [ ] 2.1 **Ch01 為什麼需要 MCP**
    - [ ] 撰寫 slides.md (第一性原理、Agent Loop)
    - [ ] 繪製概念圖 (Mermaid/ASCII)
- [ ] 2.2 **Ch02 MCP 是什麼**
    - [ ] 撰寫 slides.md (標準化協定、USB 類比)
    - [ ] 撰寫 Before/After 對比文件
- [ ] 2.3 **Ch03 三大核心功能**
    - [ ] 撰寫 slides.md (Tools/Resources/Prompts)
    - [ ] 建立 JSON Schema 範例檔

## 3.0 第二階段：核心實作開發 (Phase 2: Core Implementation)
- [ ] 3.1 **Ch05 Lab 1: Hello MCP**
    - [ ] 實作 `basic_tool.py` (加法器、打招呼)
    - [ ] 撰寫操作指引 (如何使用 Inspector)
- [ ] 3.2 **Ch05 Lab 2: Resources & Prompts**
    - [ ] 實作 `resources_prompts.py`
    - [ ] 測試讀取資源與調用 Prompt

## 4.0 第三階段：整合與協定 (Phase 3: Integration)
- [ ] 4.1 **Ch04 通訊協定理論**
    - [ ] 撰寫 slides.md (stdio vs HTTP)
    - [ ] 繪製通訊時序圖 (Mermaid)
- [ ] 4.2 **Ch06 Client 整合實戰**
    - [ ] 提供 `claude_desktop_config.json` 範本
    - [ ] 實作 `client.py` (Python SDK Client)

## 5.0 第四階段：進階應用 (Phase 4: Advanced)
- [ ] 5.1 **Ch07 Remote Server**
    - [ ] 實作 `remote_server.py` (SSE 支援)
- [ ] 5.2 **Ch08 安全性與總結**
    - [ ] 撰寫安全性檢查清單
    - [ ] 整理推薦 Server 列表

## 6.0 第五階段：期末專案 (Phase 5: Final Project)
- [ ] 6.1 撰寫專案需求書 (Project Brief)
- [ ] 6.2 建立評分標準
