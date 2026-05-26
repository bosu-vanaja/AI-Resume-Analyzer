from skill_extractor import extract_skills


def generate_suggestions(text, skills):
    suggestions = []
    text_lower = text.lower()

    # 1. No skills detected
    if len(skills) == 0:
        suggestions.append(
            "⚠️ No technical skills detected. Add skills like Python, SQL, Embedded C, VLSI, or Java."
        )

    # 2. Very few skills
    elif len(skills) < 5:
        suggestions.append(
            "📌 Add more technical skills to improve ATS ranking and recruiter visibility."
        )

    # 3. Missing Projects section
    if "project" not in text_lower:
        suggestions.append(
            "💡 Add a Projects section to showcase practical experience."
        )

    # 4. Missing Experience / Education keywords
    required_sections = ["experience", "education", "skills"]
    missing = [sec for sec in required_sections if sec not in text_lower]

    if missing:
        suggestions.append(
            f"📄 Missing important sections: {', '.join(missing)}"
        )

    # 5. Generic pro tip
    suggestions.append(
        "✨ Use bullet points and quantify achievements (e.g., 'Improved performance by 20%')."
    )

    return suggestions


def analyze_resume(text):
    skills = extract_skills(text)

    # ATS SCORE LOGIC (simple but effective)
    score = min(len(skills) * 10, 100)

    # Smart suggestions added
    suggestions = generate_suggestions(text, skills)

    return {
        "skills": skills,
        "score": score,
        "suggestions": suggestions
    }