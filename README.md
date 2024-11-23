
# AES-GCM Encryption and Decryption

This document explains how the encryption and decryption process works in the provided code using AES-GCM (Advanced Encryption Standard - Galois/Counter Mode).

## Requirements

To run the encryption and decryption code, ensure the following dependencies are installed on your system:

#### **1. Install Python 3 and `pip` (if not already installed)**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
   
#### **2. Install the pycryptodome library**
To install the `pycryptodome` library, use one of the following methods:
- **Via apt** (recommended for system-wide installation):
```bash
sudo apt install python3-pycryptodome
```
- **Via pip** (for virtual environments or the latest version):
```bash
pip install pycryptodome
```

---

#### **3. If you encounter an error like `externally-managed-environment` while installing with pip, you can override it using the following command**
```bash
pip install pycryptodome --break-system-packages
```
## Encryption Process

### 1. **Input Parameters**
- **Password**: A user-provided passphrase, e.g., `"your_secure_password"`.
- **Plaintext**: The message you want to encrypt, e.g., `"Your secret string"`.

### 2. **Key Derivation**
The password is converted into a cryptographic key using a **Key Derivation Function (KDF)**:
- **Salt**: A random 16-byte value is generated (`get_random_bytes(16)`).
- **KDF (PBKDF2)**: Combines the password and salt using a secure hash function (SHA-256 by default) and performs multiple iterations (100,000 in your code). This ensures the derived key is unique and strong.

**Output**:
- A **256-bit key** (32 bytes) is derived.

---

### 3. **Encryption with AES**
AES-GCM mode is used for encryption:
- **GCM (Galois/Counter Mode)**: Provides encryption and built-in integrity checks (via the authentication tag).

Key steps:
1. **Nonce**: A random, unique 16-byte value is generated automatically (`cipher.nonce`).
2. **Encrypt and Digest**: The plaintext is encrypted into ciphertext, and an authentication tag is produced to ensure the ciphertext's integrity.

**Output**:
- **Ciphertext**: The encrypted version of the plaintext.
- **Tag**: The authentication tag, used during decryption to verify data integrity.

---

### 4. **Encoding the Encrypted Data**
The salt, nonce, ciphertext, and tag are concatenated into a single binary string in the following order:
1. **Salt** (16 bytes)
2. **Nonce** (16 bytes)
3. **Tag** (16 bytes)
4. **Ciphertext** (variable length, same as plaintext)

This combined binary string is then **Base64-encoded** to ensure it can be safely transmitted as a single string.

**Output**:
- A single Base64-encoded string representing all components of the encrypted data.

---

## Why This Works
1. **Salt**: Ensures that even if the same password is reused, the derived key will be different for each encryption.
2. **Nonce**: Ensures that the same plaintext encrypted with the same key produces different ciphertexts.
3. **Authentication Tag**: Protects against tampering by ensuring that decryption will fail if the ciphertext or nonce has been altered.
4. **AES-GCM**: Provides robust encryption and built-in integrity checks, making it secure for most applications.

---

## Decryption Workflow
The decryption process reverses the encryption:
1. Decode the Base64-encoded string to retrieve the binary data.
2. Split the binary data into its components:
   - Salt (16 bytes)
   - Nonce (16 bytes)
   - Tag (16 bytes)
   - Ciphertext (remaining bytes)
3. Use the salt to regenerate the same cryptographic key from the password.
4. Recreate the AES-GCM cipher using the key and nonce.
5. Decrypt the ciphertext and verify its authenticity using the tag.

---

### **Important Note**
Ensure you always:
- Use a **new, random salt** for each encryption.
- Never reuse the **same nonce** across multiple encryptions with the same key.

#### Why is this important?
1. **Salt**:
   - The salt ensures that the key derived from a password is unique for each encryption.
   - Reusing the same salt allows attackers to detect patterns in the derived keys, making your encryption vulnerable to dictionary or rainbow table attacks.

2. **Nonce**:
   - The nonce ensures that encrypting the same plaintext with the same key produces different ciphertexts.
   - Reusing the nonce with the same key can lead to **nonce reuse attacks**, where attackers may recover plaintexts, deduce relationships between messages, or compromise the key itself.

#### What about tag?
**Tag**:
   - The tag is automatically generated during encryption and ensures the integrity and authenticity of the ciphertext.
   - It verifies that the ciphertext has not been tampered with and is tied to the plaintext, key, and nonce.
   - Users don’t need to manage the tag manually, as it is directly handled by the AES-GCM encryption process.


Both the **salt** and **nonce** are essential for maintaining the confidentiality and integrity of encrypted data. Always generate fresh random values for each encryption operation.

