import urllib.request
import json
upID = 21620236
num = 100
data = urllib.request.urlopen('https://space.bilibili.com/ajax/member/getSubmitVideos?mid='+str(upID)+'&pagesize='+str(num)+'&tid=0&page=1&keyword=&order=pubdate')
jsondata = json.load(data)
x = 0
for item in jsondata['data']['vlist']:
	imgdata = urllib.request.urlopen('http:'+item['pic'])
	img = imgdata.read()
	file = open(str(upID)+'img'+str(x)+'.jpg','wb')
	file.write(img)
	x = x + 1