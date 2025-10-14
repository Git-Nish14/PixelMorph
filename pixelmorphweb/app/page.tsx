"use client"; // client component for useState, events

import { useState, ChangeEvent } from "react";
import axios from "axios";
import "./globals.css";

export default function Page() {
  const [file, setFile] = useState<File | null>(null);
  const [effect, setEffect] = useState<string>("cooltone");
  const [output, setOutput] = useState<string | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return alert("Select an image!");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/process-image/${effect}`,
        formData,
        { responseType: "blob" }
      );
      setOutput(URL.createObjectURL(response.data));
    } catch (err) {
      console.error(err);
      alert("Error processing image. Check backend.");
    }
  };

  return (
    <div className="container">
      <h1>PixelMorph</h1>

      <input type="file" accept="image/*" onChange={handleFileChange} />

      <select value={effect} onChange={(e) => setEffect(e.target.value)}>
        <option value="cooltone">Cooltone</option>
        <option value="grayscale">Grayscale</option>
        <option value="blur">Blur</option>
        <option value="sharp">Sharp</option>
        <option value="contrast">Contrast</option>
        <option value="vintage">Vintage</option>
        <option value="vignette">Vignette</option>
      </select>

      <button onClick={handleUpload}>Process</button>

      {output && (
        <div className="output">
          <h3>Processed Image:</h3>
          <img src={output} alt="Processed" width={512} />
        </div>
      )}
    </div>
  );
}
