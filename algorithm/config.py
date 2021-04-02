import redis


train_db = "comments_zh"  # comments_zh tmp1
predict_db = "tmp1"

threshold_role = 6
threshold_dr = 8
threshold_ner = 4

part_cluster = None
role_cluster = None
dr_cluster = None
rs_cluster = None
heatage_cluster = None

# Config your filter strategy
# 铁定水军：11889
part_delete = {12741: 6, 24964: 6, 12217: 5, 11904: 5, 12420: 5, 11889: 6}
role_delete = {5738: 6, 5746: 3, 5735: 5, 5686: 2, 5737: 4, 5597: 5}
dr_delete = {781: 5, 1275: 5, 1276: 4, 1123: 2, 1147: 3, 1004: 6}
rs_delete = {}  # 感觉不出了，经过三重过滤，到这里基本没废话了

train_part = True
train_role = False
train_dr = False
train_rs = False

keys = ['comment_text', 'be_contents', 'like_count', 'reply_count', 'be_co_retweet', 'be_co_comments','be_co_like']
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
