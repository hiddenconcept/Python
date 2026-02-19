import sys
from pywin32_testutil import non_admin_error_codes
from scrapy.all import*
from urllib import parse
import re

iface = "eth0"

#eth0 - ethernet
def get_login_pass():

    user = none
    password = none
def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        get_login_pass(body)

try:
    sniff(iface=iface, prn=pkt_parser, store = 0)
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)