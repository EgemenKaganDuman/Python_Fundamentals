# Örnek 1: Kullanıcıdan pozitif bir tam sayı alana kadar tekrar soran program yazın.
# Kullanıcı negatif veya sıfır girerse tekrar sormalı.
# Kullanıcıdan doğru giriş alındığında program sonlanmalı.
#
# print('Programi kapatmak için bitir yazin. Devam etmek istiyorsanız devam edelim yazın.')
# while True:
#     devamkontrol = str(input('Devam mı? Bitsin mi?'))
#
#     if devamkontrol == 'Devam':
#         sayikontrol = int(input('Pozitiflik durumunu kontrol etmek istediğiniz sayıyı girin: '))
#     elif devamkontrol == 'Bitir':
#         print(f'Program sonlandırıldı')
#         break
#     if sayikontrol > 0:
#         print(f'Tebrikler girdiğiniz sayi pozitif!/n Girdiğiniz sayı: {sayikontrol} ')
#     elif sayikontrol == 0:
#         print(f'Girdiğiniz sayi 0')
#     elif sayikontrol < 0:
#         print(f'Girdiğiniz sayi negatif!/n Girdiğiniz sayı: {sayikontrol} ')

# Kullanıcıdan alınan sayı asal mı değil mi?

# while True:
#     sayi = int(input("Sorgulamak İstediğiniz Sayıyı Girin : "))
#     sayi1 = 2
#     sayi = sayi % 2
#     if sayi == 0:
#         print('Sayi Asal sayi değildir.')
#     elif sayi != 0:
#         print('Sayi asal sayidir.')
#         break

#alternatif çözüm.
# sayi = int(input('Sayı giriniz: '))
# if sayi <2:
#     print('2den küçük sayıların asallık kontrolü yapılamaz.')
# else:
#     is_prime = True
#
#     sayac = 2
#     while sayac < sayi:
#         if sayi % sayac== 0:
#             is_prime = False
#             break
#         sayac += 1
#
#     if is_prime:
#         print(f'{sayi} asaldır..!')
#     else:
#         print(f'{sayi} asal degildir')
# Kullanıcıdan alınan sayının faktöriyelini hesaplayalım.

# sayi = int(input('Sayı giriniz: '))
# fact=1
# if sayi<0:
#     print('sayı negatif olamaz')
#
# while sayi>1:
#     fact=fact*sayi
#     sayi=sayi-1
#     print(fact)

# Alternatif Çözüm

sayi = int(input('Sayı: '))

if sayi < 0:
    print(f'Sıfırdan küçük sayıların faktöriyeli hesaplanmaz..!')
elif sayi == 1 or sayi == 0:
    print(f'Faktöriyel : 1')
else:
    sonuc = 1

    while sayi > 0:
        sonuc *= sayi
        sayi -= 1

    print(f'Faktöriyel: {sonuc}')