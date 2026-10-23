#!/usr/bin/env python3
"""Small helper to verify the setup environment."""
import sys

def main() -> int:
    print("RED setup helper")
    print(f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    if sys.version_info >= (3, 8):
        print("Environment OK: Python 3.8+")
        return 0
    else:
        print("Environment error: Python 3.8 or newer required")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())