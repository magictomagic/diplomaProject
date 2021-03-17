import redis
import json
import jieba
import jieba.analyse
import time
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

corpus_file = "idf.txt.big"  # "idf.txt.big"
stop_words = open("stopWords.txt", encoding='utf-8').read()
corpus_fp = open(corpus_file, 'a+', encoding='utf-8')
raw_corpus = open(corpus_file, encoding='utf-8').readlines()
topK = 10


def remove_stop_words(data_list):
    word_list = []
    for data in data_list:
        if data not in stop_words:
            word_list.append(data)
    return word_list


def preheat_cache(db, sensitivity=4):
    """
    preheat 分词引擎
    add new words if discovered from comments,
    everytime service started, traversal the database, add new words to cache
    takes long time...
    wish astringency
    """
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    jieba.analyse.set_idf_path(corpus_file)
    raw_comment = r.hgetall(db)
    raw_new_words_hash_map = {}
    start_time1 = time.time()
    for key, raw_value in raw_comment.items():
        value = json.loads(raw_value)
        comment_text = value['comment_text']
        comment_array = comment_text.split('|')
        comment = []
        for text in comment_array:
            # comment.append('/'.join(jieba.cut(text)))
            comment.append('/'.join(jieba.analyse.extract_tags(text, topK=topK)))
        comment_row = '/'.join(comment)
        no_stop_words = remove_stop_words(comment_row.split('/'))
        for word in no_stop_words:
            if word in raw_new_words_hash_map:
                raw_new_words_hash_map[word] = raw_new_words_hash_map[word] + 1
            else:
                raw_new_words_hash_map[word] = 0
            jieba.add_word(word)
    print('add new words finished')
    new_words_hash_map = {}
    for key_word, times in raw_new_words_hash_map.items():
        if times >= sensitivity:
            new_words_hash_map[key_word] = times
    end_time1 = time.time()
    print("cost " + str(end_time1 - start_time1))
    append_corpus(new_words_hash_map)


def append_corpus(new_words):
    corpus = set()
    size = len(new_words)
    for item in raw_corpus:
        w = item.split(' ')[0]
        corpus.add(w)
    print(len(corpus))
    for key_word, times in new_words.items():
        if key_word not in corpus and len(key_word) > 2:
            new_item = '\n' + key_word + " " + str(topK)  # str(times/size)
            print(new_item)
            corpus_fp.write(new_item)


def text_to_matrix():
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tf_idf = transformer.fit_transform(vectorizer.fit_transform(raw_corpus))
    weight = tf_idf.toarray()  # 太大，就限制严一点
    print(weight)


if __name__ == '__main__':
    # print(remove_stop_words(['首先', '你好', '难道说']))
    # preheat_cache("comments_zh")  # comments_zh
    text_to_matrix()

    # print(raw_corpus)
