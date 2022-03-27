#!/bin/python3

# Import libraries
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# Public key, private key generation
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
private_key, public_key = key, key.publickey()

# Encrypt the data
plain_text = "this is the message"
cipher = PKCS1_OAEP.new(public_key)
encrypted_text = cipher.encrypt(plain_text.encode("utf8"))

# Decrypt the data
cipher = PKCS1_OAEP.new(private_key)
decrypted_text = cipher.decrypt(encrypted_text).decode("utf8")

# Print results
print(encrypted_text)
print(decrypted_text)
