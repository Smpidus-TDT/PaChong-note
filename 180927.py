'''
今日头条--爬虫
爬虫的知识体系：
1.前端html,css,js，浏览器相关知识；
2.各种数据库的运用；
3.http协议的了解；
4.对于前后台联动的方案；

Scrapy Engine（引擎） SCHDULER（调度器） DOWNLOADER（下载器）
Spiders(蜘蛛)

http://www.lfd,uci.edu/~gohlke/pythonlibs/
windows-scrapy依赖包
pip install scrapy

scrapy startproject 
hello_world
windows切盘
'''
------------------
'''
>scrapy startproject city_58
>cd city_58
>scrapy genspider spider_city_58 58.com  #58.com 主域名

重写start_requests()时候，注意start_urls属性会不会启动；
__init__.py 中start_requests
for url in self.start_urls:
    yield self.make_requests_rom_url(url)
启动链之所以是启动链，because它在startrequst的时候，就是调用了它里面的url构建第一个request，so它在这启动but一旦你把它重写了，and你没有手动地把这个东西给它加上去，你的startrequest里面的url不会被调用。

'''
from scrapy import cmdline
cmdline.execute('Scrapy crawl spider_city_58'.split())
['Scrapy','crawl','spider_city_58']

------------------
'''
常用的选择器
1.BeautifulSoup lxml
2.css xpath re
3.pyquery
----------------------------------------------------------------
css(query)
应用给定的CSS选择器，返回SelecterList的一个实例
query是一个包含CSS选择器的字符串
在后台，通过cssselect库和.xpath()方法，CSS查询会被转换为Xpath查询
注解：为了方便起见，该方法也可以通过response.css()调用
----------------------------------------------------------------
CSS3选择器
选择器           例子      例子描述
.class           .intro    选择class="intro"的所有元素。
#id              #firstname  选择id="firstname"的所有元素。
*                *         选择所有元素。
element          p         选择所有<p>元素。
element,element  div,p     选择所有<div>元素和所有<p>元素。
element element  div p     选择<div>元素内部的所有<p>元素。
element>element  div>p     选择父元素为<div>元素的所有<p>元素。
----------------------------------------------------------------
HTML是成对出现的，也有单个出现的；
HTML标签；
----------------------------------------------------------------
Xpath的使用方法
选取节点
Xpath使用路径表达式在XML文档中选取节点。节点是通过沿着路径或者step来选取的。
下面列出了最有用的路径表达式：
表达式    描述
nodename  选取此节点的所有子节点
/         从根节点选取
//        从匹配选择的当前节点选择文档中的节点，而不考虑他们的位置。
.         选取当前的节点
..        选取当前节点的父节点。
@         选择属性。
----------------------------------------------------------------
pyquery,对异常做了处理
'''
----------------------------------------------------------------
#code:utf8
from scrapy import Selector
from pyquery import PyQuery
with open('index.html',encoding='utf-8') as f:
    text = f.read()
print(text)

#sel = Selector(text=text)
jpy = PyQuery(text)

items = jpy('li')
for i in items.items():
    print(i.attr('class'))

----------------------------------------------------------------
'''
Item管道（Item Pipeline）
主要负责处理由蜘蛛从网页中抽取Item，主要任务是清洗、验证和存储数据。
当页面被蜘蛛解析后，将被发送到Item管道，并经过几个特定（就像滤网一样，可以是一个也可以是很多张）的次序处理数据。
每个Item管道的组件都是有一个简单的方法组成的Python类。
它们获取了Item并执行它们的方法，同事还需要确定是否需要在Item管道中继续执行下一步或是直接丢弃掉不处理。

Item管道作用：数据校验，数据去重，数据存储，清洗html。
去重最好在url阶段，链接的阶段；
清洗html，可以做各种各样的清洗；
------------------------------------------
Item管道主要函数（每个管道就是一个类）：
process_item(self,item,spider)--------必须实现（也是用的最多的方法）；
open_spider(self,spider)-------非必需，为爬虫启动的时候调用；
close_spider(self,spider)------非必需，为爬虫关闭的时候调用；
from_crawler(cls,crawler)------非必需，也是在启动的时候调用，比open_spider早。
'''
----------------------------------------------------------------
#价格，需不需要计算增值税
#管道的基础利用
>process_item(self,item,spider)

