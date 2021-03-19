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
elif sysstr == "Windows":
    sys.setrecursionlimit(100000)
else:
    print("System incompatible")
    sys.exit(0)

# 如果存在，就不build了
CreateModels(train_db)

cft = CommentsFilter(predict_db, output=True)


# cft.role()
