# 毕业设计

## 功能

过滤微博垃圾评论

## 不足

+ 只适配**部分结构的网页版**
+ 第一次加载速度较慢

## 系统架构

TODO

## 爬虫&算法 逻辑

详见[流水账][5]

## 调试&运行 方法

### 前后端`任督二脉`

+ `git clone https://github.com/magictomagic/diplomaProject.git`到`Ubuntu20.04TLS`
+  到[这里][4]下载`redis`数据库文件，`systemctl stop redis`后`ps -ef | grep redis`确保无`redis`进程正在运行，`dump.rdb`覆盖掉`127.0.0.1>config get dir`路径下的同名文件
+ 在类似[这样的][1]或[这样的][2]微博页面，加载油猴脚本，加载方法见[这里][3]

### 后端到算法`任督二脉`

+ 根据`comments_filter.py`中的`import`进行各种粒度的调试

## 运行效果

### B站

<iframe src="//player.bilibili.com/player.html?aid=799928595&bvid=BV1ty4y1b7CM&cid=320279055&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

### Youtube

TODO



[1]: https://weibo.com/5594216204/K956U4wBC?type=comment
[2]: https://weibo.com/7272731818/K9wgdcrM3?type=comment
[3]: https://github.com/magictomagic/diplomaProject/tree/main/frontEnd
[4]: TODO
[5]: https://github.com/magictomagic/magictomagic.github.io/blob/master/_posts/2021-02-02-%E6%AF%95%E8%AE%BE%E8%BF%9B%E7%A8%8B.md