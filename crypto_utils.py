import os
import json
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

    ext = os.path.splitext(file_path)[1]
    metadata = json.dumps({'ext': ext}).encode().ljust(128, b' ')  # 128 bytes

    encrypted_path = file_path + ".enc"
    with open(encrypted_path, 'wb') as f:
        f.write(salt + iv + metadata + ciphertext)

    os.remove(file_path)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    salt = file_data[:16]
    iv = file_data[16:32]
    metadata_raw = file_data[32:160].rstrip(b' ')
    metadata = json.loads(metadata_raw.decode())
    ext = metadata['ext']
    ciphertext = file_data[160:]

    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ciphertext))

    decrypted_path = file_path.replace('.enc', '') + ext
    with open(decrypted_path, 'wb') as f:
        f.write(data)

    os.remove(file_path)
