# coding = utf8

HOSTS = [
    "apple@8.8.8.8:4444"
    # "qiuweilue@219.135.102.83:9529"
]

PWD = 'appleisgood'

shadowsocks_local_port = 1086
shadowsocks_config = {
    "server":"google.com",
    "server_port":8089,
    "local_port":shadowsocks_local_port,
    "password":"appleisnotgood",
    "timeout":600,
    "method":"aes-256-cfb"
}

home_dir = "/home/apple"
privoxy_install_path = '/usr/local/privoxy'
privoxy_port = 8118
