import os
import sys

def read_file(filename, subfolder="messages"):
    filepath = os.path.join(subfolder, filename)

    # Check if the file exists
    if not os.path.isfile(filepath):
        print(f"Error: The file at '{filepath}' does not exist or is not a valid file.")
        sys.exit(1)
    
    # Try to open the file and read it
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