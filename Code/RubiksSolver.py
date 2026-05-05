from CubeFunctions import *
import twophase.solver as sv

# Receive Scrambled Cube string
cubeState = receiveSolution()
print("Current Cube State: ", cubeState, "\n")

# Solve the Cube
rawString = sv.solve(cubeState, 17, 2)

# Turn the raw solve string into List of Moves
moveList = parseMoves(rawString)
print("Solution: ", moveList, "\nSolution Length:", len(moveList), " Turns \n")

# Send each move intstruction to corresponding Motor
executeSolve(moveList)

GPIO.cleanup()



