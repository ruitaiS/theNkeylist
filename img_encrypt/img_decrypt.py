from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def decrypt_image(input_encrypted_path, output_decrypted_path, key):
    # Step 1: Read the encrypted data
    with open(input_encrypted_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Step 2: Extract the IV and ciphertext
    iv = encrypted_data[:AES.block_size]  # First 16 bytes for IV
    ciphertext = encrypted_data[AES.block_size:]
    
    # Step 3: Decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Recreate the cipher
    padded_data = cipher.decrypt(ciphertext)
    
    # Step 4: Remove padding
    original_data = unpad(padded_data, AES.block_size)
    
    # Step 5: Save the decrypted data back as an image
    with open(output_decrypted_path, 'wb') as decrypted_file:
        decrypted_file.write(original_data)

# Usage
key = get_random_bytes(32)  # AES-256 key (32 bytes)
decrypt_image('encrypted_image.aes', 'decrypted_image.jpg', key)
