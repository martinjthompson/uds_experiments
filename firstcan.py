import time
import can
import udsoncan
import logging
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)
# logging.
if __name__ == "__main__":
    logging.info("Start")
    os.system('sudo ip link set can0 up type can bitrate 500000 dbitrate 2000000 restart-ms 1000 berr-reporting on fd on')
#    os.system('sudo ip link set can1 up type can bitrate 500000 dbitrate 2000000 restart-ms 1000 berr-reporting on fd on')
    logging.info("Setup CAN")
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
#    can1 = can.interface.Bus(channel = 'can1', bustype = 'socketcan')
    msg = can.Message(is_extended_id=False, arbitration_id=0x123, data=[0x02, 0x3e, 0x00])
    for arb in range (0x7ff,0x700,-1):
        msg.arbitration_id = arb
        logging.info("Send %s", msg)
        can0.send(msg)
        time.sleep(0.01)
#    logging.info("recv...")
#    print (can1.recv())
                      
    


