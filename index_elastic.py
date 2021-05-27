from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pandas as pd
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize


index_name = "demo_simcse"
path_index = "config/index.json"
model_embedding = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
path_data = "data/data_title.csv"
batch_size = 128
client = Elasticsearch()


def embed_text(batch_text):
    batch_embedding = model_embedding.encode(batch_text)
    return [vector.tolist() for vector in batch_embedding]


def index_batch(docs):
    requests = []
    titles = [tokenize(doc["title"]) for doc in docs]
    title_vectors = embed_text(titles)
    for i, doc in enumerate(docs):
        request = doc
        request["_op_type"] = "index"
        request["_index"] = index_name
        request["title_vector"] = title_vectors[i]
        requests.append(request)
    bulk(client, requests)


print(f"Creating the {index_name} index.")
client.indices.delete(index=index_name, ignore=[404])
with open(path_index) as index_file:
    source = index_file.read().strip()
    client.indices.create(index=index_name, body=source)

docs = []
count = 0
df = pd.read_csv(path_data).fillna(' ')
for index, row in df.iterrows():
    count += 1
    item = {
        'id': row['id'],
        'title': row['title']
    }
    docs.append(item)
    if count % batch_size == 0:
        index_batch(docs)
        docs = []
        print("Indexed {} documents.".format(count))
if docs:
    index_batch(docs)
    print("Indexed {} documents.".format(count))

client.indices.refresh(index=index_name)
print("Done indexing.")


