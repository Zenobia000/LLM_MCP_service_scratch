# 第九章：綜合實戰專案 - 打造你的 AI 工具箱

## 專案概述

在這個綜合專案中，你將建立一個完整的 MCP Server，包含多個實用工具，並整合到 Claude Desktop 或自己的 AI 應用中。

### 專案目標
1. 整合前面章節所學的所有概念
2. 建立一個可用於日常工作的 AI 工具箱
3. 學習如何設計、實作、測試和部署 MCP Server

---

## 專案架構

```
my-ai-toolbox/
├── src/
│   ├── __init__.py
│   ├── server.py          # 主 Server 檔案
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── file_tools.py  # 檔案操作工具
│   │   ├── web_tools.py   # 網路相關工具
│   │   └── data_tools.py  # 資料處理工具
│   ├── resources/
│   │   └── templates.py   # Resources 定義
│   └── prompts/
│       └── templates.py   # Prompt 模板
├── tests/
│   └── test_tools.py
├── pyproject.toml
└── README.md
```

---

## 實作步驟

### Step 1：專案初始化

```bash
# 建立專案目錄
mkdir my-ai-toolbox
cd my-ai-toolbox

# 初始化 Python 專案
uv init
uv add fastmcp pydantic httpx
```

### Step 2：主 Server 實作

```python
# src/server.py
from mcp.server.fastmcp import FastMCP
from .tools import file_tools, web_tools, data_tools
from .resources import templates as resource_templates
from .prompts import templates as prompt_templates

# 初始化 MCP Server
mcp = FastMCP("My AI Toolbox")

# 註冊所有工具
file_tools.register(mcp)
web_tools.register(mcp)
data_tools.register(mcp)

# 註冊 Resources
resource_templates.register(mcp)

# 註冊 Prompts
prompt_templates.register(mcp)

if __name__ == "__main__":
    mcp.run()
```

---

## 工具實作範例

### 1. 檔案操作工具集

```python
# src/tools/file_tools.py
import os
import json
from pathlib import Path
from typing import List, Dict, Any

def register(mcp):
    @mcp.tool()
    def search_files(
        directory: str,
        pattern: str,
        recursive: bool = True
    ) -> List[str]:
        """
        搜尋符合模式的檔案

        Args:
            directory: 搜尋目錄
            pattern: 檔案名稱模式 (支援 * 和 ?)
            recursive: 是否遞迴搜尋子目錄
        """
        path = Path(directory)
        if not path.exists():
            raise ValueError(f"目錄不存在: {directory}")

        method = path.rglob if recursive else path.glob
        files = [str(f) for f in method(pattern) if f.is_file()]
        return files

    @mcp.tool()
    def analyze_project_structure(root_dir: str) -> Dict[str, Any]:
        """
        分析專案結構，生成檔案樹和統計資訊
        """
        stats = {
            "total_files": 0,
            "total_dirs": 0,
            "file_types": {},
            "largest_files": [],
            "structure": {}
        }

        for root, dirs, files in os.walk(root_dir):
            stats["total_dirs"] += len(dirs)
            stats["total_files"] += len(files)

            for file in files:
                ext = Path(file).suffix or "no_extension"
                stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1

                file_path = Path(root) / file
                if file_path.exists():
                    size = file_path.stat().st_size
                    stats["largest_files"].append({
                        "path": str(file_path),
                        "size": size
                    })

        # 只保留前 10 個最大的檔案
        stats["largest_files"].sort(key=lambda x: x["size"], reverse=True)
        stats["largest_files"] = stats["largest_files"][:10]

        return stats
```

### 2. 網路工具集

```python
# src/tools/web_tools.py
import httpx
from bs4 import BeautifulSoup
import json

def register(mcp):
    @mcp.tool()
    async def fetch_and_summarize(
        url: str,
        selector: str = None
    ) -> str:
        """
        抓取網頁內容並提取特定部分

        Args:
            url: 網頁 URL
            selector: CSS 選擇器（可選）
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            if selector:
                elements = soup.select(selector)
                content = '\n'.join([elem.get_text(strip=True) for elem in elements])
            else:
                # 移除 script 和 style 標籤
                for script in soup(["script", "style"]):
                    script.decompose()
                content = soup.get_text(strip=True)

            # 限制長度
            if len(content) > 5000:
                content = content[:5000] + "...[內容已截斷]"

            return content

    @mcp.tool()
    async def api_request(
        url: str,
        method: str = "GET",
        headers: dict = None,
        body: dict = None
    ) -> dict:
        """
        發送 API 請求並返回 JSON 結果
        """
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                json=body if method in ["POST", "PUT", "PATCH"] else None
            )
            response.raise_for_status()
            return response.json()
```

### 3. 資料處理工具集

```python
# src/tools/data_tools.py
import json
import csv
from typing import List, Dict, Any
import statistics

def register(mcp):
    @mcp.tool()
    def json_to_csv(json_data: List[Dict], output_path: str) -> str:
        """
        將 JSON 資料轉換為 CSV 檔案
        """
        if not json_data:
            return "沒有資料可轉換"

        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = json_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(json_data)

        return f"已成功轉換 {len(json_data)} 筆資料至 {output_path}"

    @mcp.tool()
    def analyze_data(data: List[float]) -> Dict[str, float]:
        """
        對數值資料進行統計分析
        """
        if not data:
            return {"error": "沒有資料可分析"}

        return {
            "count": len(data),
            "mean": statistics.mean(data),
            "median": statistics.median(data),
            "mode": statistics.mode(data) if len(set(data)) < len(data) else None,
            "std_dev": statistics.stdev(data) if len(data) > 1 else 0,
            "min": min(data),
            "max": max(data),
            "range": max(data) - min(data)
        }
```

