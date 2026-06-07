# 🧠 LLM Output Denoising System (Multi-Agent AI Pipeline)

---

## 🧠 System Architecture

The system follows a modular multi-agent pipeline that progressively refines and validates LLM outputs.
User Input
│
▼
LLM Response Generator (Groq API)
│
▼
Claim Extraction Agent
│
▼
Fact Checking Agent
│
▼
Consistency Checking Agent
│
▼
Style Improvement Agent
│
▼
Final Review Agent
│
▼
Final Output + Quality Scores


---

## 🔄 Architecture Flow (Visual Box Diagram)


┌──────────────────────────────┐
│ User Input │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Groq LLM Generator │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Claim Extraction Agent │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Fact Checking Agent │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Consistency Checking Agent │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Style Improvement Agent │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Final Review Agent │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│ Final Response + Score │
└──────────────────────────────┘


---

## 💡 Why This Project Matters

Large Language Models often produce:
- Hallucinated facts  
- Inconsistent reasoning  
- Unstructured responses  

This system solves that by introducing a **multi-agent verification pipeline** that improves:

- Accuracy  
- Reliability  
- Readability  
- Consistency  

---

## 🤖 Agents Overview

- **Claim Extraction Agent** → Extracts factual statements from LLM output  
- **Fact Checking Agent** → Validates claims using reasoning  
- **Consistency Checking Agent** → Detects contradictions in response  
- **Style Agent** → Improves grammar and readability  
- **Final Review Agent** → Produces final polished output with scoring  

---

## 🎯 Input & Output

### 📥 Input:
User enters a natural language question.

Example:

Where is the Eiffel Tower located?


### 📤 Output:
- Verified factual response  
- Improved readability  
- Consistency-checked output  
- Final quality score (0–100)  

---

## 🎯 Key Features

- 🤖 LLM-based response generation using Groq API  
- 🔍 Claim extraction  
- ✅ Fact verification system  
- 🔄 Consistency checking  
- ✍️ Style improvement module  
- 🧾 Final review agent  
- 📊 Score-based evaluation system  
- 🧩 Fully modular multi-agent architecture  

---

## 🛠️ Tech Stack

- Python 🐍  
- Groq API  
- dotenv  
- Multi-agent pipeline architecture  
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
```bash
git clone https://github.com/nandana-rnair/llm-denoising-system.git
cd llm-denoising-system

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables
Create a .env file:
GROQ_API_KEY=your_api_key_here


5. Run the project
python main.py
👩‍💻 Author

Nandana R Nair