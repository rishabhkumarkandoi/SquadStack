"""
Run this file by providing a file path.
"""

import sys

from file_processor import FileProcessor


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        FileProcessor(file_path).process_file()
    except IndexError:
        print("Please provide file path in command line argument")