from scrapy.exceptions import DropItem
class PricePipeline(object):
    vat_factor = 1.15
	def process_item(self,item,spider)
	    if item['price']:
		    if item['pric_excludes_vat']:
			    item['price'] = item['price'] * self.vat_factor  #判断是否加入增值税*...
			return item  #要传到下一个，必须进行return
		else:
		    raise DropItem('Missing price in %s' % item) #如何不存在这个价格，直接抛出异常
#注意：要么抛异常，要么返回item
----------------------------------------------------------------
#管道里过滤数据(比上面高级一点，多了一个set)
from scrapy.exceptions import DropItem
class DuplicatesPipeline(object):
    def __init__(self):
	    self.ids_seen = set()
	def process_item(self,item,spider):
	    if item['id'] in self.ids_seen：#找到了就抛出
		    raise DropItem("Duplicate item found:%s" % item)
		else:
		    self.ids_seen.add(item['id'])
			return item  #return就到了下一个管道

----------------------------------------------------------------
#实战举例---将数据写入文件
>open_spider(self,spider)
>close_spider(self,spider)

import json
class JsonWriterPipeline(object):
    def open_spider(self,spider):   #启动时  打开文件
	  self.file = open('items.jl','w')
	  
	def close_spider(self,spider):   #关闭时  关闭文件
	  self.file.close()
	  
	def process_item(self,item,spider):  #管道进行序列号json.dumps（把它变成一个字符串写到文件中去）
	  line = json.dumps(dict(item))+"\n"
	  self.file.write(line)
	  return item
----------------------------------------------------------------
#把mongo做进去了
>from_crawler(cls,crawler)
import pymongo

class MongoPipeline(object):
    collection_name = 'scrapy_items'
	def __init__(self,mongo_uri,mongo_db): #赋值两个属性
	  self.mongo_uri = mongo_uri
	  self.mongo_db  = mongo_db
	  
	  @classmethod
	    def from_crawler(cls,crawler):
		  return cls(
		    mongo_uri=crawler.settings.get('MONGO_URI'),
			mongo_db=crawler.settings.get('MONGO_DATABASE','items')
		  )
----------------------------------------------------------------
#就是在mongodb中插入了一条数据
>from_crawler(cls,crawler)

 def open_spider(self,spider):  #爬虫打开数据库
   self.client = pymongo.MongoClient(self.mongo_uri)
   self.db = self.client[self.mongo_db]
   
def close_spider(self,spider):  #完成时关闭数据库
    self.client.close()
	
def process_item(self,item,spider):  #管道的时候，做了一个操作insert_one插入一条数据
    self.db[self.collection_name].insert_one(dict(item))
	return item
----------------------------------------------------------------
'''
创建项目scrapy startproject city58
创建爬虫 scrapy genspider city58_test 58.com
注：项目名一定不能喝爬虫名重复，  58.com主域名(只能生成这个域名下的信息)
'''
#city58_test.py
# -*- coding:utf-8 -*-
import scrapy
from pyquery import PyQuery
from items import City58Item

class City58TestSpider(scrapy.Spiders):
    name = 'city58_test'
	allowed_domains = ['58.com']
	start_urls = ['http://bj.58.com/chuzu']  #启动链
	
	def parse(self,response): #启动链，然后就直接会回调默认回调这个解析器
	    jpy = PyQuery(response.text)
		li_;ost = jpy('body > div.mainbox > div > div.content > div.listBox > ul > li').items()  #拿到了所有的li标签
#需要遍历（每个li标签）成一个自动帮你封装成一个PyQuery对象，需要调用到方法.items()
		for it in li_list:  #it就是li一个整体
		    a_tat = it('div.des > h2 > a')  #第一步，拿到a标签
		    item = City58Item()
			item['name'] = a_tag.txt #name就是a标签的text属性tag.text()
			item['url'] = a_tag.attr('href')
			item['price'] = it('div.listliright > div.money > b').text()  #绝对路径
			yield item #yield它可以不结束这个函数，返回一系列的值（return只能取掉这个list的第一条数据）
			#进入到item管道，pipeline.py
			
		
		
