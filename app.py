import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
st.set_page_config(page_title="AI Chatbot Mentor", page_icon="🤖", layout="centered")
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("gemini")
)

if 'selected_module' not in st.session_state:
    st.session_state.selected_module = None
if 'messages' not in st.session_state:
    st.session_state.messages = []

MODULES = {
    "Python": "Python programming, syntax, libraries, best practices, data structures, OOP",
    "SQL": "SQL queries, databases, joins, optimization, stored procedures",
    "Power BI": "Power BI dashboards, DAX, data visualization, data modeling",
    "EDA": "Exploratory Data Analysis, statistics, data cleaning, visualization",
    "Machine Learning": "ML algorithms, model training, evaluation, scikit-learn",
    "Deep Learning": "Neural networks, CNNs, RNNs, transformers, TensorFlow, PyTorch",
    "Generative AI": "LLMs, prompt engineering, Gen AI applications, fine-tuning",
    "Agentic AI": "AI agents, autonomous systems, multi-agent frameworks, LangChain agents"
}

# Module selection screen
if st.session_state.selected_module is None:
    st.title("👋 Welcome to AI Chatbot Mentor")
    st.write("Your personalized AI learning assistant.")
    st.write("Please select a learning module to begin your mentoring session.")

    st.write("### 📌 Available Modules:")
    selected = st.selectbox("Choose your module:", list(MODULES.keys()))

    if st.button("Start Learning", type="primary"):
        st.session_state.selected_module = selected
        st.session_state.messages = []
        st.rerun()


else:
    module = st.session_state.selected_module

    st.title(f"Welcome to {module} AI Mentor")
    st.write(f"I am your dedicated mentor for **{module}**. How can I help you today?")

    st.divider()

    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            with st.chat_message("user"):
                st.write(msg['content'])
        else:
            with st.chat_message("assistant"):
                st.write(msg['content'])


    user_input = st.chat_input("Ask your question here...")

    if user_input:

        st.session_state.messages.append({"role": "user", "content": user_input})


        with st.chat_message("user"):
            st.write(user_input)

        system_prompt = f"""You are an AI mentor specialized ONLY in {module}.

Your strict rules:
1. ONLY answer questions related to {MODULES[module]}
2. If a question is NOT related to {module}, respond EXACTLY with:
   "Sorry, I don't know about this question. Please ask something related to {module}."
3. Do NOT answer questions outside your domain under ANY circumstances
4. Be educational, clear, and helpful for questions within your domain

Examples of what to reject:
- Questions about other programming languages (if module is Python)
- Questions about databases (if module is Machine Learning)
- General knowledge questions unrelated to {module}
- Questions about other technical topics outside {module}"""

        full_prompt = system_prompt + "\n\nConversation History:\n"

        for msg in st.session_state.messages:
            if msg['role'] == 'user':
                full_prompt += f"\nUser: {msg['content']}"
            else:
                full_prompt += f"\nAssistant: {msg['content']}"

        full_prompt += "\n\nAssistant:"


        response = model.invoke(full_prompt)


        if isinstance(response.content, list):
            ai_response = response.content[0]['text']
        else:
            ai_response = response.content

        st.session_state.messages.append({"role": "assistant", "content": ai_response})

        # Display AI response
        with st.chat_message("assistant"):
            st.write(ai_response)

    if len(st.session_state.messages) > 0:
        st.divider()

        col1, col2 = st.columns([3, 1])

        with col1:
            # Create downloadable text
            conversation_text = f"AI Chatbot Mentor - {module} Session\n"
            conversation_text += "=" * 60 + "\n\n"

            for msg in st.session_state.messages:
                role = "You" if msg['role'] == 'user' else "AI Mentor"
                conversation_text += f"{role}: {msg['content']}\n\n"
                conversation_text += "-" * 60 + "\n\n"

            st.download_button(
                label="📥 Download Conversation",
                data=conversation_text,
                file_name=f"{module.replace(' ', '_')}_mentor_session.txt",
                mime="text/plain",
                use_container_width=True
            )

        with col2:
            if st.button("🔄 Change Module", use_container_width=True):
                st.session_state.selected_module = None
                st.session_state.messages = []
                st.rerun()