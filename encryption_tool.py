import base64

class EncryptMain:
    def encrypt_password(self, password):
        return base64.b64encode(password.encode()).decode()
    
    def decrypt_password(self, encoded_str):
        return base64.b64decode(encoded_str).decode()

s = input("Enter password for encryption: ")

enc = EncryptMain()

encrypted = enc.encrypt_password(s)
print("encryption password:", encrypted)

decrypted = enc.decrypt_password(encrypted)
print("decrypted password:", decrypted)
