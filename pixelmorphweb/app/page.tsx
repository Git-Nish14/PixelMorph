import Link from "next/link";
import ImageUploader from "../components/ImageUploader";

export default function Page() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-[#1a1a1a] via-[#2d2d2d] to-[#1a1a1a] relative overflow-hidden">
      {/* Animated background orbs */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#d97757] rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-pulse"></div>
        <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-[#c17c5c] rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-pulse delay-1000"></div>
        <div className="absolute bottom-1/4 left-1/3 w-96 h-96 bg-[#a8674f] rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-pulse delay-2000"></div>
      </div>

      {/* Main content */}
      <div className="relative z-10 container mx-auto px-4 py-12 flex flex-col min-h-screen">
        {/* Hero section */}
        <div className="flex-1 flex flex-col items-center justify-center max-w-6xl mx-auto w-full">
          <div className="text-center mb-12 space-y-4">
            <div className="inline-block">
              <div className="flex items-center justify-center gap-3 mb-4">
                <div className="w-12 h-12 bg-gradient-to-br from-[#d97757] to-[#c17c5c] rounded-xl flex items-center justify-center transform rotate-6 hover:rotate-12 transition-transform duration-300">
                  <span className="text-2xl">🎨</span>
                </div>
                <h1 className="text-6xl md:text-7xl font-bold bg-gradient-to-r from-[#d97757] via-[#e8a088] to-[#d97757] bg-clip-text text-transparent">
                  PixelMorph
                </h1>
              </div>
            </div>

            <p className="text-xl md:text-2xl text-gray-400 max-w-2xl mx-auto leading-relaxed">
              Transform your images with cutting-edge AI processing.
              <span className="block mt-2 text-[#d97757]">
                Fast. Powerful. Beautiful.
              </span>
            </p>
          </div>

          {/* Image Uploader Card */}
          <div className="w-full max-w-6xl">
            <div className="bg-[#2d2d2d] rounded-2xl shadow-2xl border border-[#3d3d3d] backdrop-blur-sm p-8 hover:border-[#d97757] transition-all duration-300 hover:shadow-[#d97757]/20">
              <ImageUploader />
            </div>
          </div>

          {/* How It Works Section */}
          <div className="w-full max-w-6xl mt-20">
            <div className="text-center mb-10">
              <h2 className="text-3xl md:text-4xl font-bold text-white mb-3">
                How It Works
              </h2>
              <p className="text-gray-400">
                Transform your images in three simple steps
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="relative">
                <div className="bg-[#2d2d2d]/50 backdrop-blur-sm rounded-xl p-8 border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300 text-center group">
                  {/* Step number */}
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gradient-to-br from-[#d97757] to-[#c17c5c] rounded-full flex items-center justify-center font-bold text-white text-sm">
                    1
                  </div>

                  <div className="text-5xl mb-4 group-hover:scale-110 transition-transform">
                    📤
                  </div>
                  <h3 className="text-xl font-semibold text-white mb-3">
                    Upload Image
                  </h3>
                  <p className="text-gray-400 text-sm">
                    Drag and drop or click to upload your image. Supports all
                    major formats.
                  </p>
                </div>
              </div>

              <div className="relative">
                <div className="bg-[#2d2d2d]/50 backdrop-blur-sm rounded-xl p-8 border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300 text-center group">
                  {/* Step number */}
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gradient-to-br from-[#d97757] to-[#c17c5c] rounded-full flex items-center justify-center font-bold text-white text-sm">
                    2
                  </div>

                  <div className="text-5xl mb-4 group-hover:scale-110 transition-transform">
                    🎨
                  </div>
                  <h3 className="text-xl font-semibold text-white mb-3">
                    Choose Effect
                  </h3>
                  <p className="text-gray-400 text-sm">
                    Select from our curated collection of professional-grade
                    effects.
                  </p>
                </div>
              </div>

              <div className="relative">
                <div className="bg-[#2d2d2d]/50 backdrop-blur-sm rounded-xl p-8 border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300 text-center group">
                  {/* Step number */}
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2 w-8 h-8 bg-gradient-to-br from-[#d97757] to-[#c17c5c] rounded-full flex items-center justify-center font-bold text-white text-sm">
                    3
                  </div>

                  <div className="text-5xl mb-4 group-hover:scale-110 transition-transform">
                    ⚡
                  </div>
                  <h3 className="text-xl font-semibold text-white mb-3">
                    Download Result
                  </h3>
                  <p className="text-gray-400 text-sm">
                    Get your transformed image instantly. High quality, every
                    time.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Features */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-20 w-full max-w-6xl">
            <div className="bg-[#2d2d2d]/50 backdrop-blur-sm rounded-xl p-6 border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300 group">
              <div className="text-3xl mb-3 group-hover:scale-110 transition-transform">
                ⚡
              </div>
              <h3 className="text-lg font-semibold text-white mb-2">
                Lightning Fast
              </h3>
              <p className="text-gray-400 text-sm">
                Process images in seconds with our optimized pipeline
              </p>
            </div>

            <div className="bg-[#2d2d2d]/50 backdrop-blur-sm rounded-xl p-6 border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300 group">
              <div className="text-3xl mb-3 group-hover:scale-110 transition-transform">
                🎯
              </div>
              <h3 className="text-lg font-semibold text-white mb-2">
                Pixel Perfect
              </h3>
              <p className="text-gray-400 text-sm">
                Advanced algorithms for stunning results every time
              </p>
            </div>

            <div className="bg-[#2d2d2d]/50 backdrop-blur-sm rounded-xl p-6 border border-[#3d3d3d] hover:border-[#d97757] transition-all duration-300 group">
              <div className="text-3xl mb-3 group-hover:scale-110 transition-transform">
                🔒
              </div>
              <h3 className="text-lg font-semibold text-white mb-2">
                Private & Secure
              </h3>
              <p className="text-gray-400 text-sm">
                Your images are processed securely and never stored
              </p>
            </div>
          </div>
        </div>

        {/* Footer */}
        <footer className="mt-20 pt-8 border-t border-[#3d3d3d]">
          <div className="max-w-6xl mx-auto px-4">
            <div className="flex flex-col md:flex-row justify-between items-center gap-6">
              <div className="text-center md:text-left">
                <div className="flex items-center gap-2 justify-center md:justify-start mb-2">
                  <span className="text-xl">🎨</span>
                  <span className="text-lg font-semibold text-[#d97757]">
                    PixelMorph
                  </span>
                </div>
                <p className="text-gray-500 text-sm">
                  Transforming pixels into possibilities
                </p>
              </div>

              <div className="flex gap-8 text-sm">
                <Link
                  href="#"
                  className="text-gray-400 hover:text-[#d97757] transition-colors"
                >
                  About
                </Link>
                <Link
                  href="#"
                  className="text-gray-400 hover:text-[#d97757] transition-colors"
                >
                  Privacy
                </Link>
                <Link
                  href="#"
                  className="text-gray-400 hover:text-[#d97757] transition-colors"
                >
                  Terms
                </Link>
                <Link
                  href="#"
                  className="text-gray-400 hover:text-[#d97757] transition-colors"
                >
                  Contact
                </Link>
              </div>
            </div>

            <div className="mt-8 pt-6 border-t border-[#3d3d3d] text-center">
              <p className="text-gray-500 text-sm">
                © {new Date().getFullYear()} PixelMorph. Crafted with passion
                and Python.
              </p>
            </div>
          </div>
        </footer>
      </div>
    </main>
  );
}
