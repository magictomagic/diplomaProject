import sys
# sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser


# 关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径

def what_fuck(content):
    USAGE = "usage:    python extract_tags_stop_words.py [file name] -k [top k]"

    parser = OptionParser(USAGE)
    parser.add_option("-k", dest="topK")
    parser.add_option("-w", dest="withWeight")
    opt, args = parser.parse_args()

    if opt.topK is None:
        topK = 10
    else:
        topK = int(opt.topK)

    if opt.withWeight is None:
        withWeight = False
    else:
        if int(opt.withWeight) is 1:
            withWeight = True
        else:
            withWeight = False

    jieba.analyse.set_stop_words("stopWords.txt")
    jieba.analyse.set_idf_path("idf.txt.big")

    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)
    if withWeight is True:
        for tag in tags:
            print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
    else:
        print(",".join(tags))  # 然后把重复出现三次及以上的词加到 idf.txt.big 中（遍历去重）


if __name__=='__main__':
    what_fuck("蔡徐坤妈卖批")