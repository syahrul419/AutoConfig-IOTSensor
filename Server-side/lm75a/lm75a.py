import sys
import smbus
import time
address = 0x48

while True:
    try:    
        if 1 < len(sys.argv):
                address = int(sys.argv[1], 16)

        # Read I2C data and calculate temperature
        bus = smbus.SMBus(1)
        raw = bus.read_word_data(address, 0) & 0xFFFF
        raw = ((raw << 8) & 0xFF00) + (raw >> 8)
        temperature = (raw / 32.0) / 8.0
        # Print temperature
        print ('Temperature: {0:0.2f} *C'.format(temperature))
        time.sleep(1)
        pass

    except Exception as e:
        continue

