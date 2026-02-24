import os
import tempfile
import streamlit as st
import threading
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from docloader import load_doc, get_path
from splitter import get_splitter
from langchain_huggingface import HuggingFaceEmbeddings
from rerank import retrieve
from ragchain import rag_chain
from pdf import pdf_display
from evalm import cos_similarity, bleu_score, answer_relevance
from grails import check_prompt
from styles import get_custom_css
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(
    page_title="DocQA | Document Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(get_custom_css(), unsafe_allow_html=True)
if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

st.markdown("""
<div class='hero-container'>
    <div class='hero-badge'>DOCUMENT AI</div>
    <div class='hero-title'>Document Intelligence</div>
    <div class='hero-subtitle'>Transform your documents into actionable insights with AI. Ask questions, extract knowledge, and accelerate decision-making with precision and speed.</div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Your Document", type="pdf")
if uploaded_file:
    doc=load_doc(uploaded_file)
    
    if st.button("Process Document"):
        st.session_state.processed = True
        st.rerun()
    
    if st.session_state.get('processed'):
        with st.sidebar:
            if st.session_state.get('pdf_page'):
                if st.button("← Back to Full PDF", key="reset_pdf"):
                    st.session_state.pdf_page = None
                    st.rerun()
            pdf_display(get_path(uploaded_file))
        
        st.markdown("<div class='section-header'>Configuration</div>", unsafe_allow_html=True)
        chunking_tech=st.selectbox("Select chunking technique",["Recursive Character Textsplitter","Character Text Splitter","Token based Chunking","Semantic Chunking"])
        
        if 'comp_retriever' not in st.session_state:
            splitter=get_splitter(chunking_tech)
            df=splitter.split_documents(doc)
            os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
            model=ChatGroq(model="llama-3.1-8b-instant")
            embeddings=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
            st.markdown("<div class='status-badge'>Flashrank Reranker Active</div>", unsafe_allow_html=True)
            st.session_state.comp_retriever=retrieve(df,embeddings)
            st.session_state.chain=rag_chain(model,st.session_state.comp_retriever)
            st.session_state.embeddings=embeddings
            res=st.session_state.chain.invoke({'input':'Generate exactly 3 specific questions that can be answered from this document. Format: one question per line, no numbering, no bullets.', 'chat_history':[]})
            st.session_state.suggestions=[ans.strip().lstrip('0123456789.-) ') for ans in res['answer'].split('\n') if ans.strip() and '?' in ans][:3]
        
        comp_retriever=st.session_state.comp_retriever
        chain=st.session_state.chain
        embeddings=st.session_state.embeddings
        
        st.markdown("<div class='section-header'>Suggested Questions</div>", unsafe_allow_html=True)
        with st.expander("View intelligent suggestions based on your document"):
            for i, s in enumerate(st.session_state.suggestions[:3]):
                if st.button(s, key=f"suggest_{i}",use_container_width=True):
                    st.session_state.selected_question = s
                    st.rerun()
        
        if st.session_state.chat_history:
            for idx, msg in enumerate(st.session_state.chat_history):
                role = "user" if isinstance(msg, HumanMessage) else "assistant"
                with st.chat_message(role):
                    if isinstance(msg, AIMessage) and '|||PAGE:' in msg.content:
                        answer, page_info = msg.content.split('|||PAGE:')
                        st.markdown(answer)
                        if st.button(f"📄 Go to Page {page_info}", key=f"history_page_{idx}"):
                            st.session_state.pdf_page = int(page_info)
                            st.rerun()
                    else:
                        st.markdown(msg.content)
        
        query = st.chat_input('Enter your question here...')
        if 'selected_question' in st.session_state:
            query = st.session_state.selected_question
            del st.session_state.selected_question
        
        if query:
            with st.chat_message("user"):
                st.markdown(query)
            st.session_state.chat_history.append(HumanMessage(content=query))
            docs=comp_retriever.invoke(query)
            is_suggested = query in st.session_state.suggestions
            if not is_suggested and not check_prompt(query, docs[0].page_content if docs else ""):
                with st.chat_message("assistant"):
                    msg="I am sorry, I cannot answer questions out of docs"
                    st.error(msg)
                    st.session_state.chat_history.append(AIMessage(content=msg))
            else:
                res=cos_similarity([query],docs,embeddings)[0][0]
                result=chain.invoke({'input':query,'chat_history':st.session_state.chat_history})
                pg=(docs[0].metadata.get('page',0)+1)
                answer_with_page = f"{result['answer']}|||PAGE:{pg}"
                st.session_state.chat_history.append(AIMessage(content=answer_with_page))
                with st.chat_message("assistant"):
                    st.success(result['answer'])
                    with st.expander("📊 Evaluation Metrics"):
                        rel=answer_relevance(result['answer'],docs[0].page_content,embeddings)
                        a=bleu_score([result['answer']], [docs[0].page_content])
                        st.markdown(f"""
                        <div class='enterprise-card'>
                            <div class='metric-label'>Cosine Similarity</div>
                            <div class='metric-value'>{res:.4f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        st.markdown(f"""
                        <div class='enterprise-card'>
                            <div class='metric-label'>Answer Relevance</div>
                            <div class='metric-value'>{rel:.4f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        st.markdown(f"""
                        <div class='enterprise-card'>
                            <div class='metric-label'>BLEU Score</div>
                            <div class='metric-value'>{a:.4f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    if st.button(f"📄 Go to Page {pg}", key=f"goto_page_{len(st.session_state.chat_history)}"):
                        st.session_state.pdf_page = pg
                        st.rerun()
