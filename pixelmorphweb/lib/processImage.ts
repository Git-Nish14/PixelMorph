import axios from "axios";

/**
 * Sends an image file to the backend for processing and returns a URL for the processed image.
 * @param file - The image file to process
 * @param effect - The effect to apply (backend route parameter)
 * @returns URL string for the processed image
 */
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
      { responseType: "blob" } // receive as binary
    );

    // Convert the binary response to a URL to display in frontend
    const blob = new Blob([response.data]);
    return URL.createObjectURL(blob);
  } catch (error: any) {
    console.error(
      "Image processing failed:",
      error.response?.data || error.message
    );
    throw new Error("Processing failed. Please try again.");
  }
}
