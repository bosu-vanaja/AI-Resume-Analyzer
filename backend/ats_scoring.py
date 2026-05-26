def calculate_ats_score(skills, text):

    score = 0

    if text is None:
        text = ""

    # Skill weight (60%)
    score += len(skills) * 8

    # Resume length quality (20%)
    word_count = len(text.split())

    if word_count > 500:
        score += 20
    elif word_count > 250:
        score += 15
    elif word_count > 100:
        score += 10

    # Keyword boost (10%)
    keywords = ["project", "experience", "education"]
    for k in keywords:
        if k in text.lower():
            score += 3

    return min(score, 100)


def rank_resumes(resume_list):
    return sorted(resume_list, key=lambda x: x["score"], reverse=True)