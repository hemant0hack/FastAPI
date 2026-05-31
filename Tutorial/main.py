from fastapi import FastAPI    #import FastAPI

app = FastAPI()     # FastAPI instance

@app.get("/")       # path operation decorator
async def root():
    return {"message": "Hello World"}