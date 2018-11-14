
'''初始Python爬虫'''
#1.使用urllib包获取百度首页信息
#导入urllib.request
>>>import urllib.request
#打开网址，返回一个类文件对象
>>>f=urllib.requq.urlopen("http://www.baidu.com")
#打印前500字符
>>>f.read(500)
#打印前500字符并修改编码为utf-8
>>>f.read(500).decode('utf-8)
-------------------------------
#2.使用Requests库获取百度首页信息
>>>import requests   #导入requests库
#使用requests.get方法获取网页信息
>>>r = requests.get('https://www.baidu.com/')
>>>r

>>>r.text  #打印结果

>>>r.encoding='utf-8'   #修改编码
>>>r.text   #打印结果
-----------------------------------
#在PytCharm中运行
import urllib.request
f=urllib.requq.urlopen("http://www.baidu.com")
print(f.read(500))
print(f.read(500).decode('utf-8))
---------
import requests 
r = requests.get('https://www.baidu.com/')
print(r)
print(r.text)

r.encoding='utf-8'
print(r.text)
-----------------------------------------
'''
爬虫三步走
获取数据：Requests ，Urllib
解析数据：Xpath ，BeautifulSoup4
保存数据：保存本地 ， 数据库
'''
----------------------------------
'''爬虫第一步：使用requests获得数据；
导入requests>>>requests.get'''
import requests
#。text文本内容
r = requsts.get('https://book.douban.com/subject/1084336/commets').text
----------------------------
'''爬虫第二步：使用BeautifulSoup4解析数据
导入bs4>>>解析网页数据>>>寻找数据>>>for循环打印'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)
------------------
'''
爬虫第三步：使用pandas保存数据
导入pandas>>>新建list对象>>>使用to_csv写入
'''
import pandas
comments = []
for item in pattern:
    comments.append(item.string)
df = pands.DataFrame(comments)
df.to_csv('comments.csv')
-------------------------------------------------
>pip install requests
>pip install BeautifulSoup4
>pip install lxml
#非官方http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
>pip install lxml-3.8.0-cp39-cp36m-win_amd64.whl
>>>pip list
-----------------------------------------------
'''
Requests唯一的一个非转基因的Python HTTP库，人类可以安全享用。
警告：非专业使用其他HTTP库会导致危险的副作用，包括：安全缺陷症、冗余代码症、重新发明轮子症、啃文档症、抑郁、头疼、甚至死亡。

Requests库的7个主要方法
requests.request() 构造一个请求，支撑一下各方法的基础方法
requests.get()    获取HTML网页的主要方法，对应HTTP的GET
requests.head()   获取HTML网页头信息的方法，对应HTTP的HEAD
requests.post()   获取HTML网页提交POST请求方法，对应HTTP的POST
requests.put()    获取HTML网页提交PUT请求方法，对应HTTP的PUT
requests.patch()  获取HTML网页提交局部修改请求，对应HTTP的PATCH
requests.delete() 获取HTML网页提交删除请求，对应HTTP的DELETE
----------
Response对象的属性
r.status_code http   请求返回状态，200表示连接成功
r.text         返回对象的文本内容
r.content      猜测返回对象的二进制形式
r.encoding     分析返回对象的编码方法
r.apparent_encoding    响应内容编码方式（备选编码方式）

'''
------------------------------------
#阻止JavaScript加载；
import requests   #导入Requests库
url = ''             #输入url
r = request.get(url,timeout=20)    #使用get方法
print(r.text)            #打印返回
print(r.raise_for_status())   #抛出异常
--------------------------
#爬取网页通用框架
#定义函数》设置超时》异常处理》调用函数
import requests
def getHTMLText(url):
    try:
	    r = requests,get(url,timeout=20)
		r,raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
    except:
	    return "产生异常"
if __name == '__main__'
    url = ""
	print(getHTMLText(url))
----------------------------------------
'''
爬虫协议：
也被叫做robots协议，告诉网络蜘蛛哪些页面可以抓取，哪些页面不能抓取；
文件规范：
必须将robots.txt代码保存为文本文件
必须将该文件保存到网站的顶级目录下
robots.txt文件必须命名为robots.txt;
https://www.baidu.com//robots.txt

爬虫建议：
爬取互联网公开数据
尽量放慢你的速度
尽量遵循robots协议
不要用于商业用途
不要公布爬虫程序与数据
----------------
拦截所有的机器人：
User-agent:*
Disallow:/
允许所有的机器人：
User-agent:*
Disallow:

相当于它想要机器人是延迟的一个时间,10s
Crawl-delay:10

'''
----------------------------------------------------
'''
#使用Xpath解析豆瓣短评
获取文本内容用text()
获取注释用comment()
获取其它任何属性用@xx,
如：
@href
@src
@value
想要获取某个标签下所有文本（包括子标签下的文本），使用string
如<p>123<a>来获取我啊</a></p>，这边如果想要得到的文本为"123来获取我啊"，则需要使用string
starts-with匹配字符串前面相等
contains匹配任何位置相等

#导入lxml》返回xml结构》寻找数据
Elements>>Copy>>Copy Xpath
'''
import requests
from lxml import etree   
html='''省略'''
s = etree.HTML(html)      
print(s.xpath())
----------------------------------------------
import requests
from lxml import etree   
html='https://book.douban.com/subject/1084336/commets/'
r = requests.get(url).text
#print(r)
s = etree.HTMl(r)
print(s.xpath('//*[@id="comments"]/ul/li[1]div[2]/p/text()'))

#https://book.douban.com/subject/1084336/reviews
#//*[@id="review_1000104_short"]/div
-------------------------------------------------------------------#手写Xpath
import requests
from lxml import etree 
html='https://book.douban.com/subject/1084336/commets/'
r = requests.get(url).text
s = etree.HTMl(r)
print(s.xpath('//div[@class="comment"]/p/text()')[0])

-------------------------------
'''
print(s.xpath('//*[@id="comments"]/ul/li[1]div[2]/p/text()'))
print(s.xpath('//*[@id="comments"]/ul/li[2]div[2]/p/text()'))
print(s.xpath('//*[@id="comments"]/ul/li[3]div[2]/p/text()'))
'''
----------------------------------
'''
open   pandas   csv   numpy   matplotlib
open函数用法：新建对象f   写入数据
open函数的打开模式：
r    只读，若不存在文件会报错
w    只写，若不存在文件自动新建
a    附加到文件末尾
rb,wb,ab    操作二进制
r+    读写模式打开
https://yiyibooks.cn/
http://pandas.pydata.org/pandas-docs/stable/
pandas中文文档（10min)
to_exce;()实例方法：用于将DataFrame保存到Excel
DataFrame是一个表格或者类似二维数组的结构，它的各行表示一个实例，各列表示一个变量。
'''
#使用pandas保存豆瓣短评数据
import requests
from lxml import etree
url = 'https://book.douban.com/subject/1084336/commets/'
r = req.get(url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')

with open('1002365528.txt','w',encoding='utf-8') as f:
    for i in file:
	    print(i)
	    f.write(i)
----------------------------------------------------
#pandas保存数据到Excel：导入相关库，创建随机值，保存到Excel
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,3))
print(df.head())

df.to_csv('numpppy.csv')
#>>>生成了一个6*3的一个矩阵

------------------------------
#将数据保存到本地
import requests
from lxml import etree
#爬虫三部走：第一步使用requests然后获得网页的源代码
url = 'https://book.douban.com/subject/1084336/commets/'
r = req.get(url).text
#第二步就是用Xpath作为一个解析工具，把我们想要爬去的数据解析出来
s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')
#第三步使用pandas来吧这些解析完成数据保存到本地
import pandas as pd
df = pd.DataFrame(file)
#print(df.head())
df.to_excel('smpidus.xlsx')
---------------------------------
#pandas的用法：导入pandas   创建DataFrame对象   保存到Excel
import pandas as pd
df = pd.DataFrame(file)
df.to_excel('smpidus1002365528.xlsx')
-----------------------------------------------------------------
'''
爬虫的一般思路
1.抓取网页、分析请求。
2.解析网页、寻找数据。
3.储存数据、多页处理。

分析具体网页
翻页后URL不变；
google安装JSONView
https://www.zhihu.com/people/excited-vczh/following
设置请求头》获取数据》保存数据
#print(response)
#print(df.head())
#print(response.status_code)
list extend()
'''
-------------------
# -*- coding:utf-8 -*-
import requests
import pandas as pd
import time
headers ={
    'user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

user_data = []
def get_user_data(page):
    for i in range(page):
	url ='https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'.format(i=20)
	
    response = requests.get(url,headers=headers).json()['data']
    user_data = extend(response)
	print("正在爬取第%s页"% str(i+1))
	time.sleep(1)
	
if __name__ == '__main__':
    get_user_data(10)
	df = pd.DataFrame.from_dict(user_data)
	df.to_csv('user.csv')

----------------------------------
'''
MongoDB将数据存储为一个文档，数据结构由键值（key=>value)对组成。
https://zhuanlan.zhihu.com/p/29986675
先按照第三方库pip install pymongo
2.安装插件File》Plugins》mongo
mongo可视化，可以直接点右边MongoClientExplorer》点击设置Settings》
点击+，测试链接Test Connection》测试正常点击okok；
'''
---------------------------------------------
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

client = MongoClient()
db = client.test   #连接test数据库，没有自动创建
my_set = db.set    #使用set集合，没有则自动创建

my_set.insert({"name":"yyy","age":18})
---------------------------------------------------
'''
http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false

爬去拉钩
https://m.weibo.cn/
https://weibo.cn/

'''
----------------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pymongo import MongoClient

client = MongoClient()
db = client.logou   #连接logou数据库，没有自动创建
my_set = db.job    #使用job集合，没有则自动创建

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSSchoolJob=0'

payload ={
    'first:false',
	'pn':'2',
	'kd':'爬虫',
}

headers = {
    'Cookie':'user_trace_token=20171117135802-07146f87-cf57-4a73-be20-34ba4e82e13a; LGUID=20171117135803-463b7052-cb5c-11e7-992f-5254005c3644; _ga=GA1.2.470250633.1510898287; JSESSIONID=ABAAABAAADEAAFI8471D5A7DC89DFC501F50F52F2491907; X_HTTP_TOKEN=7ab9c1f522fca859b83727e038be5159; _gid=GA1.2.535523667.1537489097; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20180921083005-165f988a176118-077b96dc22ee44-43480420-2073600-165f988a1771fe; _gat=1; LGSID=20180921082950-73543d11-bd35-11e8-a290-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0s0000KlmKuCTsdU2iko7GlgkQIeU9iMOaDnsMzSoyOOTpMHb7AF1vRdFQV1wGQRKfzWGGf2Dhcxx8Z2OeFjE_eD5pQKHQM8DVlq9Mv5BrXF9LtY7aUGD1xFYuqlkyRpE3DUpzaaobTRjwPG8BuOP-cbfCX1n3t3Ki5gFaSMvJGZxpemU6.Db_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzt5jzLdqPqe5Q8d4QQPOQ9tOZjlOQjEosSxH9LenrOWSo9tqvZuY3Ihej4qrZu43xU_sSxH9vX8Zxl3x5u9vN3ISkmh5ZuuvyNqPMQblXgZJyAp7WFEL4rkf0.U1Yk0ZDqs2v4VnL3FHcsdIjA80KspynqnfKY5TL3YVT-nWjDv_LAdIjA80KGUHYznWR0u1ddugK1nfKdpHdBmy-bIykV0ZKGujYzPsKWpyfqnWfY0AdY5HDsnHIxnH0krNtknjc1g1nznW9xn1msnfKopHYs0ZFY5Hmsr0K-pyfq0AFG5HcsP7tkPHR0UynqP16knH64n16zg1Dsnj7xnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5HD0uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1YkPH01nWRkn1mvP103rjTLPjRsP0Kzug7Y5HDdn1TYrjbLrjTknWR0Tv-b5HbknHw-mWP9nj0sPARzPWb0mLPV5H97fHNDnYFarH0dwjPDf1f0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5HD0UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn1D3P10Lg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YdrHckn6%26ck%3D3502.2.77.272.150.265.139.264%26shh%3Dwww.baidu.com%26sht%3D78040160_26_pg%26us%3D1.0.1.0.1.301.0%26ie%3Dutf-8%26f%3D3%26ch%3D1%26tn%3D78040160_26_pg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2520%25E6%258B%259B%25E8%2581%2598%26rqlang%3Dcn%26inputT%3D2412%26prefixsug%3Dlago%26rsp%3D0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_zz_b16bba_5f2009_%25E7%25BD%2591%25E6%2598%2593%2B%25E5%2586%2585%25E6%258E%25A8%25E6%258B%259B%25E8%2581%2598; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535424750,1537489097,1537489806,1537489812; TG-TRACK-CODE=index_search; LGRID=20180921083021-8628914a-bd35-11e8-baf2-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537489837; SEARCH_ID=44c4bf0c721c45fb84806e120205bbe0',
	'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
}

response = requests.post(url,data=payload,headers=headers)
#print(response.text)
#print(response.json()['content']['positionResult']['result'])
my_set.insert(response.json()['content']['positionResult']['result'])
----------------------------------------------------------------------------------------
#翻页爬取
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pymongo import MongoClient
import time

client = MongoClient()
db = client.logou   #连接logou数据库，没有自动创建
my_set = db.job    #使用job集合，没有则自动创建

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSSchoolJob=0'

#定义一个函数
def get_job_info(page):
    for i in range(page):
        payload ={
            'first:false',
	        'pn':i,
	        'kd':'爬虫',
        }
        headers = {
            'Cookie':'',
	        'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	        'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
        }
		response = requests.post(url,data=payload,headers=headers)
		if response.status_code == 200:
		    my_set.insert(response.json()['content']['positionResult']['result'])
		else:
		    print("Somthing Wrong!")
		print("正在爬取" +str(i+1) +"页"）
		time.sleep(s)
		

        response = requests.post(url,data=payload,headers=headers)
        my_set.insert(response.json()['content']['positionResult']['result'])
if __name__ == '__main__':
    get_job_info(27)
----------------------------------------------------------------------------------------
#新库 pip install fake_useragent
import requests
from pymongo import MongoClient
import time
from take_useragent import UserAgent

client = MongoClient()
db=client.test
lagou = db.lagou

headers ={
    'Cookie':'',
	'Referer':'',
}

def get_job_info(page,kd):
    for i in range(page):
	url = ''
	payload ={
	    'first':'false',
		'pn':'str(i),
		'kd':kd,
	}
	
	ua = UserAgent()
	headers['user-agent'] = ua.random
	response = requests.post(url,data=payload,headers=headers)
	
	if response.status_code == 200:
	    job_json = response.json()['content']['positionResult']['result']
		lagou.insert(job_json)
		#print(job_json)
	
	else:
	    print('Somthing Wrong!')
		
	print('正在爬取第' + str(i+1) +'页的数据...'
	time.sleep(3)
	
if __name__ == '__main__':
    get_job_info(3,'Python')
----------------------------------------------------------------------------------------
'''
爬取淘宝商品数据
全能的Selenium  环境搭建  简单使用
实战环节   使用Selenium爬取淘宝思路讲解+代码分析
pip install selenium
chromedriver(不需要cookies)
'''
------------------------------------------------------------------------------------
# -*- coding:utf-8 -*-
#!/usr/bin/env python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("htttp://www.baidu.com")
--------------------------------------------------------------
# -*- coding:utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

elem = driver.find_element_by_xpath('//*[@id="kw"]')
elem.send_keys("Python selenium",Keys.ENTER)
print(driver.page_source)
--------------------------------------------------------------
# -*- coding:utf-8 -*-
#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")

elem = driver.find_element_by_xpath('//*[@id="kw"]')
elem.send_keys("Python selenium",Keys.ENTER)
print(driver.page_source)
--------------------------------------------------------------
# -*- coding:utf-8 -*-
#!/usr/bin/env python
#爬取淘宝,搜索进行翻页  PyQuery跟前端挂钩

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
from pymongo import MongoClient
import re

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

client = MongoClient()
db = client.taobao
data = db.data

def search(kd):
    try:
	    browser.get('https://www.taobao.com/')
		input = wait.until(EC.presence_of_element_located((By_CSS_SELECTOR,"#q")))
		submit = wait.until(EC_element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
		input.send_keys(kd)
		submit.click()
		total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
		get_products()
		return total.text
	except TimeoutException:
	    return search()
		
def next_page(page_number):
    try:
	    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > input")))
		submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
		input.clear()
		input.send_keys(page_number)
		submit.click()
		wait.until(EC.text_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > url > li.item.active > span'),str(page_number)))
		get_products()
	execpt TimeoutException:
	    next_page(page_number)
		
def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'mainsrp-itemlist .items .item')))
	html = browser.page_source
	doc = pq(html)
	items = doc('mainsrp-itemlist .items .item').items()
	for item in items:
	    product = {
		    'image':item.find('.pic .img').attr('src'),
			'price':item.find('.price').text(),
			'deal':item.find('.deal-cnt').text()[:-3],
			'title':item.find('.title').text(),
			'shop':item.find('.shop').text(),
			'location':item.find('.location').text(),
		}
		print(product)
		data.insert(product)
		
def main(kd):
	total = search(kd)
	total = int(re.compile('(\d+)').search(total).group(1))
	
	#抓取全部换成:10更换为total + 1
	for i in range(2,10):
	    next_page(i)
		
if __name__ == '__main__':
    main('大衣')
--------------------------------------------------------------



















