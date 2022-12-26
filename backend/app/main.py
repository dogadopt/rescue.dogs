from fastapi import FastAPI
from .routers import rescue_dog

##api_router.include_router(recipe.router, prefix="/recipes", tags=["recipes"])

app = FastAPI()

app.include_router(rescue_dog.router)

@app.get("/")
async def welcome():
    """Welcomes you to the rescue dog API

    Returns:
        string: Welcome message
    """
    return "Welcome to the rescue dog API!"
