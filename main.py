import time
from elasticsearch import Elasticsearch
import streamlit as st
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize


@st.cache(allow_output_mutation=True)
def load_es():
    model_embedding = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
    client = Elasticsearch()
    return model_embedding, client


def embed_text(text):
    text_embedding = model_embedding.encode(text)
    return text_embedding.tolist()


def search(query, type_ranker):
    if type_ranker == 'SimCSE':
        time_embed = time.time()
        query_vector = embed_text([tokenize(query)])[0]
        print(len(query_vector))
        print('TIME EMBEDDING ', time.time() - time_embed)
        script_query = {

            "script_score": {
                "query": {
                    "match_all": {}
                }
                ,
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'title_vector') + 1.0",
                    "params": {"query_vector": query_vector}
                }
            }
        }
    else:
        script_query = {
            "match": {
              "title": {
                "query": query,
                "fuzziness": "AUTO"
              }
            }
        }

    response = client.search(
        index='demo_simcse',
        body={
            "size": 10,
            "query": script_query,
            "_source": {
                "includes": ["id", "title"]
            },
        },
        ignore=[400]
    )

    result = []
    print(response)
    for hit in response["hits"]["hits"]:
        result.append(hit["_source"]['title'])
    return result



def run():
    st.title('Test semantic search')
    ranker = st.sidebar.radio('Rank by', ["BM25", "SimCSE"], index=0)
    st.markdown('Here is example')
    st.text('')
    input_text = []
    comment = st.text_input('Write your test content!')
    input_text.append(comment)

    if st.button('SEARCH'):
        with st.spinner('Searching ......'):
            if input_text is not '':
                print(f'INPUT: ', input_text)
                if ranker == 'SimCSE':
                    result_ = search(input_text[0], 'SimCSE')
                else:
                    result_ = search(input_text[0], 'BM25')
                for i in result_:
                    st.success(f"{str(i)}")


if __name__ == '__main__':
    model_embedding, client = load_es()
    run()
