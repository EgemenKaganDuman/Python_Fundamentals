#for loop
#For Loop ile yoğun olarak kullanılan ''in'' operatörü ve range() fonksiyonu tanıdık.

# 'in' & 'not in'

#in
# print('b' in 'burak') #True döndü 'burak ın içinde b harfi var.
# print('U' in 'burak') #False döndü çünkü büyük U harfi yok.
#
# #not in (in işlevinin tam tersi
# print('b' not in 'burak') #False döndü 'burak ın içinde b harfi var.
# print('U' not in 'burak') #True döndü çünkü büyük U harfi yok.

#range() fonksiyonu
#range(100) --> çıktı olarak 0'dan başlayıp 99'a kadar bir sayı aralığı oluşturur.
#range(10, 20) --> çıktı olarak 10'dan başlayıp 20'ye kadar 1, 1 artan ve 19'da biten bir aralık yaratacak.
# range(10, 50, 2) --> çıktı 10'dan başlayıp iki iki artarak 49'da aralığı bitirir.

#rakamları ekrana yazdıralım

# for sayac in range(10):
#     print(sayac, end=', ')

#10 ile 50 arasındaki çift sayıları ekrana yazdırdık.
# for sayac in range(10, 51, 2):
#     print(sayac, end=', ')

# 0 ile 100 arasındaki kaç tane çift kaç tane sayı var bulalım. Ekrana yazdıralım

# sayacift = 0
# sayactek = 0
# for sayac in range(101):
#     if sayac % 2 == 0:
#         sayacift += 1
#     else:
#         sayactek += 1
#
# print(f'Tek sayı miktarı: {sayactek} Çift sayı miktarı: {sayacift}')

# Örnek: Range fonksiyonıunu başlangıç, bitiş ve adım miktarlarını kullanıcıdan alalım.
# Bu belirtilen aralıkta ki tam sayıların karesini alarak ekrana yazdıralım

sayial1 = int(input('Rangein ilk başlangıcı için sayı ata:' ))
sayial2 = int(input('Rangein bitişi için sayı ata:' ))
sayial3 = int(input('Rangein artırma sayısı için sayı ata:' ))

for i in range(sayial1,sayial2+1,sayial3):
    print(i**2)

