import redis


train_db = "comments_zh"  # comments_zh tmp1
predict_db = "comments_zh"

threshold_role = 6
threshold_dr = 8
threshold_ner = 4

part_cluster = None
role_cluster = None
dr_cluster = None
rs_cluster = None
heatage_cluster = None

# Config your filter strategy
part_delete = {}
role_delete = {2: 5, 3: 4}
dr_delete = {}
rs_delete = {}

train_part = True
train_role = False
train_dr = False
train_rs = False

keys = ['comment_text', 'be_contents', 'like_count', 'reply_count', 'be_co_retweet', 'be_co_comments','be_co_like']
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
