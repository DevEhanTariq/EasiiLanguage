import sys
import os
from .commands import *

args = sys.argv[1:]
command = args[0]
directory = os.getcwd()

def main():
    if not args:
        print("Usage: mycli <command>")
        exit()

    if command == "hello":
        hello()
        print(directory)

    elif command == "bye":
        bye()
        print(directory)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()