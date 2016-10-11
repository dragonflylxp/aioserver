#coding:utf-8
import time
import traceback
import asyncio
from tools import AIOHttpClient
from core import *

@Task.add_asyncio_task
async def fetch_urls(loop):
    while True:
        t1 = time.time()
        try:
            urls = ['www.baidu.com','www.sina.com','www.sohu.com']
            futures = []
            for url in urls:
                futures.append(asyncio.ensure_future(do_fetch(loop,url)))
            done,pending = await asyncio.wait(futures, return_when=asyncio.ALL_COMPLETED)
            if pending:
                print('Warning: some urls fail to fetch!')
        except:
            print(traceback.format_exc())
        t2 = time.time()
        print('Fetch urls ucess! cost:'+str(t2-t1)+'(sec)|sleep:1(min)...')
        await asyncio.sleep(60)

async def do_fetch(loop, url):
    resp = await AIOHttpClient.post(loop, url)
    if resp.get('status') != 200:
        print('Fetch url failed! url:',url)
