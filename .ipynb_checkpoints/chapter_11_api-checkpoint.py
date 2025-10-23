from fastapi import FastAPI


app = FastAPI()


@app.get("/say_hi/")
def say_hi():
    return {"Hi": "There"}


@app.get("/say_hello/{name}")
def say_hello(name: str) -> str:
    return {"Hello": name}
