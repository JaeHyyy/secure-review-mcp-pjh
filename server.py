from fastmcp import FastMCP

mcp = FastMCP("Secure-Review-PJH")

@mcp.tool
def ping() -> str:
    """헬스체크"""
    return "ok"

if __name__ == "__main__":
    mcp.run()