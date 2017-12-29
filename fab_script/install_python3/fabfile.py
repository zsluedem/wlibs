# coding=utf8
from __future__ import absolute_import
import os
import sys
from yaml import load
from fabric.api import env, run

from fabric.context_managers import cd
from fabric.contrib.files import append, exists
from fabric.operations import sudo, put
from fabric.api import local, env, hosts, run, parallel

BASE_DIR = os.path.split(os.path.abspath(__file__))[0]


with open('config.yml') as f:
    config = load(f)

pwd = config.get('pwd')
env.hosts = config.get('host')
env.passwords = dict((h, pwd) for h in config.get('host'))

install_path = config.get('install_path')

@parallel
def install_dependency():
    # sudo('yum groupinstall -y development')
    sudo('yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel')

@parallel
def install_python():
    install_dependency()
    home_dir = run('echo $HOME')
    put(os.path.join(BASE_DIR, 'Python-3.6.4.tgz'), home_dir)
    with cd(home_dir):
        run('tar -zxvf Python-3.6.4.tgz')
    with cd(os.path.join(home_dir, 'Python-3.6.4')):
        run('./configure --prefix={}'.format(install_path))
        run('make')
        sudo('make install')

@parallel
def install_virtualenv():
    sudo('{} install virtualenv'.format(os.path.join(install_path, 'bin/pip3')))


@parallel
def control():
    home_dir = run('echo $HOME')

    exec_p = os.path.join(home_dir, 'lenv/bin/pip')
    with cd(os.path.join(home_dir, 'JZquantBack')):
        run('{} install -r requirements.txt'.format(exec_p))
