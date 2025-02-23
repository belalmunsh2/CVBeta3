from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.generator import router as generator_router
from app.routes.promo import router as promo_router
from app.routes.payment import router as payment_router

app = FastAPI()

# Configure CORS - VERY IMPORTANT 
origins = [
    "https://cuddly-engine-pjwvppv46rqgf7q7j-5173.app.github.dev",  # <----  MAKE SURE THIS IS EXACTLY AS IN THE ERROR!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(generator_router, prefix="/api", tags=["generator"])
app.include_router(promo_router, prefix="/api", tags=["promo"])
app.include_router(payment_router, prefix="/api", tags=["payment"])

@app.get("/")
async def root():
    return {"message": "Hello Backend is working"}

# REMOVE THIS BLOCK - Not needed in Codespaces
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)