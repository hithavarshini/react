
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import FlashrankRerank, CrossEncoderReranker
from langchain_community.document_compressors import JinaRerank
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
def retrieve(df,embeddings,compressor):
    vect=FAISS.from_documents(df,embeddings)
    retriever=vect.as_retriever()
    return ContextualCompressionRetriever(base_compressor=compressor,base_retriever=retriever)
def get_reranker(method):
    if method=='Flashrank Reranker':
        return FlashrankRerank()
    elif method=='BGE Ranker':
        model=HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-base")
        return CrossEncoderReranker(model=model)
    else:
        return JinaRerank()
    