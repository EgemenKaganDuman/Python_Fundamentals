#Nested For

# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i * j}')
#     print('============================')

# Kare yaptırma
# for i in range(1,5):
#     for j in range (1,20):
#         print('X', end='')
#     print(' ')

# Listeler
# Uygulama içerisinde anlık olarak değer saklayan bir yapıdır.
# arabalar ['dodge', 'ford', 'nissan'] uygulama ilk çalıştığında buradaki liste yaratılır.
# Uygulama çalıştığı sürece bu liste üzerinde işlemler yapabiliriz.
# Örneğin yeni araba ekleme, araba silme gibi işlemler yapılabilir.
# Lakin uygulama durdurulduğunda tüm bu değişiklikler kaybolur.
#Uygulama tekrar çalıştırıldığında liste ilk haliye karşımıza gelir. Yani harddisk gibi değerleri kalıcı olarak tutmaz.
# Bu bağlamda listelerin RAM'in HEAP alanında yaratıldığını anlayabiliriz.

# Listelerde index mantığı bulunmaktadır. Örnek listemiz olan arabalar bakacak olursak 0. Index'te dodge bilgisinin tutulduğunu görebiliriz.
# Index değerleri sıfırdan başlar vektörel olarak artı yönde artarak devam eder.
# Liste içerisinde farklı tiplerde değerlerde saklayabiliriz.

boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfield', 'Antony Jasua', 'George Forman']
print(boxers[0]) #Mike Tyson
print(boxers[2]) #Lenox Lewis
print(boxers[3]) #Evander Holyfield

# listemizin sonuna yeni bir item ekleyin 'Rocky Mariciano

boxers.append('Rocky Marciaona')
print(boxers)

# 4. İndex'e floyd Mayweather ekle
boxers.insert(4,'Floyd Mayweather')
print(boxers)

# item value 'Antony Jasua' olan itemi silin

boxers.remove('Antony Jasua')
print(boxers)

# 0. İndex'teki itemi silin
boxers.pop(0)
print(boxers)

# Olmayan indexi silerken nasıl handle edilir?

try:
    # boxers.pop(10) #Listede olmayan bir index değeri verirsek IndexError raise edilir.
    print(boxers)
except IndexError as err:
    print(err)

boxers.sort() #Liste sıralamaya yarar, a'dan z'ye çalıştığı gibi scler büyükleride sıralardı
print(boxers)

current_heavy_weight = ['Antony Jausa', 'Denial Dubba', 'Tyson Fury']
boxers.extend(current_heavy_weight)
print(boxers)

# Liste içerisinde for loop ile dolaşabiliyoruz.

for boxer in boxers:
    print(boxer)

# Kullanıcıdan alınan bir söz öbeğindeki sesli harfler sesli_harfler = [],
# sessiz harfleri sessiz_harfler = [] yazsın, ayrıca bir harf listeye bir kez eklensin.

# sample input --> bu1rak yılmaz, boşluk, rakam ve büyük harf sıkıntıları da çözülsün.