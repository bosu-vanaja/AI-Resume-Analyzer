from flask import Flask, request, jsonify
from flask_cors import CORS
from pdf_parser import extract_text_from_pdf
from analyzer import analyze_resume

app = Flask(__name__)

# Enable CORS for frontend connection
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Check if file is sent
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "Empty file selected"}), 400

        print("📄 File received:", file.filename)

        # Extract text from PDF
        text = extract_text_from_pdf(file)

        if not text or text.strip() == "":
            return jsonify({"error": "Could not extract text from PDF"}), 400

        print("🧠 Resume analysis started...")

        # Analyze resume
        result = analyze_resume(text)

        print("✅ Analysis completed successfully")

        return jsonify(result)

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({
            "error": "Server error occurred",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    print("🔥 Backend running at http://127.0.0.1:5000")
    app.run(debug=True)