"""
Remote Notify - Send desktop notifications to remote Linux machines via SSH.

A Python library and command-line tool for sending desktop notifications
to remote Ubuntu/Linux machines using SSH and notify-send.

Example usage:
    >>> from remote_notify import RemoteNotificationManager
    >>> manager = RemoteNotificationManager()
    >>> manager.send_notification("192.168.1.10", "user", "password", "Hello!")

Command line usage:
    $ remote-notify
    $ rnotify  # short alias
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"

from .core import RemoteNotificationManager
from .config import ConfigManager

# Define what gets imported with "from remote_notify import *"
__all__ = [
    "RemoteNotificationManager",
    "ConfigManager",
    "__version__",
]

# Package metadata
__title__ = "remote-notify"
__description__ = "Send desktop notifications to remote Linux machines via SSH"
__url__ = "https://github.com/yourusername/remote-notify"
__author_email__ = __email__
__maintainer__ = __author__
__maintainer_email__ = __email__
__keywords__ = ["ssh", "notification", "remote", "desktop", "linux", "ubuntu"]