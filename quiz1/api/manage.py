import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.initializer import IncludeAPIRouter
from application.main.config import settings
from application.main.authentication import models
from application.main.authentication.database import engine


models.Base.metadata.create_all(engine)

def get_application():
    _app = FastAPI(title=settings.API_NAME,
                   description=settings.API_DESCRIPTION,
                   version=settings.API_VERSION)
    _app.include_router(IncludeAPIRouter())
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


app = get_application()


@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    print("On App Shutdown i will be called.")


if __name__ == "__main__":
    uvicorn.run(app = "manage:app", host=settings.HOST, port=settings.PORT, log_level=settings.LOG_LEVEL, use_colors=True,reload=True, timeout_keep_alive= 1000)
