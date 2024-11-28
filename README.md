
# AES-GCM Encryption and Decryption

This document explains how the encryption and decryption process works in the provided code using AES-GCM (Advanced Encryption Standard - Galois/Counter Mode).

---

## Requirements

#### **Make Sure Python3 and pip are installed**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
   
#### **Install the pycryptodome library**

- **Via apt**
```bash
sudo apt install python3-pycryptodome
```
- **Via pip**
```bash
pip install pycryptodome
```
#### **If you get an `externally-managed-environment` error while installing with pip, you can try overriding it:**
```bash
pip install pycryptodome --break-system-packages
```