#!/usr/bin/env python3
"""Small helper to verify the local environment for the Blue setup."""

import platform
import sys

MIN_VERSION = (3, 8)


def main():
    version = sys.version_info
    print(f"Python version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    if (version.major, version.minor) < MIN_VERSION:
        print(f"Error: Python {MIN_VERSION[0]}.{MIN_VERSION[1]}+ is required.")
        return 1
    print("Environment OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
