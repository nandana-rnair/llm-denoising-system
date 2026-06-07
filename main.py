from pipeline import run_pipeline
from utils.llm import call_llm


def print_section(title, content):

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)
    print(content)

def main():
    question = input("Ask a question: ")
# Generate original response from LLM
    response = call_llm(question)
# Send response through all agents in the pipeline
    result = run_pipeline(response)

# Display original LLM response
    print_section(
        "1. ORIGINAL LLM RESPONSE",
        result["original"]
    )
# Display Fact Checking Agent output
    print_section(
        "2. FACT CHECKING AGENT REVIEW",
        result["fact_checked"]
    )
  # Display Consistency Agent output
    print_section(
        "3. CONSISTENCY AGENT REVIEW",
        result["consistency"]
    )
# Display Final Reveiew Agent output
    print_section(
        "4. STYLE IMPROVEMENT AGENT REVIEW",
        result["style"]
    )
    print_section(
        "5. FINAL REVIEW AGENT",
        result["final"]
    )
    print("\n")
    print("=" * 70)
    print("6. QUALITY IMPROVEMENT SUMMARY")
    print("=" * 70)
    print(f"Original Response Score     : {result['scores']['original']}/100")
    print(f"Fact Checked Score         : {result['scores']['fact_checked']}/100")
    print(f"Consistency Score          : {result['scores']['consistency']}/100")
    print(f"Style Improved Score       : {result['scores']['style']}/100")
    print(f"Final Response Score       : {result['scores']['final']}/100")

    improvement = (
        result["scores"]["final"]
        - result["scores"]["original"]
    )
# Display improvement result
    if improvement > 0:
        print(f"\nOverall Improvement        : +{improvement} points")
    elif improvement < 0:
        print(f"\nOverall Improvement        : {improvement} points")
    else:
        print("\nOverall Improvement        : 0 points")
    print("\n")
    print("=" * 70)
    print("7. FULL PIPELINE OUTPUT")
    print("=" * 70)
    print(result)
    # Run the progsram when main.py is executed
if __name__ == "__main__":
    main()