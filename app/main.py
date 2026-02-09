from fastapi import FastAPI
from app.api.routes import router

# Create FastAPI app
app = FastAPI(
    title="Resilio Image AI Backend",
    description="Image-based emergency severity analysis using Gemini Vision",
    version="1.0.0"
)

# Register API routes
app.include_router(router)

# Health check endpoint
@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Resilio Image AI Backend"
    }
