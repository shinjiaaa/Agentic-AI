"""
Demo v1 — Tool Use (가장 기본)
사용자 질문 → LLM이 도구 자동 선택 → 결과 받아서 답변
"""

import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env 파일에서 OPENAI_API_KEY 로드
client = OpenAI()


# 1. 도구 함수
def compound_interest(principal: float, rate: float, years: int) -> float:
    """복리 이자 계산. principal=원금, rate=연이율(0.05=5%), years=기간."""
    return principal * (1 + rate) ** years


# 2. 도구 schema (LLM에 알려줄 형식)
tools = [{
    "type": "function",
    "function": {
        "name": "compound_interest",
        "description": "복리 이자 계산. principal=원금, rate=연이율(0.05=5%), years=기간.",
        "parameters": {
            "type": "object",
            "properties": {
                "principal": {"type": "number"},
                "rate": {"type": "number"},
                "years": {"type": "integer"},
            },
            "required": ["principal", "rate", "years"],
        },
    },
}]


# 3. 실행
question = "100만원을 연 5%로 3년 복리 굴리면 얼마?"
messages = [{"role": "user", "content": question}]

# 1차 호출: LLM이 도구 호출 결정
response = client.chat.completions.create(
    model="gpt-4o", messages=messages, tools=tools,
)
msg = response.choices[0].message
messages.append(msg)

# 도구 실행
for call in msg.tool_calls:
    args = json.loads(call.function.arguments)
    print(f"[Tool call] compound_interest({args})")
    result = compound_interest(**args)
    print(f"  → {result}")
    messages.append({
        "tool_call_id": call.id,
        "role": "tool",
        "content": str(result),
    })

# 2차 호출: 결과 받아 최종 답변 생성
final = client.chat.completions.create(model="gpt-4o", messages=messages)
v1_answer = final.choices[0].message.content

print(f"\n[v1 답변]\n{v1_answer}")
