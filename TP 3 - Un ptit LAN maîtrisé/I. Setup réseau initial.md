🌞 **`ping` d'un client du `LAN1` vers un client du `LAN 2`**
```
PC1> show ip
NAME
: PC1[1]
IP/MASK : 10.3.1.1/24
GATEWAY : 10.3.1.254
DNS
MAC
00:50:79:66:68:00
LPORT : 20026
RHOST:PORT
127.0.0.1:20027
MTU : 1500

PC1> ping 10.3.2.2
84 bytes from 10.3.2.2 icmp_seq=1 ttl=62 time=41.389 ms
84 bytes from 10.3.2.2 icmp_seq=2 ttl=62 time=38,424 ms 84 bytes from 10.3.2.2 icmp_seq=3 ttl=62 time=33.709 ms
84 bytes from 10.3.2.2 icmp_seq=4 ttl=62 time=29.687 ms
84 bytes from 10.3.2.2 icmp_seq=5 ttl=62 time=23.024 ms
```

🌞 **Capture Wireshark `ping_partie1`**
[Echange ICMP entre deux LAN](ping_entre_deux_lan.pcapng)

🌞 **Afficher les adresses MAC des routeurs**
```
R2#show arp
Protocol Address Age (min) Hardware Addr Type Interface
Internet 10,3.12.1 24 c401.05da.0001 ARPA FastEthernet0/0
Internet 10.3.12.2  - c402.060a.0000 ARPA FastEthernet0/0
Internet 10.3.2.2   0  0050.7966.6802 ARPA FastEthernet1/0
Internet 10.3.2.1  17 050.7966.6803 ARPA FastEthernet1/0
Internet 10.3.2.254 - c402.060.0010 ARPA FastEthernet1/0
```

***

🌞 **Prouvez que vous avez déjà un accès internet sur `r1`**
```
R1#ping 8,8,8,8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
Success rate is 100 percent (5/5), round-trip min/avg/max = 60/79/96 ms
```

🌞 **Accès internet `LAN1`**
```
PC1> ping 8.8.8.8

184 bytes from 8.8.8.8 icmp_seq=1 ttl=59 time=39.400 ms
184 bytes from 8.8.8.8 icmp_seq=2 ttl=59 time=44.366 ms
184 bytes from 8.8.8.8 icmp_seq=3 ttl=59 time=39.093 ms
```

🌞 **Accès internet `LAN2`**
```
PC3> ping 1.1.1.1

84 bytes from 1.1.1.1 icmp_seq=1 ttl=57 time=47.942 ms
84 bytes from 1.1.1.1 icmp_seq=2 ttl=57 time=45.632 ms
84 bytes from 1.1.1.1 icmp_seq=3 ttl=57 time=52.843 ms
84 bytes from 1.1.1.1 icmp_seq=4 ttl=57 time=62.019 ms
```