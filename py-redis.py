# coding=utf8

from redis import *

redis_config = {
    "host": "192.168.1.104",
    "port": 6379
}

r = StrictRedis(redis_config)

# 写到pipe管道
# pipe = r.pipeline()
#
# # 只是保存到本地内存中
# pipe.set('pip10','hello1')
# pipe.set('pip11','world')
#
# pipe.execute()

# 读取
res = r.get('py-db')
print res
