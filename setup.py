from setuptools import setup, find_packages

setup(
    name="fix_reactor_workflow",
    version="1.0.0",
    packages=find_packages(include=["fix_reactor_workflow", "fix_reactor_workflow.*"]),
    entry_points={
        "console_scripts": [
            "fix_reactor_workflow=fix_reactor_workflow.cli:main",
        ],
    },
    install_requires=[],
    description="A tool to fix corrupted aux_id in JSON files.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/fix_reactor_workflow",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)