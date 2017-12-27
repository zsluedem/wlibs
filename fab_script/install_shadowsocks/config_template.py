# coding = utf8

# the hosts you want to install ss and privoxy
HOSTS = [
    "apple@8.8.8.8:4444"
    # "qiuweilue@219.135.102.83:9529"
]

# hosts password
PWD = 'appleisgood'

# ss bind port
shadowsocks_local_port = 1086

# ss config
shadowsocks_config = {
    "server":"google.com",
    "server_port":8089,
    "local_port":shadowsocks_local_port,
    "password":"appleisnotgood",
    "timeout":600,
    "method":"aes-256-cfb"
}

# some download will put in this dir
home_dir = "/home/apple"

# privoxy install path
privoxy_install_path = '/usr/local/privoxy'

# privoxy bind port
privoxy_port = 8118
