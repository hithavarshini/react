from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter, TokenTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
def get_splitter(method):
    if method=='Recursive Character Textsplitter':
        return RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
    elif method=='Character Text Splitter':
        return CharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=30
        )
    elif method=='Token Text Splitter':
        return TokenTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
    else:
        return SemanticChunker(
            embeddings=HuggingFaceEmbeddings(
                model="sentence-transformers/all-MiniLM-L6-v2"
            ),
            breakpoint_threshold_type="percentile"
        )

