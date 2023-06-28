# 1. Serial communication in python.
# 2. Create gui like we have connection on com port with a connect button that generate graphs and table.
# 3. Understanding qt designer
import time
import serial

# ser = serial.serial(
#    port='Enter Port',
#    baudrate=9600,
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.SEVENBITS
# )

# input = 1
# while 1:
#    # get keyboard input
#    input = input(">> ")
#    if input == 'exit':
#       ser.close()
#       exit()

#    else:
#         ser.write(input + '\r\n')
#         out = ''

# time.sleep(1)
# while ser.inWaiting() > 0:
#    out += ser.read(1)

# if out != '':
#    print
#    ">>" + out

port = serial.serial('COM1', 9600)  # Replace 'COM1' with your actual port name
while True:
    data = port.read()
    print(data)
port.write(b'Hello, Arduino!')
port.close()
