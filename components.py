from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class cls_EmbeddingModel:

    def __init__(self, embedding_model, device):
        self.embedding_model = embedding_model
        self.device = device

    def initialize_model(self):
        hf_model = HuggingFaceEmbeddings(
            model_name=self.embedding_model,
            model_kwargs={"device": self.device},
            encode_kwargs={"normalize_embeddings": False},
            multi_process=True if self.device == "cuda" else False,
        )
        return hf_model


class cls_FAISS:

    def __init__(self, db_path, embedding_model):
        self.db_path = db_path
        self.embedding_model = embedding_model

    def load_vector_store(self):
        db = FAISS.load_local(folder_path=self.db_path,
                              embeddings=self.embedding_model,
                              allow_dangerous_deserialization=True)
        return db

    def init_retriever(self, top_k=1):
        db = self.load_vector_store()
        retriever = db.as_retriever(search_kwargs={'k': top_k})
        return retriever


class cls_GenLLM:
    PROMPT_TEMPLATE = """Answer the question based only on the following context. 
                    If 100% out of context, immediately say you don't know.
                    {context}

        Question: {question}
        """

    def __init__(self, gen_model, retriever):
        self.gen_model = gen_model
        self.retriever = retriever

    def initialize_model(self):
        llm = HuggingFaceEndpoint(repo_id=self.gen_model,
                                  task="text-generation",
                                  max_new_tokens=512,
                                  do_sample=False,
                                  repetition_penalty=1.03,
                                  provider="auto")

        chat_model = ChatHuggingFace(llm=llm)
        return chat_model

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def response(self, query):
        prompt = ChatPromptTemplate.from_template(self.PROMPT_TEMPLATE)
        qa_chain = ({
            "context": self.retriever | self.format_docs,
            "question": RunnablePassthrough(),
        }
                    | prompt
                    | self.initialize_model()
                    | StrOutputParser())

        return qa_chain.invoke(query)
    