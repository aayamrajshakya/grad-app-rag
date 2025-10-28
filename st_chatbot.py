# Reference: https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/search_and_chat.py

import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory


def app():
    st.set_page_config(page_title="Graduation Application RAG", page_icon="📚")
    st.subheader("📚 Graduation Application RAG")
    st.write(
        "No paid AI tool was used for any part of this RAG project. Just good ol' open-source stuff :)"
    )

    text = "*Part of the CSE 4633 Artificial Intelligence project*"
    st.markdown(text)
    st.write("-----")

    msgs = StreamlitChatMessageHistory()

    if len(msgs.messages) == 0:
        msgs.clear()
        msgs.add_ai_message("How can I help you?")
        st.session_state.steps = {}

    avatars = {"human": "😉", "ai": "🧠"}
    for idx, msg in enumerate(msgs.messages):
        with st.chat_message(avatars[msg.type]):
            # Render intermediate steps if any were saved
            for step in st.session_state.steps.get(str(idx), []):
                if step[0].tool == "_Exception":
                    continue
                with st.status(
                    f"**{step[0].tool}**: {step[0].tool_input}", state="complete"
                ):
                    st.write(step[0].log)
                    st.write(step[1])
            st.write(msg.content)

    if prompt := st.chat_input(
        placeholder="What is the application deadline for Fall 2026?"
    ):
        st.chat_message("user").write(prompt)

    university_choice = st.sidebar.selectbox(
        "Which university would you like to inquire about?",
        ("Northeastern University", "UMass Amherst", "Mississippi State University"),
    )


if __name__ == "__main__":
    app()
