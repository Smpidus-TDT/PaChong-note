分布式系统
what分布式系统？
分布式系统就是把一些计算机通过网络连接起来，然后协同工作。

协同工作需要解决两个问题：
任务分解--
把一个问题插解成若干个独立任务，每个任务在一台节点上运行，实现多任务的并发执行；
节点通信--
节点之间互相通信，需要设计特定的通信协议来实现。协议可以采用RPC或Message Queue等方式。

eg:
scrapy_redis
消息队列
rabbitmq
scrapy_rabbitmq分布式
celery初步
--------------------------------------------------------
Redis数据库的安装
1.什么是Redis？
Redis是一个使用ANSIC编写的开源、支持网络、可选持久性的键值对存储数据库；
（默认把数据存储到内存里面）

通信，两个队列：
第一个是request队列：去存放我们所有的request调度器的队列，里面就是我们所要考虑的url；
第二个去重指纹队列：
所有的节点能对这两个队列进行共享，理论上就ok。

2.如何安装Redis？
64位
前往：https://github.com/MicrosoftArchive/redis/releases
下载Redis-x64-3.2.100.zip

安装：
resis-server --service-install redis.windows.conf --loglevel verbose

启动服务：
redis-server --service-start

scrapy_redis的安装：
pip instal scrapy_redis
------------------------------------------------------
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
  name = 'myspider'
  
  def parse(self,response):
    #do stuff
	pass
	
#改变基类
------------------------------------
scrapy_redis配置

#Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#第一个所指的配置是指你用redis作为储存，储存里面两个重要的队列；一是request队列和你的去重整合队列（你把它一配就意味着你更改了这种去重的队列）；下面这个指的是去重函数；

#Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#去重函数也改成redis进行去重，所以，这两个是一定有必要的；

#（一是它的存储的request和指纹的队列改到redis里面，二就是去重方案也就是去重函数）

ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':300
}
#这个是官方默认它也要求你配，但它并不是一定要配的。这是一个管道的配置，其实就是把你抓取到的内容，也就是item也到redis里面去储存一份。如果你配置了它就多了一个管道就多了一层，然后你的item会在redis里面再储存一次，这个不是一定有必要的；

#'json' or 'msgpack' as serializers.
#SCHEDULER_SERIALIZER = "scrapy_redis.picklocompat"
这个是指序列化的方案，就是指你的那个request。request只是一个对象，它是一个对象的话，他要存储就变成一个字符串，要么变成一个比特码。当然这个用的是一个内置库picklocompat。如果你熟悉的话也可以转成json.

#Don't cleanup redis queues,allows to pause/resame crawls.
#SCHEDULER_PERSIST = True
这个是故障重跑的配置；

#Schedule requests using a priority queue.(default)
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
优先级，就是说url的排序就是在这里做的；

#Alternative queues.
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
这三个都关于就是采用什么样的队列；

#The item pipeline serializes and stores the items in this redis key .
#REDIS_ITEMS_KEY = '%(spider)s:items'
队列的名字,可以有机会连接上可视化工具；

#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379
如果你用本地了，就是你的redis和你的爬虫是在一台机器上，那这个就不一定有必要的。它有默认的，直接连接本地；

#Specify the full Redis URL for connecting(optianal).
#If set,this takes precedence over the REDIS_HOST and REDIS_PORT settings.
#REDIS_URL = 'redis://user:pass@hostname:9001'
redis它作为一个数据库肯定是可以设置密码的，你就会用到这个方法；
--这两种方式任选其一，有覆盖作用；

#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'
这个指你是怎么去实例化你的redis，也就是由谁来产生redis这个对象；

#REDIS_ATART_URLS_AS_SET = False
指队列，redis里面的一种类型叫做set（跟我们python里面的set是一样的特性），就是不允许出现重复的元素；

#REDIS_START_URLS_KEY = '%(name)s:start_urls'
存储的键值名字是怎么的规则；

#REDIS_ENCODING = 'latinl'
是一个编码，最好不要去动它；
------------------------------------
1.运行爬虫（不会立马跑起来，由于队列已经改到redis里面了）
scrapy crawl 爬虫名
2.启动
redis-cli lpush myspider:start_urls http://google.com
第一个启动链需要我们手动塞入list，根据所选的类型去做

redis-cli sadd myspider:start_urls http://google.com
第二种set类型

--------------------------------------------------------
#重点是我们只需要替换它的继承类；
#city58_test.py
# -*- coding:utf-8 -*-
import scrapy
from pyquery import PyQuery
from items import City58Item
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider

