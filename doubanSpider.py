#coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#定义一个函数用于抓取豆瓣书籍２５０的信息
def catchMessage():
	i=0
	while i <= 250:
		urlStr = 'https://book.douban.com/top250?start=%d'%i
		page = urllib2.urlopen(urlStr) 
		contents = page.read() 
		soup = BeautifulSoup(contents) 
		print('豆瓣图书250')	
		for tag in soup.find_all('tr', class_='item'): 
			book_Name = tag.div.a['title']
			book_UsName = tag.span.get_text() 
			book_Message = tag.p.get_text()
			book_score = tag.find('span',attrs={'class':"rating_nums"}).string
			peopleNum = tag.find('span',attrs={'class':'pl'}).string
			peopleNum = peopleNum.replace('(','').replace(')','').replace('\n','').strip()
			print("%s\n%s\n%s\n%s\n%s"%(book_Name, book_UsName, book_Message, book_score, peopleNum)) 		                     
			print("正在把书籍信息写入本地文件。。。。。。")
			print("="*60)		
			result='\n'+ book_Name +'\n'+ book_UsName +'\n'+ book_Message +'\n'+  book_score +'\n'+ peopleNum +'\n'+'*'*60 +'\n'
			saveBookMessage(result)	
		i+=25
#定义一个函数用于保存抓取到的数据至本地文本文件中
def saveBookMessage(result):
	file=open('bookMessage.txt','a+')
	file.write(result)
	file.close()
catchMessage()
