import nltk
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def cos_similarity(query,doc,embedding):
    q=embedding.embed_query(query[0])
    d=[]
    for docs in doc:
        if docs.page_content.strip():
            e=embedding.embed_query(docs.page_content)
            d.append(e)
    return cosine_similarity([q], d)
def bleu_score(predictions,references):
    chencherry=SmoothingFunction()
    ans=[sentence_bleu([nltk.word_tokenize(ref.lower())],nltk.word_tokenize(pred.lower()),
    smoothing_function=chencherry.method1) for pred,ref in zip(predictions,references)]
    return np.mean(ans)

def answer_relevance(answer,context,embedding):
    ans_emb=embedding.embed_query(answer)
    ctx_emb=embedding.embed_query(context)
    return cosine_similarity([ans_emb],[ctx_emb])[0][0]

