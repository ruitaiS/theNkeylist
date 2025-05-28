from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import argparse
import sys

if len(sys.argv) != 2:
    print("Bad input.")
    sys.exit(1)
encrypted_message = sys.argv[1]

# Decrypt
try:
    decoded_data = base64.b64decode(encrypted_message)
    password = decoded_data[:16].decode('utf-8')
    salt = decoded_data[16:32]
    nonce = decoded_data[32:48]
    tag = decoded_data[48:64]
    ciphertext = decoded_data[64:]
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_msg = cipher.decrypt_and_verify(ciphertext, tag).decode()

    print("Decrypted Message:\n")
    print(f"{decrypted_msg}\n")

except Exception as e:
        print(f"Error during decryption: {e}")
