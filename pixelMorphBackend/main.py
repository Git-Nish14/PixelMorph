from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PixelMorph backend is running successfully!"}

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    image = Image.open(file.file)

    gray_image = image.convert("L")

    buf = io.BytesIO()
    gray_image.save(buf, format='JPEG')
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/jpeg")
