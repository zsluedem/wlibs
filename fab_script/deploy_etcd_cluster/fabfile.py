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

etcd_pkg = config.get('etcd_pkg')
pwd = config.get('pwd')
env.hosts = config.get('host')

env.passwords = dict((h, pwd) for h in config.get('host'))

@parallel
def install_etcd():
    home_dir = run('echo $HOME')
    put(os.path.join(BASE_DIR, etcd_pkg), home_dir)
    with cd(home_dir):
        run('tar -zxvf {}'.format(etcd_pkg))
        run('mv {} etcd'.format(etcd_pkg.split('.tar')[0]))
        run('rm {}'.format(etcd_pkg))
    with cd(os.path.join(home_dir, 'etcd')):
        sudo('cp ./etcd /usr/local/bin')
        sudo('cp ./etcdctl /usr/local/bin')
    with cd(home_dir):
        run('rm -rf ./etcd')

def set_up_cluster():
    run('etcd --name infra0 --initial-advertise-peer-urls http://192.168.99.100:2380 --data-dir /data/var/lib/etcd\
  --listen-peer-urls http://192.168.99.100:2380 \
  --listen-client-urls http://192.168.99.100:2379,http://127.0.0.1:2379 \
  --advertise-client-urls http://192.168.99.100:2379 \
  --initial-cluster-token etcd-cluster-1 \
  --initial-cluster infra0=http://192.168.99.100:2380,infra1=http://192.168.99.101:2380,infra2=http://192.168.99.102:2380 \
  --initial-cluster-state new')

for i in env.hosts:
    print i