from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
def get_splitter(method):
    if method=='Recursive Character Textsplitter':
        return RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
    elif method=='Semantic Chunking':
        return SemanticChunker(
            embeddings=HuggingFaceEmbeddings(
                model="sentence-transformers/all-MiniLM-L6-v2"
            ),
            breakpoint_threshold_type="percentile"
        )
    else:
        semantic = SemanticChunker(
            embeddings=HuggingFaceEmbeddings(
                model="sentence-transformers/all-MiniLM-L6-v2"
            ),
            breakpoint_threshold_type="percentile"
        )
        recursive = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        
        class HybridSplitter:
            def split_text(self, text):
                semantic_chunks = semantic.split_text(text)
                final_chunks = []
                for chunk in semantic_chunks:
                    if len(chunk) > 500:
                        final_chunks.extend(recursive.split_text(chunk))
                    else:
                        final_chunks.append(chunk)
                return final_chunks
        
        return HybridSplitter() 

