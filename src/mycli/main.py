import sys
from .commands import *

args = sys.argv[1:]
command = args[0]

def main():
    if not args:
        print("Usage: mycli <command>")
        exit()

    if command == "create":
        create(args)

    elif command[0:2] == "./":
        run(command)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()