from component_class import cls_EmbeddingModel, cls_FAISS, cls_GenLLM

_embedding = cls_EmbeddingModel(embedding_model="all-mpnet-base-v2",
                                device="cpu")
embedding = _embedding.initialize_model()

_retriever = cls_FAISS(db_path="faiss_index", embedding_model=embedding)
retriever = _retriever.init_retriever(top_k=2)

_rag = cls_GenLLM(gen_model="Qwen/Qwen2.5-7B-Instruct", retriever=retriever)
rag = _rag.qa_chain()

print(rag.invoke("When is the deadline for international graduate students at Northeastern University?"))
