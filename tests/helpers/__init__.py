"""
Helper utilities for tests.
"""

from pathlib import Path


def get_project_root():
    """
    Get the project root directory.
    
    Returns:
        Path: Absolute path to project root
    """
    return Path(__file__).parent.parent.parent


def get_stop_hook_path():
    """
    Get the path to stop_hook.sh relative to project root.
    
    Returns:
        Path: Absolute path to stop_hook.sh
    """
    return get_project_root() / "stop_hook.sh"

# Made with Bob
