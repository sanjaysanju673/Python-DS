'''
@Author: v sanjay kumar
@Date: 2024-07-22 1:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 1:00:30
@Title : Access Environment Variables
'''

import os

def get_environment_variable(var_name):
    '''Returns the value of the specified environment variable.
    
    Parameters:
    var_name (str): The name of the environment variable.
    
    Returns:
    str: The value of the environment variable if it exists, else a message indicating it is not found.
    '''
    value = os.getenv(var_name)
    if value is not None:
        return value
    else:
        return f"Environment variable '{var_name}' not found."

def main():
    # List of environment variables to access
    variables = ['PATH', 'HOME', 'USER']
    
    for var in variables:
        print(f"{var}: {get_environment_variable(var)}")

if __name__ == "__main__":
    main()
