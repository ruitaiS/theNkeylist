from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64
import file_handler
import param_handler

params = param_handler.get_params()
password = params.password
if params.filename:
    print(f"Encrypting file: {params.filename} with password: {params.password}")
    message = file_handler.read_file(params.filename)
elif params.message:
    print(f"Encrypting string: {params.message} with password: {params.password}")
    message = params.message
else:
    print("Parameter Error: Neither 'filename' nor 'message' was provided.")
    sys.exit(1)

try:
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    encrypted_msg = base64.b64encode(
        salt + cipher.nonce + tag + ciphertext
    ).decode()

    if params.filename:
        filename, _ = os.path.splitext(params.filename)
        file_handler.write_file(encrypted_msg, filename+params.encrypted_filetype, overwrite = params.encrypt_overwrite)
        #file_handler.write_file(decrypted_msg, filename, params, op="encrypt")) TODO
    elif params.save_encrypted_msg:
        filename = encrypted_msg[:8]
        file_handler.write_file(encrypted_msg, filename+params.encrypted_filetype, overwrite = params.encrypt_overwrite)
    else:
        print("Encrypted Message:", encrypted_msg)
except ValueError as e:
    print(f"Unknown error during encryption: {e}")

#TODO:
#os.system('cls' if os.name == 'nt' else 'clear')