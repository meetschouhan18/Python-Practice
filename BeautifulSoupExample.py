import bs4
import requests

#bs4 contain BeautifulSoup class which is used to extract information out of html page

r = requests.get('http://www.piemr.edu.in')
s = bs4.BeautifulSoup(r.text)
e = s.select('div')
print(len(e))
print(e[1].getText())

#getText prints code as text
print(str(e[1]))

#prints code
