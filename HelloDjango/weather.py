#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import codecs
import urllib.request
import re

def find_code(city_dict,name):
	return city_dict[name]
	
def readfile(filepath):
	output = codecs.open(filepath,'r','utf-8')	
	line = output.readline()	
	city_dict = {}
	while line:
		city = line.strip(' \n').split(' : ')
		city_dict[city[0]] = city[1]
		line = output.readline()
	output.close()
	return city_dict

def weatherfind(city_name):
	if isinstance(city_name, bytes):
		city_name = city_name.decode('utf-8')
	cityname_dict = readfile('HelloDjango/cites.txt')
	try:
		city_code = find_code(cityname_dict,city_name)
		
	except:
		city_code = None
		return(u'未找到:%s，请核对后重新输入！！！' % city_name)
		
	if city_code != None:
		url = 'http://www.weather.com.cn/weather1d/%s.shtml#around2' % city_code
	#	print(url)
		content = urllib.request.urlopen(url).read().decode('utf-8')
		
		key1='var hour3data='              #设置关键字1
		key2="</script>"                   #设置关键字2
		pa=content.find(key1)+22 					 #找出关键字1的位置
		pt=content.find(key2,pa)           #找出关键字2的位置(从字1后面开始查找)
		urlx=content[pa:pt].strip('"]]}\n')#.split('","')   #得到关键字1与关键字2之间的内容(即想要的数据)
		#print(urlx[:60])
		ptr = re.compile(r'\d+\w\d+\w,\w+,\w+,[-]?\d+℃,\w+,\w+[,]?[\d]?') #匹配天气信息
		weather = re.findall(ptr,urlx)
		return weather