#!/bin/sh
# ......DHCP......
logger -p syslog.info "......DHCP........."
/etc/init.d/odhcpd stop >/dev/null 2>&1
/etc/init.d/dnsmasq stop >/dev/null 2>&1
# ...wan...............
brctl show > /opt/br.log
ifconfig >> /opt/br.log
ip addr show >> /opt/br.log
brctl addif br-lan eth1 >/dev/null 2>&1
brctl stp br-lan on
ip addr del 192.168.1.5 dev eth1 >/dev/null 2>&1 #删除原先的wan地址
ip addr del 192.168.2.1 dev br-lan >/dev/null 2>&1 #删除原先的lan地址
ip addr add 192.168.1.5/24 dev br-lan >/dev/null 2>&1 #重新设置lan地址
ifconfig eth1 up >/dev/null 2>&1
ifconfig br-lan up >/dev/null 2>&1
route del -net 239.0.0.0  netmask 255.0.0.0 >/dev/null 2>&1
route add default gateway 192.168.1.2 > /dev/null 2>&1 #重新添加默认路由
# ......IPv6.....................
logger -p syslog.info "......IPv6............"
ip6tables -P INPUT ACCEPT
ip6tables -P FORWARD ACCEPT
ip6tables -F