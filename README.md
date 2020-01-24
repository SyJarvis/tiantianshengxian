# 天天生鲜网站

一个生鲜网站



## 一、开发环境

1. ubuntu18.04
2. python:3.6.8
3. django:1.8.2
4. pycharm



### 二、项目模块列表

1. 用户模块
2. 商品模块
3. 订单模块
4. 购物车模块



### 三、项目所需服务列表

1. mysql

   ​	用来存储用户信息、商品信息以及订单信息

2. redis

   ​	内存型数据库，主要充当数据缓存，用来存储session、用户购物车的商品id等

3. FastDFS

   ​	文件存储服务，用来存储图片文件，然后在mysql数据库里存储文件的url地址

4. nginx

   ​	web服务器，常用来做负载均衡，充当指挥使。

5. celery

   ​	异步处理的任务队列，用来异步处理邮件发送。

6. uwsgi

   ​	本项目中用来实现后台运行程序。



### 四、说明：

1. 前端的页面文件也已经打包好了，如果是新手的话，请使用下面这个命令来安装所需依赖包。

```
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
```

2. fast_client这个模块我已经放在依赖这个文件夹下了，你可以自己解压文件来安装，使用这个命令

```
pip install setup.py install
```

或者把fdfs_client这个文件夹复制到你的开发环境的site-packages目录下，然后就可以导入了。

3. 有任何问题可以加我微信，欢迎跟我说，不是咨询，只是想认识更多志同道合的人，一起学习，大家加油。
