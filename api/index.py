from flask import Flask, request, jsonify, send_file
import os
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return send_file("../index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message empty hai"}), 400

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
