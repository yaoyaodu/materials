import requests
from lxml import etree # 用于解析
import pandas as pd  

website = 'http://www.jkl.com.cn/shop.aspx'
uaagent = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'}

# 1. 拿取每个城区网址
obtain_info = requests.get(url=website,headers=uaagent).text
# print(obtain_info)
jiexi = etree.HTML(obtain_info)
chengqu = jiexi.xpath('//div[@class="infoLis"]//@href')  #解析数据,拿取每个城区的网址。找网址标签对应的class: infoLis 一个/代表一个层级，//代表多个层级
# print(chengqu)
# 获取并解析每个城区网址中的内容
for qu in chengqu:
	chengquwebsite = 'http://www.jkl.com.cn/' + qu
	# print(chengquwebsite)
	obtain_info_eachqu = requests.get(url=chengquwebsite,headers=uaagent).text
	jiexi1 = etree.HTML(obtain_info_eachqu)
	dianpumingcheng = jiexi1.xpath('//span[@class="con01"]/text')
	xiangxidizhi = jiexi1.xpath('//span[@class="con02"]/text')
	dianhua = jiexi1.xpath('//span[@class="con03"]/text')
	yingyeshijian = jiexi1.xpath('//span[@class="con04"]/text')
	list1 = []
	for dianming in dianpumingcheng:
		dianmingxin = dianming.strip()
		list1.append(dianmingxin)
	data = pd.DataFrame({'店名':list1,'地址':xiangxidizhi,'电话':dianhua,'营业时间':yingyeshijian})
	data.to_csv('C:/店铺信息.csv',index=False,header=0,mode='a',encoding='ANSI')

#print(list1)





