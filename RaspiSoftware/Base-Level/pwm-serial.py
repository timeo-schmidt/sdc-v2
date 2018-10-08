import serial
# b'1439:1403:0\r\n'
ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    ser.reset_input_buffer()
    # print(str(ser.readline()).split(":"))
    print(str(ser.readline())[2:-5].split(":"))
