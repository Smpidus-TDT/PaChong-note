#coding=utf-8
'''
使用正则获取url然后批量下载
'''
#导入正则表达式模块
import re
#导入urllib.request模块
import urllib.request


def getHtml(url):
    htmlCode = urllib.request.urlopen(url).read()
    return htmlCode

def getImagesAddress(htmlCode):
    htmlCode = htmlCode.decode('utf-8')
    imagesList = re.findall(r'src="(.*?\.(jpg|png))"', htmlCode)
    print(len(imagesList))
    return imagesList
def downloadImages(imagesList):
    j = 1
    for image in imagesList:
        imageUrl = image[0]
        if (imageUrl.endswith('.jpg')):
            urllib.request.urlretrieve(imageUrl, 'F:\\douyu\\images\\%d.jpg'%j)
        else:
            urllib.request.urlretrieve(imageUrl, 'F:\\douyu\\images\\%d.png'%j)
        j += 1

if  __name__ == '__main__':
    htmlCode = getHtml('https://www.douyu.com/')
    imagesList = getImagesAddress(htmlCode)
    downloadImages(imagesList)