class City58TestSpider(RedisSpider):  #修改继承
    name = 'city58_test'
	allowed_domains = ['58.com']
	start_urls = ['http://bj.58.com/chuzu']  
	
	def parse(self,response): 
	    jpy = PyQuery(response.text)
		li_;ost = jpy('body > div.mainbox > div > div.content > div.listBox > ul > li').items()  
		for it in li_list:  
		    a_tat = it('div.des > h2 > a')  
		    item = City58Item()
			item['name'] = a_tag.txt 
			item['url'] = a_tag.attr('href')
			item['price'] = it('div.listliright > div.money > b').text()  #绝对路径
			yield item
		if not li_list:
		    return
		pn = response.meta.get('pn',1)
		pn += 1
		response.meta['pn'] = pn
		if pn >5:   #不要爬的太狠哦，限制在5页
		    return
		req = response.follow('/chuzu/pn2/'.format(pn),                       callback=self.parse,
		                       meta={'pn':pn})
		yield req
		
	def error_back(self,e):
	    _ = self
		print(e)
		print('我报错了')
--------------------------------------------------------
设置配置文件settings,redis 默认端口6379；

#Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy redis.scheduler.Scheduler"

#Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#SCHEDULER_PERSIST = True
#REDIS_URL = 'redis://localhost:6379'
#REDIS_ATART_URLS_AS_SET = False
--------------------------------------------------------
启动redis：
进入安装redis目录下，
输入redis-server --service-start
--------------------------------------------------------
在main.py运行
from scrapy.cmdline import execute
execute('scrapy crawl city58_test'.split())
--------------------------------------------------------
进入安装redis目录下，
输入redis-cli lpush city58_test:start_urls http://bj.58.com/chuzu/

它不会像scrapy一样关闭的；
项目分割
--------------------------------------------------------
设置配置文件settings
REDIS_ATART_URLS_AS_SET = True
可视化工具，安装完成后启动它，进行连接；
redis默认有16个数据库；删掉之前的才可以重启跑动；


跑的时候，输入下面命令塞一个连接进入；
redis-cli sadd myspider:start_urls http://google.com

SCHEDULER_PERSIST = True 不清除；
绑定一个事件CtrlC停止才起作用；
--------------------------------------------------------
消息队列：（留言机制，request，Response）
1.在计算机科学中，消息队列（英语：Message queue)是一种进程间通信或同一进程的不同线程间的通信方式，软件的贮列用来处理一系列的输入，通常是来自用户；

2.消息队列提供了异常的通信协议，每一个贮列中的记录包含详细说明的数据，包含发生的时间，输入设备的种类，以及特定的输入参数，也就是说：消息的发送者和接收者不需要同时与消息队列交互。消息会保存在队列中，直到接收者取回它；

3.一个WIMP环境像是Microsoft Windows，借由优先的某些形式（通常是事件的时间或是重要性的顺序）来存储用户产生的事件到一个时间贮列中。系统把每个事件从时间贮列中传递给目标的应用程序。
--------------------------------------------------------
RabbitMQ消息队列
RabbitMQ是一种消息队列，用于程序间的通信。
形象地说：MQ就像一个邮局，发送者将消息写入MQ，MQ负责把消息发送给接收者。
RabbitMQ 可支持 Java，PHP，Python，Go，JavaScript，Ruby等多种语言。

模型：
生产者P经过路由器X，然后他就会分布到不同的队列里面去（amq.gen-RQ6..，amq.gen-As8...），之后供给不同的消费者去消费（C1，C2）；
整个分布式里面，我们既是生产者又是消费者，每个人都有可能会生产出url；
--------------------------------------------------------
介绍scrapy-rabbitmq-link
#Enable RabbitMQ scheduler
SCHEDULER = "scrapy_rabbitmq_link.scheduler.SaaS"

#Provide AMQP connection string
RABBITMQ_CONNCTION_PARAMETERS ='amqp://guest:guest@localhost:5672/'

#Set response status codes to requeue messages on 
SCHEDULER_REQUEUE_ON_STATUS = [500]

#Middleware acks RabbitMQ messages on success
DOWNLOADER_MIDDLEWARES ={
  'scrapy_rabbitmq_link.middleware.RabbitMQMiddleware':999
}
--------------------------------------------------------
不基于scrapy
Celery--分布式任务队列
Celery需要一个发送和接受消息的传输者。RabbitMQ和Redis中间人的消息传输支持所有特性，但也提供大量其他实验性方案的支持，包括用SQLite进行本地开发。
from celery import Celery

app = Celery('hello',broker='amqp://guest@localhost//')

@app.task
def hello():
  return 'hello world'

--------------------------------------------------------
