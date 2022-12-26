from fastapi import FastAPI
from dotenv import dotenv_values
from azure.cosmos import CosmosClient
from azure.cosmos import PartitionKey, exceptions
from .routers import rescue_dog


config = dotenv_values(".env")
DATABASE_NAME = "dogadopt"
CONTAINER_NAME = "rescuedogs"

app = FastAPI()

app.include_router(rescue_dog.router)

@app.on_event("startup")
async def startup_db_client():
    app.cosmos_client = CosmosClient(config["URI"], credential = config["KEY"])
    await get_or_create_db(DATABASE_NAME)
    await get_or_create_container(CONTAINER_NAME)
     
async def get_or_create_db(db_name):
    try:
        app.database  = app.cosmos_client.get_database_client(db_name)
        return app.database.read()
    except exceptions.CosmosResourceNotFoundError:
        print("Creating database")
        return app.cosmos_client.create_database(db_name)
     
async def get_or_create_container(container_name):
    try:        
        app.container = app.database.get_container_client(container_name)
        return app.container.read()   
    except exceptions.CosmosResourceNotFoundError:
        print("Creating container with id as partition key")
        return app.database.create_container(id=container_name, partition_key=PartitionKey(path="/id"))
    except exceptions.CosmosHttpResponseError:
        raise

@app.get("/")
async def welcome():
    """Welcomes you to the rescue dog API

    Returns:
        string: Welcome message
    """
    return "Welcome to the rescue dog API!"
