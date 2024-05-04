#!/usr/bin/python3
"""Fabric script to archive from the contents of the web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Makes an archive from web_static folder
    """

    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the archive path
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the archive
    try:
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None
