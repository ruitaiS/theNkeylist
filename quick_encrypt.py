from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import secrets, string

message = input("Message: ")

try:
    password = ''.join(secrets.choice(
        string.ascii_letters + string.digits + string.punctuation
        ) for _ in range(16))
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    encrypted_msg = base64.b64encode(
        password.encode('utf-8') + salt + cipher.nonce + tag + ciphertext
    ).decode()
    print(f"\n{encrypted_msg}")

except ValueError as e:
    print(f"\nUnknown error during encryption: {e}")
