from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
client=Groq(api_key=os.getenv('GROQ_API_KEY'))

def check_prompt(inp, doc_context):
    prompt = f"""You are a document relevance checker. Determine if the question is related to the document content.

    Document context: {doc_context[:500]}

    Question: {inp}

    Respond with ONLY 'relevant' if the question is about the document content, or 'irrelevant' if it's a general question unrelated to the document."""
    
    model = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    res = model.choices[0].message.content.strip().lower()
    return res=='relevant'

