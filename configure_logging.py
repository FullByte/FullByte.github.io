#!/usr/bin/env python3
"""
Logging configuration for MkDocs build to suppress verbose git plugin messages
"""

import logging
import sys

def configure_quiet_logging():
    """Configure logging to suppress verbose git-revision-date messages."""
    # Get the git-revision-date plugin logger
    git_logger = logging.getLogger('mkdocs.plugins.git_revision_date_localized')
    git_logger.setLevel(logging.WARNING)
    
    # Also suppress the RSS plugin verbose messages
    rss_logger = logging.getLogger('mkdocs.plugins.rss')
    rss_logger.setLevel(logging.WARNING)
    
    # Configure root logger to be less verbose
    root_logger = logging.getLogger()
    if root_logger.level < logging.WARNING:
        root_logger.setLevel(logging.INFO)

if __name__ == "__main__":
    configure_quiet_logging()
