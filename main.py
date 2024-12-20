from fastapi import FastAPI , Request
from website.routers.users.users_command import router as user_router_command
from website.routers.users.users_query import router as user_router_query
from website.routers.posts import router as post_router
from DAL.persistence.engine import Base , engine
import uvicorn
import time
from contextlib import asynccontextmanager

app = FastAPI()


asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(user_router_command)
app.include_router(user_router_query)
app.include_router(post_router)

if __name__ == "__main__":
    uvicorn.run(app)