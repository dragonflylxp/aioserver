#coding:utf-8
import os
import sys
import imp
import traceback
import asyncio
from aiohttp import web
import re

loop = asyncio.get_event_loop()
app  = web.Application(loop=loop)

"""初始化http server"""
async def init_svr(host,port):
    svr = await loop.create_server(app.make_handler(),host,port)
    print('Server started at http://{}:{}...'.format(host,str(port)))
    return svr

"""启动事件循环"""
def start(host='0.0.0.0',port=None):
    try:
        loop.run_until_complete(init_svr(host,port))
        loop.run_forever()
    except:
        print(traceback.format_exc())
    finally:
        loop.stop()

"""加载业务:
    1.添加task类型job
    2.注册http类型route
"""
def load_biz_dir(dir_path):
    for fname in os.listdir(dir_path):
        if fname[-3:] != '.py':
            continue
        fpath = os.path.join(dir_path, fname)
        if not os.path.isfile(fpath):
            continue
        imp.load_source('_biz_' + fname[:-3], fpath)

"""任务管理"""
class Task(object):
    _tasks = []

    @classmethod
    def add_asyncio_task(cls, func):
        loop = asyncio.get_event_loop()
        Task._tasks.append(asyncio.ensure_future(func(loop)))
        return func

    @classmethod
    def get_asyncio_tasks(cls):
        return Task._tasks

"""注册route"""
class Router(object):
    @classmethod
    def route(cls, **kwargs):
        def deco(func):
            url = kwargs.get('url') or '/'
            if not url.startswith('/'): url = '/'+url
            methods = kwargs.get('methods') or ('GET',)
            methods = ('*',) if '*' in methods else methods
            for method in methods:
                app.router.add_route(method,url,func)
            return func
        return deco
