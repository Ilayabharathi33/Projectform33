from fastapi import FastAPI  # type: ignore[import]
import requests # type: ignore[import]
app = FastAPI()
@app.get("/Mj")
def fetch():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    result = response.json()
    return result


