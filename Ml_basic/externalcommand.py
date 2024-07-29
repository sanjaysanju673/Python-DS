'''
@Author: v sanjay kumar
@Date: 2024-07-18 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:00:30
@Title : Call an External Command
'''

import subprocess

def call_external_command(command):
    '''Calls an external command and prints its output and errors.

    Parameters:
    command (str): The command to be executed.
    
    Returns:
    None
    '''
    try:
        # Run the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Print the standard output
        print("Output:")
        print(result.stdout)
        
        # Print the standard error (if any)
        if result.stderr:
            print("Error:")
            print(result.stderr)
        
        # Print the return code
        print(f"Return code: {result.returncode}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    command = input("Enter the command to execute: ")
    call_external_command(command)

if __name__ == "__main__":
    main()
