# main.py
import uvicorn

async def app(scope, receive, send):
    ...

if __name__ == "__main__":
    uvicorn.run("main:app",  port=80, log_level="info")
