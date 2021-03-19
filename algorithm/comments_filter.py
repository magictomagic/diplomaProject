from algorithm.train.model_generator import *
from algorithm.predict.prophet import *
from algorithm.config import *

# 如果存在，就不build了
CreateModels(train_db)

cft = CommentsFilter(predict_db, output=False)


# cft.role()
