FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN uv pip install --system "mcp[cli]" fastmcp uvicorn starlette

COPY remote_server.py .

EXPOSE 8000

# 使用 uvicorn 啟動 mcp.sse_app
# 這是 FastMCP 提供的標準 ASGI 應用屬性
CMD ["uvicorn", "remote_server:mcp.sse_app", "--host", "0.0.0.0", "--port", "8000"]