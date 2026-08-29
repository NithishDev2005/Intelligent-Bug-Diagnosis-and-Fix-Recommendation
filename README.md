# 🐞 Smart Bug Analysis

AI-powered software bug diagnosis and fix recommendation platform using multi-agent analysis, a local LLM, and Retrieval-Augmented Generation (RAG).

---

## 📌 Overview

Smart Bug Analysis helps developers investigate software bugs by automatically analyzing bug reports, stack traces, and historical defect information.

The system accepts:

- Bug title
- Description
- Error type
- Stack trace
- Component
- Technologies

It processes this information through specialized agents and historical bug retrieval to produce a structured diagnosis.

The final result provides:

- Severity
- Priority
- Failure point
- Error type
- Similar historical bugs
- Probable root cause
- Confidence
- Recommended fix
- Preventive action

---

## 🎯 Problem Statement

Developers spend considerable time manually investigating software bugs, understanding stack traces, searching historical issues, identifying root causes, and deciding appropriate fixes.

This project aims to automate these activities using AI-assisted multi-agent analysis and historical defect knowledge.

---

## 🚀 Features

### Bug Triage

Determines:

- Severity: LOW, MEDIUM, HIGH, or CRITICAL
- Priority: P1, P2, P3, or P4
- Reasoning

The system also applies deterministic rules for serious application errors to improve classification consistency.

### Log and Stack Trace Analysis

Analyzes error information and identifies:

- Failure point
- Error type
- Important error information
- Failure reasoning

### Historical Bug Retrieval

Uses RAG and semantic similarity search to retrieve relevant historical bugs.

### Similar / Duplicate Bug Detection

Compares the submitted bug with historical bugs and identifies potentially related issues.

### Root Cause Analysis

Combines the current bug, log analysis, and similar historical bugs to determine the probable root cause and confidence.

### Remediation

Provides:

- Recommended fix
- Preventive action
- Remediation reasoning

### Multi-Agent Orchestration

A central orchestrator coordinates the agents and combines their results into a final diagnosis.

### Streamlit Dashboard

Provides a simple web interface for submitting bugs and viewing diagnosis results.

### FastAPI

Provides a REST API for accessing the diagnosis pipeline independently of the Streamlit interface.

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       User          │
                         │    Bug Report       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Streamlit UI      │
                         │     app.py          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │       api.py        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                  ┌──────────────────────────────────┐
                  │     Diagnosis Orchestrator       │
                  └───────────────┬──────────────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
      ┌─────────────┐      ┌─────────────┐     ┌──────────────┐
      │ Triage      │      │ Log Analysis │     │ RAG / Similar│
      │ Agent       │      │ Agent        │     │ Bug Retrieval│
      └─────────────┘      └─────────────┘     └──────┬───────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │ Root Cause      │
                                              │ Agent           │
                                              └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │ Remediation     │
                                              │ Agent           │
                                              └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │ Final Diagnosis │
                                              └─────────────────┘
```

---

## 🔄 Diagnosis Workflow

```text
Bug Report
    │
    ▼
Triage Agent
    │
    ▼
Log Analysis Agent
    │
    ▼
Historical Bug Retrieval
    │
    ▼
Similar Bug Detection
    │
    ▼
Root Cause Agent
    │
    ▼
Remediation Agent
    │
    ▼
Final Diagnosis
```

### Workflow

1. User submits a bug report.
2. Triage Agent determines severity and priority.
3. Log Analysis Agent analyzes the error and stack trace.
4. RAG searches the historical bug knowledge base.
5. Similar bugs are identified.
6. Root Cause Agent determines the probable root cause.
7. Remediation Agent recommends a fix and preventive action.
8. Diagnosis Orchestrator combines the results.
9. Streamlit displays the final diagnosis or FastAPI returns it through the API.

---

## 🧠 RAG Architecture

The system uses historical defect information as its knowledge base.

```text
Historical Bug Reports
        │
        ▼
Bug Documents
        │
        ▼
Sentence Transformer Embeddings
        │
        ▼
ChromaDB Vector Store
        │
        ▼
Semantic Similarity Search
        │
        ▼
Similar Historical Bugs
        │
        ▼
Root Cause Analysis
```

RAG allows the system to use historical defect knowledge when analyzing new bugs.

---

## 🤖 LLM Architecture

The project uses a local LLM through Ollama.

```text
Application
     │
     ▼
LLM Service
     │
     ▼
Ollama
     │
     ▼
Local LLM
```

Using a local LLM keeps the core inference workflow on the development machine and avoids requiring a cloud LLM API for the diagnosis pipeline.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Ollama | Local LLM inference |
| Streamlit | Web dashboard |
| FastAPI | REST API |
| Uvicorn | FastAPI server |
| ChromaDB | Vector database |
| Sentence Transformers | Text embeddings |
| Scikit-learn | Similarity and ML utilities |
| Pydantic | Data validation and structured models |
| Requests | HTTP communication |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📁 Project Structure

```text
SMART-BUG-ANALYSIS/
│
├── agents/
│   ├── triage_agent.py
│   ├── log_analysis_agent.py
│   ├── duplicate_detection_agent.py
│   ├── root_cause_agent.py
│   └── remediation_agent.py
│
├── data/
│   └── historical bug data
│
├── models/
│   └── agent_models.py
│
├── orchestrator/
│   └── bug_diagnosis_orchestrator.py
│
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── services/
│   └── llm_service.py
│
├── tests/
│
├── utils/
│
├── api.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Directory Responsibilities

