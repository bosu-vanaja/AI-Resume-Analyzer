SKILLS_DB = [
    # 💻 Software skills
    "python", "java", "javascript", "html", "css",
    "react", "node", "flask", "django", "sql",
    "machine learning", "ai", "numpy", "pandas",

    # ⚡ Hardware / VLSI / Core ECE
    "vlsi", "verilog", "systemverilog", "vhdl",
    "physical design", "physical verification",
    "dft", "sta", "timing analysis",
    "asic", "fpga",

    # 🚗 Embedded & EV
    "embedded systems", "microcontroller", "microprocessor",
    "iot", "embedded c", "rtos",
    "electric vehicles", "ev", "battery management system",

    # 🧠 Electronics basics
    "digital electronics", "analog electronics",
    "signal processing", "communication systems"
]


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS_DB:
        if skill in text:
            found.append(skill)

    return found