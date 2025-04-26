import argparse
from .main import find_corruptions, fix_file

def main():
    parser = argparse.ArgumentParser(description="Fix corrupted aux_id in JSON files.")
    parser.add_argument("directory", help="Directory to scan for JSON files.")
    args = parser.parse_args()

    directory = args.directory
    corrupt_files = find_corruptions(directory)
    if corrupt_files:
        print("Found corrupt aux_id in:")
        for f in corrupt_files:
            print(f"  {f}")
        if input("Fix all? (y/N): ").lower() == "y":
            for f in corrupt_files:
                fix_file(f)
            print("All fixed.")
    else:
        print("No corrupt aux_id found.")

if __name__ == "__main__":
    main()