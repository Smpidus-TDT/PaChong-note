day zero:
#!/usr/bin/env python

#只要变为执行文件，就需先声明；env找环境变量
#!/usr/bin/ python

print ("Hello World!")

#windows
python 180717.py

#Linux 授权chmod 755 180717.py 
./180717.py

File>Project>Directory>python file
view>too>settings>file and code templates;
变量：存东西调用；
name = "Smpidus TDT"
name2 = name
print("My name is",name,name2)

name = "PaoChe Ge"
print (name,name2)
#变量名只能是字母、数字或下划线的任意组合，第一个字符不能是数字；



day one:用户交互程序
注释：一行使用#
多行使用：三个单引号或者三个双引号
'''   '''
"""   """

#!/usr/bin/env python
name = input("name:")
#integer整型,
#raw_input 2.x  ； input 3.xrange
#input 2.x = 接收的什么格式就是什么格式；无双引号是变量；
name = int(input("age:"))
#打印数据类型,  整型，在转义回去
print（type(age),type(str(age)
name = input("job:")
name = input("salary:")

info = '''
--------info of  %s------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name,name,age,job,salary)

print(info)

"""格式化输出，
%d 只能输入数字，帮你检测
%f 浮点型，小数
%s
"""

#第二种方式
info2 = '''
----- info of {_name} ---
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
		   
print(info2)

#第三种方式
info3 = '''
----- info of {0} ---
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary=salary)
print(info3)

-------if else流程判断
#密码用密文显示，py标准库，调用模块getpass
#pycharm里面看不出来，可以在命令行进行执行
#不加单引号，默认为变量；
import getpass

_username = 'alex'
_password = 'abc123'
username = input("username:")
password = input("password:")
#password = getpass.getpass("password:")

if _username == username and _password == password:
    print("Welcome user {name} login..".fomat(name=username))
else:
    print("Invalid username or password!")

print(username,password)

-----IndentationError代表缩进错误
--你以为你拥有了物质，其实是物质拥有了你，你成为了物质的奴隶。
猜年龄
age_of_oldboy = 56
guess_age = int(input("guess age:"))
if guess_age == age_of_oldboy:
    print("yes,you got it")
elif guess_age > age_of_oldboy:
    print ("think smaller.")
else :
    print("think bigger!")


--while循环
#不断循环，True代表真，说明这个条件成立；break跳出
count = 0
while True:
    print("count:",count)
    count = count+1 #count+=1
	if count == 1000:
	    break

--结合起来
age_of_oldboy = 56

count = 0
while True:
    if count = 3:
	    break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it")
		break
    elif guess_age > age_of_oldboy:
        print ("think smaller.")
    else :
        print("think bigger!")
	#计数
	count +=1
	
------优化
age_of_oldboy = 56

count = 0
while count <3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it")
		break
    elif guess_age > age_of_oldboy:
        print ("think smaller.")
    else :
        print("think bigger!")
	count +=1

-----人性化
age_of_oldboy = 56

count = 0
while True:
    if count = 3:
	    break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it")
		break
    elif guess_age > age_of_oldboy:
        print ("think smaller.")
    else :
        print("think bigger!")
	count +=1
#if count ==3:
else:
    print("you have tried too many times..fuck off")
	
	
Day Three:
----while循环优化

#
for i in range(10):
    print("loop",i)

#隔1个打一个
for i in range(0,10,3):
    print("loop",i)
	
#隔2个打一个
for i in range(0,10,2):
    print("loop",i)
	
#使用for循环，break结束循环
age_of_oldboy = 56
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it")
		break
    elif guess_age > age_of_oldboy:
        print ("think smaller.")
    else :
        print("think bigger!")
	count +=1
else:
    print("you have tried too many times..fuck off")


#3次失败后是否继续玩,如果输入n就退出；count=0重置；
age_of_oldboy = 56
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it")
		break
    elif guess_age > age_of_oldboy:
        print ("think smaller.")
    else :
        print("think bigger!")
	count +=1
	if count == 3:
	    continue_confirm = input("do you want to keep guessing")
		if countinue_cofirm != 'n':
		    count = 0
else:
    print("you have tried too many times..fuck off")


----左鼠标加入断点，进入调试；
----continue跳出本次循环，进入下次循环
for i in range(0,10):
    if i <5:
	    print("loop",i)
	else:
	    continue
    print("hehe")

---循环套循环
---break结束当前循环，大循环是10次；
for i in range(10):
    print('----------',i)
	for j in range(10):
	    print(j)
#小于5，结束当前循环，打印6次；	
		if j >5:
		    break


#写博客；

ASCII 255 1bytes
    -->1980 gb2312 7xxx
	    --->1995 GBK1.0 2w+
		  --->2000 GB18030 27xxx
		--->unicode 2bytes
		   --->uft-8 en:1byte,zh:3bytes

金角大王
http://www.cnblogs.com/alex3714/articles/5465198.html
http://www.cnblogs.com/alex3714/category/770733.html


Day four:模块初识

模块（库）不要使用中文命名；
----标准库（直接调入）、第三方库（需要下载安装）
自己写入的模块
放入此目录下python/lib/site-packages；
或者放入环境变量；

sys是一个模块，需要调用打印，需要加入点；
调入sys，默认导入系统里面自带的；起模块名字不能跟文件名一样；
import sys

print(sys.path) #打印出模块文件目录，打印环境变量；
#python第三库库一般默认在site-packages文件夹中；
#标准库放到python/lib/；

import sys
print(sys.argv)
#打印了绝对路径（调用时就采用了绝对路径）；
#命令行打印相对路径；python sys_mod.py 1 2 3
print(sys.argv[2])

import os
os.system("dir")
#打印出目录，出现乱码没事；Windows中的utf-8和工具打印的不一样；

import os
#cmd_res = os.system("dir") #执行命令，不保存结果；0成功，-1失败；
#cmd_res = os.popen("dir") #打印内存的结果
cmd_res = os.popen("dir").read()#read打印出来就是中文；
print("-->",cmd_res)
os.mkdir("new_dir") #新建一个目录；

Day five：pyc是什么（预编译后的）

#py2 login.py调用后自动生成login.pyc;
#py3 login.py 调用后生成一个文件夹_pycache_中生成了login.pyc;
#c应该是compiled的缩写才对；
#Java是一种先编译后解释的语言（预编译）；
javac hello.java
java hello
#在命令行先预编译；


"""当Python程序运行时，编译的结果则是保存位于内存中PyCodeObject中，当Python程序运行结束时，Python解释器则将PyCodeObject写回到pyc文件中；
"""

#2-05数据类型

1.数字
int整型
long长整型
float浮点型
complex复数
#type查看数据类型
命令行输入
py3无长整型，自动转换；py2整型和长整型
type(2*32)
type(2**62)

#浮点型float，包含小数----E标记表示10的幂，
#命令行输入52.3E4  值
#命令行输入52.3* 10**4 值
#复数complex   j为序数，工程领域，例如：量子学；


2.布尔值  真或假 1或0  
True False
>>>a=0
>>>if a:print('a')
...
>>>a=1
>>>if a:print('a')
...
a

http://edu.51cto.com/course/6039.html?source=so

#三元运算
>>>a,b,c = 1,3,5
>>>d = a if a >b else c
>>>d
5
>>>d = a if a <b else c
>>>d
1

#进制
二进制与十六进制之间如何互相转换
https://jingyan.baidu.com/article/47a29f24292608c0142399cb.html

十进制

十六进制0123456789ABCDEF  （15）后缀H ，前缀0X

#bytes类型  字节 
#二进制decode转为字符串；encode解码；string<----->bytes
#py2  不区分 ；
#py3 不能拼接字符串和字节包，也无法在字节包里搜索字符串（反之亦然）；
#--传数据到对方设备上，必须转为二进制；
http://www.cnblogs.com/txw1958/archive/2012/07/19/2598885.html
>>>'$20'.encode('utf-8')
#解码
>>>b'\xe2\x82\xac20'.decode('utf-8')


msg="我爱西安"

print(msg)
#不声明，默认系统自带的
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8")


链接：
https://pan.baidu.com/s/1g1YjtFFljPJkkjRdTk_Yeg
密码：c6u8

#列表的使用 切片
import copy  #独立一个模块，进行深层copy（克隆）
names = ["4zhangyang","#!guyun","xxiangpeng",["alex","jack"],"chenronhua","xuliangchen"]
#name2 = names.copy()   #浅copy是一层
#浅copy是一层，深copy是两层；
name2 = copy.deepcopy(names)
#name2=names
print(names)
print(name2)
names[2] = "向鹏"  #修改为中文
names[3][0]="ALEXANDER" #修改为大写字母



names = ["4zhangyang","#!guyun","xxiangpeng",["alex","jack"],"chenronhua","xuliangchen"]

#循环
for i in names:
    print(i)

#range(1,10,2)
	
print(names[0:-1:2]) #跳着切
print(names[::2])     #0和-1可以省略
pint(mames[:])




#通过空格或者逗号
name ="zhangyang guyun xiangpeng xuliangchen"
names = ["zhangyang","guyun","xiangpeng","xuliangchen"]
print(names)
print(names[0],names[2])
print(names[1:3]) #切片
print(names[3]) #切片
print(names[-1]) #切片,选最后一个
print(names[-3:-1]) #取后面，倒序排列；
print(names[-2:])   #取最后两个值，0可以省略
print(names[:3])    #取前面三个值，0可以省略


name ="zhangyang guyun xiangpeng xuliangchen"
names = ["zhangyang","guyun","xiangpeng","chenronghua"，"xuliangchen"]
names.append("leihaidong") #追加
names.insert(1,"chenronghua") #插入
names.insert(3,"xinzhiyu")
names[2] = "xiedi"  #修改
#delete
#names.remove("chenronghua")
#del names[1] = nmaes.pop(1)
#nmaes.pop() #pop删除最后一个
print(names)
print(names.index("xiedi")) #查找所在位置
print(names[names.index("xiedi")]) #查找到打印出来


names = ["4zhangyang","#!guyun","xiangpeng","xuliangchen"]
print(names.count("chenronghua")) #总数
#names.chlear() #清空
names.reverse() #反转
names.sort()    #排序,特殊符号第一，下来是数字，再下来是字母（按ascii码顺序排列）；

print(names)
names2 = [1,2,3,4]  #隔壁班级

names.extend(names2)  #合并过来
#del names2  #删除变量
print(names)

------------------
#浅copy
import copy

person=['name',['saving',,100]]

'''三种模式
p1=copy.copy(peerson)
p2=person[:]
p3=list(person)
'''
p1=person[:]
p2=person[:]

#举例：p1是自己，p2是他媳妇，他们有共同的银行卡，取了50元；
p1[0]='alex'
p2[0]='fengjie'
p1[1][1]=50

print(p1)
print(p2)
--------------------------------------
#元组tuple（只读列表）不能进行增删改，只能查；
它只有2个方法，一个是count，一个是index；
name = ('alex','jack')
names.append('ddd')
#报错
-------------------------------------
#购物车程序

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),
]
shopping_list = []  #为空
#请输入你的工资（第一）
salary = input("Input your salary:")
if salary.isdigit():   #默认为字符串，判断工资是不是数字
    salary = int(salary)   #转换成整型int
	while True:
	    for index,item in enumerate(product_list):  #打印商品列表
		    print(index,item)
        #for item in product_list:
		    #print(product_list.index(item).item)通过下标查找编号

		user_choice = input("选择要买嘛？>>>:")
		if user_choice.isdigit():  #
		    user_choice = int(user_choice)  
			if user_choice < len(product_list) and user_choice >=0:
			    p_item = product_list[user_choice]  #通过下标查找编号
				if p_item[1] <= salary`:  #买的起
				    shopping_list.append(p_item)  #添加到shoppint_list
					salary -= p_item[1]
					#高亮显示\033[31;1m%s\033[0m，%s
					print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
					#salary余额
				else:
				    print("\033[]41;1m你的余额只剩[%s]啦，还买个什么\033[0m" % salary)
				#大于6，商品不存在
				else:
				    print"("product code [%s] is not exist!"% user_choice)  
		elif user_choice == 'q'
		    print("----------shopping list--------------")
			for p in shopping_list:
			    print(p)
			print("Your current balance:",salary)
			exit()
		else:
		    print("invalid option")
		

-----------------------------
命令行
>>> a = [1,2,3]
>>> enumerate(a)

>>>for i in enumerate(a):print(i)
---------------------------------
字符串
name = "my \tname is alex "

print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("ex"))
print(name.expandtabs(tabsize=30))    #加入\t
print(name[name.find("name"):9])   #字符串也可以切片，跟列表一样
print(name.find("y")    #返回4，字符串也可以切片
-----------------------------------------------------------------
name = "my \tname is {name} and i am {old}"
print(name.fomat(name='alex',year=23))
print(name.fomat_map({'name':'alex'.'year':12}))   #字典，很少用到
print(name.isalnum())   #阿拉伯字符,包含小数字母
print('ab123'.isalnum())
print('abA'.isalpha())   #大写字母
print('1A'.isdecimal())   #十进制
print('1A'.isdigit())     #是否整数
print('a 1A'.isidentifier())    #判断是不是一个合法的标识符（变量名）
#切记不可用中文，大小写字母，空格
print('33'.isnumeric())  #只有数字
print('My Name Is '.istitle())
print('My Name Is '.isprintable())  #tty file ,drive file
print('My Name Is '.isupper())
print('+'.join(['1','2','3']))
print(name.ljust(50,'*'))    #长度50，不够用*补全
print(name.rjust(50,'-'))
print('Alex'.lower())       #把大写变为小写
print('Alex'.upper())        #把小写变为大写
print('\nAlex'.lstrip())      #从左边去空格
print('Alex\n'.rstrip())      #从右边去空格
print('   Alex\n'.strip())      #两边都去掉
print('---')
------------------------------------------------
p = str.maketrans("abcdefli","123$@456")  #加密
print('alex li'.translate(p))
------------------------------------------------
print('alex li'.replace('l','L',1))    #把小写l替换大写L,只替换一个,1
print('alex lil'.rfind('l'))  #从左往右，查找到最后一个值的小标返回
print('1+2+3+4'.split('+'))   #有一段字符，将数字提取出来
print('1+2\n+3+4'.splitlines())   #按换行来取
print('Alex Li'.swapcase()）  #大小写呼唤
print('lex li'.title())       #第一个字母大写
print('lex li'.zfill(50))      #不够了进行填充；
-----------------------------------------------------------
http://www.cnblogs.com/alex3714/articles/5717620.html

---------------------------------------------------------
集合 字典
dict是无序的
key必须是唯一的，so天生去重
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
print(info)
#print(info["stu1101"])

info["stu1101"]="武藤兰"   #存在进行修改
info["stu1104"]="CangJingkong"   #没有进行新增
print(info)

#del删除
del info["stu1101"]
info.pop("stu1101")
info.popitem()   #随机删除
print(info)
------------------------------
#查找
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

#info['stu1104']   #查找时，不存在会报keyerror，不建议使用
print(info.get('stu1103'))   #安全获取状态用get

print('stu1103' in info)   #info.has_key("1103")  in py2.x
-----------------------------------------------------------
多级字典嵌套及操作
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
#key不要写中文，这里只是演示；
av_catalog["大陆"]["1024"][1] += ",可以在国内做镜像"
#av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
#ouput ['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']


av_catalog.setdefault("taiwan",{"www.baidu.com":[1,2])  #能取到值进行修改，取不到进行新增
print(av_catalog)

-----------------------
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
b = {
    'stu1101': "Alex",
	1:3,
	2:5;
}
info.update(b)  #（b相当于参数）两个字典合并，交叉更新，无交叉创建
c = info.fromkeys([6,7,8],"test")   #c
print(c)
print(info.items())

c = dict.fromkeys([6,7,8],[1,{"name","Alex"},444]) 
print(c)
c[7][1]['name'] = "Jack Chen"   #一份列表的数据全部修改，除非只有一层
print(c)
------------------------------------
字典的循环

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

for i in info:
    print(i,info[i])  #最基本循环，建议用这个循环
	
#上面直接，下面直接but把字典变成列表（数据量大，需等待）；
for k,v info.items():
    print(k,v)
-------------------------------
三级菜单

data = {
    '北京':{...},
	    '昌平':{
		    "沙河":["oldboy","test"],
			"天通苑":["链家地产","我爱我家"],
		},
		'朝阳':{
		    "望京":["奔驰","陌陌"],
			"国贸":["CICC","HP"],
			"东直门":["Advent","飞信"],
		.},
		'海淀':{},
         }，
		 '山东':{
		    "德州":{},
			"青岛":{},
			"济南":{},
		}，
		 '广东':{
		    "东莞":{},
			"常熟":{},
			"佛山":{},
		}，
} 
		 
exit_flag = False

#while True:
while not exit_flag:
    for i in data:
	    print(i)   #第一层
		
	choice = input("选择进入1>>:")
	if choice in data:
	    while not exit_flag:
		    for i2 in data[choice]   #进入下一层
			    print("\t",i2)     #第二层
			choice2 = input("选择进入2>>:")
			if choice2 in data[choice]:
				while not exit_flag:
		            for i3 in data[choice][choice2]:   #进入下一层
			             print("\t\t",i3)    #第三层
			        choice3 = input("选择进入3>>:")
					if choice3 in data[choice][choice2]:
					    for i4 in data[choice][choice2][choice3]:
						    print("\t\t",i4)   #第四层
			            choice4 = input("最后一层，按b返回>>:")	
						if choice4 == "b":
						    pass     #相当于什么都不做，是占位符，不进行报错；
						elif choice4 == "q":
				             exit_flag = True
					if choice3 == "b":
				        break
			         elif choice3 == "q":
				         exit_flag = True
				if choice2 == "b":
				        break
			         elif choice2 == "q":
				         exit_flag = True
----------------
'''
购物车
用户入口
1.商品信息存在文件里
2.已购商品，余额记录

商家入口：
2.可以添加商品，修改商品价格
http://www.cnblogs.com/alex3714/articles/5740985.html

《追风筝的人》 《白鹿原》《林达看美国》4部曲
开始看书

列表（增删改查，可以嵌套任何东东）、元组（只读列表）都是有序的；
字符串（只查，不可以修改）；
字典是无序的，通过key找值；
集合是无序的（去重，关系测试--交集、并集、差集、子集....）
'''
list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_2 = set([2,6,0,66,22,8,4])
print(list_1,type(list_1))

>>>{1,4,5,7,3,6,7,9}{2,6,0,66,22,8,4}
#取交集
print(list_1.intersection(list_2))

>>>{4,6}
#并集
print(list_1.union(list_2))
>>>{0,1,2,3,4,5,6,7,66,9,8,22}
#差集（在我这里有你那里没有，在你那里有我这儿没有）
 #1里面有2里面没有 in list_1 but not in list_2
print(list_1.difference(list_2)) 

print(list_2.difference(list_1))

#子集
list_3 = set ([1,3,7])
print(list_1.issubset(list_2))
>>>False
print(list_3.issubset(list_1))
>>>True 
#父集
print(list_1.issuperset(list_2))
>>>False
print(list_1.issuperset(list_3))
>>>True 

#对称差集
print(list_1,symmetric_difference(list_2)

print("---------------")
list_4 = set ([5,6,7,8])
print(list_3.isdisjont(list_4)) #return true if two sets have a null in 
--------------------------------------------------

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_2 = set([2,6,0,66,22,8,4])

#交集
print(list_1 & list_2)
#并集
print(list_2 | list_1)
#差集difference
print(list_1 - list_2) # in list 1 but not in list 2
#对称差集
print(list_1 ^ list_2)
#子集subset and upperset

#本身去重，没有重复信息
list_1.add(999)  #添加一项
list_1.update([888,777,555])   #添加多项

print(list_1.pop())  #任意删除

print(list_1 remove()) #不存在报错

print(list_1 discard("888"))  #删除没有返回
------------------------------------------------------
'''
http://www.cnblogs.com/alex3714/articles/5717620.html
windows默认打开编码是gbk，py里面打开默认utf-8，不匹配；
----------------------
Somehow, it seems the love I knew was always the most destructive kind
不知为何，我经历的爱情总是最具毁灭性的的那种
........
------------------
'''
data = open("yesterday",encoding="utf-8").read()
print(data)
-----------------------
#文件句柄（赋给f文件对象）,r读模式；
f  = open("yesterday",'r',encoding="utf-8") 
data = f.read()
data2 = f.read()
print(data)
#print('----------data2-------%s-----',%data2)
------------------------------------
#w写模式，创建一个文件，就会覆盖到之前的；
f = open("yesterday2",'w',encoding="utf-8") 
f.write("我爱你,\n")
f.write("康,\n")

---------------------------------------------
#a = append 追加
f = open("yesterday2",'a',encoding="utf-8") 

f.write("我爱你...,\n")
f.write("康...,\n")
f.close()
------------------------------
f = open("yesterday2",'a',encoding="utf-8") 
f.write("\n when i was young i listen to the radio...,\n")
data =f.read()
print('---read',data)
f.close()
-------------------------------------
f = open("yesterday2",'r',encoding="utf-8") #文件句柄
	
#打印前5行
for i in range(5):
    print(f.readline())
------------
f = open("yesterday2",'r',encoding="utf-8")
for line in f.readlines():
    print(line.strip())
--------------
#循环low loop
f = open("yesterday2",'r',encoding="utf-8")
for index,line in enumerate(f.readlines())
    
    if index == 9:
        print('-------我是分割线-------')
	   continue
	print(line.strip())
-----------------------------
#一行一行读取，内存只保存一行high bige
f = open("yesterday2",'r',encoding="utf-8")
count = 0
for line in f:
    if count == 9:
	    print('-------我是分割线-------')
		continue
    print(line)
	count +=1
--------------------------------
f = open("yesterday2",'r',encoding="utf-8")
for index,line in enumerate(f.readlines())
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
print(f.tell())	
f.seek(10)  # 回到第10,打印一行，从当前位置到换行符
print(f.readline())
	
print(f.ecoding)
print(f.flush())   #达到一定程度进行刷新,例如：交了钱未刷新
print(dir(f.buffer())

----------------------------------
#实时刷新
>>>f = open("test.text","w")
>>>f.write("hello1\n")
7   #打开文件无内容
>>>f.flush()          #刷新一次
>>>f.write("hello2\n")
7
>>>f.flush()
	
----------------------------------
>>>print("#")  #打印#直接换行
#
>>> sys.stdout.write("#")
#1
>>> sys.stdout.write("#####")
#4
---windows无法使用
#打印进度条,flush缓冲
import sys,time

for i in range(20):
    sys.stdout.write("#")
	sys.stdout.flush()
	time.sleep(0.1)
-----------------------------
#截断，指定和不指定--从0开始
f = open("yesterday2",'a',encoding="utf-8")
#f.truncate()   #什么都不写会将文件清空
f.seek(10)      #跳转到10开始截断
f.truncate(20)
-------------------------
'''已读和追加的格式  ，读写'''
#a+追加读
f = open("yesterday2",'r+',encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
f.write("------------diao----------------")
print(f.readline())
-------------------------------------------
#写读，先创建文件
#修改的时候，原文件几个字符就修改几个字符（内容覆盖）
f = open("yesterday2",'w+',encoding="utf-8")  
print(f.readline())
print(f.readline())
print(f.readline())
f.write("------------diao----------------1\n")
f.write("------------diao----------------1\n")
f.write("------------diao----------------1\n")
f.write("------------diao----------------1\n")
print(f.tell())  #写4行
f.seek(10)
print(f.tell())   #从第10行
print(f.readline())
f.write("should be at the begining of the second line")
f.close()
------------------------------------------
#rb 读二进制文件py3 ，在网络传输时使用
f = open("yesterday2",'rb')
print(f.readline())
print(f.readline())
print(f.readline())

#写读二进制，这个文件以二进制编码的
f = open("yesterday2",'wb')
f.write("hello binary\n".encode())  #本身的编码
f.close()
---------------------------------------------------
3-7\8

#vim先读取文件写入缓存中，在进行修改；
#打开旧文件，写入新文件
f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday2.bak","w",encoding="utf-8")

for line in f:
    if "肆意的快乐" in line:
	    line = line.replace("肆意的快乐","肆意的快乐等Alex享受")
	f_new.write(line)
f.close()
f_new.close()
-------------------------------
#实现简单的shell sed替换功能
import sys 
f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday2.bak","w",encoding="utf-8")

find_str = sys.argv[1]
replace_str = sys.argv[2]
for line in f:
    if "find_str" in line:
	    line = line.replace(find_str,replace_str)
	f_new.write(line)
f.close()
f_new.close()	
#操作完了一定要关闭	
---------------------------------
#同时打开多个文件，with帮你自动关闭
import sys 
f = open("yesterday2","r",encoding="utf-8")

with open("yesterday2","r",encoding="utf-8") as f ,\
     open("yesterday2","r",encoding="utf-8") as f2:
    for line in f:
	    print(line)
		#一行代码不能超过80个字符,\
--------------------------------------------------------
#字符编码与转码
http://www.cnblogs.com/luotianshuai/articles/5735051.html
acsill不能存储中文，只能存英文和数字，占8个字节
Unicode可以存储中文，一个占2个字节
utf-8，英文字符按acsill,中文Unicode
(py2)
#-*- coding:uft-8 -*-
import sys
print(sys.getdefaultencoding())

s = "您好"
s_to_unicode = s.decode("uft-8")
s_to_gbk = s.decode("uft-8").encode("gbk")  #之前是utf-8，解码为encode
print(s_to_gbk)
	
------------------
(py2)
#SecureCRT工具
#-*- coding:uft-8 -*-
import sys
print(sys.getdefaultencoding())

s = "您好"
s_to_unicode = s.decode("uft-8")
print(s_to_unicode,type(s_to_unicode))
s_to_gbk = s_to_unicode.encode("gbk")
print(s_to_gbk)
	
gbk_to_utf8 = s_to_gbk.decode("gbk").encode("uft-8")
print(gbk_to_utf8)
---------------------------------
(py2)
#-*- coding:uft-8 -*-
import sys
print(sys.getdefaultencoding())

s = u"您好"
print(s)

s_to_gbk = s.encode("gbk")
print(s_to_gbk)
	
gbk_to_utf8 = s_to_gbk.decode("gbk").encode("uft-8")
print(gbk_to_utf8)
--------------------------------------------------------
py3,默认Unicode，
#-*- coding:gbk -*-
s ="你好"
s_gbk = s.encode("gbk")
print(s_gbk)
print(s.encode())

gbk_to_utf8 = s.gbk.decode("gbk").encode("utf-8")
print("utf8",gbk_to_utf8)

------------------------------------------
#不管是py2还是py3都需要先转成Unicode
文件编码修改为了GBk
#-*- coding:gbk -*-   #文件头声明文件编码gbk;

import sys
print(sys.getdefaultencoding())


s = "你哈"  #虽然文件声明为gbk，但是程序里面s还是Unicode
print(s.encode("gbk"))  #因为是base类型，所有不能显示
print(s.encode("uft-8"))

print(s.encode("utf-8").decode("uft-8").encode("gb2312"))
#gb2312和gbk输出格式是一样的，gbk向下兼容gb2318,gb2318向下兼容gb2312(他们是向下兼容的),"你哈"在gbk中有2万7千多个，在gb2312有7千多，如果一个里面一个里面没有就无法进行转换；

print(s.encode("utf-8").decode("uft-8").encode("gb2312").decode("gb2312"))
#先告诉它你是gb2312(decode("gb2312")),输出是中文；
-----------------------------------------------------------
http://www.cnblogs.com/alex3714/articles/5740985.html
'''
函数与函数式编程
编程的方法：
面向对象：华山派----类----定义关键字class
面向过程：少林派----过程----定义关键字def
函数式编程：逍遥派----函数----定义关键字def
'''
#函数
def func1():
    '''testing1'''
    print('in the func1')
	return 0
#过程，没有返回中的函数,在python中给过程定义了返回值；
def func2():
    '''testing2'''
    print('in the func2')
	
x=func1()
y=func2()
print('from func1 retun is %s' %x)
>>>返回0
print('from func1 retun is %s' %y)
>>>没有定义，返回None
--------------------------------
def logger():
    with open('a.txt'.'a') as f:
        f.write('end action\n')
	
def test1():
    print ('in the test1')
	
	logger()
def test2():
    print ('in the test2')
	
	logger()
def test3():
    print ('in the test3')
	
	logger
	
#定义函数优点：代码重复利用；
--------------------
import time
def logger():
    time_format = '%Y-%m-%d %X'
	time_current = time.strftime(time_format)
	with open('a.txt'.'a') as f:
        f.write('%s end action\n' %time_current)
def test1():
    print ('in the test1')
	logger()
def test2():
    print ('in the test2')
	logger()
def test3():
    print ('in the test3')
	logger
#定义函数优点：可扩展性，保存一致性
-------------------------------------

def test1():
    print('in the test1')
>>>没有定义，返回None
def test2():
    print('in the test2')
	return 0
>>>定义返回0，返回是0	
def test3():
    print('in the test3')
	return 1,'hello',['alex','wupeqi'],{'name':'alex'}
>>>定义了返回1，返回到元组，把多个值放到元组里面	
x=test1()
y=test2()
z=test3()
print (x)
print (y)
print (z)

'''总结：
返回值数=0，返回None；
返回值数=1，返回object；
返回值数>1：返回tuple;
'''
-----------------
#形参和实参
def test(x,y)
    print(x)
	print(y)
	
test(1,2)
'''
实参：实际存在，占用空间的1,2
形参：x,y
实参和形参一一对应的；'''
----------------------------
def test(x,y)
    print(x)
	print(y)	
test(y=2,x=1) #与形参顺序无关
test(x=2,3)
>>>报错
test(3,y=2)  #满足了一一对应的关系
test(3,x=2)
>>>报错
test(3,6,y=2)  #关键字不能放到
>>>报错
test(3,z=2,y=6)
----------------------------
#默认参数特点：调用函数的时候，默认参数非必须传递
def test(x,y=2)
    print(x)
	print(y)
	
test(1)
>>>1  2
----------------------------
用途：1.默认安装值
def conn(host,port=3306)
    pass
	
conn()
----------------------------
#位置参数(赋值不能超)，默认参数，关键字参数(在位置参数后面)
#参数组
def test(x,y,z=2)
    print(x)
	print(y)
	
test(1,2,z=3)
------------------------
#实参的数目不固定，形参怎么写？
def test(*args)
    print(args)
test(1,2,3,4,5,5)
test(*[1,2,4,5,5])  
# *args=*[1,2,4,5,5]   args=tuple[1,2,4,5,5]
----
def test1(x,*args):
    print(x)
	print(args)
	
test1(1,2,3,4,5,6,7)
----
#**smpidus:把n关键字参数，转换成字典的方式
def test2(**kwargs):
    print(kwargs)
	print(kwargs['name'])
	print(kwargs['age'])
	print(kwargs['sex'])
test2(name='smpidus',age=8,sex='F')
>>>存为字典
#test2(**{'name':'smpidus','age':'8'})
----------
def test3(name,**kwargs):
    print(name)
	print(kwargs)
test3('smpidus')
#未指定，就成为了一个空字典；




3-14












