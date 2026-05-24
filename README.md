# AI Resume Analyzer

An AI-powered Resume Analyzer that compares resumes against job descriptions and provides match scores, skill analysis, and recommendations.

## Features

- Resume text analysis
- PDF resume upload support
- TF-IDF match score calculation
- Skill extraction and comparison
- Missing skills detection
- Personalized recommendations
- Fast and responsive React UI

## Tech Stack

### Frontend
- React
- Vite
- Axios
- CSS

### Backend
- FastAPI
- Scikit-learn
- PyPDF
- Python

### Deployment
- Render
- GitHub

## How It Works

1. Upload a PDF resume or paste resume text.
2. Paste a job description.
3. The system extracts skills from both inputs.
4. Calculates:
   - TF-IDF similarity score
   - Skill match percentage
   - Missing skills
5. Displays recommendations to improve resume-job alignment.

## Project Structure

```
Resume-Analyzer/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
└── README.md
```

## Live Demo

- Frontend: https://resume-analyzer-1-9ntj.onrender.com
- Backend API: https://resume-analyzer-kzqo.onrender.com
- API Docs: https://resume-analyzer-kzqo.onrender.com/docs

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Future Improvements

- ATS score visualization
- Semantic matching using Sentence Transformers
- AI-powered resume suggestions
- Resume keyword highlighting
- Downloadable PDF report
- Authentication and user accounts

## Author

**Shreekar**

- GitHub: https://github.com/Shreekar84
