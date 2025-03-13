import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.generator import router as generator_router
from app.routes.promo import router as promo_router
from app.routes.payment import router as payment_router
from app.routes.pdf_routes import router as pdf_router

# Configure logging at DEBUG level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("DEBUG log message from main.py - DEFINITIVE LOGGING TEST - IS DEBUG LOGGING WORKING?")

app = FastAPI()

# Configure CORS - VERY IMPORTANT 
origins = [
    "https://cuddly-engine-pjwvppv46rqgf7q7j-5173.app.github.dev",  # Frontend origin
    "https://cuddly-engine-pjwvppv46rqgf7q7j-8000.app.github.dev",  # Backend origin
    "http://localhost:5173",  # Local frontend
    "http://localhost:8000",  # Local backend
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
app.include_router(pdf_router, tags=["pdf"])

@app.get("/")
async def root():
    return {"message": "Welcome to the CV Generator API"}

# REMOVE THIS BLOCK - Not needed in Codespaces
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)