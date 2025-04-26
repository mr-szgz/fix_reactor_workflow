# Updated Makefile to build static binaries for macOS-arm64, GNU/Linux, and Ubuntu x86_64

# Variables
PACKAGE_NAME = fix_reactor_workflow
VERSION = $(shell python3 setup.py --version)
PLATFORMS = macos-arm64 manylinux1_x86_64 win_amd64

.PHONY: all clean build install release update-readme help

# Default target
all: build

# Build the package for all target systems
build: clean
	@for platform in $(PLATFORMS); do \
	  python3 setup.py bdist_wheel --plat-name=$$platform; \
	  mv dist/*.whl dist/$(PACKAGE_NAME)-$(VERSION)-$$platform.whl; \
	  echo "Built binary for $$platform"; \
	done
	@echo "Build complete. Check the 'dist/' directory for output."

# Clean up build artifacts
clean:
	rm -rf build dist *.egg-info
	mkdir -p dist
	@echo "Cleaned up build artifacts."

# Install the package locally
install:
	pip install .

# Create a GitHub release using gh CLI
release: build
	@if [ -z "$(shell ls -A dist)" ]; then \
	  echo "Error: No files found in 'dist/' directory. Ensure the build step completed successfully."; \
	  exit 1; \
	fi
	gh release create v$(VERSION) dist/* --title "Release v$(VERSION)" --notes "Automated release for version $(VERSION)"
	@echo "GitHub release created for version $(VERSION)."

# Update README with the current version
readme:
	python3 scripts/update_readme.py
	echo "Updated README with version $(VERSION) and real URLs."

# Help command
help:
	@echo "Available targets:"
	@echo "  build    - Build the package for all target systems"
	@echo "  clean    - Remove build artifacts"
	@echo "  install  - Install the package locally"
	@echo "  release  - Create a GitHub release using gh CLI"
	@echo "  readme - Update README with the current version"
	@echo "  help     - Show this help message"