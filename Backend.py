from flask import Flask, request, jsonify
import os
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return "BABU Backend is running 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Tumhara naam BABU hai.
Tum friendly Hindi/Hinglish AI assistant ho.
User se helpful aur respectful tareeke se baat karo.

User:
{message}

BABU:
"""
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
