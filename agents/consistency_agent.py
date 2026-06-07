from utils.llm import call_llm
# Function to check whether the text contains contradictions or logical errors
def consistency_agent(text: str):

    prompt = f"""
You are a CONSISTENCY AGENT.

RULES:
- Check for contradictions.
- Check for logical inconsistencies.
- If no issues exist, write None.
- Do not invent problems.
- Do not add new facts.

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