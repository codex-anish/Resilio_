from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gemini_ai import analyze_image_from_url


router = APIRouter()

# ✅ Request body schema
class ImageURLRequest(BaseModel):
    emergencyId: str
    imageUrl: str


@router.post("/ai/image-url")
def analyze_image(request: ImageURLRequest):
    # 1️⃣ Extract data
    emergency_id = request.emergencyId
    image_url = request.imageUrl

    # 2️⃣ Analyze image
    ai_result = analyze_image_from_url(image_url)

    # 3️⃣ Send result back to authority
    

    return {
        "status": "analysis completed",
        "analysis": ai_result
    }
