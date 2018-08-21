from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests

baseURL = 'https://apps.carleton.edu/campus/directory/?search_for=faculty&department=Computer+Science'
page = requests.get(baseURL)
soup = BeautifulSoup(page.content, 'html.parser')

faculty = soup.find_all('li', class_="person")
for f in faculty:
	# print("{}{}".format(f, '\n'))

	name = f.find('div', class_="group1").find('a').text
	title = f.find('p').text
	website = f.find('div', class_="urls")
	website = website.find('a')['href'] if website != None else ""
	print("Name: {} \nTitle: {} \nWebsite: {} \n".format(name, title, website))




