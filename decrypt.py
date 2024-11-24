from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# User Input
encrypted_message = "hTahCgIoFij8qQrfXY4Av8G8LvVkWL4A4xd7itfTefISYsEfVK5CZu7Qc1XTgX2DilKYr4Fr7FvYQ2qI/jqx"  # Replace with the base64 string from encryption
password = "pwd" # Same as password used for encryption

# Extract the parameters and derive the key
decoded_data = base64.b64decode(encrypted_message)
salt = decoded_data[:16]          # First 16 bytes (salt)
nonce = decoded_data[16:32]       # Next 16 bytes (nonce)
tag = decoded_data[32:48]         # Next 16 bytes (tag)
ciphertext = decoded_data[48:]    # Remaining bytes (ciphertext)
key = PBKDF2(password, salt, dkLen=32, count=100000)

# Decrypt
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print("Decrypted Message:", plaintext.decode())
