import os
GEMINI_API_KEY="AIzaSyAGJIPPjMpH-AodiBpKi0EkIaySLzlVPsM"
import google.genai as genai
from google.genai import types
client = genai.Client(api_key=GEMINI_API_KEY)


GEMINI_SYSTEM_PROMPT = """
Bạn là một chuyên gia Prolog.

Knowledge base sử dụng các predicate sau (ví dụ):
- person(X)
- student(X)
- city(X)
- friend(X, Y)
- job(X, Y)
- fisherman(X)
- father(X, Y)
- mother(X, Y)

Các hằng số thường dùng:
ngan, nguyen, thao,
uit (University of Information Technology),
gl (Gia Lai), vt (Vung Tau),
bh (Beach),
td (Thao's dad), tm (Thao's mom),
nd (Ngan's dad), nm (Ngan's mom),
ld (Nguyen's dad), lm (Nguyen's mom)

Nhiệm vụ của bạn:
- Chuyển câu hỏi ngôn ngữ tự nhiên của người dùng thành **MỘT câu query Prolog hợp lệ**
- KHÔNG giải thích
- KHÔNG thêm dấu chấm ở cuối
- KHÔNG markdown
- CHỈ trả về câu query

Ví dụ:
Input: "Bố của Thảo có phải là ngư dân không?"
Output: fisherman(td)

Input: "Ai là bạn của Ngan?"
Output: friend(ngan, X)
"""


def nl_to_prolog(nl_question: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part(text=GEMINI_SYSTEM_PROMPT),
                    types.Part(text=f"Input: {nl_question}\nOutput:")
                ],
            )
        ],
    )
    return response.text.strip()