'''
copy>>Copy Selector
body > div.mainbox > div > div.content > div.listBox > ul > li:nth-child(1)
--nth-child(1)相当于python里面切片，选中某一个li,因为它是一系列的；
如果需要所有的，就需要将后面nth-child(1)取掉；

非常精准的绝对路径；
<a href   就是a标签的Herf属性

yield item 就是yield到管道；yield request就是把它yield到调度器里面去；
'''
----------------------------------------------------------------
#items.py
import scrapy

class City58Item(scrapy.Item):
    #define the fields for you item here like:
	name = scrapy.Field()  #三个字段的定义
	price = scrapy.Field()
	url = scrapy.Field()
----------------------------------------------------------------
#pipeline.py
import json

class City58Pipeline(object):
    
	def open_spider(self,spider):
	    self.file = open('58_chuzu.txt','w',encoding='utf-8')
		print('打开文件了')
	def process_item(self,item_spider):
	    line = '{}\n'.format(json.dumps(dict(item))  #字符串，写到文件里是吧先用个东西把它承接一下,进行换行
		self.file.write(line)  #写到文件中
	    return item
		
	def close_spider(self,spider):
	    self.file.close()
		print('关闭文件了')

----------------------------------------------------------------
'''
settings.py   写完pipeline.py管道，激活管道(一些列)，按后面300数字进行排列
'''
TIEM_PIPELINES ={
    'city58.pipelines.City58Pipeline':300,
}
----------------------------------------------------------------
#新建文件main.py
from scrapy.cmdline import execute
execute('scrapy crawl city58_test'.split())

----------------------------------------------------------------
'''
中间件(Middlewares):下载中间件(Downloader Middlewares)和蜘蛛中间件（Spider Middlewares);
最重要的思想就是：拦截；
下载中间件：拦截request和response的；
--它是在最外围，request通过下载中间件直接去下载，是一个很关键的出口（出口之前）；
蜘蛛中间件：拦截（三个部分）response 、request 和items；
======================================
相同点：都是拦截；
不同点：拦截的东西不一样，拦截的位置不同。
======================================
反爬策略在下载中间里面做什么？挂代理，挂cookie，挂User-Agent等；
Spider是对response request的一些做一些校验像这样的奇怪工作；
========================

下载中间件三大函数：
process_request(request,spider)
process_response(request,response,spider)
process_exception(request,exception,spider)
强调它是处理process_request抛出的异常；

1.process_request(request,spider)主要函数
返回值（只有四种情况）：
返回None      ------默认None
返回request    -----就是把它重新放回了调度器里面放回了队列里面（跟yield item),就相当于重试，它也不会再调用后面的哪些中间件里面的process_request,;
返回response        -----代表着你伪造了一个response；
raises IgnoreRequest   -----抛出异常；
--挂代理，挂cookie，挂User-Agent等；就在这个函数里；
例如：你要去体检，
你进去了直接体检返回None；
你排队到了却忘记带学生证，回去取再来排队，返回request；
你进入后未体检，医生给你个假证明，你就走了，返回response；
你去了直接没让你进医院就直接让你走了，返回raise IgnoreRequest;

2.process_response(request,response,spider)主要函数
返回值：
返回response   ---传递了这个response
返回request    ---被重新退回队列准备重新去访问，相当于回炉重造，就是下载下来了却发现跟你想要的不一样，然后你就让它重新去请求这个url，
raise IgnoreRequest  ---抛出异常；强调一点，截止操作就是一个request对应一个response，所以你忽略了它的request理论上讲它当然要忽略它的response，这两个函数之所以都统一用这个方法做忽略，就是这个原因。
忽略了它最重要的一个点就是拦截到你忽略它的这个中间件为止，后面的中间件不会再去拦截它。如果你这一次一忽略后面的中间件被拦截了，它也到不了爬虫里面，也就是后面的过程就全部没有了；


3.process_exception(request,exception,spider)主要函数
返回值：
返回None   ---就是没有处理；
返回response   --没有处理传到下一个中间里的process_exception处理，如果返回response，就相当于被纠正了。因为你在process_exception里是为了去拿回一个response，这个时候process_exception放回了一个response，就相当于错误被纠正了。拿到了正确的response，其实就又回到了刚刚从下载器下载一个数据，然后穿过所有的Process_response.没有返回response时，就会回调所有中间里面的process_response,也就是它就认为你这个错误被纠正了，然后纠正了之后返回正常的（response），就跟正常的通过其余中间件一样的。返回request就比较惨了，这就又是回炉重造这个过程；
返回request   ---就是又被寄回队列准备重新请求。

---exception就是异常（所听到的各种报错），这个异常在逻辑上依然是拦截的那个概念；
它拦截的就是process——request，第一个函数；
如果发现了异常，就会被所有的中间件的这个函数process_exception拦截，一层层拦一直到有人处理了这个异常；

ua标识请求我的这个人是什么终端
random随机数

Ctrl+变蓝就可以直接跳转查看；
重置中间件import scrapy.downloadermiddlewares.retry
重试
'''
#middleware.py

from scrapy import signals
from random
import scrapy.downloadermiddlewares.retry


class UAMiddleware(object):

    ua_list =[
	    'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36',
		'(KHTML,like Gecko) Chrome/62.0.3202.94 Safari/537.36',
		'Mozilla/5.0 (Compatible:Baiduspider/2.0: +http://www.baidu.com/search/spider.html)',
		'Mozilla/5.0 (Compatible:MSIE 9.0:Windows NT 6.1:Trident/5.0)',
		'Mozilla/5.0 (Compatible:Googlebot/2.1: +http://www.google.com/bot.html)',
		'Mozilla/5.0 (Compatible:bingbot/2.0: +http://www.bing.com/bingbot.html)',
	]

	#第一个壳
    def process_request(self,request,spider):
	    ua = random.choices(self.ua_list)
		request.headers['User-Agent'] = ua
		print(request.url)
		print(request.headers['User-Agent'])
	
	#第2个壳
	def process_response(self,request,response,spider):
	    return response
		
	#第3个壳
	def process_exception(self,request,exception,spider):
	    pass
----------------------------------------------------------------
#city58_test.py
# -*- coding:utf-8 -*-
import scrapy
from pyquery import PyQuery
from items import City58Item

class City58TestSpider(scrapy.Spiders):
    name = 'city58_test'
	allowed_domains = ['58.com']
	start_urls = ['http://bj.58.com/chuzu'，
	              'http://bj.58.com/chuzu/pn2/']  #至少访问两个链接
	
	def parse(self,response): #启动链，然后就直接会回调默认回调这个解析器
	    jpy = PyQuery(response.text)
		li_;ost = jpy('body > div.mainbox > div > div.content > div.listBox > ul > li').items()  #拿到了所有的li标签
#需要遍历（每个li标签）成一个自动帮你封装成一个PyQuery对象，需要调用到方法.items()
		for it in li_list:  #it就是li一个整体
		    a_tat = it('div.des > h2 > a')  #第一步，拿到a标签
		    item = City58Item()
			item['name'] = a_tag.txt #name就是a标签的text属性tag.text()
			item['url'] = a_tag.attr('href')
			item['price'] = it('div.listliright > div.money > b').text()  #绝对路径
			yield item #yield它可以不结束这个函数，返回一系列的值（return只能取掉这个list的第一条数据）
			#进入到item管道，pipeline.py
----------------------------------------------------------------
'''
settings.py
#ROBOTSTXT_OBEY = True		将这个关闭，True修改为False，协议不需要反而缠上干扰；
然后激活中间件

DOWNLOADER_MIDDLEARES = {
    'city58.middleware.MyCustomDownloaderMiddleware':543,
}
名字修改（跟管道的配置一样，数字就是一系列中间件的排序）
DOWNLOADER_MIDDLEARES = {
    'city58.middleware.UAMiddleware':543,
}

中间件远比管道复杂，因为它本身有大量的内置中间件；
这种内置中间件它也有排序，然后你自己在自定义级别也有排序；
这样就会导致你的排序跟系统内置的一些排序，可能会导致一些很奇怪的问题；
后面数字越小，代表它越远离下载器；数字越大越靠近下载器；
也就是数字越小的request就越想通过；
request就是出去的是最先通过的如果数字越小，那数字越小就相应的response越往后面通过；
response编号越大的时候，它就越先通过编号大的中间件；
scrapy本身的内置中间件的排序是什么样子？？？
然后合理安排这个顺序；
书序不一样是影响特别大；

通过main.py跑一编
from scrapy.cmdline import execute
execute('scrapy crawl city58_test'.split())

>>>这个是翻页，会比上一次的数据过多；
----------------------------------------------------------------
CookiesMiddleware
class scrapy.downloadermiddlewares.cookies.CookiesMiddleware
该中间件使得爬取需要cookie（例如使用session）的网站成为了可能。其追踪了webserver发送的cookie，并在之后的request中发送回去，就如浏览器所做的那样。
以下设置可以用来配置cookie中间件：
COOKIES_ENABLED
COOKIES_DEBUG

单spider多cookie session
Scrapy通过使用cookiejar Request meta key 来支持单spider追踪多cookie session。默认情况下其使用一个cookie jar（session），不过您可以传递一个标识符来使用多个。

例如：
for i,url in enumerate(urls):
  yield  scrapy.Request("http://www.example.com",meta={'cookiejar':i}),
    callback=self.parse_page)
================================	
#session是代表一个会话；
会话就是你点开一个浏览器，比如你进入淘宝，搜一个东西后打开一个淘宝。对淘宝来讲你这三个页面，也就是首页、搜索页和商品页这三个页面加起来，叫session。也就是说它是整个网页整个过程里面，所有的页面加起来那东西叫session，而这个session通常情况下就是用cookie进行标识的，所以就得存在一个问题，大家可以想象一下如果你打开了cookie管理，然后它又是通过cookie来标识，你是否是同一个session的时候，又会出现什么情况出现你其中的一个爬虫，然后你抓了成千上万的数据，而你所有的数据都是从一个session里面拿的，大家觉得有没有问题？？？这不明摆着让服务器识别出来嘛。怎么可能有一个人用一个session用一个会话用一台电脑，就拿我很多很多数据呢？？？这一看就是爬虫的行为。
所以为了更真实理论上讲，我们应该用多session，就是说就像是真的是有不同的人，打开了这个网页而且通过不同的session。
有很多方法首先你要改变自己的ip，二你要是模拟多种session。
那怎么模拟多种session？？？
就是在你发送你yield出现这个request的时候，做一个配置，它有一个配置叫做cookiejar（就是做一个标识它并不需要你），有一个很特别的东西，随便传个东西给你可以随便传个数字。
在上方的例子里面其实就是随便传了一个数字，因为像它是你把一个list外面套一个这个东西enumerate(urls)，就其实是把它的索引和它的元素一起取出来了，然后把它设置成一个数字，这个数字代表的就是某一个session，如果你还有链接用了同一个数字，比如说这个是2，你这个meta=2，就是这个jar等于2，如果你又yield一个链接，然后把这个cookiejar也设置成2，scrapy它的内部就认为它们两应该是同一个session。
当然你也可以让它每一个页面，都有不同的session，你可以随机生成数字，然后把它的这个cookiejar设置的都不一样。所以你要根据自己的需求去选择是否启用多session模式。


================================
需要注意的是cookiejar meta key不是“黏性的（sticky）。您需要在之后的request请求中接着传递。

例如：
def parse_page(self,response):
  #do some processing
  return scrapy.Request("http://www.example.com/otherpage",
    meta={'cookiejar':response.meta['cookiejar]},
	callback=self.parse_other_page)
	
--黏性的，你要对每一个你yield出来的request做控制，它是不能往下延续着往下传递的，也就是说比如你yield一个request，然后回调到了一个函数。这个函数在yield一个数据出来，你必须依然手动的去设置这个cookiejar，去指定它用哪个session。

-------------------------------------------------------
request对象叫请求对象（就是出去的那个对象）；
response对象是由你的request对象换回来的（你向服务器发送一个request，响应了你然后它就返回一个response的相应对象给你）；
所以他们是成对出现的，出现一个热切托肯定会出现一个response（你去服务器里面请求了一下，它请求完后又返回一个响应给你）。

Request对象

基础参数
url   请求的url
callback   请求回来的response处理函数
meta   用来在“页面”之间传递数据
headers   页面的headers数据
cookie   设置页面的cookies

基础高级参数
encoding   请求的转换编码
priority   链接优先级
dont_filter   强制不过滤
errback   错误回调

对象方法
copy()   复制一个一模一样的对象
replace():对对象参数进行替换

Request.meta一些特殊的keys
dont_redirect  不转跳
dont_retry     不重置
handle_httpstatus_list
handle_httpstatus_all
dont_merge_cookies(see cookies parameter of Request)
cookiejar
dont_cache
redirect_urls
bindaddress
dont_obey_robotstxt

download_timeout    超时
download_maxsize
download_latency
download_fail_on_dataloss
proxy
ftp_user(See FTP_USER for more info)
ftp_password(See FTP_PASSWORD for more info)
referrer_policy
max_retry_times
--------------------------------
Response对象
基础参数
url   请求的url
body   请求回来的html
meta   用来在“页面”之间传递数据
headers   页面的headers数据
cookie   设置页面的cookies
Request   发出这个response的request对象

对象方法
copy()   复制一个一模一样的对象
replace():对对象参数进行替换
urljoin()   将页面相对路径传入，返回绝对路径
follow()   传入一个相对路径直接返回一个request对象
--------------------------------
Response对象方法的综合利用
import scrapy
class QuotesSpider(scrapy.Spider):
  name = "quotes"
  start_urls =[
    'http://quotes.toscrape.com/page/1/',
  ]
  def parse(self,response):
    for quote in response.css('div.quote')
	  yield{
	    'text':quote.css('span.text::text').extract_first(),
		'author':quote.css('small.author::text').extract_first(),
		'tags':quote.css('div.tags a.tag::text').extract(),
	  }
	  #翻页，是否为空，本身是相对路径，返回回来就是绝对路径
	  next_page = response.css('li.next a::attr(href)').extract_first()
	  if next_page is not None:
	    next_page = response.urljoin(next_page)
		yield scrapy.Request(next_page,callback=self.parse)
--------------------------------
import scrapy
class QuotesSpider(scrapy.Spider):
  name = "quotes"
  start_urls =[
    'http://quotes.toscrape.com/page/1/',
  ]
  def parse(self,response):
    for quote in response.css('div.quote')
	  yield{
	    'text':quote.css('span.text::text').extract_first(),
		'author':quote.css('small.author::text').extract_first(),
		'tags':quote.css('div.tags a.tag::text').extract(),
	  }
	  next_page = response.css('li.next a::attr(href)').extract_first()
	  if next_page is not None:
		yield response.follow(next_page,callback=self.parse)
#直接返回了response对象

'''	
----------------------------------------------------------------
#city58_test.py
# -*- coding:utf-8 -*-
import scrapy
from pyquery import PyQuery
from items import City58Item
from scrapy.http import Request

class City58TestSpider(scrapy.Spiders):
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
		
		req = response.follow('chuzu/pn2/,callback = self.parse)
		yield req
		#理由为：follow函数式host(主域名)+相对路径，在本例中也就是http://bj.58.com/+chuzu/pn2/
		
		test_request1 = Request('http://bj.58.com/chuzu/pn3,
		                        callback=self.parse,
								errback=self.error_back,
								headers={},
								cookies={},
								priority=10,
								)
        #priority优先级
		
		test_request2 = Request('http://bj.58.com,
		                        callback=self.parse,
								errback=self.error_back,
								headers={},
								priority=10,
								meta={'dont_redirect':True}
								)
		#dont_redirect不转发
		
		test_request3 = Request('http://bj.58.com,
		                        callback=self.parse,
								errback=self.error_back,
								headers={},
								priority=10,
								dont_filter=True,
								#meta={'dont_redirect':True}
								)
		#禁止它转发,  #2已经请求一次了，3再次请求就失败了，所以dont_filter=True强制不过滤（就会造成死循环）；
		
		yield test_request1
		yield test_request2
		yield test_request3
		
	def error_back(self,e):
	    _ = self
		print(e)
		print('我报错了')

		






----------------------------------------------------------------
select * from sync_db order by id desc limit 10

select * from sync_id
不行