# Import all agents used in the denoising pipeline
from agents.fact_checking_agent import fact_checking_agent
from agents.consistency_agent import consistency_agent
from agents.style_agent import style_agent
from agents.final_review_agent import final_review_agent
# Import quality scoring function

from evaluation.metrics import quality_score

def run_pipeline(text):
    original = text
    fact_checked = fact_checking_agent(original)
    consistency_fixed = consistency_agent(fact_checked)
    styled = style_agent(consistency_fixed)
    final = final_review_agent(styled)
    scores = {
        "original": quality_score(original),
        "fact_checked": quality_score(fact_checked),
        "consistency": quality_score(consistency_fixed),
        "style": quality_score(styled),
        "final": quality_score(final)
    }
    return {
        "original": original,
        "fact_checked": fact_checked,
        "consistency": consistency_fixed,
        "style": styled,
        "final": final,
        "scores": scores
    }