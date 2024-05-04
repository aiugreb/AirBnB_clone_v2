#!/usr/bin/python3
"""
Based on 1 and 2, fabric script to full deploy
"""

from fabric.api import *
from datetime import datetime
from os.path import isfile
env.hosts = ['35.174.208.96', '52.91.120.160']


def do_pack():
    """Makes an archive from web_static folder"""
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


def do_deploy(archive_path):
    """deploys the archive to the web servers"""
    if not isfile(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        release_dir = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(release_dir, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, release_dir, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(release_dir, no_ext))
        run('rm -rf {}{}/web_static'.format(release_dir, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(release_dir, no_ext))
        return True
    except Exception as er:
        return False


def deploy():
    """Deploys the website"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
