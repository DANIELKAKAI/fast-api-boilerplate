from fastapi import FastAPI


from src.database import engine, Base

from src.users.router import router as users_router
from src.items.router import router as items_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "Azure"}


app.include_router(users_router)
app.include_router(items_router)
