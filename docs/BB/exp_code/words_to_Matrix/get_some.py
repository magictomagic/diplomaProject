import redis
import json
import jieba
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

raw_comment = r.hgetall('comments_zh')
i = 0
for key, raw_value in raw_comment.items():
    i = i + 1
    if i < 10:
        r.hset('tmp_c', key, raw_value)