# # 1'den 100'e kadar olan sayıların toplamını for ve while döngüsü kullanarak ayrı ayrı bulun. ÇÖZÜLDÜ
#
# toplam = 0
# for i in range(100):
#     toplam = i + toplam
#
# print(f'{toplam}')

# Kullanıcıdan alınan bir söz öbeğindeki sesli harfler sesli_harfler = [],
# sessiz harfleri sessiz_harfler = [] yazsın, ayrıca bir harf listeye bir kez eklensin.

# word = input('Type something ').lower()
# sesli_harfler_listesi = ['a','e','ı','i','o','ö','u','ü']
# sesli_harfler = []
# sessiz_harfler = []
# for c in word:
#     if c not in sesli_harfler and c not in sessiz_harfler:
#         if c in sesli_harfler_listesi:
#             sesli_harfler.append(c)
#         else:
#             sessiz_harfler.append(c)
#
# print(f'Sesli Harfler: {sesli_harfler}\nSessiz Harfler: {sessiz_harfler}')

# users listem olacak. bu listeki kişilere kurumsal mail adresi oluşturacağız.
#burak.yilmaz@outlook.com

users = ['burak yılmaz', 'ertuğrul', 'hakan bear yılmaz', 'kerim abdul cabbar ökkeş', '']
#yukarıdaki listedeki kişilere mail adresi yaratalım ve mail_address listesine ekleyelim.
mail_adresses = []

for user in users:
    user_names = user.split(' ')
    for item in user_names:
        if item == ' ':
            user_names.remove(item)
        if user == ' ':
            continue
        elif len(user_names) >= 2:
            mail_adres = f'{user_names[0]}.{user_names[-1]}@outlook.com'
            mail_adresses.append(mail_adres)

print(mail_adresses)

# sample input --> bu1rak yılmaz, boşluk, rakam ve büyük harf sıkıntıları da çözülsün.

# 3. Kullanıcıdan 5 tane sayı alarak bir liste oluşturun ve ardından bu listeyi ekrana yazdırın.
# Kullanıcıdan 5 tane tam sayı alarak bir listeye ekleyin.
# Listeyi ekrana yazdırın

# sayial = 5
#
# for i in range(6):
#