# AI Resume Analyzer

An AI-powered Resume Analyzer web application that extracts skills from resumes, calculates ATS score, and provides improvement suggestions using Python Flask backend.

---

## Features

- Upload PDF resumes
- Extract skills automatically from resume text
- Generate ATS (Applicant Tracking System) score (0–100)
- Provide resume improvement suggestions
- Fast backend processing using Flask API
- Simple and clean frontend UI

---

## Tech Stack

### Frontend:
- HTML
- CSS
- JavaScript
### Backend:
- Python 
- Flask
- Flask-CORS

### Libraries Used:
- flask
- flask-cors
- PyPDF2
- re (Regular Expressions)

---

## How to Run the Project:

1️⃣ Clone Repository
```bash
git clone https://github.com/bosu-vanaja/AI-Resume-Analyzer.git
cd AI-resume-analyzer
2️⃣ Install Dependencies
pip install flask flask-cors PyPDF2
3️⃣ Run Backend
cd backend
python app.py
4️⃣ Open Frontend
Open:
frontend/index.html

API Endpoint:

POST /analyze
Uploads resume and returns extracted data.
Response Example:
{
  "skills": ["python", "vlsi", "verilog"],
  "ats_score": 90,
  "suggestions": ["Add more project details", "Use bullet points"]
}

## Demo_Images:

Add your screenshots inside demo_images/ folder and update README like this:
![Home](demo_images/image1.jpg)
![Upload](demo_images/image2.jpg)
![Result](demo_images/image3.jpg)

## Future Improvements:

AI-based resume ranking
Better ATS scoring model
Cloud deployment (Render / Vercel)
Login system for users
Multi-format resume support (DOCX, TXT)

## Author

Built by "BOSU VANAJA"
