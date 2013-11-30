import re
from scapy.sendrecv import sniff
from scapy.layers.inet import TCP
from http import HTTPRequest

class watch(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
    def logSites(self, packet):
        if packet.haslayer(TCP):
            data = packet.getlayer(TCP)
            
            try:
                request = HTTPRequest(data.load)
                print "%s %s%s" % (request.command, request.headers['host'], request.path)
            except: pass
            
    def run(self):
        sniff(filter="src %s and dst port %d" % (self.ip, self.port), prn=self.logSites)