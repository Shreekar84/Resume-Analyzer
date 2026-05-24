#  AI Resume Analyzer

An AI-powered Resume Analyzer that compares resumes against job descriptions using semantic similarity and skill matching. Upload a PDF resume or paste resume text to receive an instant analysis of how well it matches a job description.

## Live Demo

🔗 Frontend: https://resume-analyzer-three-hazel.vercel.app

🔗 Backend API: https://lavish-blessing-production-b046.up.railway.app

---

##  Features

- 📄 Upload Resume PDF
- 📝 Paste Resume Text
- 🤖 AI-Powered Semantic Similarity Analysis
- 🎯 Skill Matching Score
- 🔍 Missing Skills Detection
- 💡 Personalized Recommendations
- ⚡ FastAPI REST API Backend
- 🎨 Responsive React Frontend

---

## Tech Stack

### Frontend
- React.js
- Axios
- CSS

### Backend
- FastAPI
- Sentence Transformers
- Scikit-learn
- PyPDF
- Uvicorn

### Deployment
- Vercel
- Railway
- GitHub

---

## 📂 Project Structure

```text
Resume-Analyzer/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
└── README.md
```

## 📡 API Endpoints

### Analyze Resume Text

```http
POST /analyze
```

Request Body:

```json
{
  "resume_text": "Experienced Python Developer...",
  "job_description": "Looking for a Python Developer..."
}
```

### Analyze Resume PDF

```http
POST /analyze-pdf
```

Form Data:

```text
resume_file : PDF
job_description : Text
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Shreekar84/Resume-Analyzer.git
cd Resume-Analyzer
```

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

<<<<<<< HEAD
## Screenshots
![Img loading..](Screenshots/Screenshot%20(165).png)
![Img2 loading..](Screenshots/Screenshot%20(166).png)
![Img3 loading..](Screenshots/Screenshot%20(167).png)


## 📊 How It Works

1. Upload a PDF resume or paste resume text.
2. Enter a job description.
3. The application extracts skills from both inputs.
4. Sentence Transformers generate embeddings for semantic comparison.
5. Cosine similarity calculates the semantic match score.
6. Skill matching identifies common and missing skills.
7. Results are displayed with recommendations.

---

## 🎯 Future Improvements

- ATS Resume Scoring
- LLM-Based Resume Suggestions
- Authentication & User Accounts
- Resume History Tracking
- PostgreSQL Database Integration
- Downloadable Analysis Reports
- Interactive Data Visualizations

---
## 👨‍💻 Author
**Shreekar**

GitHub: https://github.com/Shreekar84

---

⭐ If you found this project useful, consider giving it a star on GitHub!
