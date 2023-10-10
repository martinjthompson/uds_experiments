import time
import can
import udsoncan
import logging
import os

log = logging.getLogger()
log.setLevel(logging.INFO)
# logging.
#ids = range(0x7ff, 0x700, -1)
#ids = range(0x1819000, 0x800, -1)
ids = range(0x18fffff, 0x1819000, -1)

data_options = [[0x02, 0x3e, 0x00],]
data_options.append([0x02, 0x3e,0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
data_options.append([0x02, 0x3e,0x00, 0x55, 0x55, 0x55, 0x55, 0x55])
if __name__ == "__main__":
    logging.info("Start")
    os.system('sudo ip link set can0 up type can bitrate 500000 dbitrate 2000000 restart-ms 1000 berr-reporting on fd on')
#    os.system('sudo ip link set can1 up type can bitrate 500000 dbitrate 2000000 restart-ms 1000 berr-reporting on fd on')
    logging.info("Setup CAN")
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
#    can1 = can.interface.Bus(channel = 'can1', bustype = 'socketcan')
    msg = can.Message(is_extended_id=False, arbitration_id=0x123, data=[0x02, 0x3e, 0x00])
    
    for arb in ids:
        msg.arbitration_id = arb
        ext_options = [True]
        if arb < 0x800:
            ext_options.append(False)
        for ext in ext_options:
            msg.is_extended_id=ext
            for data in data_options:
                msg.data = bytes(data)
                msg.dlc = len(msg.data)
                logging.info("Send %s", msg)
                can0.send(msg)
                time.sleep(0.03)
#    logging.info("recv...")
#    print (can1.recv())
                      
    


