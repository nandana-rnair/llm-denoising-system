from utils.llm import call_llm
 # Function which make the text concise
def conciseness_agent(text):
 # Create instructions for llm
    prompt = f"""
You are a CONCISENESS AGENT.

Remove repetition and unnecessary content.

Return EXACTLY:

REMOVED:
- removed item 1
- removed item 2

CONCISE TEXT:
<cleaned text>

TEXT:
{text}
"""
 # Send the prompt to the LLM and return the response
    return call_llm(prompt)