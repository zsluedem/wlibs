# coding=utf8
import json
import os

from fabric.api import env, run
from fabric.context_managers import cd
from fabric.contrib.files import append, exists
from fabric.operations import sudo

from .config import *

env.hosts = HOSTS

env.password = PWD

privoxy_get_url = "http://www.privoxy.org/sf-download-mirror/Sources/3.0.26%20%28stable%29/privoxy-3.0.26-stable-src.tar.gz"

privoxy_config = """
user-manual /usr/local/privoxy/share/doc/privoxy/user-manual/
confdir %s/etc
logdir %s/var/log/privoxy
filterfile default.filter
logfile logfile
listen-address  127.0.0.1:%s
toggle  1
enable-remote-toggle  0
enable-remote-http-toggle  0
enable-edit-actions 0
enforce-blocks 0
buffer-limit 4096
enable-proxy-authentication-forwarding 0
forward-socks5t / 127.0.0.1:%s .
forwarded-connect-retries  0
accept-intercepted-requests 0
allow-cgi-request-crunching 0
split-large-forms 0
keep-alive-timeout 5
tolerate-pipelining 1
socket-timeout 300
forward 192.168.*.*/ .
forward 10.*.*.*/ .
forward 127.*.*.*/ .
forward 172.16.*.*/ .
forward 172.17.*.*/ .
forward 172.18.*.*/ .
forward 172.19.*.*/ .
forward 172.20.*.*/ .
forward 172.21.*.*/ .
forward 172.22.*.*/ .
forward 172.23.*.*/ .
forward 172.24.*.*/ .
forward 172.25.*.*/ .
forward 172.26.*.*/ .
forward 172.27.*.*/ .
forward 172.28.*.*/ .
forward 172.29.*.*/ .
forward 172.30.*.*/ .
forward 172.31.*.*/ .
"""
privoxy_config = privoxy_config % (privoxy_install_path, privoxy_install_path, privoxy_port, shadowsocks_local_port)


def install_shadowsocks():
    sudo('pip install shadowsocks')
    if exists('/etc/shadowsocks.json', True):
        sudo('rm /etc/shadowsocks.json')
    with cd('/etc'):
        append('shadowsocks.json', json.dumps(shadowsocks_config), use_sudo=True)


def start_shadowsocks():
    with cd(home_dir):
        sudo("sslocal -c /etc/shadowsocks.json -d start")
        # run("screen -d -m sleep 60")


def install_privoxy():
    with cd(home_dir):
        run('wget {}'.format(privoxy_get_url))
        run('tar -zxvf privoxy-3.0.26-stable-src.tar.gz')
    with cd(os.path.join(home_dir, 'privoxy-3.0.26-stable')):
        run('autoheader && autoconf')
        run('./configure --prefix={}'.format(privoxy_install_path))
        run('make')
        sudo('useradd privoxy')
        sudo('make install')


def start_privoxy():
    privoxy_config_path = os.path.join(privoxy_install_path, 'config')
    sudo('echo "{}" > {}'.format(privoxy_config, privoxy_config_path))
    with cd(privoxy_install_path):
        sudo('./sbin/privoxy --user privoxy ./config')


def deploy():
    install_shadowsocks()
    start_shadowsocks()
    install_privoxy()
    start_privoxy()
