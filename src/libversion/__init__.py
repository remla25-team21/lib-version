"""
Version-aware library that provides version information.
"""
import importlib.metadata
import os
from pathlib import Path


class VersionUtil:
    """Utility class to provide version information for the package."""
    
    @staticmethod
    def get_version():
        """
        Get the version of the library.
        
        Returns:
            str: The version of the library.
        """
        try:
            # Try to get version from package metadata (installed package)
            return importlib.metadata.version("remla25-team21-lib-version")
        except importlib.metadata.PackageNotFoundError:
            # If not installed, try to get version from git
            return VersionUtil._get_version_from_git()
    
    @staticmethod
    def _get_version_from_git():
        """
        Try to get version from Git tags.
        
        Returns:
            str: The version from Git tags or a fallback version.
        """
        import subprocess
        
        try:
            # Get the directory of the current file
            current_dir = Path(__file__).parent.parent.parent.absolute()
            
            # Try to get the git version
            git_command = ["git", "-C", str(current_dir), "describe", "--tags", "--abbrev=0"]
            version = subprocess.check_output(git_command, stderr=subprocess.DEVNULL).decode().strip()
            
            # Remove 'v' prefix if present
            if version.startswith('v'):
                version = version[1:]
                
            return version
        except (subprocess.SubprocessError, FileNotFoundError):
            # Fallback version if git command fails
            return "0.0.0"

# Convenience export
get_version = VersionUtil.get_version