import os
import sys
import argparse

def validate_params(params):
    if bool(params.filename) == bool(params.message):
        print("Error: Specify one of 'filename' or 'message', but not both.")
        sys.exit(1)

def get_params():
    parser = argparse.ArgumentParser(description="Script for file encryption or decryption.")
    parser.add_argument('-p', '--password', type=str, help='The password', required=True)
    parser.add_argument('-f', '--filename', type=str, help='The name of the file')
    parser.add_argument('-m', '--message', type=str, help='The message')
    params = parser.parse_args()
    validate_params(params)

    # User Configurable Parameters:
    params.subfolder="messages"
    params.encrypted_filetype=".enc"
    params.decrypted_filetype=".dec"
    params.encrypt_overwrite=True
    params.decrypt_overwrite=True
    params.save_encrypted_msg=False
    params.show_decrypted_msg=True

    return params

def read_file(filename, subfolder="messages"):
    filepath = os.path.join(subfolder, filename)

    if not os.path.isfile(filepath):
        print(f"Error: The file at '{filepath}' does not exist or is not a valid file.")
        sys.exit(1)
    
    try:
        with open(filepath, 'r') as file:
            file_contents = file.read()
        return file_contents
    except IOError as e:
        print(f"Error: Could not open file '{filepath}' due to an IOError: {e}")
        sys.exit(1)

def write_file(message, filename, subfolder="messages", overwrite=True):
    filepath = os.path.join(subfolder, filename)

    if not overwrite and os.path.isfile(filepath):
        print(f"Error: The file '{filepath}' already exists and overwrite is set to False.")
        sys.exit(1)
    
    try:
        with open(filepath, 'w') as file:
            file.write(message)
        print(f"Message saved to: '{filepath}'.")
    except IOError as e:
        print(f"Error: Could not write to the file '{filepath}' due to an IOError: {e}")
        sys.exit(1)
