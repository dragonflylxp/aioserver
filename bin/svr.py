#coding:utf-8
import os
import sys
import signal
import path
import core

signal.signal(signal.SIGTERM, lambda signo,frame:asyncio.get_event_loop().stop())
if __name__ == '__main__':
    core.load_biz_dir(path._BIZ_PATH)
    core.start(host='127.0.0.1',port=7788)
