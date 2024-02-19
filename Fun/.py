import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/?auth=login-google1tap&login=google1tap'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')


#p = open("div_results", "w")
#p.write(str(soup.find_all('div')))
#class="css-xdandi"><h3'

#t= open("html_file2", "w")
#t.write(soup.prettify())

p = open("div_results", "w")
for i in soup.find_all("div", class_="css-xdandi"):
    p.write(i.parent.parent.name + '\n')
    