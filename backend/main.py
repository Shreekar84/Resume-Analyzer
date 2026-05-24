from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# Load model once when app starts
model = SentenceTransformer("all-MiniLM-L6-v2")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://resume-analyzer-three-hazel.vercel.app",
    "https://resume-analyzer-cgslvm9ay-shreekar-s-projects1.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Model
# -----------------------------

class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str

# -----------------------------
# Skills Database
# -----------------------------

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
    "github",
    "fastapi",
    "tensorflow",
    "pytorch",
    "flask"
]

# -----------------------------
# Skill Extraction
# -----------------------------

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills

# -----------------------------
# Main Analysis Logic
# -----------------------------

def generate_analysis(resume_text, job_description):

    # -----------------------------
    # TF-IDF Similarity
    # -----------------------------

    # texts = [
    #     resume_text,
    #     job_description
    # ]

    # vectorizer = TfidfVectorizer()

    # vectors = vectorizer.fit_transform(texts)

    # tfidf_similarity = cosine_similarity(
    #     vectors[0:1],
    #     vectors[1:2]
    # )[0][0]

    # tfidf_score = round(
    #     tfidf_similarity * 100,
    #     2
    # )

    # -----------------------------
    # Semantic Similarity
    # -----------------------------

    # Semantic Similarity

    resume_embedding = model.encode(
        resume_text,
        convert_to_numpy=True
    )

    job_embedding = model.encode(
        job_description,
        convert_to_numpy=True
    )

    semantic_score = round(
        float(
            cosine_similarity(
                resume_embedding.reshape(1, -1),
                job_embedding.reshape(1, -1)
            )[0][0]
        ) * 100,
        2
    )

    print("Semantic Score:", semantic_score)

    # -----------------------------
    # Skill Analysis
    # -----------------------------

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )

    common_skills = (
        set(resume_skills)
        &
        set(job_skills)
    )

    missing_skills = sorted(
        list(
            set(job_skills)
            -
            set(resume_skills)
        )
    )

    skill_score = round(
        (
            len(common_skills)
            /
            len(job_skills)
        ) * 100,
        2
    ) if job_skills else 0

    # -----------------------------
    # Response
    # -----------------------------

    return {
    "semantic_match_score": semantic_score,
    "skill_match_score": skill_score,
    "resume_skills": resume_skills,
    "job_skills": job_skills,
    "missing_skills": missing_skills,
    "recommendations": [
        f"Learn {skill.title()}"
        for skill in missing_skills
    ]
    }

# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():
    return {
        "message":
        "AI Resume Analyzer API Running"
    }

# -----------------------------
# Text Resume Endpoint
# -----------------------------

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

# -----------------------------
# PDF Resume Endpoint
# -----------------------------

@app.post("/analyze-pdf")
async def analyze_pdf(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):

    pdf = PdfReader(
        resume_file.file
    )

    resume_text = ""

    for page in pdf.pages:

        text = page.extract_text()

        if text:
            resume_text += (
                text + "\n"
            )

    if not resume_text.strip():
        return {
            "error":
            "Could not extract text from PDF"
        }

    return generate_analysis(
        resume_text,
        job_description
    )