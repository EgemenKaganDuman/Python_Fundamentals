# Dictionary (Sözlük)
# Sözlükler, liste ve tuple gibi bir başka koleksiyon yapısıdır.
# Sözlükler key value mantığında çalışırlar.

release_year_movie = {
    'Fight Club': 1999,
    'Matrix': 1999,
    'Interstaller': 2014,
    'Inception': 2018,
    'Dune': 2021
}

# Herhangi bir value'yu ekrana basın
# Path 1

print(f'Interstaller Relase Year: {release_year_movie.get("Interstaller")}')

# Path 2

print(f'Interstaller Relase Year: {release_year_movie["Interstaller"]}')

# Sözlüğün tüm anahtarlarını ekrana basalım.
for key in release_year_movie.keys():
    print(key)

# Sözlüğün tüm valuelarını ekrana yazalım.

for value in release_year_movie.values():
    print(value)

# Sözlüğün tüm varlığını ekrana basalım.

for key,value in release_year_movie.items():
    print(f'Movie Name: {key} - Release Year: {value}')

# # CRUD operations
# # Bir uygulamanın yüzde 70-80 CRUD (Create-Read-Update-Delete) operasyonları kapsar.
# # Yukarıda zaten okuma işlemi yaptık.
#
# # create
#
# release_year_movie['Joy'] = 2015
# print(release_year_movie)
#
# # update
#
# release_year_movie.update({
#     'Joy': 2016
# })
# print(release_year_movie)
#
# # delete
# del release_year_movie['Joy']
# print(release_year_movie)
#
# products = [
#     {'name': 'Everlast Pro Boxing Gloves', 'price': 49.99},
#     {'name': 'Everlast Punching Bags', 'price': 119.99},
#     {'name': 'Everlast Hand Wrap', 'price': 9.99},
#     {'name': 'Macbook Pro', 'price': 345.99},
#     {'name': 'Lenovo x1 Carbon', 'price': 165.99}
# ]
#
# # products listesinde tüm ürünlerin fiyatlarını toplayarak ekrana basın
# total = 0
# for product in products:
#     total += product.get('price')
#     print(f'Total: {total}')
#
# # product listesindeki ürünlerin fiyatı 100.00 büyük olan ürünleri listeleyin
#
# for product in products:
#     total = product.get('price')
#     if total > 100.00:
#             print(f'Total: {product.get("name")}')
# #alternatif çözüm
#
# for product in products:
#     if product['price'] > 100.00:
#         print(product)
#
# # Ürün adı içerisinde Everlast geçen ve ürün fiyatı 30.00 ile 130.00 arasında olan ürünleri listeleyin
#
# for product in products:
#     if 'Everlast' in product['name'] and 30.00 <= product['price'] <= 130.00:
#         print(product)

# CRUD - Category create-read-update-delete, veri sözlük tutulacak
from uuid import uuid4, uuid1
from pprint import pprint
#
# categories = {
#     'd28b9953-6968-488b-9e93-43acddd7da24': {
#         'name': 'Boxing Equipment',
#         'description': 'Best boxing equipment'
#     },
#     'cfc784be-95ba-471d-9c7d-e02c4c39902e': {
#         'name': 'MMA Equipment',
#         'description': 'Best MMA equipment'
#     }
#
# }
#
#
# while True:
#     process = input('Process: ')
#
#     match process:
#         case 'exit':
#             print('Application has been closing..!')
#             break
#         case 'create':
#             uuid4()
#             categories[str(uuid4())] = {
#                 'name': input('Type a category name: '),
#                 'description': input('Type a description: ')
#             }
#             pass
#         case 'get all':
#             pprint(categories)
#             pass
#         case 'get by id':
            # category_id = input('Id: ')
            # if category_id  == 'd28b9953-6968-488b-9e93-43acddd7da24':
            #     print(categories.get('d28b9953-6968-488b-9e93-43acddd7da24'))
# Alternatif çözüm.
#             category_id = input('Id: ')
#             result: dict | None = categories.get(category_id)
#             if result is None:
#                 print('There is no such a category..!')
#             else:
#                 pprint(result)
#
#             pass
#         case 'update':
#             category_id = input('Id: ')
#             new_name = input('Name: ')
#             new_description = input('Description: ')
#             categories.update({
#                 category_id: {
#                     'name': new_name,
#                     'description': new_description
#                 }
#             })
#             print(f'{category_id} has been edited..!')
#             pprint(categories.get(category_id))
#             pass
#         case 'delete':
#             category_id = input('Id: ')
#             del categories[category_id]
#             print(f'{category_id} has been removed..!')
#             pprint(categories)
#             pass
#         case _:
#             print('Please type a valid process name..!')