- `agents/` — Specialized bug analysis agents.
- `models/` — Structured data and validation models.
- `orchestrator/` — Coordinates the complete diagnosis workflow.
- `rag/` — Embeddings, vector storage, and historical bug retrieval.
- `services/` — Reusable application services such as LLM integration.
- `data/` — Historical bug knowledge.
- `tests/` — Unit and integration tests.
- `utils/` — Supporting utilities.
- `api.py` — FastAPI application.
- `app.py` — Streamlit application.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/NithishDev2005/SMART-BUG-ANALYSIS.git
cd SMART-BUG-ANALYSIS
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Ollama Setup

Verify Ollama:

```bash
ollama --version
```

Check available models:

```bash
ollama list
```

Make sure the model configured in the project's LLM service is available.

---

## ▶️ Running the Application

The application consists of a FastAPI backend and Streamlit frontend.

### Start FastAPI

Open a terminal and run:

```bash
python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

The API runs at:

```
http://127.0.0.1:8000
```

Health check:

```
http://127.0.0.1:8000/
```

### Start Streamlit

Open another terminal and activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run:

```bash
streamlit run app.py
```

The dashboard runs at:

```
http://localhost:8501
```

---

## 🔌 API Documentation

### Health Check

```
GET /
```

Example response:

```json
{
  "message": "Smart Bug Analysis API is running"
}
```

### Diagnose Bug

```
POST /diagnose
```

Example request:

```json
{
  "title": "NullPointerException in User Profile",
  "description": "Application crashes when opening a user profile.",
  "error_type": "NullPointerException",
  "stack_trace": "UserService.getProfile(UserService.java:142)",
  "component": "User Service",
  "technologies": "Java, Spring Boot"
}
```

The diagnosis response contains:

- Severity
- Priority
- Failure point
- Error type
- Similar bugs
- Probable root cause
- Confidence
- Recommended fix
- Preventive action

---

## 🧪 Example Diagnosis

### Example Input

```
Title: NullPointerException in User Profile
Description: Application crashes when opening a user profile.
Error Type: NullPointerException
Stack Trace: UserService.getProfile(UserService.java:142)
Component: User Service
Technologies: Java, Spring Boot
```

### Example Output

```
Severity: HIGH
Priority: P1

Failure Point:
UserService.getProfile(UserService.java:142)

Error Type:
NullPointerException

Similar Bugs:
BUG-001
BUG-017
BUG-003

Root Cause:
UserProfile object can be null when optional profile data is missing.

Confidence:
HIGH

Recommended Fix:
Add null validation before accessing the affected object
and ensure the object is properly initialized.

Preventive Action:
Add null-safety checks, unit tests, and validation
for the affected user profile flow.
```

---

## 🧪 Testing

### Compile Check

```bash
python -m compileall agents orchestrator models rag services
```

### Orchestrator Test

```bash
python -m tests.test_orchestrator
```

### Pipeline Test

```bash
python -m tests.test_bug_diagnosis_pipeline
```

The project has also been tested through the Streamlit dashboard and FastAPI endpoint using different bug scenarios.

---

## 📊 Validation

The application has been tested with multiple bug types.

### NullPointerException

The system identified:

```
Severity: HIGH
Priority: P1
Error Type: NullPointerException
```

and retrieved related historical bugs.

### TimeoutException

The system also analyzed a database timeout scenario:

```
Severity: MEDIUM
Priority: P2
Error Type: TimeoutException
```

and produced relevant similar bugs, root-cause analysis, recommended remediation, and preventive action.

These tests demonstrate that the pipeline can process different categories of software bugs.

---

## 🔐 Security

The project excludes local and sensitive files from Git using `.gitignore`.

```
venv/
__pycache__/
*.pyc
.env
.streamlit/secrets.toml
data/chroma_db/
```

Sensitive credentials and API keys should never be committed to the repository.

The generated ChromaDB data is also excluded from version control.

---

## 📈 Project Status

### Completed

- ✅ Project setup
- ✅ Data models
- ✅ Historical bug dataset
- ✅ Text embeddings
- ✅ ChromaDB vector store
- ✅ RAG retrieval
- ✅ Triage Agent
- ✅ Log Analysis Agent
- ✅ Duplicate Detection Agent
- ✅ Root Cause Agent
- ✅ Remediation Agent
- ✅ Diagnosis Orchestrator
- ✅ Complete diagnosis pipeline
- ✅ FastAPI integration
- ✅ Streamlit dashboard
- ✅ Multi-bug testing
- ✅ Syntax validation
- ✅ Git/GitHub version control
- ✅ Deterministic triage consistency rules

### Current Status

The core Smart Bug Analysis platform is complete and operational.

---

## 🔮 Future Improvements

Potential future improvements include:

- GitHub Issues integration
- Jira integration
- Automatic bug-ticket creation
- User authentication
- Production database support
- Cloud deployment
- Advanced evaluation metrics
- Diagnosis analytics
- Support for additional programming languages
- Optional cloud-based LLM providers
- Automated learning from newly resolved bugs

---

## 🎓 Project Highlights

This project demonstrates practical implementation of:

- Multi-agent AI architecture
- Local LLM integration
- Retrieval-Augmented Generation
- Vector databases
- Semantic similarity search
- REST API development
- Streamlit application development
- Structured AI outputs
- Deterministic validation rules
- Software testing
- Git and GitHub workflow

---

## 👨‍💻 Author

**Nithish**

Smart Bug Analysis — AI-powered software debugging and fix recommendation platform.
