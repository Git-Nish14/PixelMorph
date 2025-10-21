import axios from "axios";

export async function processImage(
  file: File,
  effect: string
): Promise<string> {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await axios.post(
      `${process.env.NEXT_PUBLIC_API_URL}/process-image/${effect}`, // use your deployed backend
      formData,
      { responseType: "blob" }
    );

    const blob = new Blob([response.data]);
    return URL.createObjectURL(blob);
  } catch (error: any) {
    // Log full error details to the console
    console.error("Image processing failed:");
    if (error.response) {
      console.error("Response data:", error.response.data);
      console.error("Status:", error.response.status);
      console.error("Headers:", error.response.headers);
    } else if (error.request) {
      console.error("No response received:", error.request);
    } else {
      console.error("Error message:", error.message);
    }
    throw new Error("Processing failed. Check console for details.");
  }
}
