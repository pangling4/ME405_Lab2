import serial
import struct
from matplotlib import pyplot as pp

#Kp = input('Please enter a proportional gain value for the step response test: ')
timeList = []
positionList = []

with serial.Serial ('COM5', 19200, timeout = 1) as s_port:
    print(s_port.name)
    #s_port.write(Kp.encode("UTF-8"))   # Write bytes, not a string
    s_port.write(b'150\r')
    s_port.readline()
    try:
        while True:
            line = s_port.readline().replace(b' ', '').replace(b'\n', '').replace(b'\r', '').split(b',')
            print(line)
            [time] = struct.unpack('f',line[0])
            [pos] = struct.unpack('f',line[1])
            print(time, pos)
            timeList.append(struct.unpack('f',line[0]))
            positionList.append(struct.unpack('f',line[1]))
    except:
        pass
         
#     while True:
#         try:
#             line = s_port.readline().split(b',')
#             timeList.append(float(line[0]))
#             positionList.append(float(line[1]))
#             if line is null:
#                 break
#         except:
#             pass
    print("done recording data")

print(timeList)
print(positionList)
fig, plt = pp.subplots()
plt.plot(timeList, positionList)
plt.set(xlabel = "Time, ms", ylabel = "Position, rad")
# display plot
pp.show()