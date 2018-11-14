'''
Ϊʲô��Ҫ����HTTP���������
ʲô��ץ����
�ȸ�--������ģʽ��
-----------------------------------
�����������ã�
Elements��Ԫ����壩��
������ҳԴ����HTML�е���һԪ�أ��ֶ��޸���һԪ�ص����Ժ���ʽ����ʵʱ�����������õ�������

Console��������壩��
�ڿ����ڼ䣬����ʹ�ÿ���̨����¼�����Ϣ������ʹ������Ϊshell��ҳ������JavaScript������
windows.open('https://github.com/Smpidus-TDT')

Sources��Դ������壩��
��Դ������������öϵ�������JavaScript������ͨ��Workspaces�������������ӱ����ļ���ʹ�ÿ����߹��ߵ�ʵʱ�༭����

Network��������壩��
�ӷ�����ҳҳ������Request�����HTTP�����õ��ĸ���������Դ��Ϣ������״̬����Դ���͡���С������ʱ��ȣ������Ը�������������������Ż���

Performance��������壩��
ʹ��ʱ����������ͨ����¼�Ͳ鿴��վ���������ڷ����ĸ����¼������ҳ�������ʱ���ܡ�

Memory���ڴ���壩��
����webӦ�û���ҳ���ִ���¼��Լ��ڴ�ʹ�������

Application��Ӧ����壩��
��¼��վ���ص�������Դ��Ϣ�������洢���ݣ�Local Storage��Session Storage ��IndexedDB��Web SQL��Cookies�����������ݡ����塢ͼƬ���ű�����ʽ��ȡ�

Security����ȫ��壩��
ʹ�ð�ȫ�����Ի�����ݣ�֤������ȵȡ�

Audits�������壩��
�Ե�ǰ��ҳ������·�����������ҳ���ܷ������ϣ�������һЩ�Ż����顣�����г�����û���õ���CSS�ļ��ȡ�

��������5������
1.Controls���ؼ���
ʹ����Щѡ����Կ���Network�����磩������ۺ͹��ܡ�

2.Filters����������
ʹ����Щ���Կ����������б�����ʾ��Щ��Դ��
��ʾ����סCmd��Mac����Ctrl(Window/Linux)��Ȼ��������������ͬʱѡ������������

3.Overview��������
���ͼ����ʾ������Դ��ʱ���ᡣ�����������Ŷ��ֱ�ѵ�����������ζ����Щ��Դ��ͬʱ������

4.Requests Table�������б�
���б��г��˼�����ÿ����Դ��Ĭ������£��˱�ʱ��˳������Ҳ�����������Դ�ڶ�������Ԫ��Դ���ƿ��Ի�ø�����Ϣ��
��ʾ���Ҽ������б���κα�������������ӻ�ɾ����Ϣ�С�

5.Summary����Ҫ��
��Ҫ����������������������������������ͼ���ʱ�䡣

Preserve log��¼���е�log
Disable cache������

Headers��
General
Request Headers������
Response Headers������
ע��http��������״̬�ģ������Ͻ����һ��HTTP���󷢸������������ǲ����ж�Ҳ����������Ǹ����ʲô��û�У�Request Headersʲô��û�У�����ʲô����֪���ˣ�������Ҫ�ж�����˭���ڸ�������ʲô�����ͱ��뿴Request Headers����
��������ʲô���ݵ�ʱ���㷢����������ع��������ݺ�������Ĵ���ȥ�������������в��
˵��request headers��������������������в�����������д����û��ģ����ȫ��
˵��request headers��������������������в�����������Щ����û��ģ����ȫ�����������������ô������󣬻��߽���������������߽����������󣬲��ܽ�ʲô�����㱻������Ŷ������ݼ�̫���㱻������Ŷ���������Ҫ�ص�request headers������ʵʵ�ء�����ϸϸ�ؿ������ÿһ��������ȥ�۲��Լ�����¶���ˡ�

viewsource���ǿ���ʵ����������

Request Headers������
Response Headers������
����ô����������ô���أ�
cookie�����Ƿ������������֤���������header�Ĳ���֮һ��

eg�����������֤����Ҫ���м��������֤��
Referer�����������ʵ��ָ����ϼ������ӡ�

----------------------------------------
��������
filter�����������ı��ֶλ�֧�ָ��ֹؼ��֣�ʹ������ͨ���������Զ���Դ�����������簴���ļ���С����ʹ��larger-than�ؼ��֡�

�ؼ����б�
domain����
����ʾ����ָ�������Դ��������ʹ��ͨ�����*����������������磬*.com��ʾ��.com��β�����������е���Դ��DevTools�����Զ���������˵����Զ������������������

has-response-header(��Ӧͷ��Ϣ)
��ʾ����ָ��HTTP��Ӧͷ��Ϣ����Դ��DevTools�����Զ���������˵����Զ������������������Ӧͷ��

Is��ʹ��is�� running���˳�WebSocket��Դ��


larger-than������)
��ʾ����ָ����С����Դ�����ֽ�Ϊ��λ��������ֵ1000��Ч������ֵ1K��

method��������
��ʾͨ��ָ����HTTP�������ͼ�������Դ��DevToolsʹ��������������HTTP������������б�
get,post...

mime-type��mime���ͣ�
��ʾָ��MIME���͵���Դ��DevToolsʹ��������������MIME������������б�

mixed-content��������ݣ�
��ʾ���л��������Դ��mixed-content:all�������ʾ��ǰ��ʾ��ʾ�����ݣ�mixed-content:displayed����

Scheme��Э�飩
��ʾͨ�����ܱ�����HTTP��scheme��http�����ܱ�����HTTPS��scheme��https����������Դ��

set-cookie-domain(cookie��)
��ʾ����Set-Cookieͷ��������Domain������ָ��ֵƥ�����Դ��DevTools�����Զ���������˵����Զ����������������Cookie��

set-cookie-name��cookie����
��ʾ����Set-Cookieͷ������������ָ��ֵƥ�����Դ��DevTools�����Զ���������˵����Զ����������������Cookie����

set-cookie-value��cookieֵ��
��ʾ����Set-Cookieͷ������ֵ��ָ��ֵƥ�����Դ��DevTools�����Զ���������˵����Զ����������������Cookie����
eg:uuid ��Ӧ��ID��ʲô���ġ�

status-code��״̬�룩
����ʾ��HTTP״̬������ָ������ƥ�����Դ��DevTools�����Զ���������˵����Զ����������������״̬�롣
eg:200,400....
----------------------------------------------
eg��
ÿ����վ���д����ĵ���������
domain:*.lianjia.com
XHR
--������ʽ

has-response-header:Set-Cookie
All 

set-cookie-domain:.lianjia.com
All 

set-cookie-name:atpsida
All

set-cookie-value:c46d7161

status-code:200
----------------------------------------------
���ơ���������������Ϣ
�Ҽ�����Requests Table�������б��Ը��ơ������ɾ��������Ϣ��һЩѡ������������صģ�����������ڵ�����Դ�ϲ�������Ҫ�Ҽ���������Դ�С�

Copy Response��������Ӧ��
����ѡ��Դ��HTTP��Ӧ���Ƶ�ϵͳ�����塣

Copy as cURL������cURL��
����ѡ��Դ������������ΪcURL�����ַ������Ƶ�ϵͳ�����塣
����Ľ���������ΪcURL���

Copy All as HAR��ȫ������ΪHAR��
��������Դ���Ƶ�ϵͳ��������ΪHAR���ݡ�HAR�ļ������������硰�ٲ�����JSON���ݽṹ��һЩ���������߿���ʹ��HAR�ļ��е������ؽ������ٲ���
�й���ϸ��Ϣ�������Web����ǿ�󹤾ߣ�HTTP�鵵��HAR����

Save as HAR with Content(���Ϊ�����ݵ�HAR)
����������������ÿ��ҳ����Դһ�𱣴浽HAR�ļ��С���������Դ������ͼ��
������ΪBase64�����ı���

Clear Browser Cache�������������棩
�����������ٻ��档��ʾ����Ҳ���Դ�Network Conditions����������������ʽ���������û������������档

Clear Browser Cookies����������Cookies��
��������Cookies��

Open in Sources Panel����Դ�ļ�����д򿪣�
��Sources��Դ�ļ�������д�ѡ������Դ��

Open Link in New Tab�����±�ǩҳ�д����ӣ�
���±�ǩҳ�д���ѡ��Դ��
����������Requests Table�������б���˫����Դ���ơ�

Copy Link Address���������ӵ�ַ��
����ԴURL���Ƶ�ϵͳ�����塣

Save�����棩
������ѡ���ı���Դ������ʾ���ı���Դ�ϡ�

Replay XHR�����·���XHR��
���·�����ѡ��XMLHTTPRequest������ʾ��XHR��Դ�ϡ�
---------------------------------------
�鿴��Դ�����ߺ�������ϵ
��סShift���ƶ���굽��Դ�Ͽɲ鿴���ķ����ߺ�������ϵ���ⲿ�����������ͣ����Դ��target��Ŀ�꣩���á�
--ȥ��Ѱ���ĸ���Initiatorÿ��������˭����


��target��Ŀ�꣩���ϲ��ң���һ����ɫ����Ϊ��ɫ����Դ��target��Ŀ�꣩���²��ң��κ���ɫ����Ϊ��ɫ����Դ����target��������
---------------------------------------
Ѱ���Ƽ��ӿڣ�

���ֻ�ܸ��������ο�����Щ���ݻ���JS��....
XHR������JS������other������ALL������Search all filesȫ�����������ȭ����

---------------------------------------
Urlȥ��
���ݿ�ȥ��

1.why��Ҫ����URLȥ�أ�
�����Ѿ�ץȡ�������ӣ����г־û���������������ʱ����ؽ���ȥ�ض��У���һ���Ƚ�ǿ��������ҪӦ������������ܣ�����Ҫ�����������ӡ�

2.���ȷ��ȥ��ǿ�ȣ�
������ȡ����ȷ��ʹ��ȥ��ǿ�ȣ�
ץȡ������һ��Сʱ�ڣ�����Ҫ���Ѿ�ץȡ���������־û���
ץȡ������һ���ڣ���ץȡ����������30w���£�����Ҫ��ץȡ������һ����Լ򵥵ĳ־û���
ץȡ������һ�����ϣ���Ҫ��ץȡ���������רҵ�ĳ־û���

3.URLȥ�ط��������ֽ������
A�Ѿ���õ�����ϵ�У�
scrapy-deltafetch
scrapy-craql-once
scrapy-redis
--�ֲ�ʽ��ܣ�Ҳ��������������urlȥ�أ��ϵ�
scrapy-redis-bloomfilter
--���ӽ�ʡ�ڴ棬���Դ洢����url��������ļ�ǿ��

B�Լ�������
�Լ�д��init_add_request����
��������ʵ��
---------------------------------------
scrapy-deltafetch��װ
1.��װBerkeley DB
--�ڹ������أ�������
https://www.lfd.uci.edu/-gohlkee/pythonlibs/#bsddb3
2.��װbsddb3

3.��װscrapy-deltafetch


scrapy-deltafetch�����ã�spider�м����
SPIDER_MIDDLEWARES ={
  'scrapy_deltafetch.DeltaFetch':100,
}
# --�Ƿ�������
DELTAFETCH_ENABLED = True
--�ļ�·��
DELTAFETCH_DIR = 'D:\work'
--�Ƿ�����
DELTAFETCH_RESET = 1
--����������������
scrapy crawl example -a deltafetch_reset =1

deltafetch_key
---------------------------------------
scrapy-deltafetchʵ��
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
��spider�м����
import scrapy-deltafetch

from .muddlewar import DeltaFetch
--�鿴Դ��
process_spider_output ���أ�

_get_key����һ��Ψһ��ʶ
--�õ�һ���ؼ���key��deltafetch_key��
request_fingerprint(request)
--ȥ��ָ��

hash �����ַ���
---------------------------------------
dupefilter.py
set ���Ե�Ψһ�ģ�
��ȥ�صĺ��ģ�def request_seen(self,request)
scrapy(�������)	��ͣ���ڻָ�����ķ���
if self.file:
    self.file.write(fp +os.lineseep)
ʵ������
--url�־û��Լ�Ҫ����
---------------------------------------

����һ����Ŀ
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



--��settings�л���ROBOTSTXT_BEY =True �޸�ΪFalse��
--main.py
---------------------------------------
д�������ļ�main.py����������

pipelines.py




---------------------------------------
#init_utils��ʵ��
def init_add_request(spider,url:str):
"""
�˷��������ڣ�scrapy������ʱ�����һЩ�Ѿ��ܹ���url�������治��Ҫ�ظ���
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
����SCHEDULER_PERSIST = True ��ʵ�ֶ��в������
���ʵ�ֹ��ϴӶϵ�����

---------------------------------------
���ݿ�ȥ��
�����Ͻ�������Ӧ�����ȶ�url����ȥ�ɹ������ݿ�ȥ����һ����ǣǿ�ķ���
���ݿ�ȥ�أ�Ӧ�þ���ʹ�����ݿⱾ��ĸ��ֻ���ȥȥ�أ���Ψһ��

---------------------------------------

�������
����ѡ��ǹ�ϵ���ݿ�MongoDB��
'''
