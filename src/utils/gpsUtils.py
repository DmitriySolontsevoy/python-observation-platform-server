import serial


class GPSUtils:
    
    @staticmethod
    def get_coordinates():
        serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)                         
        not_read = True;

        while not_read:
            if(serialPort.in_waiting > 0):
                serialString = serialPort.readline().decode('Ascii')
                if "$GPGLL" in serialString:
                    not_read = False;
                    
                    bits = serialString.split(",")
                    latitude = round(float(bits[1]) / 100, 5)
                    longitude = round(float(bits[3]) / 100, 5)
                  
                    return latitude, longitude
