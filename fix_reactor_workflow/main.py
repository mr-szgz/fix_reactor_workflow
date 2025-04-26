#!/usr/bin/env python3

import os
import json
import shutil
import argparse
import sys
import glob

def find_corruptions_in_file(file_path, target_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        nodes = data.get("nodes", [])
        for node in nodes:
            aux_id = node.get("properties", {}).get("aux_id", "")
            if aux_id == target_string:
                return True  # Corruption found
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return False  # No corruption found

def find_corruptions(path, target_string):
    corrupt_files = []
    if os.path.isfile(path):
        if path.endswith(".json") and find_corruptions_in_file(path, target_string):
            corrupt_files.append(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                file_path = os.path.join(path, filename)
                if find_corruptions_in_file(file_path, target_string):
                    corrupt_files.append(file_path)
    return corrupt_files

def create_backup(file_path):
    backup_path = f"{file_path}~"
    try:
        shutil.copy(file_path, backup_path)
        print(f"Backup created: {backup_path}")
    except Exception as e:
        print(f"Error creating backup for {file_path}: {e}")

# Update the fix_file function to include backup creation
def fix_file(path, target_string, fixed_string):
    try:
        create_backup(path)  # Create a backup before modifying the file
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        nodes = data.get("nodes", [])
        fixed = False
        for node in nodes:
            if node.get("properties", {}).get("aux_id", "") == target_string:
                node["properties"]["aux_id"] = fixed_string
                fixed = True
        if fixed:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            print(f"Fixed aux_id in file: {path}")
    except Exception as e:
        print(f"Error fixing file {path}: {e}")

def main(paths, target_string, fixed_string, auto_confirm):
    all_paths = []
    for path in paths:
        all_paths.extend(glob.glob(path))

    if not all_paths:
        print(f"No files or directories matched the patterns: {paths}")
        sys.exit(1)

    for path in all_paths:
        corrupt_files = find_corruptions(path, target_string)
        if corrupt_files:
            print(f"Found corrupt aux_id in {path}:")
            for f in corrupt_files:
                print(f"  {f}")
            if auto_confirm or input("Fix all? (y/N): ").lower() == "y":
                for f in corrupt_files:
                    fix_file(f, target_string, fixed_string)
                print("All fixed.")
        else:
            print(f"No corrupt aux_id found in {path}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fix corrupted aux_id in JSON files.")
    parser.add_argument("paths", nargs="+", help="Files, directories, or wildcard patterns to scan for JSON files.")
    parser.add_argument("--target", default="comfyui-reactor-node.git", help="Target string to search for (default: comfyui-reactor-node.git).")
    parser.add_argument("--fixed", default="Gourieff/comfyui-reactor-node", help="String to replace the target with (default: Gourieff/comfyui-reactor-node).")
    parser.add_argument("--yes", action="store_true", help="Automatically confirm fixing all corrupt files.")
    args = parser.parse_args()

    main(args.paths, args.target, args.fixed, args.yes)