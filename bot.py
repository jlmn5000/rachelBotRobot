import socket
import create

def forward():
        print ('go forward')
        robot.go(move_speed,0)

def reverse():
        print ('reverse')
        robot.go((move_speed*-1),0)

def right():
        print ('turn right')
        robot.go(0,(turn_speed*-1))

def left():
        print ('turn left')
        robot.go(0,turn_speed)

def stop():
        print ('stop')
        robot.playSong( [(60,8),(64,8),(67,8),(72,8)] )
        robot.stop()
                
move_speed = 10
turn_speed = 15                

ROOMBA_PORT = ('/dev/ttyUSB0')

robot = create.Create(ROOMBA_PORT)

robot.toSafeMode()

clisock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
clisock.connect( ('173.174.147.109', 23000) )
while 1:
        message = (clisock.recv(10))
        if message == "8":
                forward()
        if message == "2":
                reverse()
        if message == "6":
                right()
        if message == "4":
                left()
        if message == "5":
                stop()

clisock.close()
robot.close()
