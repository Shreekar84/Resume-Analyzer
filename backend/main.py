from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


skills_db = [
    "python",
    "java",
    "javascript",
    "react",
    "html",
    "css",
    "sql",
    "docker",
    "aws",
    "machine learning",
    "nodejs",
    "mongodb",
    "git",
    "github"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def generate_analysis(resume_text, job_description):

    texts = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    tfidf_score = round(similarity * 100, 2)

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    common_skills = set(resume_skills) & set(job_skills)

    missing_skills = sorted(
        list(set(job_skills) - set(resume_skills))
    )

    skill_score = round(
        (len(common_skills) / len(job_skills)) * 100,
        2
    ) if job_skills else 0

    return {
        "tfidf_match_score": tfidf_score,
        "skill_match_score": skill_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing_skills,
        "recommendations": [
            f"Learn {skill.title()}"
            for skill in missing_skills
        ]
    }


@app.get("/")
def home():
    return {
        "message": "Resume Analyzer API Running"
    }


# Existing text endpoint
@app.post("/analyze")
def analyze(data: ResumeRequest):

    if not data.resume_text.strip():
        return {
            "error":
            "Resume text cannot be empty"
        }

    if not data.job_description.strip():
        return {
            "error":
            "Job description cannot be empty"
        }

    return generate_analysis(
        data.resume_text,
        data.job_description
    )


# New PDF endpoint
@app.post("/analyze-pdf")
async def analyze_pdf(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):

    pdf = PdfReader(resume_file.file)

    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    if not resume_text.strip():
        return {
            "error":
            "Could not extract text from PDF"
        }

    return generate_analysis(
        resume_text,
        job_description
    )