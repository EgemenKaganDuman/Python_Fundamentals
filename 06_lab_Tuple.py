# Tuple (Demetler)
# Liste gibi değişik veri tiplerini içerisinde barındarabilen koleksiyonlardan biridir. Listeler gibi index mantığına sahiptir.
# lakin listelerin sahip olduğu append(), remove() etc fonksiyonlara sahip değildir. Listeler gibi RAM'in hesap alanında yaşarlar.
# Demetleri hangi senaryoda kullanmamalıyız ya da hangi senaryoda tercih etmeliyiz. Tuple üzerinde create, update, delete gibi işlemler yapamıyoruz. Tuple sadece okuma
# amaçlı kullandığımız bir yapıdır. Bu minvalde okuma hızı listelerden daha iyidir.

tuple_1 = ('Galatasaray', 'Beşiktaş', 'Adanademir Spor', 'Trabzonspor', 'Fenerbahçe')
tuple_2 = ('Eagels', 'Seahawks', 'Redskins', 'Vikings')

tuple_3 = tuple_1 + tuple_2

print(tuple_3)

#Slicing (Dilimleme): Hem Tuple hem de listelerde kullanabildiğim bir tekniktir.

print(tuple_3[0:3])
print(tuple_3[2:4])
print(tuple_3[::2])
print(tuple_3[-1])
print(tuple_3[::-1])
print(tuple_3[::-2])
print(tuple_3[4::-2])
print(tuple_3[4::2])

tuple_4 = ('Sarıyer', ('Suadiye', 'Fenerbahçe'), ('Nişantaşı', ('Ulus', 'Etiler')))

print(tuple_4[0])
print(tuple_4[1][0])
print(tuple_4[2][1][1])
print(tuple_4[1][1])
print(tuple_4[2][0])

my_family = [('Burak Yılmaz', 36, 'best'), ('Hakan Yılmaz', 39, 'bear'), ('İpek Yılmaz', 41, 'keko')]
print('---------')
# Unboxing işlemi yapacağız.

for full_name, age, user_name in my_family:
    print(f'Full Name: {full_name}\n'
          f'Age: {age}\n'
          f'User Name: {user_name}\n'
          '-------')

