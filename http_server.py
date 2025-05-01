import os, logging, uvicorn
from freshdesk_mcp.server import mcp

app = mcp.app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    port = int(os.getenv("PORT", 8000))
    logging.info(f"Starting HTTP MCP server on 0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
