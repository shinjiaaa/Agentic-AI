"""
Demo v2 — v1 답변에 Reflection 한 단계 추가
v1 답변을 critique agent에게 검토시키고 v2로 개선
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env 파일에서 OPENAI_API_KEY 로드
client = OpenAI()

# v1 답변 (demo_v1.py 실행 결과를 그대로 가져왔다고 가정)
question = "100만원을 연 5%로 3년 복리 굴리면 얼마?"
v1_answer = "약 1,157,625원입니다."


# Critique 프롬프트 (Binary Rubric 사용)
critique_prompt = f"""
[질문] {question}
[v1 답변] {v1_answer}

다음 3가지 기준으로 v1을 0/1 평가하고, 3/3을 충족하는 v2 답변을 작성하라.
  1. 계산 식이 표시되는가?
  2. 단위(원)가 명확한가?
  3. 가정(연 복리, 세전 등)이 적혀 있는가?

출력 형식:
평가: [점수 X/3 + 이유]
v2 답변: [개선된 답변]
"""

# Critique 실행 (가능하면 reasoning 모델 추천)
response = client.chat.completions.create(
    model="gpt-4o",  # 또는 "o1-mini"
    messages=[{"role": "user", "content": critique_prompt}],
)

print(f"[Critique 결과]\n{response.choices[0].message.content}")
