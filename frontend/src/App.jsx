import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [pdfFile, setPdfFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const getScoreColor = (score) => {
    if (score >= 75) return "#22c55e";
    if (score >= 50) return "#facc15";
    return "#ef4444";
  };

  const analyzeResume = async () => {
    try {
      setLoading(true);

      let response;

      if (pdfFile) {
        const formData = new FormData();

        formData.append("resume_file", pdfFile);
        formData.append(
          "job_description",
          jobDescription
        );

        response = await axios.post(
          "https://resume-analyzer-kzqo.onrender.com/analyze-pdf",
          formData,
          {
            headers: {
              "Content-Type":
                "multipart/form-data",
            },
          }
        );
      } else {
        response = await axios.post(
          "https://resume-analyzer-kzqo.onrender.com/analyze",
          {
            resume_text: resumeText,
            job_description: jobDescription,
          }
        );
      }

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert(
        "Something went wrong. Check backend server."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">

      <h1>AI Resume Analyzer</h1>

      <p className="subtitle">
        Upload your resume or paste text and
        instantly compare it against a job
        description.
      </p>

      <h3>Paste Resume Text</h3>

      <textarea
        placeholder="Paste Resume Here..."
        rows="8"
        value={resumeText}
        onChange={(e) =>
          setResumeText(e.target.value)
        }
      />

      <h3>OR</h3>

      <div className="file-upload">
        <h3>Upload Resume PDF</h3>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) =>
            setPdfFile(e.target.files[0])
          }
        />

        {pdfFile && (
          <div className="file-info">
            📄 {pdfFile.name}
          </div>
        )}
      </div>

      <h3>Job Description</h3>

      <textarea
        placeholder="Paste Job Description Here..."
        rows="8"
        value={jobDescription}
        onChange={(e) =>
          setJobDescription(
            e.target.value
          )
        }
      />

      <button
        onClick={analyzeResume}
        disabled={loading}
      >
        {loading
          ? "Analyzing..."
          : "Analyze Resume"}
      </button>

      {result && (
        <div className="results">

          <h2>Analysis Results</h2>

          <div className="score-grid">

            <div className="score-card">
              <h3>TF-IDF Match</h3>

              <p
                className="big-score"
                style={{
                  color: getScoreColor(
                    result.tfidf_match_score
                  ),
                }}
              >
                {result.tfidf_match_score}%
              </p>
            </div>

            <div className="score-card">
              <h3>Skill Match</h3>

              <p
                className="big-score"
                style={{
                  color: getScoreColor(
                    result.skill_match_score
                  ),
                }}
              >
                {result.skill_match_score}%
              </p>
            </div>

          </div>

          <h3>Resume Skills</h3>

          <div className="skill-container">
            {result.resume_skills?.map(
              (skill) => (
                <span
                  key={skill}
                  className="skill-tag"
                >
                  {skill}
                </span>
              )
            )}
          </div>

          <h3>Job Skills</h3>

          <div className="skill-container">
            {result.job_skills?.map(
              (skill) => (
                <span
                  key={skill}
                  className="skill-tag"
                >
                  {skill}
                </span>
              )
            )}
          </div>

          <h3>Missing Skills</h3>

          <div className="skill-container">
            {result.missing_skills?.length >
            0 ? (
              result.missing_skills.map(
                (skill) => (
                  <span
                    key={skill}
                    className="missing-tag"
                  >
                    {skill}
                  </span>
                )
              )
            ) : (
              <p>None 🎉</p>
            )}
          </div>

          <h3>Recommendations</h3>

          {result.recommendations?.length >
          0 ? (
            result.recommendations.map(
              (item, index) => (
                <div
                  key={index}
                  className="recommendation"
                >
                  ✓ {item}
                </div>
              )
            )
          ) : (
            <p>
              No recommendations needed
            </p>
          )}

        </div>
      )}

      <footer>
        Built using React, FastAPI,
        Scikit-Learn, TF-IDF & PDF Parsing
      </footer>

    </div>
  );
}

export default App;