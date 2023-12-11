#!/usr/bin/python3
"""Pack web_static folder to an archive"""

from fabric.api import *
import os
import time

env.hosts = ['54.237.23.212', '54.236.47.5']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """Deploy to a server"""
    if os.path.exists(archive_path):
        path = './AirBnB_clone_v2'
        put(
            local_path='{}/{}'.format(path, archive_path), remote_path='/tmp/')

        file_name, file_extension = archive_path.split('.tgz')
        version, without_extens = file_name.split('/')
        releases = '/data/web_static/releases'
        run('sudo mkdir -p {}/{}/'
            .format(releases, without_extens))
        run('sudo tar -xzf /tmp/{}.tgz -C {}/{}/'
            .format(without_extens, releases, without_extens))
        run('sudo rm /tmp/{}.tgz'
            .format(without_extens))
        run('sudo mv {}/{}/web_static/* {}/{}/'
            .format(releases, without_extens, releases, without_extens))
        run('sudo rm -rf {}/{}/web_static'
            .format(releases, without_extens))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}/{}/ /data/web_static/current'
            .format(releases, without_extens))
        print('New version deployed!')
        return True
    else:
        return False
