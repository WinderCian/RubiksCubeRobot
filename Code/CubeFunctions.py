import RPi.GPIO as GPIO
import time
import socket

# Pin Numbers For Motors & Drivers
motors = {
    "U" : {"step": 27, "dir": 22},  # Yellow Face
    "B" : {"step": 23, "dir": 24},  # Orange Face
    "R" : {"step": 12,  "dir": 16}, # Green Face
    "L" : {"step": 5,  "dir": 6},   # Blue Face
    "F" : {"step": 19, "dir": 26},  # Red Face
    "D" : {"step": 20, "dir": 21},  # White Face
    }
    
# / ------ GPIO Setup ------ /
GPIO.setmode(GPIO.BCM)

for motor in motors.values():
    # Declare Each Motor Control Pin an Output
    GPIO.setup(motor["step"], GPIO.OUT)
    GPIO.setup(motor["dir"], GPIO.OUT)

def receiveSolution():
    # Function creates a localhost server to receive the string from the Client GUI
	HOST = "0.0.0.0"
	PORT = 8080

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((HOST, PORT))
	server.listen(1)

	print("Waiting for Solved String")

	conn, addr = server.accept()
	inputString = conn.recv(1024).decode()
	
	return inputString.strip()


def parseMoves(inputString):
    # Function takes the raw solve string from 'sv.solve()' and transforms it into a list with one element per move
    cleanString = inputString.split("(")[0].strip()
    solveString = cleanString.split()
    
    return (solveString)


def stepMotor(face, steps, direction):
    # Function turns the motor for the corresponding face, number of steps and in the correct direction
    GPIO.output(motors[face]["dir"], direction)

    for _ in range(steps):
        GPIO.output(motors[face]["step"], 1)
        time.sleep(0.005)
        GPIO.output(motors[face]["step"], 0)
        time.sleep(0.005)
        
    time.sleep(0.1)



def executeMove(move):
    # Function translates a move from its Cube notation to Motor instructions
    face = move[0]
    modifier = move[1:]

    motor = motors[face]
    direction = 1
    steps = 50
    
    if modifier == "3":
        direction = 0
        
    elif modifier == "2":
        steps = 100

    stepMotor(face, steps, direction)



def executeSolve(moves):
    # Function takes the list of moves and passes each of them throught the 'executeMove()' function
    for move in moves:
        print(f"Executing: {move}")
        executeMove(move)
    
    print("Cube Solved!")
    return 0
        
