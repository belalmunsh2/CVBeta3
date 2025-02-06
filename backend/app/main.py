from fastapi import FastAPI
import uvicorn
from app.routes import generator

app = FastAPI()

app.include_router(generator.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)