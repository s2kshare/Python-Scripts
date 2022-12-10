import requests
from bs4 import BeautifulSoup

url = "https://www.pcgamer.com/au/news"
response = requests.get(url)
bodyArr = []
soup = BeautifulSoup(response.content, 'html.parser')

headerArr = []
# Pull Carousel Headlines
for x in soup.findAll('span','article-name'):
    # Removing tags + clutter
    original = str(x)
    unwrapped = str(x.unwrap())
    # <span> tag
    firstHalf = unwrapped[:len(unwrapped)-7]
    # </span> tag
    secondHalf = unwrapped[-7:]
    # Replace to whitespace
    firstEdit = original.replace(firstHalf, '')
    secondEdit = firstEdit.replace(secondHalf, '')

    headerArr.append(secondEdit)

# Find Body tag articles
bodyNews = soup.find_all('div','content')
for x in bodyNews:
    if str(x) != "":
        bodyArr.append(x.text.strip())

for x in headerArr:
    print('Header: {}'.format(x))

print()
print('-----------------------------------------------------\n')


# Filter Body Headlines
for x in bodyArr:
    newsbodyArr = x.splitlines()
    title = newsbodyArr[0]
    author = newsbodyArr[5]
    date = newsbodyArr[7]
    desc = newsbodyArr[11]
    print('Article: {}\nDescription: {}\nAuthor: {}\n{}'.format(title, desc, author, date.capitalize()))
    print('\n-----------------------------------------------------\n')