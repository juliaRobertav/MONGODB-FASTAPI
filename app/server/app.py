from fastapi import FastAPI

from app.server.routes.student import router as StudentRouter


# import sys
# default_path = "C:\\Users\\GUJ4CA\\Documents\\fastapi-mongo"
# sys.path.append(default_path)

app = FastAPI()


app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
