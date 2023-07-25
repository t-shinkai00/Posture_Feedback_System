from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/api")
async def root(request: Request):
    print(request.headers)
    return {"message": "Hello World"}
