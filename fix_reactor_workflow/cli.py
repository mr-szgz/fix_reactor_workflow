import argparse
from fix_reactor_workflow.main import main as main_function

def main():
    parser = argparse.ArgumentParser(description="Fix corrupted aux_id in JSON files.")
    parser.add_argument("paths", nargs="+", help="Files, directories, or wildcard patterns to scan for JSON files.")
    parser.add_argument("--target", default="comfyui-reactor-node.git", help="Target string to search for (default: comfyui-reactor-node.git).")
    parser.add_argument("--fixed", default="Gourieff/comfyui-reactor-node", help="String to replace the target with (default: Gourieff/comfyui-reactor-node).")
    parser.add_argument("--yes", action="store_true", help="Automatically confirm fixing all corrupt files.")
    args = parser.parse_args()

    main_function(args.paths, args.target, args.fixed, args.yes)

if __name__ == "__main__":
    main()