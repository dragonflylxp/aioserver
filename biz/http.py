#coding:utf-8
import time
import traceback
import asyncio
import ujson
from core import *

def response(data={}):
    body = ujson.dumps({"status":200, "message":"sucess","data":data})
    return web.Response(body=body.encode(),content_type='application/json',charset='utf-8')

@Router.route(url=r"hello/world", methods=('GET','POST'))
async def hello_world(req):
    data = await req.json()
    return response(data)
