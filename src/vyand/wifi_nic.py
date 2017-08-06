import logging

from attentive import StoppableThread
from scapy.all import sniff
from scapy.layers import dot11

logger = logging.getLogger(__name__)

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


class HandleDot11:
    def __init__(self):
        self.ap_list = []

    def packet_handler(self, pkt):
        if pkt.haslayer(dot11):
            if pkt.type == 0 and pkt.subtype == 8:
                if pkt.addr2 not in self.ap_list:
                    self.ap_list.append(pkt.addr2)
                    print('AP MAC: {mac} with SSID: {ssid}'.format(mac=pkt.addr2, ssid=pkt.info))

    def __call__(self, *args, **kwargs):
        self.packet_handler(*args)


class WiFiNicListener(StoppableThread):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface

    def run(self):
        handler = HandleDot11()
        while not self.stopped:

            sniff(iface=self.interface, prn=print)
            # sniff(iface=self.interface, prn=handler)
