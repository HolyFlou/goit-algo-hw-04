from sys import argv
from dir import get_dir

def main():
    if len(argv) > 1:
        get_dir(argv[1])

if __name__ == "__main__":
    main()
