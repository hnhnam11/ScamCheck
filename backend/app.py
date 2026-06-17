```python
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

Đánh giá mức độ nghiêm trọng theo 4 mức:

- Nghiêm trọng: Gần như chắc chắn là lừa đảo. Có dấu hiệu yêu cầu chuyển tiền, cung cấp OTP, mật khẩu, thông tin ngân hàng hoặc giả mạo cơ quan/tổ chức.
- Cao: Có nhiều dấu hiệu lừa đảo rõ ràng và nguy cơ mất tiền hoặc mất thông tin cá nhân cao.
- Trung bình: Có một số dấu hiệu đáng ngờ nhưng chưa đủ cơ sở để khẳng định là lừa đảo.
- Thấp: Không phát hiện dấu hiệu lừa đảo rõ ràng hoặc mức độ rủi ro thấp.

Trả lời theo đúng mẫu:

KẾT LUẬN:
(Có dấu hiệu lừa đảo / Không có dấu hiệu lừa đảo / Cần thận trọng)

MỨC ĐỘ:
(Nghiêm trọng / Cao / Trung bình / Thấp)

PHÂN TÍCH:
- Ý 1
- Ý 2
- Ý 3

Chỉ trả về kết quả phân tích, không thêm lời chào hoặc giải thích khác.
"""
    )

    return response.text

if __name__ == "__main__":
    app.run(debug=True)
```
