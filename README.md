
# AES-GCM Encryption and Decryption with PyCryptodome
---

## Requirements

Linux: chmod+x and run `install_ubuntu_python3_dependencies.sh`

Step by step is below:

#### **Make sure Python3 and pip are installed:**

Linux:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Windows:
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```
   
#### **Install the pycryptodome library:**

For more detailed installation instructions, please refer to the [PyCryptodome Documentation](https://www.pycryptodome.org/src/installation).

```bash
sudo apt install python3-pycryptodome
```
or using pip (on windows):
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


### Examples:
```bash
#Encrypt the contents of a file
python encrypt.py -f foo.txt -p password123

#Encrypt a string
python encrypt.py -m "hello world!" -p password123

#Decrypt an encrypted file
python decrypt.py -f foo.enc -p password123

#Decrypt an encrypted string
python decrypt.py -m o92UunLpDmuhPY/gULkZC4ih7PLqXksWQKuqEc5Rth27mFo3poMQnG8tHbNuLxRAIfwX8ntrerpEsfUZ -p password123
```

## User Parameters

Several user configurable parameters can be changed from within the `param_handler.py` file:

### File Directory
By default the code looks in the "messages" subdirectory when using the -f flag
```bash
params.subfolder="messages"
```

### File Extension

```bash
params.encrypted_filetype=".enc"
params.decrypted_filetype=".dec"
```

### Overwrite Behavior

```bash
params.encrypt_overwrite=True
params.decrypt_overwrite=True
```

### Encrypt / Decrypt Behavior

```bash
params.save_encrypted_msg=False
params.show_decrypted_msg=True
```


### Security Note
It’s recommended to clear your terminal history after you're done so that passwords and unencrypted messages do not get stored. 

Bash (Ubuntu):
```bash
history -c && clear
```

Powershell (Windows):
```bash
clear-history; clear-host
```

---

