# **PixelMorph**


**PixelMorph** is a web application that allows users to **apply artistic effects to images** in real-time. Built with **Next.js** on the frontend and **FastAPI** on the backend, it supports effects like blur, grayscale, and more. PixelMorph leverages modern **CI/CD pipelines** for smooth and automated deployments.

---

## **🚀 Features**

- **Upload and process images in real-time**
- **Multiple image effects**: blur, grayscale, etc.
- **High-resolution image support**
- Frontend built with **Next.js** for performance and SSR
- Backend built with **FastAPI**, easily extendable for new effects
- **CI/CD pipelines** for automated deployment and updates

---

## **📁 Project Structure**

```text
PixelMorph/
├─ pixelMorphBackend/      # FastAPI backend
│  ├─ main.py             # API routes
│  ├─ ai_services.py      # Image processing logic
│  └─ requirements.txt    # Backend dependencies
├─ pixelMorphWeb/          # Next.js frontend
│  ├─ pages/              # Next.js pages
│  ├─ components/         # React components
│  └─ lib/processImage.ts # Frontend API helper
├─ README.md
└─ .gitignore
```

## **⚡ Tech Stack**

- **Frontend:** Next.js, React, TypeScript, Axios
- **Backend:** FastAPI, Python, Pillow/OpenCV
- **Deployment:** Vercel (frontend), AWS EC2 (backend)
- **Other:** Environment variables, CORS, CI/CD pipelines

---

## **💻 Getting Started**

### Backend Setup
```bash
cd pixelMorphBackend
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```
### Frontend Setup
```cd pixelMorphWeb
npm install               # or yarn
# Add backend URL
echo "NEXT_PUBLIC_API_URL=http://18.117.133.97:8000" > .env.local
npm run dev               # or yarn dev
Open http://localhost:3000
```
## **🌐 Deployment**
```Frontend: Hosted on Vercel (HTTPS enabled)

Backend: Hosted on AWS EC2

Frontend calls the backend API directly using the deployed backend URL.
```

##**⚙️ CI/CD Pipelines**
```Frontend (Next.js):

Automatic builds on every push to main via Vercel

Steps:
Clone repository
Install dependencies (npm install)
Build frontend (next build --turbopack)
Deploy to Vercel
Backend (FastAPI):
Hosted on AWS EC2 with CI pipeline

Steps:
Pull latest code on push to main
Activate virtual environment
Install dependencies (pip install -r requirements.txt)
Restart backend process (pm2 or systemd)

Benefits: Automatic deployment, reduced downtime, synced frontend/backend updates
```
##**🛠 Usage**
```
Upload an image via the UI

Select an effect (blur, grayscale, etc.)

Click Process → View processed image

Optionally, download the transformed image
```
##**📈 Future Enhancements**
```
Add more AI-powered effects
Batch image processing
User accounts and image history
Mobile-friendly UI improvements
```
##**📦 License**

This project is MIT Licensed – see LICENSE

##**🔗 Links**

Live Frontend: https://pixelmorphaws.vercel.app

Backend Docs: http://18.117.133.97:8000/docs

## **Created by Nish Patel**
LinkedIn: https://www.linkedin.com/in/nishpatel14

Portfolio: https://nishpatel.dev
