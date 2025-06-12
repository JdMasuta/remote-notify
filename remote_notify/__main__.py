"""
Main entry point for the remote-notify package.

This allows the package to be run as a module:
    python -m remote_notify
"""

from .cli import main

if __name__ == "__main__":
    main()