
# AES-GCM Encryption and Decryption with PyCryptodome
---

## Requirements

#### **Make Sure Python3 and pip are installed**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
   
#### **Install the pycryptodome library**

For more detailed installation instructions, please refer to the [PyCryptodome Documentation](https://www.pycryptodome.org/src/installation).

```bash
sudo apt install python3-pycryptodome
```
or
```bash
pip install pycryptodome
```
#### **If you get an `externally-managed-environment` error while installing with pip, you can try:**
```bash
pip install pycryptodome --break-system-packages
```

---

## Running the code


The encryption and decryption processes are executed via the command line using the `encrypt.py` and `decrypt.py` scripts. Both scripts follow a similar structure:

```bash
python [script].py [input type] [input value] -p [password]
```

The input type can be `-f` to specify a filename, or `-m` to read a string directly from the terminal.

When encrypting, the password following the `-p` flag can be any secure password of your choice. When decrypting, the provided password must match the password that was used when encrypting the file.


### Examples
```bash
#Encrypt the contents of a file:
python encrypt.py -f foo.txt -p password123

#Encrypt a string:
python encrypt.py -m "hello world!" -p password123

#Decrypt an encrypted file:
python decrypt.py -f foo.enc -p password123

#Decrypt an encrypted string:
python decrypt.py -m o92UunLpDmuhPY/gULkZC4ih7PLqXksWQKuqEc5Rth27mFo3poMQnG8tHbNuLxRAIfwX8ntrerpEsfUZ -p password123
```

### Security Note
It’s recommended to clear your terminal history after you're done so that passwords and unencrypted messages do not get stored. In Bash, the command is:
```bash
history -c && clear
```

---

## Default Behavior and Configurable Parameters

