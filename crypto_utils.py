import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=1000000)

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    return data[:-data[-1]]

def encrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = get_random_bytes(16)
    key = derive_key(password.encode(), salt)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data))

    encrypted_path = file_path + ".enc"
    with open(encrypted_path, 'wb') as f:
        f.write(salt + iv + ciphertext)

    os.remove(file_path)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    salt = file_data[:16]
    iv = file_data[16:32]
    ciphertext = file_data[32:]
    key = derive_key(password.encode(), salt)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ciphertext))

    decrypted_path = file_path.replace('.enc', '.dec')
    with open(decrypted_path, 'wb') as f:
        f.write(data)

    os.remove(file_path)
