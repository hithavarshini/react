
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import FlashrankRerank
def retrieve(df,embeddings):
    vect=FAISS.from_documents(df,embeddings)
    retriever=vect.as_retriever()
    compressor=FlashrankRerank()
    return ContextualCompressionRetriever(base_compressor=compressor,base_retriever=retriever)