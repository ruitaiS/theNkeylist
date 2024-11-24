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
    print(f"Decrypting file: {params.filename} with password: {params.password}")
    encrypted_message = file_handler.read_file(params.filename)
elif params.message:
    print(f"Decrypting string: {params.message} with password: {params.password}")
    encrypted_message = params.message
else:
    print("Parameter Error: Neither 'filename' nor 'message' was provided.")
    sys.exit(1)


# Decrypt
try:
    decoded_data = base64.b64decode(encrypted_message)
    salt = decoded_data[:16]          # First 16 bytes (salt)
    nonce = decoded_data[16:32]       # Next 16 bytes (nonce)
    tag = decoded_data[32:48]         # Next 16 bytes (tag)
    ciphertext = decoded_data[48:]    # Remaining bytes (ciphertext)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_msg = cipher.decrypt_and_verify(ciphertext, tag).decode()

    filetype = ""
    if params.filename:
        filename, filetype = os.path.splitext(params.filename)
        file_handler.write_file(decrypted_msg, filename+params.decrypted_filetype, overwrite = params.decrypt_overwrite)
        #file_handler.write_file(decrypted_msg, filename, params, op="decrypt")) TODO
    else:
        print("Decrypted Message:", decrypted_msg)
except ValueError as e:
    if str(e) == "MAC check failed":
        print("Error: MAC check failed. (Check the password)")
    elif str(e).startswith("Invalid base64-encoded string"):
        print("TODO")
        #if params.filename and filetype and filetype != params.encrypted_filetype:
        #    print("Error: Invalid base64-encoded string. (Check the file extension, and that the message is properly copied)")
        #elif params.message or (filetype and (filetype == params.encrypted_filetype)):
        #   print("Error: Invalid base64-encoded string. (Check if the encrypted message is properly copied)")
    else:
        print(f"Unknown error during decryption: {e}")
