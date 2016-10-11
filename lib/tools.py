#coding=utf-8

import logging
import logging.config
import traceback
import time
import asyncio
import aiohttp

class Log():
    logger = None

    @classmethod
    def set_up(cls, log_cnf):
        logging.config.fileConfig(log_cnf['config_file'])
        Log.logger = logging.getLogger(log_cnf['default_logger'])

    def getLog(self):
        if Log.logger == None:
            Log.logger = logging.getLogger('simple')
        return Log.logger


class AIOHttpClient:
    """异步http客户端"""

    @staticmethod
    async def post(loop, url, params=None, timeout=8):
        try:
            t1 = time.time()
            with aiohttp.ClientSession() as session:
                with aiohttp.Timeout(timeout, loop=loop):
                    async with session.post(url, data=params) as resp:
                        assert resp.status == 200
                        json = await resp.json()
            t2 = time.time()
            Log().getLog().info("url=%s|spendTime=%s", url, (t2 - t1))
            return json
        except:
            Log().getLog().exception("==== url[%s] ====", url)
            raise
        finally:
            pass

    @staticmethod
    async def get(loop, url,timeout=8):
        pass
