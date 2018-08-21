from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen

baseURL = 'http://cs.carleton.edu/faculty/jondich/courses/cs257_s16/'
html = urlopen(baseURL).read()
soup = BeautifulSoup(html, "lxml")

officeHoursString = str(soup.find("div", "office_hours"))
ignoreChars = ['<','>','/','=','br','div','em','class','"']

for ch in ignoreChars:
	officeHoursString = officeHoursString.replace(ch, "")

print '\n'+officeHoursString+'\n'