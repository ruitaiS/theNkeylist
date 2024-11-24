from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# User Input
message = "Hello my brudda! :)))"
password = "abc123"

# Encryption
salt = get_random_bytes(16)
key = PBKDF2(password, salt, dkLen=32, count=100000)
cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# Concatenate all parameters into a single binary string
encrypted_message = base64.b64encode(
    salt + cipher.nonce + tag + ciphertext
).decode()

print("Encrypted Message:", encrypted_message)
