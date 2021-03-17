from toolkit import *
import jieba.analyse

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# 最后记得把这句加上，注释掉是因为执行太慢了
# preheat_cache('comments_zh')

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
raw_comment = r.hgetall('tmp_c')


vectorizer = CountVectorizer()
transformer = TfidfTransformer()

for key, raw_value in raw_comment.items():
    value = json.loads(raw_value)
    comment_text = value['comment_text']
    comment_array = comment_text.split('|')
    comment = []
    for text in comment_array:
        comment.append('/'.join(jieba.cut(text)))
    comment_row = '/'.join(comment)
    no_stop_words = remove_stop_words(comment_row.split('/'))
    print(no_stop_words)


# if __name__ == '__main__':
