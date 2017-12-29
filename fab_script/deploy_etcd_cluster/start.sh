nohup etcd --name infra0 --initial-advertise-peer-urls http://192.168.99.100:2380 --data-dir /data/var/lib/etcd\
  --listen-peer-urls http://192.168.99.100:2380 \
  --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls http://192.168.99.100:2379 \
  --initial-cluster-token etcd-cluster-1 \
  --initial-cluster infra0=http://192.168.99.100:2380,infra1=http://192.168.99.101:2380,infra2=http://192.168.99.102:2380 \
  --initial-cluster-state new > /data/var/log/etcd.log &

nohup etcd --name infra1 --initial-advertise-peer-urls http://192.168.99.101:2380 --data-dir /data/var/lib/etcd\
  --listen-peer-urls http://192.168.99.101:2380 \
  --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls http://192.168.99.101:2379 \
  --initial-cluster-token etcd-cluster-1 \
  --initial-cluster infra0=http://192.168.99.100:2380,infra1=http://192.168.99.101:2380,infra2=http://192.168.99.102:2380 \
  --initial-cluster-state new > /data/var/log/etcd.log &

nohup etcd --name infra2 --initial-advertise-peer-urls http://192.168.99.102:2380 --data-dir /data/var/lib/etcd\
  --listen-peer-urls http://192.168.99.102:2380 \
  --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls http://192.168.99.102:2379 \
  --initial-cluster-token etcd-cluster-1 \
  --initial-cluster infra0=http://192.168.99.100:2380,infra1=http://192.168.99.101:2380,infra2=http://192.168.99.102:2380 \
  --initial-cluster-state new > /data/var/log/etcd.log &