from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get():
    return {"message": "Hello World"}

@app.post("/items/{quantity}")
async def create(quantity: int):
    return {"message": f"{quantity} items created"}