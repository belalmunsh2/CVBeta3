from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generator
from app.routes import promo

app = FastAPI()

# Configure CORS - VERY IMPORTANT 
origins = [
    "https://symmetrical-orbit-9xxvqjqqvvj3xv9g-5173.app.github.dev",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generator.router, prefix="/api")
app.include_router(promo.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello Backend is working"}

# REMOVE THIS BLOCK - Not needed in Codespaces
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)