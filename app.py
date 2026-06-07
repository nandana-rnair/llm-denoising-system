import streamlit as st
from utils.llm import call_llm
from pipeline import run_pipeline

st.set_page_config(
    page_title="LLM Output Denoising System",
    layout="wide"
)
st.title("LLM Output Denoising System")
st.write("Multi-Agent Response Refinement Pipeline")
# Input box for user question
question = st.text_input(
    "Enter your question",
    placeholder="Where is Eiffel Tower?"
)
# this run the pipeline 
if st.button("Run Pipeline"):

    with st.spinner("Generating response..."):
# Generate original response from LLM
        original_response = call_llm(question)
# Send response through all agents
        result = run_pipeline(original_response)
    st.success("Pipeline Completed")
# Display original LLM response
    st.subheader("1. Original LLM Response")
    st.write(result["original"])
    st.divider()
# Display Fact Checking Agent output
    st.subheader("2. Fact Checking Agent")
    with st.expander("View Fact Checking Output", expanded=True):
        st.text(result["fact_checked"])
    st.divider()
# Display Consistency Agent output
    st.subheader("3. Consistency Agent")
    with st.expander("View Consistency Output", expanded=True):
        st.text(result["consistency"])
    st.divider()
# Display Style Improvement Agent output
    st.subheader("4. Style Improvement Agent")
    with st.expander("View Style Output", expanded=True):
        st.text(result["style"])
    st.divider()
# Display Final Review Agent output
    st.subheader("5. Final Review Agent")
    with st.expander("View Final Output", expanded=True):
        st.text(result["final"])
    st.divider()
 # Display quality scores from each stage
    st.subheader("6. Quality Improvement Summary")
    scores = result["scores"]
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Original", scores["original"])
    col2.metric("Fact Check", scores["fact_checked"])
    col3.metric("Consistency", scores["consistency"])
    col4.metric("Style", scores["style"])
    col5.metric("Final", scores["final"])
# Calculate improvement score
    improvement = scores["final"] - scores["original"]
    st.write("---")
# Show improvement status
    if improvement > 0:
        st.success(f"Overall Improvement: +{improvement} points")
    elif improvement < 0:
        st.error(f"Overall Improvement: {improvement} points")
    else:
        st.info("Overall Improvement: 0 points")
    st.divider()
    st.subheader("7. Full Pipeline Output")
    st.json(result)