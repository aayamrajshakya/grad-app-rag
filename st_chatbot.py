import streamlit as st
from component_class import cls_EmbeddingModel, cls_FAISS, cls_GenLLM


# cached for performance
@st.cache_resource
def load_components():
    _embedding = cls_EmbeddingModel(embedding_model="all-mpnet-base-v2", device="cpu")
    embedding = _embedding.initialize_model()

    _retriever = cls_FAISS(db_path="faiss_index", embedding_model=embedding)
    retriever = _retriever.init_retriever(top_k=3)

    _rag = cls_GenLLM(gen_model="Qwen/Qwen2.5-7B-Instruct", retriever=retriever)
    return _rag


rag = load_components()


def chatbot_ui():
    st.set_page_config(page_title="Graduation Application RAG", page_icon="📚")
    st.subheader("📚 Graduation Application RAG")
    st.write("Part of the CSE 4633 AI project")
    st.markdown("*No paid tool/model was used for any part of this project. Just good ol' open-source stuff :)*")
    st.write("---")

    # maintain chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{
            "role": "ai",
            "content": "Hi! How can I help you today?"
        }]

    # display previous messages
    for msg in st.session_state.chat_history:
        with st.chat_message("assistant" if msg["role"] == "ai" else "user"):
            st.write(msg["content"])

    user_input = st.chat_input(
        "What is the application deadline for Fall 2026?")
    if user_input:
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })
        with st.chat_message("user"):
            st.write(user_input)

        # call RAG response and display
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = rag.response(user_input)
                st.write(response)

        # save AI response
        st.session_state.chat_history.append({
            "role": "ai",
            "content": response
        })


if __name__ == "__main__":
    chatbot_ui()
