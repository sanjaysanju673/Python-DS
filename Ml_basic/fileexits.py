'''
@Author: v sanjay kumar
@Date: 2024-07-18 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:00:30
@Title : Check Whether a File Exists
'''



from pathlib import Path

def check_file_exists(file_path):
    '''Checks whether a file exists at the specified path.

    Parameters:
    file_path (str): The path of the file to check.

    Returns:
    bool: True if the file exists, False otherwise.
    '''
    return Path(file_path).exists()

def main():
    file_path = input("Enter the path of the file to check: ")
    if check_file_exists(file_path):
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does not exist.")

if __name__ == "__main__":
    main()
