import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    print(f"Starting {settings.PROJECT_NAME} v{settings.VERSION}")
    print(f"Server Running on http://{settings.HOST}:{settings.PORT}/")
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=False)
