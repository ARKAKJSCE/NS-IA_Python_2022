#!/bin/python3

# Import Libraries
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto import Random

# Message, Private key
plain_text = "hi this is the message"
private_key = "privatekey123456"

# Encrypt the Data
iv = Random.new().read(AES.block_size)
cipher = AES.new(private_key.encode("utf8"), AES.MODE_CFB, iv)
encrypted_text = cipher.encrypt(plain_text.encode("utf8"))

# Decrypt the Data
cipher = AES.new(private_key.encode("utf8"), AES.MODE_CFB, iv)
decrypted_text = cipher.decrypt(encrypted_text).decode("utf8")

# Print results

print(encrypted_text)
print(decrypted_text)
