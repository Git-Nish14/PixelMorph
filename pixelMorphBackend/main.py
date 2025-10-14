from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageEnhance, ImageFilter
import io, math, os, uuid, datetime

app = FastAPI()

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Create output folder ---
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "PixelMorph backend running successfully!"}


@app.post("/process-image/{effect}")
async def process_image(effect: str, file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert("RGB")

        # Step 1: Crop to square
        width, height = image.size
        min_side = min(width, height)
        left = (width - min_side) / 2
        top = (height - min_side) / 2
        right = (width + min_side) / 2
        bottom = (height + min_side) / 2
        image = image.crop((left, top, right, bottom))
        image = image.resize((512, 512))

        # Step 2: Apply effects
        if effect == "cooltone":
            image = ImageEnhance.Contrast(image).enhance(1.3)
            image = ImageEnhance.Sharpness(image).enhance(1.4)
            r, g, b = image.split()
            image = Image.merge("RGB", (
                r.point(lambda i: i * 0.9),
                g.point(lambda i: i * 1.0),
                b.point(lambda i: i * 1.1)
            ))

        elif effect == "grayscale":
            image = image.convert("L").convert("RGB")

        elif effect == "blur":
            image = image.filter(ImageFilter.GaussianBlur(4))

        elif effect == "sharp":
            image = ImageEnhance.Sharpness(image).enhance(2.0)

        elif effect == "contrast":
            image = ImageEnhance.Contrast(image).enhance(1.8)

        elif effect == "vintage":
            r, g, b = image.split()
            image = Image.merge("RGB", (
                r.point(lambda i: i * 1.1),
                g.point(lambda i: i * 0.9),
                b.point(lambda i: i * 0.8)
            ))
            image = image.filter(ImageFilter.SMOOTH_MORE)

        elif effect == "vignette":
            vignette = Image.new("L", image.size, 0)
            width, height = image.size
            center_x, center_y = width / 2, height / 2
            max_distance = math.sqrt(center_x**2 + center_y**2)
            for x in range(width):
                for y in range(height):
                    dx = x - center_x
                    dy = y - center_y
                    distance = math.sqrt(dx**2 + dy**2)
                    intensity = 1 - (distance / max_distance) ** 1.8
                    vignette.putpixel((x, y), int(255 * max(0, intensity)))
            vignette = vignette.filter(ImageFilter.GaussianBlur(60))
            image.putalpha(vignette)
            image = image.convert("RGB")

        else:
            raise HTTPException(status_code=400, detail="Invalid effect type")

        # Step 3: Save image locally
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{effect}_{uuid.uuid4().hex[:6]}_{timestamp}.jpg"
        path = os.path.join(OUTPUT_DIR, filename)
        image.save(path, "JPEG", quality=90)

        # Step 4: Return as stream
        buf = io.BytesIO()
        image.save(buf, format="JPEG")
        buf.seek(0)

        return StreamingResponse(buf, media_type="image/jpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
