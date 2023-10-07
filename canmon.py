import can
import udsoncan
import logging
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)

        
if __name__ == "__main__":
    logging.info("Setup CAN")
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    reader = can.BufferedReader()
    notifier = can.Notifier(can0, [reader])
    seen={}
    while 1:
        msg = reader.get_message()
        if msg.arbitration_id not in seen:
            print (msg)
            seen[msg.arbitration_id] = 1
            
    


