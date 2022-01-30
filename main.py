from bs4 import BeautifulSoup
import requests

htmlFile = "THIS STRING CONTAINS THE HTML"
# Make a GET request
r = requests.get('https://www.cse.org.uk/local-energy/funding-your-project')

# check status code success code -200 -> print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


'''# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)

# Getting the name of parent tag
print(soup.title.parent.name)'''

s = soup.find('div', class_='funders-list')
content = s.find_all('p')

print(content)

s = soup.find('div', class_='funders-list')
lines = s.find_all('p')
for line in lines:
    print(line.text)

def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
    return ' '.join(soup.stripped_strings)

print(remove_tags(r.content))














