from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import FlashrankRerank, CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
def retrieve(df,embeddings,compressor):
    vect=FAISS.from_documents(df,embeddings)
    retriever=vect.as_retriever()
    return ContextualCompressionRetriever(base_compressor=compressor,base_retriever=retriever)
def get_reranker(method):
    if method=='Flashrank Reranker':
        return FlashrankRerank(top_n=3)
    elif method=='BGE Ranker':
        model=HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-base")
        return CrossEncoderReranker(model=model, top_n=3)
    else:
        model=HuggingFaceCrossEncoder(model_name="colbert-ir/colbertv2.0")
        return CrossEncoderReranker(model=model, top_n=3)
    