from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain,create_history_aware_retriever
def rag_chain(model,comp_retriever):
    context_prompt=(
        """ You are given chat history and latest user question which might reference context in the chat history,
        formulate a standalone questions which can be understood without chat history. Do not answer the question 
        just reformulate it if needed otherwise return it as is
        """
    )
    prompt_search=ChatPromptTemplate.from_messages([
        ("system",context_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{input}"),
    ]
    )
    prompt=(
        "You are an assistant for document based question answering tasks. "
        "Use the following retrieved context to answer the question. "
        "If the answer is in the context, provide it concisely in three sentences maximum. "
        "If the context does not contain the answer, say 'I am not sure.'"
        "\n\n"
        "{context}"
    )
    prompt_msg=ChatPromptTemplate.from_messages(
        [("system",prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human","{input}")
        ]
    )
    hist_chain=create_history_aware_retriever(model,comp_retriever,prompt_search)
    stuff_doc=create_stuff_documents_chain(model,prompt_msg)
    return create_retrieval_chain(hist_chain,stuff_doc)