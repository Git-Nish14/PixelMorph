"use client";

import { FC } from "react";

interface EffectSelectorProps {
  value: string;
  onChange: (value: string) => void;
}

const effects = [
  {
    id: "cooltone",
    name: "Cool Tone",
    icon: "❄️",
    description: "Add cool blue tones",
  },
  {
    id: "grayscale",
    name: "Grayscale",
    icon: "⚫",
    description: "Classic black & white",
  },
  {
    id: "blur",
    name: "Blur",
    icon: "🌫️",
    description: "Soft focus effect",
  },
  {
    id: "sharp",
    name: "Sharpen",
    icon: "✨",
    description: "Enhance details",
  },
  {
    id: "contrast",
    name: "Contrast",
    icon: "🎭",
    description: "Boost depth",
  },
  {
    id: "vintage",
    name: "Vintage",
    icon: "📷",
    description: "Retro film look",
  },
  {
    id: "vignette",
    name: "Vignette",
    icon: "🌓",
    description: "Darkened edges",
  },
];

export const EffectSelector: FC<EffectSelectorProps> = ({
  value,
  onChange,
}) => {
  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-3">
      {effects.map((effect) => (
        <button
          key={effect.id}
          onClick={() => onChange(effect.id)}
          className={`group relative flex flex-col items-center justify-center p-4 rounded-xl border-2 transition-all duration-300 ${
            value === effect.id
              ? "border-[#d97757] bg-[#d97757]/10 shadow-lg shadow-[#d97757]/20"
              : "border-[#3d3d3d] bg-[#2d2d2d]/50 hover:border-[#d97757]/50 hover:bg-[#2d2d2d]"
          }`}
        >
          {/* Selected indicator */}
          {value === effect.id && (
            <div className="absolute -top-1 -right-1 w-5 h-5 bg-[#d97757] rounded-full flex items-center justify-center">
              <svg
                className="w-3 h-3 text-white"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
          )}

          {/* Icon */}
          <div
            className={`text-3xl mb-2 transition-transform duration-300 ${
              value === effect.id ? "scale-110" : "group-hover:scale-110"
            }`}
          >
            {effect.icon}
          </div>

          {/* Name */}
          <div
            className={`text-sm font-medium text-center transition-colors ${
              value === effect.id
                ? "text-[#d97757]"
                : "text-white group-hover:text-[#d97757]"
            }`}
          >
            {effect.name}
          </div>

          {/* Description - shows on hover */}
          <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-3 py-1.5 bg-[#1a1a1a] border border-[#3d3d3d] rounded-lg opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-200 whitespace-nowrap z-10">
            <p className="text-xs text-gray-300">{effect.description}</p>
            <div className="absolute top-full left-1/2 transform -translate-x-1/2 -mt-1 border-4 border-transparent border-t-[#3d3d3d]"></div>
          </div>
        </button>
      ))}
    </div>
  );
};
