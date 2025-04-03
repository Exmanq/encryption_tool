import base64

def encrypt_password(password: str) -> str:
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encoded_str: str) -> str:
    return base64.b64decode(encoded_str).decode()

if __name__ == "__main__":
    user_password = input("Введи пароль для шифрования: ")
    encrypted = encrypt_password(user_password)
    print("Пароль в base64:", encrypted)
    
    decrypted = decrypt_password(encrypted)
    print("Decrypted пароль в base64:", decrypted)