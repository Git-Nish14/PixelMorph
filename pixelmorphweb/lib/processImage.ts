import axios from "axios";

export async function processImage(
  file: File,
  effect: string
): Promise<string> {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await axios.post(
      `http://18.117.133.97:8000/process-image/${effect}`,
      formData,
      { responseType: "blob" }
    );

    const blob = new Blob([response.data]);
    return URL.createObjectURL(blob);
  } catch (error) {
    console.error("Image processing failed:", error);
    throw new Error("Processing failed");
  }
}
