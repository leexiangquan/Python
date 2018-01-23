import requests
import bs4
from bs4 import BeautifulSoup
import re

def get_html_text(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		"Failed to load HTML"
	return ""

def fill_professors_list(text_list, html):
	soup = BeautifulSoup(html, "html.parser")
	ps = soup.find_all('p', style=re.compile("LAYOUT-GRID-MODE"))
	for i in range(len(ps)):
		p = ps[i]
		span = p.find_all('span', style=re.compile("FONT-FAMILY: 宋体"))
		if len(span) == 2:
			text_list.append([span[0].string.strip(), span[1].string.strip()])


def print_professors_list(text_list, num=20):
	tplt = "{0:^10}\t{1:{2}^15}"
	print(tplt.format("姓名", "单位", chr(12288)))
	if num > len(text_list):
		num = len(text_list)
	for i in range(num):
		info = text_list[i]
		print(tplt.format(info[0], info[1], chr(12288)))

def main():
	text_list = []
	url = "http://www.waterscience.cn/wrc/News/news_view.asp?newsid=389"
	html = get_html_text(url)
	fill_professors_list(text_list, html)
	print_professors_list(text_list, 500)

main()