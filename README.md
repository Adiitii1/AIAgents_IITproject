# AIAgents_IITproject
# 🤖 AI Product Management Suite
> **An Autonomous 5-Agent Framework for Product Discovery, Strategic Scoping, PRD Generation, and Agile Planning.**

Powered by **CrewAI**, **Google Gemini 2.5 Flash**, and **Streamlit**.

---

## 📌 Executive Overview

Product management discovery workflows often require weeks of cross-functional alignment between User Researchers, Market Analysts, Systems Architects, Product Managers, and Scrum Masters. 

The **AI Product Management Suite** compresses that multi-week discovery cycle into a **seamless 2-minute automated pipeline**. By orchestrating five specialized AI agents operating sequentially, the system transforms raw customer feedback or feature requests into production-ready Technical PRDs and estimated Jira User Stories.

---

## 🤖 Multi-Agent Architecture

Our system employs a **sequential multi-agent workflow** where each agent performs a specific role and passes verified contextual context to the next:

1. 🔍 **Senior Customer Feedback Analyst:** Extracts core user pain points, churn drivers, and sentiment from raw feedback.
2. 📈 **Market Intelligence Specialist:** Benchmarks extracted requirements against industry standards and top competitors.
3. 🎯 **Lead Product Manager:** Establishes strategic MVP boundaries, trade-offs, and explicit out-of-scope directives.
4. 📄 **Principal Technical PRD Writer:** Authors a complete Technical Product Requirements Document (PRD v1.0).
5. 🏃 **Technical Scrum Master:** Converts the PRD into an actionable Jira Sprint Backlog with *Given-When-Then* acceptance criteria and Fibonacci story points.

```mermaid
flowchart TD
    User([👤 User Query / Prompt]) --> UI[Streamlit Web App]
    UI --> CrewManager[🚀 CrewAI Sequential Process]

    subgraph AgentCrew [🤖 5-Agent AI Product Team]
        A1["🔍 Senior Customer Feedback Analyst"]
        A2["📈 Market Intelligence Specialist"]
        A3["🎯 Lead Product Manager"]
        A4["📄 Principal Technical PRD Writer"]
        A5["🏃 Technical Scrum Master"]

        A1 -->|Customer Insights| A2
        A2 -->|Market Context| A3
        A3 -->|PRD Outline| A4
        A4 -->|Detailed Requirements| A5
    end

    CrewManager -->|Kickoff| A1
    A5 -->|Final PRD & Jira Backlog| UI
    UI --> User
AI_Product_Manager/
├── 💻 Complete source code/           # Streamlit app and CrewAI orchestration logic
│   ├── app.py                         # Streamlit Web UI Frontend
│   ├── main.py                        # CrewAI setup and agent declarations
│   ├── config/                        # Agent & Task YAML configurations
│   └── tools/                         # Custom agent tools
├── 📐 Agent architecture diagram/     # Mermaid diagrams & high-res architectural flows
├── 📄 Project documentation/          # Comprehensive Word docs (PRD specs & Architecture guides)
├── 📊 Presentation (10–12 slides)/    # Executive pitch deck (PPTX & PDF)
├── 🎥 Demo video (5–10 minutes)/      # Video walkthrough link
├── requirements.txt                   # Project dependencies
└── README.md                          # Project documentation
