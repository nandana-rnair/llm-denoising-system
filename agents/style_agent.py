from utils.llm import call_llm

def style_agent(text: str):

    prompt = f"""
You are a STYLE IMPROVEMENT AGENT.

RULES:
- Improve grammar.
- Improve readability.
- Improve sentence flow.
- Do NOT change facts.
- Do NOT add new information.
- If no changes are needed, write None.

Return EXACTLY in this format:

Issues Found:
- <issue or None>

Changes Made:
- <change or None>

Updated Text:
<updated text>

TEXT:
{text}
"""

    return call_llm(prompt).strip()