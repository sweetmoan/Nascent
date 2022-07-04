from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen('http://meinparlament.diepresse.com/')
content = url.read()
soup = BeautifulSoup(content, 'lxml')

table = soup.findAll('div',attrs={"class":"content-question"})
for x in table:
    print(x.find('p').text)
