from fastapi import FastAPI
from website.routers.users import router as user_router
from website.routers.posts import router as post_router
from DAL.persistence.engine import Base , engine
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(user_router)
app.include_router(post_router)

if __name__ == "__main__":
    uvicorn.run(app)