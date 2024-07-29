'''
@Author: v sanjay kumar
@Date: 2024-07-22 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 12:30:30
@Title : List All Files in a Directory
'''

import os

def list_files_in_directory(directory):
    '''Lists all files in the specified directory.

    Parameters:
    directory (str): The path of the directory.

    Returns:
    list: A list of file names in the directory.
    '''
    try:
        # List all files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")
        return []

def main():
    directory = input("Enter the path of the directory: ")
    files = list_files_in_directory(directory)
    if files:
        print("Files in the directory:")
        for file in files:
            print(file)
    else:
        print("No files found or there was an error.")

if __name__ == "__main__":
    main()
