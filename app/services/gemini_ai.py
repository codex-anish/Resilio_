import io
import json
import requests
from PIL import Image
import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_image_from_url(image_url: str):
    try:
        r = requests.get(image_url, timeout=10)
        r.raise_for_status()
        image = Image.open(io.BytesIO(r.content)).convert("RGB")
    except Exception:
        return fallback("Failed to download image")

    prompt = """
You are an emergency response AI.
Return ONLY valid JSON.

Fields:
incident: fire | smoke | injury | collapse | normal | unknown
human_at_risk: true or false
severity: minor | serious | critical
reason: short sentence

Rules:
- Fire → critical
- Smoke + human → critical
- Injured or unconscious → critical
- Collapsed building → critical
"""

    try:
        response = model.generate_content(
            [prompt, image],
            generation_config={"temperature": 0}
        )
        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        return normalize(json.loads(text))

    except Exception:
        return fallback("Gemini API call failed")


def normalize(data):
    return {
        "incident": data.get("incident", "unknown"),
        "human_at_risk": bool(data.get("human_at_risk", False)),
        "severity": data.get("severity", "minor"),
        "reason": data.get("reason", "No clear reason")
    }


def fallback(reason):
    return {
        "incident": "unknown",
        "human_at_risk": False,
        "severity": "minor",
        "reason": reason
    }
