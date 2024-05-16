#!/usr/bin/python3
"""
    A fabfile that generates compressed files
    and folders for the web_static project
"""
from fabric.api import local
from os.path import isdir
from datetime import datetime


def do_pack():
    """Generates a tg archive of all files and folders"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
            file_name = "versions/web_static_{}.tgz".format(date)
            local("tar -cvzf {} web_static".format(file_name))
            return file_name
    except:
        return None
