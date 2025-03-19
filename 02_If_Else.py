## Kitap Hesaplama
#
# kitap_fiyati = 5  # Bir kitabın fiyatı
# #
# # kitap_sayisi = input("Kaç kitap almak istiyorsunuz? ")
#
# # Girilen değerin tamamen sayısal olup olmadığını kontrol et
# if not kitap_sayisi.isdigit():
#     print("Hata: Lütfen geçerli bir pozitif sayı giriniz!")
# else:
#     kitap_sayisi = int(kitap_sayisi)
#
#     # Geçersiz girişleri kontrol et
#     if kitap_sayisi <= 0:
#         print("Hata: Kitap sayısı pozitif bir sayı olmalıdır.")
#     elif kitap_sayisi > 100:
#         print("Hata: 100'den fazla kitap satın alınamaz.")
#     else:
#         # İndirim oranlarını belirle
#         if 1 <= kitap_sayisi <= 15:
#             indirim_orani = 5
#         elif 16 <= kitap_sayisi <= 25:
#             indirim_orani = 10
#         elif 26 <= kitap_sayisi <= 50:
#             indirim_orani = 15
#         elif 51 <= kitap_sayisi <= 75:
#             indirim_orani = 20
#         elif 76 <= kitap_sayisi <= 100:
#             indirim_orani = 25
#         else:
#             indirim_orani = 0  # Normalde buraya düşmez
#
#         # Toplam fiyat ve indirim hesaplama
#         toplam_fiyat = kitap_sayisi * kitap_fiyati
#         indirim_miktari = (toplam_fiyat * indirim_orani) / 100
#         odenecek_tutar = toplam_fiyat - indirim_miktari
#
#         # Sonucu ekrana yazdır
#         print(f"Toplam fiyat: {toplam_fiyat} TL")
#         print(f"İndirim oranı: %{indirim_orani}")
#         print(f"İndirim tutarı: {indirim_miktari:.2f} TL")
#         print(f"Ödenecek tutar: {odenecek_tutar:.2f} TL")

## Araç türü ve hızı hesaplama
#
# Kullanıcıdan araç türü ve hız bilgisi al
# arac_turu = input("Araç türünü girin (otomobil/kamyon/motosiklet): ").lower()
# hiz = input("Hızınızı girin: ")
#
# # Girilen hızın geçerli bir sayı olup olmadığını kontrol et
# if not hiz.isdigit():
#     print("Hata: Lütfen geçerli bir hız giriniz!")
# else:
#     hiz = int(hiz)
#
#     # Negatif hız kontrolü
#     if hiz < 0:
#         print("Hata: Hız negatif olamaz!")
#
#     # Araç türüne göre hız limitlerini kontrol et
#     elif arac_turu == "otomobil" and hiz >= 60:
#         print("Ceza alındı! Otomobil için hız limiti aşıldı.")
#     elif arac_turu == "kamyon" and hiz >= 30:
#         print("Ceza alındı! Kamyon için hız limiti aşıldı.")
#     elif arac_turu == "motosiklet" and hiz >= 70:
#         print("Ceza alındı! Motosiklet için hız limiti aşıldı.")
#     elif arac_turu in ["otomobil", "kamyon", "motosiklet"]:
#         print("Ceza yok.")
#     else:
#         print("Hata: Geçersiz araç türü girdiniz!")

# Disktriminant Hesaplama
#
# import math  # Karekök işlemi için
#
# # Kullanıcıdan katsayıları al
# a = float(input("a katsayısını girin: "))
# b = float(input("b katsayısını girin: "))
# c = float(input("c katsayısını girin: "))
#
# # Diskriminantı hesapla
# delta = b ** 2 - 4 * a * c
# print(f"Diskriminant (Δ): {delta}")
#
# # Kökleri hesapla
# # sqrt() fonksiyonu, bir sayının karekökünü hesaplamak için kullanılır.
# if delta > 0:
#     root1 = (-b + math.sqrt(delta)) / (2 * a)
#     root2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(f"Gerçek kökler: root1 = {root1:.2f}, root2 = {root2:.2f}")
#
# elif delta == 0:
#     root = -b / (2 * a)
#     print(f"Çift katlı kök: root1 = root2 = {root:.2f}")
#
# #Python'da Kompleks Sayılar ve İmajiner Kısım
# # Python'da karmaşık sayılar (complex numbers) doğrudan desteklenir ve j harfi ile gösterilir:
# else:
#     real_part = -b / (2 * a)
#     imaginary_part = math.sqrt(-delta) / (2 * a)
#     print(f"Kompleks kökler:")
#     print(f"root1 = {real_part:.2f} + {imaginary_part:.2f}i")
#     print(f"root2 = {real_part:.2f} - {imaginary_part:.2f}i")

