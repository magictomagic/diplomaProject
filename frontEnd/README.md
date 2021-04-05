# 调试 

## 环境

+ Ubuntu20.04TLS
+ Chrome

## Config

+ 插件管理，允许油猴读取本地文件。
+ 新建一个脚本文件，路径参考下面，填`diplomaProject.js`对应的路径。

```js
// ==UserScript==
// @name         diplomaProject
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://weibo.com/*
// @grant        GM_xmlhttpRequest
// @require      https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js
// @require      file:////home/magic/Desktop/dp/diplomaProject/frontEnd/diplomaProject.js
// ==/UserScript==

```

