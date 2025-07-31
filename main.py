from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from huggingface_hub import InferenceClient
import os

app = FastAPI()

HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN)

@app.get("/generate")
async def generate(prompt: str = Query(...)):
    try:
        image = client.text_to_image(prompt, guidance_scale=7)
        image.save("output.png")
        return JSONResponse({"message": "Image generated", "image_url": "https://yourdomain.com/output.png"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
