'''
@Author: v sanjay kumar
@Date: 2024-07-22 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 10:00:30
@Title : Print Documentation of Built-in Function
'''

def print_function_docs(func):
    '''Prints the documentation of a given Python built-in function.

    Parameters:
    func (function): The built-in function whose documentation is to be printed.

    Returns:
    None
    '''
    print(func.__doc__)

def main():
    function_name = input("Enter the name of the built-in function: ")
    try:
        func = globals()[function_name]
        print_function_docs(func)
    except KeyError:
        print(f"No built-in function named '{function_name}' found.")

if __name__ == "__main__":
    main()
