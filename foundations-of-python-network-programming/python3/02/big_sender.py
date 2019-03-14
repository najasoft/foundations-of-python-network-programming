#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - big_sender.py
# Send a big UDP packet to our server.

import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060
#values retrieved from in.h
IP_MTU_DISCOVER=10  # Set/get path MTU discover state.
IP_PMTUDISC_DO=2  #IP_PMTUDISC_DO will force all outgoing packets to have the DF bit set and an attempt to send packets larger than path MTU will result in an error. 
IP_MTU=14
if len(sys.argv) != 2:
    print('usage: big_sender.py host', file=sys.stderr)
    sys.exit(2)

hostname = sys.argv[1]
s.connect((hostname, PORT))
s.setsockopt(socket.IPPROTO_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DO)
try:
    print('MTU:', s.getsockopt(socket.IPPROTO_IP, IP_MTU))
    s.send(b'#' * 65000)
except socket.error:
    print('The message did not make it')
    print('MTU:', s.getsockopt(socket.IPPROTO_IP, IP_MTU))
else:
    print('The big message was sent! Your network supports really big packets!')
