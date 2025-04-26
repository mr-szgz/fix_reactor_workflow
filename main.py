#!/usr/bin/env python3

import os
import json
import shutil
import argparse

TARGET_STRING = "comfyui-reactor-node.git"
FIXED_STRING = "Gourieff/comfyui-reactor-node"

def find_corruptions(directory):
    corrupt_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                nodes = data.get("nodes", [])
                for node in nodes:
                    aux_id = node.get("properties", {}).get("aux_id", "")
                    if aux_id == TARGET_STRING:
                        corrupt_files.append(path)
                        break
            except Exception:
                pass
    return corrupt_files

def fix_file(path):
    # Create a .backup folder in the same directory as the file
    backup_dir = os.path.join(os.path.dirname(path), ".backup")
    os.makedirs(backup_dir, exist_ok=True)

    # Copy the original file to the .backup folder
    backup_path = os.path.join(backup_dir, os.path.basename(path))
    shutil.copy2(path, backup_path)

    # Modify the original file
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for node in data.get("nodes", []):
        if node.get("properties", {}).get("aux_id", "") == TARGET_STRING:
            node["properties"]["aux_id"] = FIXED_STRING
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
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