# Cải thiện Elasticsearch trong bài toán semantic search sử dụng phương pháp Sentence Embeddings

Trong bài viết này mình sẽ sử dụng pretrain model [SimCSE_Vietnamese](https://github.com/vovanphuc/SimeCSE_Vietnamese) để cải thiện elastic search trong bài toán semantic search.

Mọi người có thể xem bài viết hướng dẫn đầy đủ tại [đây](https://viblo.asia/p/nlp-cai-thien-elasticsearch-trong-bai-toan-semantic-search-su-dung-phuong-phap-sentence-embeddings-Qpmley4rlrd).
## Cài đặt:

```
git clone https://github.com/vovanphuc/elastic_simCSE.git
cd elastic_simCSE
pip install -r requirements.txt
```

## Đánh index cho toàn bộ data

```
python3 index_elastic.py
```

## Search keyword và so sánh giữa BM25 (elasticsearch thường) và simCSE:

```
streamlit run main.py
```

## Kết quả tìm kiếm:

<img src="https://raw.githubusercontent.com/vovanphuc/elastic_simCSE/master/images/BM25.png">

Kết quả khi sử dụng elasticsearch bình thường.

<img src="https://raw.githubusercontent.com/vovanphuc/elastic_simCSE/master/images/SimCSE_vietnamese.png">

Kết quả khi sử dụng SimCSE_VietNamese.

## Contact:

Email: vovanphuc100598@gmail.com

Facebook: [facebook.com/vovanphucc](facebook.com/vovanphucc)

Linkedin: [linkedin.com/in/vovanphuc](linkedin.com/in/vovanphuc)