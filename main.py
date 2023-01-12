# Step 0: install the requirements
# pip install requests
# pip install html5lib
# pip install bs4

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"

# Step 1: Get The Html page
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse The Html
soup = BeautifulSoup(htmlContent, 'html.parser')  # creating the soup
# print(soup.prettify()) #print in a structured format

# Step 3: Html Tree Traversal

# Get the title from the page
title = soup.title
# print(title) # it will give title tag Object.
# print(title.string) # it will give the inside text of any tag Object.

# Type of Object
# print(type(title))
# print(type(title.string))

# Get all paragraphs from the page
# paras = soup.find_all('p')
# print(paras)

# To get the first element of any tag
# print(soup.find('p'));

# to get the class/id if available in the tag
# print(soup.find('p')['class']) # class of first para tag

# to get and print the classes of all para tag
# classes = soup.find_all('p')
# all_classes = [one_p.get('class') for one_p in classes]
# print(all_classes)

# to find the classes with specific class name
# print(soup.find('p',class_='mt-2'))

# To get the text of tag
# print(soup.find('p').get_text())
# print(soup.get_text())
# OR
# print(soup.find('p').string)
# OR 
# print(soup.p.string)

# # Get all the anchor tag from the page.
# anchors = soup.find_all('a')
# LinkText = 'https://www.codewithharry.com'
# storeLink = set() # store the href of anchor tag
# for link in anchors:
#     if (link.get('href') != '#'):
#         LinkText = LinkText + link.get('href')
#         storeLink.add(LinkText)
#         print(LinkText)
#         print("\n")
# print(anchors)

# .content and .children 
# print(soup.find(id='search-toggle'))
search_toggle = soup.find(id='__next')
# for items in search_toggle.contents:
#     print(items.strings)
#     print("\n ")

# to get the innerText
for items in search_toggle.stripped_strings:
    print(items)

