async function uploadResume() {
    const fileInput = document.getElementById("fileInput");

    if (fileInput.files.length === 0) {
        alert("Please select a file");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        let response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        let data = await response.json();

        // ✅ Skills display
        document.getElementById("skills").innerText =
            "Skills: " + (data.skills?.join(", ") || "None");

        // 📊 Score display
        document.getElementById("score").innerText =
            "ATS Score: " + (data.score ?? 0);

        // 💡 Suggestions display (NEW FIX)
        let suggestionsBox = document.getElementById("suggestions");

        if (suggestionsBox) {
            suggestionsBox.innerHTML = `
                <h3>Suggestions</h3>
                <ul>
                    ${data.suggestions?.map(s => `<li>${s}</li>`).join("")}
                </ul>
            `;
        }

    } catch (error) {
        console.log(error);
        alert("Error: Failed to fetch");
    }
}