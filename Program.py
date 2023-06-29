from machine import Pin
from time import sleep

# Initializing the primary variables
Reset = False


# Defining Pin 25 (Linked to the Internal LED) on the Raspberry Pi Pico for us to send a signal out
LEDPin25 = Pin(25, Pin.OUT)

# Defining the Clock Function which determines the speed of the CPU
def ClockCycle(Hertz):
    # 1 Hertz = 1 Clock Cycle in 1 Second
    # Therfore a clock speed of 5 Hertz means 5 Clock Cycles completed in 1 Second
    
    
    # The Speed variable is the number we will enter in the time.sleep function
    Speed = 1 / float(Hertz)
    
    sleep(Speed)
    
    # Toggling the LED Pin 25 to turn on every cycle
    LEDPin25.toggle()
        
        
# The CPU Running in a loop until the reset command has been entered

Count = 0

while Reset != True:
    # User defined clock cycle speed
    ClockCycle(1)
    
    print(Count)
    Count += 1
