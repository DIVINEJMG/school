#!/usr/bin/env python3
"""Small helper script to verify the Orange setup environment."""

import sys

def main() -> int:
    print("Orange setup helper running...")
    print(f"Python version: {sys.version.split()[0]}")
    if sys.version_info >= (3, 8):
        print("✓ Python 3.8+ requirement satisfied")
    else:
        print("✗ Python 3.8+ required")
        return 1
    print("Environment verification complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())