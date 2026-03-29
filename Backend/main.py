from fastapi import FastAPI
from fetch_data import fetch
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def get():
    return fetch()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 8000)