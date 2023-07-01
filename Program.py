from machine import Pin
from time import sleep

# Initializing the primary variables
Exit = False
UserInputCheck = True
ALUPoint = False

# ROM Memory #
Documentation = ()
##############

# RAM Memory #
ProgramMemory = []
##############

# Creating the Arithmetic Logic Unit Class
class ArithmeticLogicUnit:
    def __init__(self):
        pass
    
    # The addition function that performs addition on as many numbers as you want
    def Addition(self, Numbers):
        Total = 0.0
        for Number in Numbers:
            Total += Number
        print(Total)
        
    # The subtraction function that performs subraction on as many numbers as you want
    def Subtraction(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary -= Number
        print(Primary)

# Defining Pin 25 (Linked to the Internal LED) on the Raspberry Pi Pico for us to send a signal out
LEDPin25 = Pin(25, Pin.OUT)

# Count of times the clock cycle has occured
CycleCount = 0

ALU = ArithmeticLogicUnit()

# User defines the computers clock speed
ClockSpeed = float(input("DEFINE CLOCK SPEED [HERTZ]: "))

# Defining the Clock Function which determines the speed of the CPU
def ClockCycle():
    # 1 Hertz = 1 Clock Cycle in 1 Second
    # Therfore a clock speed of 5 Hertz means 5 Clock Cycles completed in 1 Second
    
    
    # The Speed variable is the number we will enter in the sleep function
    Speed = 1 / float(ClockSpeed)
    
    LEDPin25.toggle()
    
    sleep(Speed/2)
    
    LEDPin25.toggle()

    sleep(Speed/2)
    
# Defining Check Minor Variables
ALUInputPoint = False
ALUExitPoint = False

while Exit != True:
    ClockCycle()
    CycleCount += 1
    
    if ALUPoint == True:
        if ALUInputPoint == True:
            # ALU Command Shell
            ALUInput = input("|ALU| --> ")
            
            # If the EXIT Command is entered then break from the loop
            if "EXIT" in ALUInput:
                ALUPoint = False
                UserInputCheck = True
                
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
            # If the ADD Command is present, then commence the ADD Procedure
            elif ALUInput[0:3] == "ADD":
                
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
                # Retrieve all the numbers after the ADD Command
                AdditionNumbers = ALUInput[4:]
                    
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
                # Split them into a list, based on the comma
                RawAdditionNumbers = AdditionNumbers.split(",")
                FinalAdditionNumbers = []
                
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                    
                # Run a loop iterating through the list, and changing their data type to a float
                for AdditionNumber in RawAdditionNumbers:
                    AdditionNumber = float(AdditionNumber)

                    # Then appending them into the new list, FinalAdditionNumbers which will be passed as a argument to the ALU Class
                    FinalAdditionNumbers.append(float(AdditionNumber))
                        
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
                # Call the Addition Function from the ALU Class
                ALU.Addition(FinalAdditionNumbers)
                ALUInputPoint = True
                
            # If the ADD Command is present, then commence the ADD Procedure
            elif ALUInput[0:3] == "SUB":
                
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
                # Retrieve all the numbers after the ADD Command
                SubtractionNumbers = ALUInput[4:]
                    
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
                # Split them into a list, based on the comma
                RawSubtractionNumbers = SubtractionNumbers.split(",")
                FinalSubtractionNumbers = []
                
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                    
                # Run a loop iterating through the list, and changing their data type to a float
                for SubtractionNumber in RawSubtractionNumbers:
                    SubtractionNumber = float(SubtractionNumber)

                    # Then appending them into the new list, FinalAdditionNumbers which will be passed as a argument to the ALU Class
                    FinalSubtractionNumbers.append(float(SubtractionNumber))
                        
                # Clock Cycle Pulse
                ClockCycle()
                CycleCount += 1
                
                # Call the Addition Function from the ALU Class
                ALU.Subtraction(FinalSubtractionNumbers)
                ALUInputPoint = True
        
                
    # If the UserInputCheck Variable
    elif UserInputCheck == True:
        UserInput = input("### ")
        
        # Clock Cycle Pulse
        ClockCycle()
        CycleCount += 1
        
        # If the 'EXIT' command is entered then set the Exit variable to True
        if UserInput == "EXIT" :
            Exit = True

        elif UserInput == "|ALU|":
            ALUPoint = True
            ALUInputPoint = True
            UserInputCheck = False
        
        else:
            print(UserInput)
