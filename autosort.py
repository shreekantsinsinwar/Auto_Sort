import argparse
from utils.file_handler import sort_by_extension

def main():
    parser = argparse.ArgumentParser(description='Sort files by extension')
    parser.add_argument('--source', required=True, help='Source folder')
    parser.add_argument('--destination', required=True, help='Destination folder')
    args = parser.parse_args()

    sort_by_extension(args.source, args.destination)

if __name__ == '__main__':
    main()
