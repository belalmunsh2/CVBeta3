from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes import generator

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev"],  # IMPORTANT: Replace "https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev" with your actual frontend URL if it's different, or use ["*"] for development (less secure).
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generator.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)