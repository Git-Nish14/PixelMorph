import axios from "axios";

export async function processImage(
  file: File,
  effect: string
): Promise<string> {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await axios.post(
      `${process.env.NEXT_PUBLIC_API_URL}/process-image/${effect}`,
      formData,
      { responseType: "blob" }
    );

    const blob = new Blob([response.data]);
    return URL.createObjectURL(blob);
  } catch (error: unknown) {
    console.error("Image processing failed:");

    if (axios.isAxiosError(error)) {
      // Axios error
      console.error("Response data:", error.response?.data);
      console.error("Status:", error.response?.status);
      console.error("Headers:", error.response?.headers);
    } else if (error instanceof Error) {
      // Native JS error
      console.error("Error message:", error.message);
    } else {
      console.error("Unknown error:", error);
    }

    throw new Error("Processing failed. Check console for details.");
  }
}
