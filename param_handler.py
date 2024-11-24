import argparse
import sys

def validate_params(params):
    # Ensure that either filename or message is provided, but not both or neither
    if bool(params.filename) == bool(params.message):
        print("Error: Specify one of 'filename' or 'message', but not both.")
        sys.exit(1)

def get_params():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Script for file encryption or decryption.")
    
    # Add required password argument
    parser.add_argument('-p', '--password', type=str, help='The password', required=True)
    
    # Add optional argument for filename
    parser.add_argument('-f', '--filename', type=str, help='The name of the file')
    
    # Add optional argument for the encrypted message
    parser.add_argument('-m', '--message', type=str, help='The message')

    # Parse the arguments
    params = parser.parse_args()

    # Validate the arguments
    validate_params(params)

    #TODO: Read this off the cfg file
    params.subfolder="messages"
    params.encrypt_overwrite=True
    params.decrypt_overwrite=False
    params.encrypted_filetype=".enc"
    params.decrypted_filetype=".dec"

    return params

'''
    # Proceed with the respective operation
    if params.filename:
        print(f"Processing file: {params.filename} with password: {params.password}")
    elif params.message:
        print(f"Processing message: {params.message} with password: {params.password}")
        # Call a function to handle message encryption/decryption here
    else:
        print("Error: Neither 'filename' nor 'message' was provided.")
        sys.exit(1)
'''