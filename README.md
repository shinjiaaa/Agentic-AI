## 📁 파일

- `demo_v1.py` — Tool Use
- `demo_v2.py` — Reflection 추가
- `.env.example` — API 키 설정

## ⚙️ 실행 준비

### 1. 패키지 설치

```bash
pip install openai python-dotenv
```

### 2. `.env` 파일에 API 키 작성

같은 폴더에 `.env` 파일을 만들고 본인의 OpenAI API 키를 적습니다:

```
OPENAI_API_KEY=sk-...본인_API_키...
```

### 3. 실행

```bash
python demo_v1.py
python demo_v2.py
```

---

## 📤 demo_v1.py 예상 결과

```
[Tool call] compound_interest({'principal': 1000000, 'rate': 0.05, 'years': 3})
  → 1157625.0

[v1 답변]
100만원을 연 5%로 3년 복리 운용하면 약 1,157,625원이 됩니다.
```

**핵심 관찰**:

- LLM이 "100만원" → `1000000`, "5%" → `0.05`로 자동 변환
- Docstring을 보고 `compound_interest`가 적절하다고 판단
- 결과를 받아 자연어로 답변 작성

---

## 📤 demo_v2.py 예상 결과

```
[v1 답변]
약 1,157,625원입니다.

[Critique 결과]
평가: 1/3
  1. 계산 식: 0 (식이 없음)
  2. 단위: 1 ("원" 명시됨)
  3. 가정: 0 (연 복리/세전 여부 없음)

v2 답변:
복리 공식 FV = P × (1 + r)ⁿ 적용 시,
  FV = 1,000,000 × (1 + 0.05)³
     = 1,000,000 × 1.157625
     = 1,157,625 원

가정: 연 복리, 세전 기준, 추가 입금 없음
```

---

## 🔍 v1 vs v2 핵심 차이

| 항목        | v1          | v2                 |
| ----------- | ----------- | ------------------ |
| 계산 결과   | 1,157,625원 | 1,157,625원 (같음) |
| 계산 식     | ❌          | ✅                 |
| 가정 명시   | ❌          | ✅                 |
| Rubric 점수 | 1/3         | 3/3                |

**핵심 메시지**: Reflection은 수치를 바꾸지 않는다. 도구가 보장한 정확한 수치 위에 **설명 품질**을 올린다.

---

## 🛠 흔한 에러

| 에러                        | 해결                                       |
| --------------------------- | ------------------------------------------ |
| `module 'openai' not found` | `pip install openai`                       |
| `module 'dotenv' not found` | `pip install python-dotenv`                |
| `OpenAI API key not found`  | `.env` 파일에 `OPENAI_API_KEY=sk-...` 적기 |
| `model not found: gpt-4o`   | `gpt-4o` 대신 `gpt-4o-mini` 시도           |
