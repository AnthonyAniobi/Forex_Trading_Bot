from datetime import timedelta
# from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from settings import Settings
import fastapi
from fastapi import FastAPI, Request


__all__ = ["app"]


app = FastAPI(
    version="0.0.1",
    debug=Settings.DEBUG,
    title=Settings.PROJECT_NAME,
    docs_url="/",
    redoc_url="/redoc/",
    servers=[
        {"url": Settings.PROD_SERVER_URL, "description": "Production server"},
        {"url": "http://127.0.0.1:8000/", "description": "Local Development Server"},
    ],
    description="The Foot print API",
    default_response_class=fastapi.responses.ORJSONResponse,
)


@app.get("/entry")
async def entry(request: Request):
    
    return {"answer": 'this is the answer'}


if __name__ == "__main__":
    uvicorn.run(
        app,
        debug=Settings.DEBUG,
        host=Settings.HOST,
        port=Settings.PORT,
        reload=Settings.RELOAD,
        use_colors=Settings.COLOR_LOGS,
        log_level=Settings.LOGGER_LEVEL,
    )