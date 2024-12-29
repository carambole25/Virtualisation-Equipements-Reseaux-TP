### 1. DHCP
🌞 **Prouvez avec un VPCS**
```
PC4> dhcp
DORA IP 10.3.2.10/24 GW 10.3.2.254

PC4> sh ip      

NAME        : PC4[1]
IP/MASK     : 10.3.2.10/24
GATEWAY     : 10.3.2.254
DNS         : 1.1.1.1  
DHCP SERVER : 10.3.2.253
DHCP LEASE  : 43054, 43066/21533/37682
DOMAIN NAME : dns.tp2.b2
MAC         : 00:50:79:66:68:03
LPORT       : 20020
RHOST:PORT  : 127.0.0.1:20021
MTU         : 1500

PC4> ping 1.1.1.1

84 bytes from 1.1.1.1 icmp_seq=1 ttl=59 time=20.809 ms
84 bytes from 1.1.1.1 icmp_seq=2 ttl=59 time=19.477 ms
84 bytes from 1.1.1.1 icmp_seq=3 ttl=59 time=17.022 ms
84 bytes from 1.1.1.1 icmp_seq=4 ttl=59 time=16.299 ms
84 bytes from 1.1.1.1 icmp_seq=5 ttl=59 time=20.685 ms
```

### 2. DNS
🌞 **Tests résolutions DNS**
```
PC4> dhcp
DORA IP 10.3.2.10/24 GW 10.3.2.254

PC4> sh ip

NAME        : PC4[1]
IP/MASK     : 10.3.2.10/24
GATEWAY     : 10.3.2.254
DNS         : 10.3.3.1  
DHCP SERVER : 10.3.2.253
DHCP LEASE  : 42680, 42689/21344/37352
DOMAIN NAME : dns.tp2.b2
MAC         : 00:50:79:66:68:03
LPORT       : 20025
RHOST:PORT  : 127.0.0.1:20026
MTU         : 1500

PC4> ping efrei.fr  
efrei.fr resolved to 51.255.68.208

84 bytes from 51.255.68.208 icmp_seq=1 ttl=59 time=43.690 ms
84 bytes from 51.255.68.208 icmp_seq=2 ttl=59 time=42.919 ms
84 bytes from 51.255.68.208 icmp_seq=3 ttl=59 time=44.278 ms
84 bytes from 51.255.68.208 icmp_seq=4 ttl=59 time=43.068 ms

PC4> ping dns.tp3.b2 
dns.tp3.b2 resolved to 10.3.3.1

84 bytes from 10.3.3.1 icmp_seq=1 ttl=63 time=18.995 ms
84 bytes from 10.3.3.1 icmp_seq=2 ttl=63 time=18.530 ms
84 bytes from 10.3.3.1 icmp_seq=3 ttl=63 time=17.155 ms
```

🌞 **Capture Wireshark**
[Echange DNS](echange_dns.pcapng)

### 3. HTTP
🌞 **Preuve avec un client**
```
root@localhost toto]# curl web.tp3.b2 | head
<!doctype html>
<head>
<meta name='viewport" content='width=device-width, initial-scale=1'>
<title>HTTP Server Test Page powered by: Rocky Linux</title>


[root@localhost toto]# curl supersite.tp3.b2 | head
<!doctype html>
<head>
<meta name='viewport" content='width=device-width, initial-scale=1'>
<title>HTTP Server Test Page powered by: Rocky Linux</title>
```
