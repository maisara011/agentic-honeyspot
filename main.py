from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
API_KEY = "honeyspot123"

@app.post("/api/message")
async def receive_message(data: dict, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "scam_detected": True,
        "engagement_turns": 1,
        "confidence_score": 0.91,
        "extracted_data": {
            "payment_identifiers": [],
            "suspicious_links": []
        }
    }
