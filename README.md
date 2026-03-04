# Document Intelligence

AI-powered document question-answering system with advanced RAG (Retrieval-Augmented Generation) capabilities, reranking, and evaluation metrics.

## Features

- **PDF Document Processing** - Upload and analyze PDF documents
- **Intelligent Q&A** - Ask questions and get accurate answers from your documents
- **Multiple Chunking Strategies** - Recursive, Semantic, and Hybrid text splitting
- **Advanced Reranking** - Flashrank, BGE, and ColBERT rerankers for better retrieval
- **Context Validation** - Filters out-of-context queries using LLM-based validation
- **Evaluation Metrics** - Cosine similarity, BLEU score, and answer relevance
- **Smart Suggestions** - Auto-generated questions based on document content
- **Interactive PDF Viewer** - Navigate to relevant pages directly from answers
- **Chat History** - Maintains conversation context for follow-up questions

## Project Structure

```
react/
├── src/
│   ├── core/              # Core RAG components
│   │   ├── ragchain.py    # RAG chain with history-aware retrieval
│   │   ├── rerank.py      # Document reranking implementations
│   │   ├── splitter.py    # Text chunking strategies
│   │   └── grails.py      # Query context validation
│   ├── utils/             # Utility functions
│   │   ├── docloader.py   # PDF loading utilities
│   │   └── evalm.py       # Evaluation metrics
│   ├── ui/                # UI components
│   │   ├── pdf.py         # PDF viewer component
│   │   └── styles.py      # Custom CSS styling
├── main.py               # Main Streamlit application
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd react
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the application:
```bash
streamlit run main.py
```

### Workflow

1. **Upload Document** - Upload a PDF file
2. **Process Document** - Click "Process Document" to initialize the system
3. **Configure** - Select chunking and reranking techniques
4. **Ask Questions** - Use suggested questions or type your own
5. **View Results** - Get answers with source page references and metrics

## Technologies

- **LangChain** - RAG framework and document processing
- **Streamlit** - Web interface
- **FAISS** - Vector database for similarity search
- **HuggingFace** - Embeddings (all-MiniLM-L6-v2)
- **Groq** - LLM inference (Llama 3.1)
- **Flashrank/BGE/ColBERT** - Document reranking
- **NLTK** - BLEU score calculation
- **scikit-learn** - Cosine similarity

## Chunking Strategies

- **Recursive Character** - Fixed-size chunks with overlap (500 chars, 50 overlap)
- **Semantic Chunking** - Content-aware splitting based on semantic similarity
- **Hybrid** - Combines semantic and recursive for optimal results

## Reranking Methods

- **Flashrank** - Fast lightweight reranker
- **BGE Reranker** - BAAI/bge-reranker-base model
- **ColBERT** - ColBERTv2.0 for precise reranking

## Evaluation Metrics

- **Cosine Similarity** - Query-document relevance
- **Answer Relevance** - Answer-context alignment
- **BLEU Score** - Answer quality measurement

## Key Components

### RAG Chain (`ragchain.py`)
- History-aware retrieval
- Context-based question reformulation
- Concise answer generation

### Context Validation (`grails.py`)
- Validates if queries are answerable from document
- Prevents hallucinations on out-of-context questions

### Document Loader (`docloader.py`)
- Handles PDF file uploads
- Creates temporary file paths for processing

### Reranking (`rerank.py`)
- FAISS vector store creation
- Contextual compression retrieval
- Multiple reranker implementations

## Configuration

Modify settings in `main.py`:
- Model: `llama-3.1-8b-instant`
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- Top-k retrieval: 3 documents
- Chunk size: 500 characters
- Chunk overlap: 50 characters

## License

MIT

## Contributing

Contributions welcome! Please open an issue or submit a pull request.
