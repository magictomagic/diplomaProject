from train.model_generator import *
from predict.prophet import *
from config import *

# 如果存在，就不build了
# CreateModels(train_db)

cft = CommentsFilter(predict_db)
cft.role()
