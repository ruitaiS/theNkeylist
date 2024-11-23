from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Inputs
password = "your_secure_password"
salt = get_random_bytes(16)
key = PBKDF2(password, salt, dkLen=32, count=100000)

# Encryption
cipher = AES.new(key, AES.MODE_GCM)
message = "Your secret string"
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# Concatenate all fields into a single binary string
encoded_data = base64.b64encode(
    salt + cipher.nonce + tag + ciphertext
).decode()

print("Encoded Encrypted Data:", encoded_data)


#------


# Encrypted data (single encoded string)
#encoded_data = "..."  # Replace with the base64 string from encryption

# Decode and extract the parameters
decoded_data = base64.b64decode(encoded_data)

# Extract the components
salt = decoded_data[:16]          # First 16 bytes (salt)
nonce = decoded_data[16:32]       # Next 16 bytes (nonce)
tag = decoded_data[32:48]         # Next 16 bytes (tag)
ciphertext = decoded_data[48:]    # Remaining bytes (ciphertext)

# Derive the key
password = "your_secure_password"
key = PBKDF2(password, salt, dkLen=32, count=100000)

# Decrypt
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print("Decrypted Message:", plaintext.decode())
