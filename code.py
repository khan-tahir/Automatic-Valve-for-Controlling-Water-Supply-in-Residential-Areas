from pyfirmata import Arduino, util
import time


solenoid_pin = 3  # Change this to the actual pin you are using

# Connect to the Arduino
board = Arduino('COM3') 

# Allow some time for the connection to establish
time.sleep(2)

# Function to open the solenoid valve
def open_valve():
    board.digital[solenoid_pin].write(1)

# Function to close the solenoid valve
def close_valve():
    board.digital[solenoid_pin].write(0)

# Example 
open_valve()
time.sleep(5)  # Valve remains open for 5 seconds
close_valve()

board.exit()
