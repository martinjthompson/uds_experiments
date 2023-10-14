# CAN and UDS experiments using Raspberry Pi and CAN HAT

## Driver setup

Once only per unit, follow the instructions here:

https://www.waveshare.com/wiki/2-CH_CAN_FD_HAT



## Setup

Create a python virtual environment:

> python -m venv .venv

Activate it

> . .venv/bin/activate

Install the python modules:

> pip install python-can can-isotp udsoncan

## Configure CAN

For typical automotive powertrain ECUs, the CAN bitrate is 500k and the CAN-FD data bitrate is 2M:

> sudo ip link set can0 up type can bitrate 500000 dbitrate 2000000 restart-ms 1000 berr-reporting on fd on
> sudo ifconfig can0 txqueuelen 65536


## Monitoring

For first simple dumping of messages:

> candump can0

Once the virtual environment is installed and activated, you can see the activity on the CAN bus with can_viewer.py:

> can_viewer.py -i socketcan -c can0 -b 500000 --fd --data_bitrate 2000000

This shows all messages, including those you transmit. When yo are scanning, you might not want to see everything you send, `viewer_mjt.py` has a quick hack to only show received messages.  Also, `canmon.py` in this repo just shows each CAN ID once, which can be handy.

## Sending

From the command line you can do

> cansend can0 000#11.22.33.44

to send on id `000` with 4 data bytes.

In this repo, `firstcan.py` is a quick hack for sendign a variety of conection messages on many different IDs in order to find which one the ECU responds to.  It sends on a range of IDs with various CAN frame padding schemes (some ECUs do not respond if the padding is not what they expect).  It also sends at a lower-than-saturating rate, as some ECUs are not able to throw messages away fast enough, and will miss the one you hoped they would respond to.

Scanning the first 11-bit range takes a few minutes. Scanning the whole 29-bit range will take a week or so...

# Further pointers

once you find an ID pair on which the ECU listens/resopnds, you can build on USONCAN:

https://udsoncan.readthedocs.io/en/latest/udsoncan/examples.html







