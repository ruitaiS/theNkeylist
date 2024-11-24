from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import file_handler
import param_handler

params = param_handler.get_params()
if params.filename:
    print(f"Processing file: {params.filename} with password: {params.password}")
    encrypted_message = file_handler.read_file(params.filename)
    password = params.password
elif params.message:
    print(f"Processing message: {params.message} with password: {params.password}")
    # Call a function to handle message encryption/decryption here
else:
    print("Error: Neither 'filename' nor 'message' was provided.")
    sys.exit(1)

# User Input
#encrypted_message = "hTahCgIoFij8qQrfXY4Av8G8LvVkWL4A4xd7itfTefISYsEfVK5CZu7Qc1XTgX2DilKYr4Fr7FvYQ2qI/jqx"  # Replace with the base64 string from encryption
#password = "pwd" # Same as password used for encryption

# Extract the parameters and derive the key
decoded_data = base64.b64decode(encrypted_message)
salt = decoded_data[:16]          # First 16 bytes (salt)
nonce = decoded_data[16:32]       # Next 16 bytes (nonce)
tag = decoded_data[32:48]         # Next 16 bytes (tag)
ciphertext = decoded_data[48:]    # Remaining bytes (ciphertext)
key = PBKDF2(password, salt, dkLen=32, count=100000)

# Decrypt
try:
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_msg = cipher.decrypt_and_verify(ciphertext, tag).decode()
    #file_handler.write_file(decrypted_msg, )
    print("Decrypted Message:", decrypted_msg)
except ValueError as e:
    if str(e) == "MAC check failed":
        print("Error: MAC check failed. (Most likely a wrong password or improperly copied encrypted text)")
    else:
        print(f"Error during decryption: {e}")
