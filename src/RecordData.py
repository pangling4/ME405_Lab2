import serial
from matplotlib import pyplot as pp

Kp = input('Please enter a proportional gain value for the step response test: ')
timeList = []
positionList = []

with serial.Serial ('COM5', 115200) as s_port:
    
    s_port.write(Kp.encode("UTF-8"))   # Write bytes, not a string
    s_port.write(b'\n')
    
    while True:
            
        try:
            line = s_port.readline().split(b',')
            timeList.append(float(line[0]))
            positionList.append(float(line[1]))
            
        except:
            pass

pp.plot(timeList, positionList)