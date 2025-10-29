import streamlit as st
from components import cls_EmbeddingModel, cls_FAISS, cls_GenLLM


# cached for performance
@st.cache_resource
def load_components(UNIVERSITY):
    _embedding = cls_EmbeddingModel(embedding_model="all-mpnet-base-v2", device="cpu")
    embedding = _embedding.initialize_model()

    _retriever = cls_FAISS(db_path=f"faiss_indices/{UNIVERSITY}", embedding_model=embedding)
    retriever = _retriever.init_retriever(top_k=3)

    _rag = cls_GenLLM(gen_model="Qwen/Qwen2.5-7B-Instruct", retriever=retriever)
    return _rag


def chatbot_ui():
    st.set_page_config(page_title="Graduate Application RAG",
                       page_icon="📚",
                       initial_sidebar_state="expanded")
    st.subheader("Graduate Application RAG (CSE 4633)")
    st.markdown("*No paid tool/model was used for any part of this project. Just good ol' open-source stuff :)*")

    # Reference: https://discuss.streamlit.io/t/label-and-values-in-in-selectbox/1436/6
    UNI_DICT = {
        "msstate": "Mississippi State University",
        "neu": "Northeastern University",
        "amherst": "UMass Amherst",
    }

    def format_func(option):
        return UNI_DICT[option]

    UNIVERSITY = st.sidebar.selectbox(
        label="Which university would you like to inquire about?",
        options=list(UNI_DICT.keys()),
        format_func=format_func)

    if "prev_uni" not in st.session_state or st.session_state.prev_uni != UNIVERSITY:
        st.session_state.chat_history = [{
            "role": "ai",
            "content": f"Hello! What do you wanna know today?"
        }]
        st.session_state.prev_uni = UNIVERSITY

    rag = load_components(UNIVERSITY)

    st.write("Current selection:", UNI_DICT[UNIVERSITY])

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
