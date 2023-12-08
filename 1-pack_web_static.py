#!/usr/bin/python3
"""Pack web_static folder to an archive"""
from fabric.api import *
import time
import os


def do_pack():
    """Pack a web_static folder to an archive"""
    current_time = time.strftime('%Y%m%d%H%M%S')
    print('Packing web_static to versions/web_static_{}'.format(current_time))
    local("if [ ! -d ./versions/ ]; then mkdir versions; fi;")
    local('tar -cvzf versions/web_static_{}.tgz ./web_static'
          .format(current_time))
    file_path = './1-pack_web_static.py'
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        print('web_static packed: versions/web_static_{}.tgz -> {}Bytes'
              .format(current_time, file_size))
        return f'versions/web_static_{current_time}.tgz'
    else:
        return 'None'
