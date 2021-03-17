import redis

train_db = "tmp1"

threshold_role = 6
threshold_dr = 8
threshold_ner = 4

part_cluster = None
role_cluster = None
dr_cluster = None
rs_cluster = None
heatage_cluster = None

keys = ['comment_text', 'be_contents', 'like_count', 'reply_count', 'be_co_retweet', 'be_co_comments','be_co_like']
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
