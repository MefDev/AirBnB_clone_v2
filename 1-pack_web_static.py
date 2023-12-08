#!/usr/bin/python3
"""Pack web_static folder to an archive"""
from fabric.api import *
import time


def do_pack():
    """Pack a web_static folder to an archive"""
    current_time = time.strftime('%Y%m%d%H%M%S')
    print('Packing web_static to versions/web_static_{}'.format(current_time))
    local("if [ ! -d ./versions/ ]; then mkdir versions; fi;")
    local('tar -cvzf versions/web_static_{}.tgz ./web_static'
          .format(current_time))
