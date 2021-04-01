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
    print("你 Windows 练死劲不管用")
else:
    print("System incompatible")
    sys.exit(0)

# TODO: 如果对应的 model 存在，就不 build 了
# CreateModels(train_db)

cft = CommentsFilter(predict_db, output=False)


cft.to_feel_layer_part()
