def is_valid_password(password):
    """
    Verilen şifrenin geçerli olup olmadığını kontrol eder.
    Şifre aşağıdaki kriterleri sağlamalıdır:
    - En az 16 karakter içermeli
    - En az bir büyük harf içermeli
    - En az bir küçük harf içermeli
    - En az bir rakam içermeli
    - En az bir noktalama işareti içermeli
    """

    # Şifrenin uzunluğunu kontrol et
    if len(password) < 16:
        return False

    # Kontrol değişkenleri
    has_upper = False
    has_lower = False
    has_digit = False
    has_punctuation = False

    # Noktalama işaretleri listesi
    punctuation_chars = list("!@#$%^&*(),.?\":{}|<>")

    # Şifreyi karakter karakter kontrol et
    for char in password:
        if char in punctuation_chars:
            has_punctuation = True
        elif "A" <= char <= "Z":
            has_upper = True
        elif "a" <= char <= "z":
            has_lower = True
        elif "0" <= char <= "9":
            has_digit = True

    return has_upper and has_lower and has_digit and has_punctuation


# Kullanıcıdan şifre girişi al ve kontrol et
password = input("Şifrenizi girin: ")
if is_valid_password(password):
    print("Geçerli bir şifre girdiniz!")
else:
    print("Şifre belirtilen kriterleri sağlamıyor.")
