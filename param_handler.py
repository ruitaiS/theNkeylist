import argparse
import sys

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
    params.encrypt_overwrite=True
    params.decrypt_overwrite=True
    params.save_encrypted_msg=False # encrypt -m mode will save the encrypted message with an automatically generated filename as well as display it to screen
    params.show_decrypted_msg=True # decrypt -f mode will display the decrypted message, as well as save it to file
    params.encrypted_filetype=".enc"
    params.decrypted_filetype=".dec"

    return params