#!/usr/bin/python3
"""Pack web_static folder to an archive"""

from fabric.api import *
import os

env.hosts = '54.237.23.212', '54.236.47.5'


def do_deploy(archive_path):
    """Deploy to a server"""
    if os.path.exists(archive_path):
        path = '~/Desktop/AirBnB_clone_v2'
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
