from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image, ImageEnhance, ImageFilter
import io
import math

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PixelMorph backend is running successfully!"}


@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    # --- Step 1: Open and normalize image mode ---
    image = Image.open(file.file)
    image = image.convert("RGB")  # Handles RGBA, P, etc.

    # --- Step 2: Crop to square (center crop) ---
    width, height = image.size
    min_side = min(width, height)
    left = (width - min_side) / 2
    top = (height - min_side) / 2
    right = (width + min_side) / 2
    bottom = (height + min_side) / 2
    square_image = image.crop((left, top, right, bottom))

    # --- Step 3: Resize to manageable size ---
    resized_image = square_image.resize((512, 512))

    # --- Step 4: Auto enhance contrast and sharpness ---
    enhanced = ImageEnhance.Contrast(resized_image).enhance(1.3)
    enhanced = ImageEnhance.Sharpness(enhanced).enhance(1.4)

    # --- Step 5: Apply cool tone ---
    r, g, b = enhanced.split()
    toned = Image.merge("RGB", (
        r.point(lambda i: i * 0.9),   # reduce red
        g.point(lambda i: i * 1.0),   # keep green
        b.point(lambda i: i * 1.1)    # boost blue
    ))

    # --- Step 6: Create vignette effect ---
    vignette = Image.new("L", toned.size, 0)
    width, height = toned.size
    center_x, center_y = width / 2, height / 2
    max_distance = math.sqrt(center_x**2 + center_y**2)

    for x in range(width):
        for y in range(height):
            dx = x - center_x
            dy = y - center_y
            distance = math.sqrt(dx**2 + dy**2)
            intensity = 1 - (distance / max_distance) ** 1.8
            vignette.putpixel((x, y), int(255 * max(0, intensity)))

    # --- Step 7: Blend vignette with image ---
    vignette_blur = vignette.filter(ImageFilter.GaussianBlur(60))
    toned.putalpha(vignette_blur)
    final_image = toned.convert("RGB")

    # --- Step 8: Save to buffer for streaming ---
    buf = io.BytesIO()
    final_image.save(buf, format="JPEG", quality=90)
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/jpeg")
