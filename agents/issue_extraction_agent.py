from utils.llm import call_llm

def issue_extraction_agent(text: str):

    prompt = f"""
You are an ISSUE DETECTION agent.

RULES:
- List only issues
- No explanations
- Each issue one line

TEXT:
{text}
"""

    return call_llm(prompt).strip()