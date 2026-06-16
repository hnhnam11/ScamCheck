from flask import Flask, request
from flask_cors import CORS

from google import genai

import os

app = Flask(__name__)

CORS(app)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    message = data.get("message", "")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Bạn là chuyên gia phát hiện lừa đảo.

Hãy phân tích tin nhắn sau:

{message}

Trả lời theo mẫu:

KẾT LUẬN:
...

PHÂN TÍCH:
...
"""
    )

    return response.text

if __name__ == "__main__":
    app.run(debug=True)