#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import os
import sys
sys.path.insert(0, os.getcwd())

from fabric.api import *  # noqa
env.use_ssh_config = True
env.hosts = [
    # 'a',
    'b',
    # 'c'
    # 'x',
    # 'y',
]


CMD_PYLINT = 'pylint'


def host_type():
    run('uname -s')


@task
def prepare():
    with cd('/opt'):
        run('mkdir -p env')
        run('virtualenv env')
        run('virtualenv --clear env')
        run('virtualenv --relocatable env')

@task
def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist
    put('dist/%s' % filename, '/tmp/%s' % filename)
    with cd('/opt/env'):
        with prefix('source bin/activate'):
            run('pip install /tmp/%s' % filename)


@task
def serve(port=8888, logging='error'):
    """Start the server in development mode."""
    put('app.py', '/opt/env/app.py')
    with cd('/opt/env'):
        with prefix('source bin/activate'):
            run('python app.py --port=%s --logging=%s' % (port, logging))
