#!/usr/bin/env python3

from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

def main():
    sniff(prn=packet_callback, count=1)

if __name__ in "__main__":
    main()