---

## Resources 實作

```python
# src/resources/templates.py
from mcp.server.fastmcp import Resource

def register(mcp):
    @mcp.resource("template://project/readme")
    def get_readme_template() -> str:
        """提供專案 README 模板"""
        return """
# 專案名稱

## 簡介
簡短描述專案的用途和目標

## 功能特點
- 功能 1
- 功能 2
- 功能 3

## 安裝說明
```bash
# 安裝步驟
```

## 使用方式
```python
# 程式碼範例
```

## 貢獻指南
歡迎提交 PR！

## 授權
MIT License
        """

    @mcp.resource("template://code/python-class")
    def get_class_template() -> str:
        """提供 Python 類別模板"""
        return '''
from typing import Optional, List, Dict, Any

class MyClass:
    """
    類別說明文檔
    """

    def __init__(self, name: str, value: Optional[int] = None):
        """
        初始化方法

        Args:
            name: 名稱
            value: 數值（可選）
        """
        self.name = name
        self.value = value or 0

    def process(self) -> Dict[str, Any]:
        """
        處理方法

        Returns:
            處理結果
        """
        return {
            "name": self.name,
            "value": self.value,
            "processed": True
        }
        '''
```

---

## Prompts 實作

```python
# src/prompts/templates.py

def register(mcp):
    @mcp.prompt("code-review")
    def code_review_prompt(code: str = "") -> str:
        """程式碼審查 Prompt 模板"""
        return f"""
請對以下程式碼進行全面的審查：

{code if code else "[請貼上要審查的程式碼]"}

審查要點：
1. **程式碼品質**
   - 可讀性和維護性
   - 命名規範
   - 註解品質

2. **效能考量**
   - 時間複雜度
   - 空間複雜度
   - 潛在的效能瓶頸

3. **安全性**
   - 輸入驗證
   - 錯誤處理
   - 潛在的安全漏洞

4. **最佳實踐**
   - 設計模式的使用
   - SOLID 原則
   - DRY 原則

請提供具體的改進建議和程式碼範例。
        """

    @mcp.prompt("data-analysis")
    def data_analysis_prompt(data_description: str = "") -> str:
        """資料分析 Prompt 模板"""
        return f"""
請協助分析以下資料：

{data_description if data_description else "[描述你的資料集]"}

分析需求：
1. 資料概覽和基本統計
2. 識別關鍵模式和趨勢
3. 異常值檢測
4. 相關性分析
5. 視覺化建議

請提供：
- 關鍵發現
- 可行的洞察
- 後續分析建議
        """
```

---

## 測試實作

```python
# tests/test_tools.py
import pytest
from src.server import mcp
import tempfile
import json

def test_search_files():
    """測試檔案搜尋功能"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # 建立測試檔案
        test_files = ["test1.txt", "test2.py", "data.json"]
        for filename in test_files:
            Path(tmpdir) / filename).touch()

        # 執行搜尋
        results = mcp.tools.search_files(tmpdir, "*.py")
        assert len(results) == 1
        assert "test2.py" in results[0]

def test_analyze_data():
    """測試資料分析功能"""
    test_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
    result = mcp.tools.analyze_data(test_data)

    assert result["count"] == 11
    assert result["mean"] == pytest.approx(5.45, 0.01)
    assert result["median"] == 5
    assert result["min"] == 1
    assert result["max"] == 10
```

---

## 部署與整合

### 1. 本機部署（Claude Desktop）

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "my-toolbox": {
      "command": "uv",
      "args": ["run", "/path/to/my-ai-toolbox/src/server.py"]
    }
  }
}
```

### 2. Docker 部署

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -e .

CMD ["python", "-m", "src.server"]
```

### 3. 雲端部署（使用 FastAPI）

```python
# src/api_server.py
from fastapi import FastAPI
from .server import mcp

app = FastAPI()

@app.post("/mcp/v1/messages")
async def handle_mcp_message(request: dict):
    return await mcp.handle_http_request(request)

# 部署到 Vercel/Railway/Heroku
```

---

## 學習成果檢核

完成這個專案後，你應該能夠：

- [ ] 設計並實作完整的 MCP Server
- [ ] 建立有用的 Tools、Resources 和 Prompts
- [ ] 撰寫測試確保功能正確
- [ ] 部署 Server 到不同環境
- [ ] 整合到實際的 AI 應用中使用

---

## 進階挑戰

1. **加入認證機制**：保護你的 MCP Server
2. **實作快取**：提升工具執行效能
3. **錯誤處理**：優雅地處理各種異常
4. **監控與日誌**：追蹤工具使用情況
5. **版本控制**：支援多版本 API

---

## 總結

恭喜你完成了 MCP 課程的所有內容！你現在已經掌握了：

1. MCP 的核心概念和設計理念
2. 開發各種類型的 MCP 工具
3. 部署和整合 MCP Server
4. 安全性和最佳實踐

繼續探索 MCP 生態系，建立更多有用的工具，並與社群分享你的創作！