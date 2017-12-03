# redis

> 一款 nosql 的数据库

> 用户缓存  用户 <===> nosql <===> mysql

> mongodb 是文档存储 json存储

> redis 存储结构: key - value 键值对不能重复

## 安装：

    linus检查:

    ps ajx | grep redis

    ubuntu下安装：

    sudo apt install redis-server

    默认安装到了 /etc/redis 下

    启动服务： sudo service redis start

    重启服务： sudo service redis restart / stop

## 读写操作：

    redis 是key-value的数据

    键的类型是字符串

    值的类型分为5种：

        字符串 string

        哈希 hash

        列表 list

        集合 set

        有序集合 zset

## 常用操作命令：

    string 是redis最基本的类型

    最大存储512MB数据

    设置键值：

        redis-cli 进行连接redis数据库

        set 'py3' 'hello'

        get 'py3'

        mget 获取多个值

        exists 'aa' 存在返回1 ，不存在返回0

        type key 判断值得类型

        del key 删除某个键、值

        keys * 查看所有键

        expire key seconds  expire 'pp' 10  10s后自动清除

## redis 使用密码登陆：

      auth mypassword

## hash：

  hset key name value

  type key : hash

  hget key name 获取某个键的某个属性

  hgetall key 返回奇数都是属性，偶数都是值

  hkeys key  获取所有的属性

  hvals key 获取所有的值

## list：

## set 无序

## zset 有序 权重


---

## 发布订阅： 设计模式

    消息推送

    不需要客户端请求服务器

    redis内部实现了发布订阅

    只需要客户端订阅即可！

    消息的格式：

      subscribe pingdaoname 订阅

      publish pingdaoname xiaoxi 推送

## 主从：

  在从服务器中的redis的配置文件改： /etc/redis/redis.conf

    1. 注释 bind ip
    2. 加 slaveof 主 ip （slaveof 奴隶 ）

  主从，自动完成备份

## 与python交互：

    安装redis包

    pip install redis

    两种操作方式：

    1. 直接连接数据库

    2. pipline 先写到管道里，最后操作一次execute，不用频繁操作db
