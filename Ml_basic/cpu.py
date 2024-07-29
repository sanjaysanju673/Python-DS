'''
@Author: v sanjay kumar
@Date: 2024-07-22 12:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 12:00:30
@Title : Find Number of CPUs
'''

import os

def get_number_of_cpus():
    '''Returns the number of CPUs available on the system.'''
    return os.cpu_count()

def main():
    num_cpus = get_number_of_cpus()
    print(f"Number of CPUs: {num_cpus}")

if __name__ == "__main__":
    main()
