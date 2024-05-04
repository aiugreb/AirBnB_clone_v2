#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from fabric.api import *
from os.path import isfile
env.hosts = ['35.174.208.96', '52.91.120.160']


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
    except Exception as e:
        return False
