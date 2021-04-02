from algorithm.train.model_generator import *
from algorithm.predict.prophet import *
from algorithm.config import *
import platform
import sys
sysstr = platform.system()

if sysstr == "Linux":
    import resource
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))
    sys.setrecursionlimit(100000)
    print("我这可以")
elif sysstr == "Windows":
    sys.setrecursionlimit(100000)
    print("你在 Windows 练死劲不管用")
else:
    print("System incompatible")
    sys.exit(0)

# 封装成接口
# 输入：数据库中格式的数组 key + value
# 输出：key + number
# TODO: 先前端获取评论数据，传到 python 端，看数据能否被接收到。
cft = CommentsFilter(predict_db, output=False)
cft.persist_storage()

# cft.to_feel_layer(4)
