import streamlit as st
from main import create_pm_crew

st.set_page_config(page_title="AI Product Manager Crew", page_icon="🤖", layout="wide")

st.title("🤖 AI Product Management Suite")
st.caption("Powered by CrewAI & Gemini 2.5 Flash")

# Sidebar information
with st.sidebar:
    st.header("Active Agents")
    st.markdown("""
    - 🔍 **Customer Feedback Analyst**
    - 📈 **Market Intelligence Specialist**
    - 🎯 **Lead Product Manager**
    - 📄 **Principal Technical PRD Writer**
    - 🏃 **Technical Scrum Master**
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("Ask your AI PM Crew anything..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run the crew and display output
    with st.chat_message("assistant"):
        with st.spinner("🧠 The AI PM Crew is collaborating on your request..."):
            crew = create_pm_crew()
            result = crew.kickoff(inputs={"user_query": prompt})

            # Display final output
            st.markdown(result.raw)
            st.session_state.messages.append({"role": "assistant", "content": result.raw})