# coding: utf-8

import redis
from pymongo import *

configs = {
    "mongodb": {
        "crazy_bet": {
            "host": "mongodb://user:passwd@host:port/dbname",
            "maxPoolSize":100,
            "socketKeepAlive": True
        }
    },
    "redis": {
        "publish": {
            "host": "127.0.0.1",
            "port": 6379,
            "db": 8,
            "max_connections": 8
        }
    }
}

########################################
redis_pools = {}
mongodb_pools = {}

def get_redis(dbid, standalone=False):
    conf = configs['redis'][dbid].copy()
    if standalone:
        conf.pop('max_connections', None)
        return redis.Redis(**conf)
    pool = redis_pools.get(dbid)
    if not pool:
        conf.setdefault('max_connections', 8)
        pool = redis.ConnectionPool(**conf)
        redis_pools[dbid] = pool
    return redis.Redis(connection_pool=pool)

def get_mongo(dbid):
    client_pool = mongodb_pools.get(dbid)
    if not client_pool:
        client_pool = MongoClient(**configs['mongodb'][dbid])
        mongodb_pools[dbid] = client_pool
    return client_pool
