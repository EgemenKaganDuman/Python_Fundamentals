from requests import get
from pprint import pprint

# end_point = 'https://newsapi.org/v2/everything?q=tesla&from=2025-02-12&sortBy=publishedAt&apiKey=ec7f364a694d42af9e48dec4e3ae006f'
#
# response = get(url=end_point)
#
# data = response.json()
#
# pprint(data)
# for key in data.keys():
#     print(key)

# Ödev: Gelen verinin ilk makalesinin yazarını, relaese date ini ve contentini ekrana bastır.
# Ödev 2: Search Mekanizması, end userdan bir yazar adı alıyoruz. gelen bu yazar adına sahip makale ya da makaleleri ekrana yazdırıyoruz.
# Ödev 3: Free farklı bir API (NewAPI değil), bu apiden data çekiyoruz. yine search mekanizmaları kuruyoruz. CRUD Operasyonu yapılacak. (Pazartesiye kadar yapılacak.)
# bonus ödev: search mekanizmalarından: Linear Search nedir? Araştırılsın.

# Ödev 1:
#
# print('---------------------------------------------------------')
# article = data['articles']
# if article:
#     first_article = article[0]
#     author = first_article.get('author')
#     published_date = first_article.get('publishedAt')
#     content = first_article.get('content')
#
#     pprint('First Article Details:')
#     pprint(f'Author: {author}')
#     pprint(f'Published Date: {published_date}')
#     pprint(f'Content: {content}')
# else:
#     print('No articles Found.')

# Ödev 2:

# print('---------------------------------------------------------')
#
# articles = data['articles']
#
# search_author = input('Which author are you searching for: ')
#
# found = False
#
#
# for article in articles:
#
#     author = article.get('author', 'Unknown author')
#
#     if author == search_author:
#         print(f'Here is your author: {author}')
#         pprint(f'Content: {article.get("content", "No content available")}')
#         pprint(f'Published Date: {article.get("publishedAt", "No date available")}')
#         print()
#         found = True
#
# if not found:
#     print('There is no author with this name.')

from random import randint

lst = []
for i in range(10):
    lst.append(randint(0,100))

for value, index in enumerate(lst):
    print(f'Index: {index} - Value: {value}')
    
#Ödev 3:
# while True:
#     process = input('Process: ')
#
#     match process:
#
#         case 'exit':
#             print('Application has been closing..!')
#             break
#         case 'create':
#             break
