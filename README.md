# lib-version

A version-aware Python library that provides version information. This library can be used to retrieve the version of the package, which is useful for system information in log messages, data records, and debugging.

## Features

- `VersionUtil` class that provides version information
- Automatic versioning based on Git tags
- Fallback mechanism when Git information is not available

## Installation

You can install the library directly from GitHub:

```bash
pip install git+https://github.com/remla25-team21/lib-version.git@v0.1.0
```

> [!NOTE]
> Replace `v0.1.0` with the specific version tag you want to use, or omit `@v0.1.0` to install the latest version from the main branch.

## Usage

```python
# Import the version utility
from libversion import VersionUtil

# Get the current version
version = VersionUtil.get_version()
print(f"remla25-team21-lib-version version: {version}")

# Alternatively, use the convenience function
from libversion import get_version
print(f"remla25-team21-lib-version version: {get_version()}")
```

## Development

### Prerequisites

- Python 3.8 or higher
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/remla25-team21/lib-version.git
   cd lib-version
   ```

2. Install development dependencies:
   ```bash
   pip install -e .
   ```

## Release Process

This library uses GitHub Actions to automate the release process. When a tag with the format `vX.Y.Z` is pushed to the repository, a GitHub Action will automatically:

1. Build the package
2. Create a GitHub Release with the built artifacts

To create a new release:

```bash
git tag v0.1.0
git push origin v0.1.0
```

## License

MIT
