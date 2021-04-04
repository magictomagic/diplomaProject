import os
import sys
loc = os.path.dirname(os.path.abspath(__file__))
loc = os.path.dirname(loc)
sys.path.append(loc)
from algorithm.predict.prophet import *
from algorithm.config import *
# import platform

raw_data = sys.argv[1]
# print("raw_data")
# sys.stdout.flush()
# raw_data = '{"4621646571244256":"抱抱你 韬韬不哭@YKYBtao-黄子韬 ¡评论配图","4621647769764439":"抱抱宝贝@YKYBtao-黄子韬 别哭，我一直在，一直陪伴你 ¡评论配图","4621647221622425":"宝贝你是我们的骄傲加油","4621647401189567":"韬韬加油你和韬妈真的很坚强","4621701683874254":"在🍉视频看了独家，黄子韬加油","4621669035415706":"韬爸虽然刚开始不支持韬做这一行，但是在韬韬的坚持下同意韬韬去韩国，韬以前在路边发传单，韬爸就开着车偷偷跟着一直到韬上公交车才放心，害怕韬遇到庸医就自己去学医，韬爸也一直支持韬的事业，韬回国后和韬一起开了经纪公司，是一位非常伟大的父亲，韬韬一定","4621648537326439":"抱抱韬韬 海浪一直在@YKYBtao-黄子韬","4621647846051537":"抱抱你韬爸一定会以你为荣要坚强@YKYBtao-黄子韬","4621702602949786":"在西瓜視頻看了独家，有点难受","4621702174345361":"希望我们好好对自己的亲人，从🍉视频过来的","4621704179746847":"🍉视频的独家看了更难受","4621701939464478":"🍉视频刷到的，果然上热搜了","4621648168227517":"宝贝我们陪你@YKYBtao-黄子韬","4621649142613084":"黄子韬加油海浪一直在","4621648202042171":"抱抱哥哥","4621648906422339":"韬韬不哭","4621648692774601":"心疼黄子韬，海浪永远陪着你","4621648278588039":"韬韬我们不哭@YKYBtao-黄子韬 ¡评论配图","4621647958514221":"看黄子韬哭我也好难过","4621646218397561":"韬韬不哭","4621649435170526":"心疼韬韬，给韬韬擦眼泪","4621653557904829":"抱抱你韬爸一定会以你为荣要坚强@YKYBtao-黄子韬","4621679047213115":"真的能感同身受 我爸爸不在守护我已经21天了 这21天我每天都是浑浑噩噩 妈妈更是 我不敢当着妈妈的面哭 真的很难过 那种感觉真的只有经历过才能感同身受 不是粉 是纯路人 但是想说 加油 要和妈妈保重身体  要好好的 天堂的父亲看到好好的","4621655488070322":"#黄子韬我愿意用十年换父亲一年# 宝贝，你很好@YKYBtao-黄子韬","4621649905193922":"抱抱，你很坚强，加油我陪你@YKYBtao-黄子韬","4621655198669210":"宝贝我们陪你@YKYBtao-黄子韬 ¡评论配图","4621652442483134":"抱抱韬韬，不哭，韬爸会用另一种方式一直守护着你","4621651540709756":"抱抱宝贝，你是我们的骄傲@YKYBtao-黄子韬"}'
raw_json = json.loads(raw_data)
# print(raw_json)
user_id = '666'
url_id = '666'
comment_emoji = '666'
nickname = '666'
like_count = '666'
reply_count = '666'
be_co_retweet = '666'
be_co_comments = '666'
be_co_like = '666'
author = '666'
be_contents = '666'
be_emoji = '666'
obj = {}
for key, value in raw_json.items():
    str_key = '|'.join([key, user_id, url_id])
    obj_value = {
        'comment_text': '|'.join(value.split(',')),
        'comment_emoji': comment_emoji,
        'nickname': nickname,
        'like_count': like_count,
        'reply_count': reply_count,
        'be_co_retweet': be_co_retweet,
        'be_co_comments': be_co_comments,
        'be_co_like': be_co_like,
        'author': author,
        'be_contents': be_contents,
        'be_emoji': be_emoji
    }
    str_value = json.dumps(obj_value)
    obj[str_key] = str_value
    # print(str_key)
    # print(str_value)

# print(obj)
cft = CommentsFilter(obj, output=False, test=False)
res = cft.persist_storage()
print(json.dumps(res))
# aa = r.hgetall('tmp1')
# for key, value in aa.items():
#     aa = json.loads(value)
#     print(aa)
# print(fake_json)


# print data here  to send back
# print(raw_data)
# sys.stdout.flush()
