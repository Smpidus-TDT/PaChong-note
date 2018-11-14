'''
为什么需要进行HTTP请求分析？
什么是抓包？
谷歌--开发者模式；
-----------------------------------
各个面板的作用：
Elements（元素面板）：
查找网页源代码HTML中的任一元素，手动修改任一元素的属性和样式且能实时在浏览器里面得到反馈。

Console（控制面板）：
在开发期间，可以使用控制台面板记录诊断信息，或者使用它作为shell在页面上与JavaScript交互。
windows.open('https://github.com/Smpidus-TDT')

Sources（源代码面板）：
在源代码面板中设置断点来调试JavaScript，或者通过Workspaces（工作区）连接本地文件来使用开发者工具的实时编辑器。

Network（网络面板）：
从发起网页页面请求Request后分析HTTP请求后得到的各个请求资源信息（包括状态、资源类型、大小、所用时间等），可以根据这个进行网络性能优化。

Performance（性能面板）：
使用时间轴面板可以通过记录和查看网站生命周期内发生的各种事件来提高页面的运行时性能。

Memory（内存面板）：
分析web应用或者页面的执行事件以及内存使用情况。

Application（应用面板）：
记录网站加载的所有资源信息，包括存储数据（Local Storage、Session Storage 、IndexedDB、Web SQL、Cookies）、缓存数据、字体、图片、脚本、样式表等。

Security（安全面板）：
使用安全面板调试混合内容，证书问题等等。

Audits（审核面板）：
对当前网页进行网路利用情况、网页性能方面的诊断，并给出一些优化建议。比如列出所有没有用到的CSS文件等。

网络面板的5个窗格
1.Controls（控件）
使用这些选项可以控制Network（网络）面板的外观和功能。

2.Filters（过滤器）
使用这些可以控制在请求列表中显示哪些资源。
提示：按住Cmd（Mac）或Ctrl(Window/Linux)，然后点击过滤器可以同时选择多个过滤器。

3.Overview（概览）
这个图表显示检索资源的时间轴。如果您看到多哦垂直堆叠的栏，这意味着这些资源被同时检索。

4.Requests Table（请求列表）
此列表列出了检索的每个资源。默认情况下，此表按时间顺序排序，也就是最早的资源在顶部。单元资源名称可以获得更多信息。
提示：右键单击列表的任何标题栏可以以添加活删除信息列。

5.Summary（概要）
概要窗格告诉您请求的总数，传输的数据量，和加载时间。

Preserve log记录所有的log
Disable cache不缓存

Headers：
General
Request Headers：请求
Response Headers：返回
注：http请求是无状态的（理论上讲你把一个HTTP请求发给服务器，它是不能判断也就是它如果是个裸的什么都没有，Request Headers什么都没有，它就什么都不知道了，所以它要判断你是谁你在干嘛，你想干什么，它就必须看Request Headers）；
无论你做什么操纵的时候，你发现浏览器返回过来的内容核你用你的代码去请求它的内容有差别。
说明request headers这里的整个面板里面的所有参数里面你有写参数没有模拟完全，
说明request headers这里的整个面板里面的所有参数里面你有些参数没有模拟完全，导致它发现了你用代码请求，或者叫做机器人请求或者叫做爬虫请求，不管叫什么就是你被发现了哦，你的演技太差你被发现了哦，所以你就要回到request headers，老老实实地、仔仔细细地看这里的每一个参数，去观察自己哪里露馅了。

viewsource就是看真实的整个方法

Request Headers：请求
Response Headers：返回
你怎么请求它就怎么返回；
cookie（就是服务器给你身份证）本身就是header的参数之一，

eg：发给你身份证，就要进行检查你的身份证；
Referer：这个参数其实是指你的上级的链接。

----------------------------------------
过滤请求
filter（过滤器）文本字段还支持各种关键字，使您可以通过各种属性对资源进行排序，例如按照文件大小排序使用larger-than关键字。

关键字列表：
domain（域）
仅显示来自指定域的资源。您可以使用通配符（*）来包括多个域。例如，*.com显示以.com结尾的所有域名中的资源。DevTools会在自动完成下拉菜单中自动填充它遇到的所有域。

has-response-header(响应头信息)
显示包含指定HTTP响应头信息的资源。DevTools会在自动完成下拉菜单中自动填充它遇到的所有响应头。

Is：使用is： running过滤出WebSocket资源。


larger-than（大于)
显示大于指定大小的资源（以字节为单位）。设置值1000等效于设置值1K。

method（方法）
显示通过指定的HTTP方法类型检索的资源。DevTools使用它遇到的所有HTTP方法填充下拉列表。
get,post...

mime-type（mime类型）
显示指定MIME类型的资源。DevTools使用它遇到的所有MIME类型填充下拉列表。

mixed-content（混合内容）
显示所有混合内容资源（mixed-content:all）或仅显示当前显示显示的内容（mixed-content:displayed）。

Scheme（协议）
显示通过不受保护的HTTP（scheme：http）活受保护的HTTPS（scheme：https）检索的资源。

set-cookie-domain(cookie域)
显示具有Set-Cookie头，并且其Domain属性与指定值匹配的资源。DevTools会在自动完成下拉菜单中自动填充它遇到的所有Cookie域。

set-cookie-name（cookie名）
显示具有Set-Cookie头，并且名称与指定值匹配的资源。DevTools会在自动完成下拉菜单中自动填充它遇到的所有Cookie名。

set-cookie-value（cookie值）
显示具有Set-Cookie头，并且值与指定值匹配的资源。DevTools会在自动完成下拉菜单中自动填充它遇到的所有Cookie名。
eg:uuid 对应的ID是什么样的。

status-code（状态码）
仅显示其HTTP状态代码与指定代码匹配的资源。DevTools会在自动完成下拉菜单中自动填充它遇到的所有状态码。
eg:200,400....
----------------------------------------------
eg：
每个网站都有大量的第三方出现
domain:*.lianjia.com
XHR
--正则表达式

has-response-header:Set-Cookie
All 

set-cookie-domain:.lianjia.com
All 

set-cookie-name:atpsida
All

set-cookie-value:c46d7161

status-code:200
----------------------------------------------
复制、保存和清楚网络信息
右键单击Requests Table（请求列表）以复制、保存或删除网络信息。一些选项是上下文相关的，所以如果想在单个资源上操作，需要右键单击该资源行。

Copy Response（复制响应）
将所选资源的HTTP响应复制到系统剪贴板。

Copy as cURL（复制cURL）
将所选资源的网络请求作为cURL命令字符串复制到系统剪贴板。
请参阅将复制请求为cURL命令。

Copy All as HAR（全部复制为HAR）
将所有资源复制到系统剪贴板作为HAR数据。HAR文件包含描述网络“瀑布”的JSON数据结构。一些第三方工具可以使用HAR文件中的数据重建网络瀑布。
有关详细信息，请参阅Web性能强大工具：HTTP归档（HAR）。

Save as HAR with Content(另存为带内容的HAR)
将所有网络数据与每个页面资源一起保存到HAR文件中。二进制资源（包括图像
被编码为Base64编码文本。

Clear Browser Cache（清除浏览器缓存）
清除浏览器高速缓存。提示：您也可以从Network Conditions（网络条件）抽屉式窗格中启用活禁用浏览器缓存。

Clear Browser Cookies（清除浏览器Cookies）
清除浏览器Cookies。

Open in Sources Panel（在源文件面板中打开）
在Sources（源文件）面板中打开选定的资源。

Open Link in New Tab（在新标签页中打开链接）
在新标签页中打开所选资源。
您还可以在Requests Table（请求列表）中双击资源名称。

Copy Link Address（复制链接地址）
将资源URL复制到系统剪贴板。

Save（保存）
保存所选的文本资源。仅显示在文本资源上。

Replay XHR（重新发送XHR）
重新发送所选的XMLHTTPRequest。仅显示在XHR资源上。
---------------------------------------
查看资源发起者和依赖关系
按住Shift并移动鼠标到资源上可查看它的发起者和依赖关系。这部分是你鼠标悬停的资源的target（目标）引用。
--去找寻它的根，Initiator每个链接由谁发起


从target（目标）往上查找，第一个颜色编码为绿色的资源是target（目标）向下查找，任何颜色编码为红色的资源都是target的依赖。
---------------------------------------
寻找推荐接口；

面板只能给你做出参考，有些数据会在JS中....
XHR》》》JS》》》other》》》ALL》》》Search all files全局搜索（组合拳）；

---------------------------------------
Url去重
数据库去重

1.why需要进行URL去重？
对于已经抓取过的链接，进行持久化，并且在启动的时候加载进入去重队列，是一个比较强的需求主要应对爬虫故障重跑，不需要重跑所有链接。

2.如何确定去重强度？
根据爬取周期确定使用去重强度；
抓取周期在一个小时内，不需要对已经抓取的链接做持久化；
抓取周期在一天内（或抓取的数据总量30w以下），需要对抓取链接做一个相对简单的持久化；
抓取周期在一天以上，需要对抓取链接做相对专业的持久化。

3.URL去重方法：两种解决方法
A已经造好的轮子系列：
scrapy-deltafetch
scrapy-craql-once
scrapy-redis
--分布式框架，也可以用来做这种url去重，断点
scrapy-redis-bloomfilter
--更加节省内存，可以存储上亿url，是上面的加强版

B自己造轮子
自己写的init_add_request方法
可以轻量实现
---------------------------------------
scrapy-deltafetch安装
1.安装Berkeley DB
--在官网下载，依赖包
https://www.lfd.uci.edu/-gohlkee/pythonlibs/#bsddb3
2.安装bsddb3

3.安装scrapy-deltafetch


scrapy-deltafetch的配置（spider中间件）
SPIDER_MIDDLEWARES ={
  'scrapy_deltafetch.DeltaFetch':100,
}
# --是否启动它
DELTAFETCH_ENABLED = True
--文件路径
DELTAFETCH_DIR = 'D:\work'
--是否重置
DELTAFETCH_RESET = 1
--或者下面这种重置
scrapy crawl example -a deltafetch_reset =1

deltafetch_key
---------------------------------------
scrapy-deltafetch实现
def process_spider_output*(self,respose,result,spider):
    for r in result:
	  if isinstance(r,Request):
	    key = self._get_key(r)
		  logger.info("Ignoring already visited:%s" % r)
		  if self.stats:
		    self.stats.inc_value('deltafetch/skipped',spider=spider)
		  continue
	  elif isinstance(r,(BaseItem,dict)):
	    key = self._get_key(response.request)
		self.db[key] =s tr(time.time())
		if self.stats:
		    self.stats.inc_value('deltafetch/stored',spider=spider)
		yield r
---------------------------------------
（spider中间件）
import scrapy-deltafetch

from .muddlewar import DeltaFetch
--查看源码
process_spider_output 拦截；

_get_key生成一个唯一标识
--拿到一个关键的key（deltafetch_key）
request_fingerprint(request)
--去重指纹

hash 生成字符串
---------------------------------------
dupefilter.py
set 绝对的唯一的；
（去重的核心）def request_seen(self,request)
scrapy(面向对象)	暂停后在恢复爬虫的方案
if self.file:
    self.file.write(fp +os.lineseep)
实例变量
--url持久化自己要做；
---------------------------------------

创建一个项目
# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request

class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'
	allowd_domains = ['58.com']
	start_ruls =['http://cd.58.com']
	
	def parse(self,response)
	    pass
		yield Request('http://bj.58.com',callback=self.parse)
		yield Request('http://wh.58.com',callback=self.parse)
		
'''



