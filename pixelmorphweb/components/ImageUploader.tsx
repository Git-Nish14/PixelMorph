"use client";

import { useState, ChangeEvent, useRef } from "react";
import { EffectSelector } from "./EffectSelector";
import { processImage } from "../lib/processImage";

export default function ImageUploader() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [effect, setEffect] = useState<string>("cooltone");
  const [output, setOutput] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result as string);
      };
      reader.readAsDataURL(selectedFile);
      setOutput(null);
    }
  };

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      if (droppedFile.type.startsWith("image/")) {
        setFile(droppedFile);
        const reader = new FileReader();
        reader.onloadend = () => {
          setPreview(reader.result as string);
        };
        reader.readAsDataURL(droppedFile);
        setOutput(null);
      }
    }
  };

  const handleProcess = async () => {
    if (!file) return alert("Please upload an image first!");
    setLoading(true);
    try {
      const result = await processImage(file, effect);
      setOutput(result);
    } catch (error) {
      alert("Error processing image. Try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFile(null);
    setPreview(null);
    setOutput(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const handleDownload = () => {
    if (!output) return;
    const link = document.createElement("a");
    link.href = output;
    link.download = `pixelmorph-${effect}-${Date.now()}.png`;
    link.click();
  };

  return (
    <div className="space-y-6">
      {/* Upload Area */}
      {!preview ? (
        <div
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`relative border-2 border-dashed rounded-xl p-12 transition-all duration-300 cursor-pointer ${
            dragActive
              ? "border-[#d97757] bg-[#d97757]/10"
              : "border-[#4d4d4d] hover:border-[#d97757] bg-[#1a1a1a]/50"
          }`}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            className="hidden"
          />
          <div className="flex flex-col items-center justify-center text-center space-y-4">
            <div className="w-16 h-16 bg-gradient-to-br from-[#d97757] to-[#c17c5c] rounded-full flex items-center justify-center">
              <svg
                className="w-8 h-8 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                />
              </svg>
            </div>
            <div>
              <p className="text-lg font-medium text-white mb-1">
                Drop your image here, or{" "}
                <span className="text-[#d97757]">browse</span>
              </p>
              <p className="text-sm text-gray-400">
                Supports: JPG, PNG, GIF, WebP
              </p>
            </div>
          </div>
        </div>
      ) : (
        <div className="space-y-4">
          {/* Image Preview & Output Side by Side */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Original Image */}
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-medium text-gray-400">Original</h3>
                <button
                  onClick={handleReset}
                  className="text-xs text-gray-500 hover:text-[#d97757] transition-colors"
                >
                  Change Image
                </button>
              </div>
              <div className="relative rounded-xl overflow-hidden bg-[#1a1a1a] border border-[#3d3d3d]">
                <img src={preview} alt="Original" className="w-full h-auto" />
              </div>
            </div>

            {/* Processed Image */}
            <div className="space-y-2">
              <h3 className="text-sm font-medium text-gray-400">Processed</h3>
              <div className="relative rounded-xl overflow-hidden bg-[#1a1a1a] border border-[#3d3d3d] min-h-[200px] flex items-center justify-center">
                {output ? (
                  <img src={output} alt="Processed" className="w-full h-auto" />
                ) : (
                  <div className="text-center p-8">
                    <div className="w-12 h-12 border-2 border-[#4d4d4d] border-dashed rounded-lg mx-auto mb-3 flex items-center justify-center">
                      <svg
                        className="w-6 h-6 text-gray-600"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                        />
                      </svg>
                    </div>
                    <p className="text-xs text-gray-500">
                      Select an effect and process
                    </p>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Effect Selector */}
          <div className="bg-[#1a1a1a]/50 rounded-xl p-4 border border-[#3d3d3d]">
            <label className="block text-sm font-medium text-gray-400 mb-3">
              Choose Effect
            </label>
            <EffectSelector value={effect} onChange={setEffect} />
          </div>

          {/* Action Buttons */}
          <div className="flex gap-3">
            <button
              onClick={handleProcess}
              disabled={loading}
              className="flex-1 bg-gradient-to-r from-[#d97757] to-[#c17c5c] text-white py-3 px-6 rounded-xl font-medium hover:shadow-lg hover:shadow-[#d97757]/30 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:shadow-none"
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <svg
                    className="animate-spin h-5 w-5"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                    ></circle>
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    ></path>
                  </svg>
                  Processing...
                </span>
              ) : (
                "Apply Effect ✨"
              )}
            </button>
            {output && (
              <button
                onClick={handleDownload}
                className="bg-[#2d2d2d] text-white py-3 px-6 rounded-xl font-medium border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300"
              >
                Download 📥
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
