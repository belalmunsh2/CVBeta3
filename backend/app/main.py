from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Make sure this import is present!
from app.routes import generator

app = FastAPI()

# Configure CORS - VERY IMPORTANT - REPLACE YOUR_FRONTEND_URL_HERE!
origins = [
    "https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev",  # <--  REPLACE WITH YOUR EXACT FRONTEND URL!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generator.router)

@app.get("/")
async def root():
    return {"message": "Hello Backend is working"}

# REMOVE THIS BLOCK - Not needed in Codespaces
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)