--把settings中机器ROBOTSTXT_BEY =True 修改为False；
--main.py
---------------------------------------
写到单独文件main.py中启动它；

pipelines.py




---------------------------------------
#init_utils的实现
def init_add_request(spider,url:str):
"""
此方法用于在，scrapy启动的时候添加一些已经跑过的url，让爬虫不需要重复跑
author:changliu@zaoshu.io
:return:
"""
rf = spider.crawler.engine.slot.scheduler.df
request = Request(url)
rf.request_seen(request)

# items = self.db['qichacha'].find({},cursor_timeout=True)
    #for item in items:
	#    init_add_request(spider,'http://www.qichacha.com/firm_{}.html'.format(item['pag_id']))
	
---------------------------------------
#main.py
from scrapy.cmdline import execute
execute("scrapy crawl spider_city_58".split())	
---------------------------------------
#pipelines.py
# -*- coding:utf-8 -*-
from .init_utils import init_add_request

class City58Pipeline(object):
    def process_item(self,item,spider)
	    return item 
		
	def open_spider(self,spider)
	    init_add_request(spider,'http://wh.58.com')
		
---------------------------------------
#settings
ITEM_PIPELINES = {
    'city_58.pipelines.City58Pipeline':300,
}
		
---------------------------------------
scrapy-redis
配置SCHEDULER_PERSIST = True ，实现队列不清除。
因而实现故障从断点重启

---------------------------------------
数据库去重
理论上讲，我们应该优先对url链接去成功，数据库去重是一个很牵强的方案
数据库去重，应该尽量使用数据库本身的各种机制去去重，如唯一键

---------------------------------------

数据入库
优先选择非关系数据库MongoDB；
'''
