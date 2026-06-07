from utils.llm import call_llm
# This agent performs the final validation of the response and verifies accuracy,improved text, consistency, readability.
def final_review_agent(text: str):
    prompt = f"""
You are a FINAL REVIEW AGENT.

RULES:
- Review the response.
- Do NOT add new facts.
- Do NOT rewrite the answer unless necessary.
- Keep the review short.

Return EXACTLY:

Final Assessment:
- Factually Accurate
- Consistent
- Readable

Final Response:
<final response>

TEXT:
{text}
"""
    return call_llm(prompt).strip()