# Cải thiện Elasticsearch trong bài toán semantic search sử dụng phương pháp Sentence Embeddings

Trong bài viết này mình sẽ sử dụng pretrain model [SimCSE_Vietnamese](https://github.com/vovanphuc/SimeCSE_Vietnamese) để cải thiện elastic search trong bài toán semantic search.

Mọi người có thể xem bài viết hướng dẫn đầy đủ tại [đây]().
## Cài đặt:

```
git clone 
cd 
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

