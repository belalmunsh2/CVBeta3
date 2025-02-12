from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
=======
from fastapi.middleware.cors import CORSMiddleware # Make sure this import is present!
>>>>>>> 7fc46bbd48b45c2634fe0cf4561b0963a21c8a90
from app.routes import generator

app = FastAPI()

<<<<<<< HEAD
# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev"],  # IMPORTANT: Replace "https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev" with your actual frontend URL if it's different, or use ["*"] for development (less secure).
=======
# Configure CORS - VERY IMPORTANT - REPLACE YOUR_FRONTEND_URL_HERE!
origins = [
    "https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev",  # <--  REPLACE WITH YOUR EXACT FRONTEND URL!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
>>>>>>> 7fc46bbd48b45c2634fe0cf4561b0963a21c8a90
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