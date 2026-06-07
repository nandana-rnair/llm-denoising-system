from utils.llm import call_llm

def fact_checking_agent(text: str):

    prompt = f"""
You are a FACT CHECKING AGENT.

RULES:
- Verify factual accuracy.
- Only correct facts that are definitely wrong.
- If the text is correct, do not modify it.
- Do not invent issues.
- Do not add extra information.

Return EXACTLY in this format:

Issues Found:
- <issue or None>

Corrections Made:
- <correction or None>

Updated Text:
<updated text>

TEXT:
{text}
"""

    return call_llm(prompt).strip()