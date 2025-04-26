import re
import os

# Get the current version from setup.py
version = os.popen("python3 setup.py --version").read().strip()
release_url = f"https://github.com/mr-szgz/fix_reactor_workflow/releases/tag/v{version}"
download_url = f"https://github.com/mr-szgz/fix_reactor_workflow/releases/download/v{version}"

# Path to the README file
readme_path = "README.md"

# Read the README content
with open(readme_path, "r") as file:
    content = file.read()

# Update the release URL
content = re.sub(r"\[GitHub release page\]\(.*?\)", f"[GitHub release page]({release_url})", content)

# Update the file links
content = re.sub(r"fix_reactor_workflow-[0-9]+\.[0-9]+\.[0-9]+-macos-arm64\.whl", f"fix_reactor_workflow-{version}-macos-arm64.whl", content)
content = re.sub(r"fix_reactor_workflow-[0-9]+\.[0-9]+\.[0-9]+-manylinux1_x86_64\.whl", f"fix_reactor_workflow-{version}-manylinux1_x86_64.whl", content)
content = re.sub(r"fix_reactor_workflow-[0-9]+\.[0-9]+\.[0-9]+-win_amd64\.whl", f"fix_reactor_workflow-{version}-win_amd64.whl", content)

# Update the pip install commands
content = re.sub(r"pip install .*macos-arm64\.whl", f"pip install {download_url}/fix_reactor_workflow-{version}-macos-arm64.whl", content)
content = re.sub(r"pip install .*manylinux1_x86_64\.whl", f"pip install {download_url}/fix_reactor_workflow-{version}-manylinux1_x86_64.whl", content)
content = re.sub(r"pip install .*win_amd64\.whl", f"pip install {download_url}/fix_reactor_workflow-{version}-win_amd64.whl", content)

# Write the updated content back to the README
with open(readme_path, "w") as file:
    file.write(content)

print(f"README updated with version {version} and real URLs.")