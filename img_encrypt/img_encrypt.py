from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_image(input_image_path, output_encrypted_path, key):
    # Step 1: Read the image as binary data
    with open(input_image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    # Step 2: Pad the data
    padded_data = pad(image_data, AES.block_size)  # AES.block_size = 16 bytes
    
    # Step 3: Encrypt the data
    iv = get_random_bytes(AES.block_size)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create AES cipher
    encrypted_data = cipher.encrypt(padded_data)
    
    # Step 4: Save the encrypted data (IV + ciphertext)
    with open(output_encrypted_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_data)


# Usage
key = get_random_bytes(32)  # AES-256 key (32 bytes)
encrypt_image('input.jpg', 'encrypted_image.aes', key)