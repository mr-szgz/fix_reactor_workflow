# Fix Reactor Workflow

A Python package to fix corrupted `aux_id` fields in JSON files.

## Installation

1. Clone the repository or download the source code.
2. Navigate to the `fix_reactor_workflow` directory.
3. Run the following command to install the package:

   ```bash
   pip install .
   ```

## Usage

After installation, you can use the `fix_reactor_workflow` command-line tool to scan and fix JSON files:

```bash
fix_reactor_workflow /path/to/json/files
```

- Replace `/path/to/json/files` with the directory containing the JSON files you want to process.
- The tool will identify files with corrupted `aux_id` fields and prompt you to fix them.
