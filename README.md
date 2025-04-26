# Fix Reactor Workflow

A Python package to fix corrupted `aux_id` fields in JSON files.

## Overview

`fix_reactor_workflow` is a tool designed to streamline workflows across multiple platforms, including macOS (ARM64), Linux, and Windows. This project includes a `Makefile` to simplify building, cleaning, installing, and releasing the package.

## Makefile Targets

The `Makefile` provides the following targets:

- **`make build`**: Builds the package for all supported platforms (macOS ARM64, Linux, and Windows). The resulting binaries are placed in the `dist/` directory with platform-specific naming.
- **`make clean`**: Cleans up build artifacts by removing the `build`, `dist`, and `.egg-info` directories.
- **`make install`**: Installs the package locally using `pip`.
- **`make release`**: Creates a GitHub release using the `gh` CLI. This target ensures the `dist/` directory contains build artifacts before proceeding.
- **`make help`**: Displays a list of available targets and their descriptions.

## Installation

1. Clone the repository or download the source code.
2. Navigate to the `fix_reactor_workflow` directory.
3. Run the following command to install the package:

   ```bash
   pip install .
   ```

## Installing from a Release

To install the package from a release, follow these steps:

1. Download the appropriate binary for your platform from the [GitHub release page](https://github.com/mr-szgz/fix_reactor_workflow/releases/tag/v1.0.3). The files are named as follows:
   - [fix_reactor_workflow-1.0.3-macos-arm64.whl](https://github.com/mr-szgz/fix_reactor_workflow/releases/download/v1.0.2/fix_reactor_workflow-1.0.3-macos-arm64.whl) for macOS ARM64
   - [fix_reactor_workflow-1.0.3-manylinux1_x86_64.whl](https://github.com/mr-szgz/fix_reactor_workflow/releases/download/v1.0.2/fix_reactor_workflow-1.0.3-manylinux1_x86_64.whl) for Linux
   - [fix_reactor_workflow-1.0.3-win_amd64.whl](https://github.com/mr-szgz/fix_reactor_workflow/releases/download/v1.0.2/fix_reactor_workflow-1.0.3-win_amd64.whl) for Windows

2. Use `pip` to install the downloaded file. For example:

   ```bash
   pip install https://github.com/mr-szgz/fix_reactor_workflow/releases/download/v1.0.3/fix_reactor_workflow-1.0.3-macos-arm64.whl
   ```

## Usage

After installation, you can use the `fix_reactor_workflow` command-line tool to scan and fix JSON files:

```bash
fix_reactor_workflow /path/to/json/files
```

- Replace `/path/to/json/files` with the directory containing the JSON files you want to process.
- The tool will identify files with corrupted `aux_id` fields and prompt you to fix them.

## Prerequisites

- Python 3.x
- `pip` for package installation
- `gh` CLI for creating GitHub releases (only required for maintainers)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.
