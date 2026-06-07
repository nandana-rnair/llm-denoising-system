# 🧠 LLM Output Denoising System (Multi-Agent AI Pipeline)

## 🚀 Overview

This project is a multi-agent LLM output denoising and verification system designed to improve the reliability, factual accuracy, and consistency of AI-generated responses.

It takes an input question, generates an LLM response, and then passes it through multiple specialized agents that:

- Extract claims  
- Fact-check responses  
- Detect inconsistencies  
- Improve style and clarity  
- Produce a final validated output with scoring  

---

## 🎯 Key Features

- 🤖 LLM-based response generation using Groq API  
- 🔍 Automated claim extraction  
- ✅ Fact-checking agent for verifying correctness  
- 🔄 Consistency checker to detect contradictions  
- ✍️ Style improvement agent for readability enhancement  
- 🧾 Final review agent for output validation  
- 📊 Scoring system to evaluate response quality  
- 🧩 Modular multi-agent architecture  

---

## 🏗️ System Architecture

User Input  
↓  
LLM Response Generator (Groq)  
↓  
Claim Extraction Agent  
↓  
Fact Checking Agent  
↓  
Consistency Checking Agent  
↓  
Style Improvement Agent  
↓  
Final Review Agent  
↓  
Final Clean Output + Scores  

---

## 🛠️ Tech Stack

- Python 🐍  
- Groq API  
- dotenv  
- Multi-agent architecture  
- Git & GitHub  

---

## 📁 Project Structure
llm-denoising-system/
│── agents/
│ ├── fact_checking_agent.py
│ ├── consistency_agent.py
│ ├── style_agent.py
│ ├── final_review_agent.py
│ ├── issue_extraction_agent.py
│ └── conciseness_agent.py
│
│── utils/
│ ├── llm.py
│ └── logger.py
│
│── evaluation/
│ └── metrics.py
│
│── pipeline.py
│── main.py
│── app.py
│── test_groq.py
│── requirements.txt
│── .gitignore



---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash id="s4"
git clone https://github.com/<nandana-rnair>/llm-denoising-system.git
cd llm-denoising-system


### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables

Create a .env file:
GROQ_API_KEY=your_api_key_here


5. Run the project
python main.py


💡 Example Output
Input:

Where is the Eiffel Tower located?

Output:
Fact-checked response
Consistency validated
Style improved
Final score: 100/100



👩‍💻 Author
Nandana R Nair


