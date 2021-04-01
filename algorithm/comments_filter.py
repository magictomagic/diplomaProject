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

# DO个屁，能用就行。日相为马, 和时相相害, 和月相相冲, 切忌完美主义: 如果对应的 model 存在，就不 build 了
# CreateModels(train_db)

cft = CommentsFilter(predict_db, output=False)


cft.to_feel_layer(4)
