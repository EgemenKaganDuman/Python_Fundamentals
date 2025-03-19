# # Custom Function
#
# # declare Function
#
# def function_name():
#     print('Hello.!')
#
# # Function execution or function Call
#
# function_name()
# function_name()
# function_name()
# function_name()
#
# # Fonksyionlar dinamik olmalıdır. Yani gelen değerlere alarak çalışmalılar.
#
# def greeting_people(full_name: str):
#     print(f'{full_name} salve..!')
#
#
# greeting_people('Burak Yılmaz')
# tam_ad= 'İpek Yılmaz'
#
# greeting_people(full_name=tam_ad)
#
# greeting_people(
#     full_name=input('Full Name: ')
# )
#
# def sum_two_number(x: int, y: int ) -> None:
#
#    """
#    This function sum two numbers.
#    :param x: int
#    :param y: int
#    :return: None
#    """
#    print(f'Result: {x+y}')
#
# sum_two_number(x=3,y=5)
#
# sum_two_number(
#     x=int(input('Number: ')),
#     y=int(input('Number: ')),
# )

# def is_even_odd(x: int | float) -> str:
#
#     """
#     :param x: Integer
#     :return: String
#     """
#
#     if x % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
#
# result: str = is_even_odd(x=12)
# print(result)
#

#Sign up - sign in
# import string
# users = [
#     ('beast','123'),
#     ('savage','987'),
#     ('bear', '567'),
# ]
#
# def sign_in(username: str, password: str) -> str:
#     for userName, pwd in users:
#         if userName == username and pwd == password:
#             return f'{userName} hoş geldiniz'
#
#     return 'bilgiler hatalı..!'
#
# # Yöntem 1
#
# # def sign_up(username: str, password: str) -> str:
# #     for user in users:
# #         if user[0].__eq__(username):
# #             return 'bu kullanıcı adı alındı.'
# #
# #         data = (username, password)
# #         users.append(data)
# #         return 'Üyelik işlemi tamamlandı.'
#
# #Yöntem 2
#
# def sign_up(username: str, password: str) -> str:
#     is_username_exist = any(user[0].__eq__(username) for user in users)
#     if is_username_exist:
#         return 'Bu kullanıcı adı alındı.'
#
#         pwd_is_valid = is_pwd_valid(password=password)
#         if pwd_is_valid:
#             data = (username, password)
#             users.append(data)
#             return 'Üyelik işlemi tamamlandı.'
#
#         return 'Invalid Password'
#
#
#
# def is_pwd_valid(password: str) -> bool:
#     char_set = set(password)
#
#     is_result = (
#         len(password) >= 16
#         and any(c in string.ascii_uppercase for c in char_set)
#         and any(c in string.ascii_lowercase for c in char_set)
#         and any(c in string.digits for c in char_set)
#         and any(c in string.punctuation for c in char_set)
#     )
#
#     return is_result
#
#
#
#
# result = sign_up(username='beast',password='fdasadf')
# print(result)
# print(users)


#1. yukarıdaki problemi çözün. Kullanıcı adı tekrar etmeyecek.
#2. kişi sign up olunca hemen feedback verilsin 'üyelik işlemi tamamlandı..' akabinde sign_in fonksiyonu tetiklesin.
#3. bu kodlara fonksiyonlaştırılırsa is_valid_password kodlarımızı entegre edilsin.
#4. okuma ödevi -> SoC (Seperation of Concern) & SRP (Single Responsibility Principle)


# Ödev 1: Hash kütüphanesi kullanılarak password hash lenecek.
# Ödev 2: Sıfırdan Proje açılacak. Açılan projenin adı: Software_Principle olucak.
# 01_SoC.py --> içine örnek
# 02_SRP.py --> içine örnekler
# 03_DRY.py --> içinde örnekler
# Yapılacak ve GitHub'a pushlanacak.

# Aşağıdaki listede tekrar eden sayıları saptayalım ve sözlük formatında ekrana yazdıralım. Çıktının aşağıdaki gibi olması gerekiyor.
# frequency_dict = {
#     1: 4,
#     2: 3,
#     3: 2,
# }


rakamlar = [1, 1, 1, 5, 3, 3, 5, 4, 2, 1, 5, 5, 2, 2]

def frequency_count(numbers: list) -> dict:
    frequency_dict = {}

    for item in numbers:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    return {}

frequency_count(numbers=rakamlar)