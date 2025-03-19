# Loops

# Tekrarlı işlemler yaptıracağımız zaman döngüleri kullanıyoruz.
#Örneğin Kullanıcıdan 10 tane input aldırmak istersek,ya da 0-9 yani rakamları ekrana yazdırmak istersek bir string ifadenin içerisinde
# karakterler onları kullanmak istersek loop kullanıyoruz.

# While & For Loop türlerimizdir.

# While Loop:

#Örnek 1: 0'dan 10'a kadar rakamları

# counter = 0
# while counter < 10:
#     print(counter)
#     counter = counter + 1

# Rakamları ekrana yazdırmak için sayacı bir bir arttırarak ekrana yazdırdık.

# Örnek 2: 10'dan geriye tüm sayıları yazdırın.

# counter = 10
# while counter >= 0:
#     print(counter)
#     counter = counter - 1

# Örnek 3: 0-100 arasındaki her bir tam sayıyı ekrana yazdırın.

# counter = 0
# while counter <= 100:
#     print(counter)
#     counter = counter +1

# Alternatif Çözüm yan yana yazdırma yöntemi. end komutu kullanılarak bunu sağlayabiliyoruz.

# sayac = 0
# while sayac <= 100:
#     print(sayac, end=', ')
#     sayac = sayac + 1

# Örnek 4: 0 - 100 arasındaki kaç tane çift kaç tne tek sayı bulun.

# countercift = 0
# countertek = 0
# count=0
# while count <= 100:
#     if count % 2 == 0:
#         countercift = countercift + 1
#     else:
#         countertek= countertek + 1
#     count = count +1
# print(f'Ciftler: {countercift}\nTekler: {countertek}')

# Örnek 5: 0 ile 100 arasındaki çift ve tek sayıların toplamını yazın.

# countercift = 0
# countercifttop= 0
# countertektop= 0
# countertek = 0
# count=0
# while count <= 100:
#     if count % 2 == 0:
#         countercifttop = countercifttop + count
#         countercift = countercift + 1
#     else:
#         countertektop = countertektop + count
#         countertek= countertek + 1
#
#     count = count +1
# print(f'Ciftler: {countercift}\nTekler: {countertek}')
# print(f'Ciftler: {countercifttop}\nTekler: {countertektop}')

# Örnek 6:
# kullanıcıdan alınan 2 tane tam sayı üzerinden işlem yapılacak
# Kullanıcıdan işlem türü alınacak. 'e', '+', '-' etc
# Kullanıcı 'e' girene kadar işlem yapabilecek yani sonsuz döngü kuracaksınız.

#Çözüm 1:
# sayi1 = int(input('Lutfen sayı giriniz: '))
# sayi2 = int(input('Lutfen sayı giriniz: '))
# count = 1
# while count != 0:
#     print(' e harfi girene kadar işlem devam edecektir' )
#     islemturu = str(input('İslem turunu giriniz: '))
#     if islemturu == '+':
#         toplam = sayi1 + sayi2
#         print(f'Birinci sayi ve ikinci sayinin toplamı: {toplam}')
#     elif islemturu == 'x':
#         carpim = sayi1*sayi2
#         print(f'Birinci sayi ve ikinci sayinin çarpımı: {carpim}')
#     elif islemturu == '-':
#         cikarma = sayi1-sayi2
#         print(f'Birinci sayi ve ikinci sayinin çıkarımı: {cikarma}')
#     elif islemturu == '/':
#         bolme = sayi1/sayi2
#         print(f'Birinci sayi ve ikinci sayinin bölmesi: {bolme}')
#     elif islemturu == 'e':
#         count -= 1
#
#     print('Programı kullandığınız için teşekkür ederim.')

#Çözüm 2

# while True:
#     try:
#         process = input('Process: ')
#
#         match process:
#             case 'e':
#                 print('Application has been closing..!')
#                 break
#             case '+':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 + sayi_2}')
#             case '*':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 * sayi_2}')
#             case '-':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 - sayi_2}')
#             case '/':
#                 sayi_1 = float(input('Number: '))
#                 sayi_2 = float(input('Number: '))
#                 print(f'Result: {sayi_1 / sayi_2}')
#             case _:
#                 print('Invalid Value')
#     except ZeroDivisionError as err:
#         print(err)
#     except ValueError as err:
#         print(err)