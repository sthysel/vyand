import os

import click
from attentive import quitevent

from .wifi_nic import WiFiNicListener


@click.command()
@click.option('-i', '--interface', help='The wireless LAN interface')
@click.option('-c', '--channel', help='The wireless LAN interface')
def cli(interface, channel):
    """ monitor wlan """

    os.system('iwconfig {interface} {channel}'.format(interface=interface, channel=channel))

    with WiFiNicListener(interface):
        while not quitevent.is_set():
            quitevent.wait(1)
