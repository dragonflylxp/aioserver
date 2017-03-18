# aioserver

Overview
------------
* 集成aiohttp server和client的asyncio框架
```shell
  /aioserver
     |-/bin
     |   |-path.py #路径配置
     |   |-svr.py  #框架入口，载入业务代码，启动事件循环
     |-/biz
     |   |-http.py #http请求demo
     |   |-task.py #任务job demo
     |-/lib
     |   |-core.py #框架代码：注册http route/添加task job/服务启动
     |   |-tools.py #工具： logger/aiohttp-client
     |   |-db_pool.py #数据库连接池：redis/mognodb
     |   |-mongodao.py#mongodb dao
```
Requirements
------------

* Python3.4+ (asyncio supported)
* Work on Linux


