#!/usr/bin/python3
"""Deletes out-of-date archives_v"""

import os
from fabric.api import *

env.hosts = ['35.174.208.96', '52.91.120.160']


def do_clean(number=0):
    """Deletes out-of-date archives_v.
    Args:
        number (int): The number of archives_v versions to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives_v_v = sorted(os.listdir("versions"))
    [archives_v.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives_v]

    with cd("/data/web_static/releases"):
        archives_v = run("ls -tr").split()
        archives_v = [a for a in archives_v if "web_static_" in a]
        [archives_v.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives_v]
