[TOC]

## 方向的选择
[在现实情况中，异常检测问题往往是没有标签的，训练数据中并未标出哪些是异常点，因此必须使用无监督学习][2]。因此，接下来的讨论主要放在无监督学习上。

## Tools
### SKlearn
[scikit-learn，又写作sklearn，是一个开源的基于python语言的机器学习工具包。它通过NumPy, SciPy和Matplotlib等python数值计算的库实现高效的算法应用，并且涵盖了几乎所有主流机器学习算法][1]。sklearn 中常用的模块有分类、回归、聚类、降维、模型选择、预处理。研究需要用到的模块主要是聚类，即：将相似对象自动分组。常用的算法有：k-Means、 spectral clustering、mean-shift，常见的应用有：客户细分，分组实验结果。
### Anaconda
Anaconda 提供 scikit-learn 作为其免费发行的一部分。
### PyOD
[PyOD is a comprehensive and scalable Python toolkit for detecting outlying objects in multivariate data.][3]



[1]: https://www.itread01.com/content/1551725786.html
[2]: https://www.zhihu.com/question/280696035
[3]: https://pyod.readthedocs.io/en/latest/