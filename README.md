# AI Chatbot Mentor - Domain-Specific Intelligent Learning Assistant

## Overview

AI Chatbot Mentor is an interactive, AI-powered mentoring application designed to provide focused, module-specific guidance to learners across multiple technical domains. Unlike generic chatbots, this system strictly responds only within the selected module, ensuring relevant, accurate, and distraction-free mentorship.

The application is built using **Streamlit** for the user interface and **LangChain** with **Google Generative AI (Gemini)** for LLM orchestration, enabling conversational intelligence with strict domain control.

## Features

### 1. Module Selection Interface
Users can choose from 8 specialized learning modules:
- **Python** - Programming fundamentals, data structures, OOP
- **SQL** - Database queries, joins, optimization
- **Power BI** - Dashboards, DAX, data visualization
- **EDA** - Exploratory Data Analysis, statistics
- **Machine Learning** - ML algorithms, model training
- **Deep Learning** - Neural networks, CNNs, RNNs
- **Generative AI** - LLMs, prompt engineering
- **Agentic AI** - AI agents, autonomous systems

### 2. Domain-Specific AI Mentoring
Once a module is selected, the AI mentor provides answers strictly within that domain. Questions outside the selected module are politely rejected with a standard response: *"Sorry, I don't know about this question. Please ask something related to [module name]."*

### 3. Conversation Memory
The chatbot maintains full conversation history throughout the session. All user questions and AI responses are preserved, enabling coherent and context-aware mentoring.

### 4. Download Chat History
Users can download their entire conversation as a `.txt` file at any time. This feature is valuable for:
- Creating revision notes
- Building a learning portfolio
- Offline reference and study

### 5. Module Switching
Users can switch between modules anytime using the "Change Module" button, which resets the conversation and allows selection of a new learning domain.

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.0 Flash |
| LLM Framework | LangCha
