from time import sleep
import serial


def send(message):
    ser.write(bytes(message, 'utf-8'))
    sleep(0.1)
    print(ser.readline())


ser = serial.Serial('/dev/ttyUSB0', 115200)  # Establish the connection on a specific port
sleep(3)  # Wait for arduino to boot
print('Start')
send('G')
send('G')
send('A')




