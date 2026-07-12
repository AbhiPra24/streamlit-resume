"""
Combined resume data — merges Standard SDET + AI-focused variants.
"""

RESUME_DATA = {
    "name": "Abhinav Prakash",
    "title": "Senior SDET & AI Automation Engineer",
    "email": "abhinavprakash616@gmail.com",
    "phone": "+91 94575 48199",
    "location": "Noida, India",
    "linkedin": "linkedin.com/in/abhipra24",
    "linkedin_url": "https://linkedin.com/in/abhipra24",
    "github_url": "https://github.com/AbhiPra24",
    "resume_pdf_path": "app/assets/Abhinav_Prakash_Resume.pdf",

    "summary": [
        "Senior SDET & AI Automation Engineer with **5 years** of experience building high-performance test infrastructure, AI-driven developer tools, and shared engineering utilities for complex hardware-software ecosystems.",
        "Specialized in the **Model Context Protocol (MCP)**, developing custom MCP servers and agents to bridge LLMs with local development environments — plus deep expertise in DevSecOps (IIT Roorkee PGP) with tools like Burp Suite and Wireshark integrated into automated pipelines.",
        "Expert in Python-based AI orchestration — building custom agents for Copilot CLI and Gemini CLI, automating complex engineering workflows, and architecting CI/CD pipelines with **40% faster deployment cycles**.",
    ],

    "projects": [
        {
            "title": "AI Agent Ecosystem & MCP Servers",
            "duration": "Jan 2026 – Present",
            "tags": ["MCP", "LLM", "Gemini CLI", "Copilot CLI", "AI Agents"],
            "bullets": [
                "Engineered a custom **MCP Server** to expose localized system data and private documentation to LLMs, enabling context-aware code generation and automated debugging.",
                "Developed a suite of **Custom Agents** for Copilot CLI and Gemini CLI, automating repetitive CLI tasks and providing intelligent terminal-based reasoning for system configurations.",
                "Built **AI-native Skills** that integrate with agentic workflows to perform automated API contract testing and vulnerability scanning.",
            ],
        },
        {
            "title": "DevUtils & ARM (Automation Resource Management)",
            "duration": "ChargePoint — Internal",
            "tags": ["FastAPI", "Streamlit", "Python", "Log Analysis", "AI"],
            "bullets": [
                "Architected an internal AI-integrated toolbox using **FastAPI and Streamlit** for deep log parsing and pattern recognition in complex Unix hardware-software logs.",
                "Implemented intelligent API simulations that reduced defect triage time by **30%** by predicting potential failure points in EV charging logic.",
                "Built shared engineering utilities for system setups, deep log analysis, and test orchestration across cross-functional teams.",
            ],
        },
    ],

    "experience": [
        {
            "title": "Senior Software QA Engineer",
            "company": "ChargePoint",
            "location": "Gurugram, India",
            "duration": "Apr 2025 – Present",
            "color": "#00d4ff",
            "bullets": [
                "Served as technical project QA lead, shifting the team toward **AI-augmented testing** and automated infrastructure management for critical EV charging releases.",
                "Spearheaded 'DevUtils' and 'ARM' — Python, FastAPI, and Streamlit-based shared utilities for system setups, deep log analysis, and test orchestration, **reducing defect triage time by 30%**.",
                "Integrated LLM-based analysis into Jenkins CI/CD pipelines to automatically categorize and prioritize test failures, achieving **40% faster regression cycles**.",
                "Validated complex embedded systems logic including power-sharing algorithms and secure firmware updates over OCPP protocols.",
            ],
        },
        {
            "title": "Software QA Engineer",
            "company": "ChargePoint",
            "location": "Gurugram, India",
            "duration": "Apr 2022 – Apr 2025",
            "color": "#8b5cf6",
            "bullets": [
                "Developed custom Python and Shell scripts to continuously parse Unix system logs and query RDBMS tables, cutting defect triage time by **30%**.",
                "Designed scalable test frameworks from scratch using Python and Playwright, **reducing manual infrastructure setup and test effort by 25%**.",
                "Embedded security checks using Wireshark and Burp Suite to monitor network traffic and validate API security during automated runs.",
                "Executed comprehensive backend testing and automated high-priority REST API workflows ensuring fault-tolerant communication between edge devices and cloud services.",
            ],
        },
        {
            "title": "Programmer Analyst Trainee",
            "company": "Cognizant",
            "location": "",
            "duration": "Feb 2021 – Mar 2022",
            "color": "#10b981",
            "bullets": [
                "Automated critical UI test cases for CVS Health projects using Selenium with Java, **improving pipeline reliability and test coverage**.",
                "Contributed to framework enhancements and execution pipelines, supporting Agile delivery cycles and improving overall CI efficiency.",
            ],
        },
    ],

    "education": [
        {
            "degree": "PGP, Cyber Security",
            "institution": "Indian Institute of Technology, Roorkee",
            "duration": "Jul 2023 – Mar 2024",
            "icon": "fas fa-university",
        },
        {
            "degree": "B.Tech, Electronics & Communications Engineering",
            "institution": "Jaypee Institute Of Information Technology",
            "duration": "2017 – 2021",
            "icon": "fas fa-graduation-cap",
        },
    ],

    "skills": {
        "AI & LLM Infrastructure": {
            "tags": ["Model Context Protocol (MCP)", "Custom Agents", "Gemini CLI", "Copilot CLI", "OpenAI API", "LangChain"],
            "proficiency": 88,
            "color": "#00d4ff",
        },
        "Frameworks & Languages": {
            "tags": ["Python", "Java", "Pytest", "Playwright", "Selenium", "FastAPI", "Streamlit"],
            "proficiency": 92,
            "color": "#8b5cf6",
        },
        "DevOps & Infrastructure": {
            "tags": ["Unix", "Shell Scripting", "Docker", "Jenkins", "Git", "CI/CD", "Linux"],
            "proficiency": 83,
            "color": "#00d4ff",
        },
        "Databases & Security": {
            "tags": ["PostgreSQL", "RDBMS", "Wireshark", "Burp Suite", "Network Monitoring"],
            "proficiency": 78,
            "color": "#8b5cf6",
        },
        "Protocols & APIs": {
            "tags": ["REST API", "Postman", "Swagger", "OCPP 1.6/2.0", "API Security"],
            "proficiency": 87,
            "color": "#00d4ff",
        },
    },

    "certifications": [
        {"name": "Learning Jenkins", "icon": "fas fa-cog"},
        {"name": "5 Common Test Failures", "icon": "fas fa-flask"},
        {"name": "Data Structures and Algorithms – Coding Blocks", "icon": "fas fa-code"},
    ],

    "stats": [
        {"label": "Years Experience", "value": "5+", "icon": "fas fa-bolt"},
        {"label": "Faster Deployments", "value": "40%", "icon": "fas fa-rocket"},
        {"label": "Triage Time Reduction", "value": "30%", "icon": "fas fa-bullseye"},
        {"label": "Manual Effort Saved", "value": "25%", "icon": "fas fa-robot"},
    ],

    # TODO: personalize before sharing — placeholder copy, update monthly.
    "now": {
        "updated": "July 2026",
        "items": [
            "Deep in MCP (Model Context Protocol) server development for internal ChargePoint tooling — bridging LLMs with local dev environments and station simulators.",
            "Exploring multi-agent orchestration patterns for automated test triage and CI/CD failure analysis.",
            "Studying advanced OCPP 2.0.1 conformance edge cases for EV charging power-sharing (DLM) validation.",
        ],
    },

    # TODO: replace with real repo data (or wire up the GitHub API) before sharing.
    "github_projects": [
        {
            "name": "streamlit-resume",
            "description": "This site — an interactive resume built with Streamlit, Plotly, and a dark-neon design system.",
            "url": "https://github.com/AbhiPra24/streamlit-resume",
            "language": "Python",
            "stars": 0,
        },
    ],

    # TODO: swap in real quotes/attributions before sharing.
    "testimonials": [
        {
            "quote": "One of the most thorough QA engineers I've worked with — turns ambiguous bug reports into precise, reproducible test cases.",
            "author": "Placeholder Name",
            "role": "Engineering Manager",
            "company": "ChargePoint",
        },
        {
            "quote": "Built internal tooling that took our regression cycle from days to hours. Genuinely force-multiplying work.",
            "author": "Placeholder Name",
            "role": "Senior Software Engineer",
            "company": "ChargePoint",
        },
    ],

    # TODO: link real posts/talks before sharing; remove the section if none exist yet.
    "writing": [
        {
            "title": "Building an MCP Server for Local Dev Tooling",
            "url": "https://github.com/AbhiPra24",
            "date": "2026",
            "summary": "Notes on bridging LLM agents with private documentation and station simulators via the Model Context Protocol.",
        },
    ],
}
