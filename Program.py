from machine import Pin
from time import sleep

# Initializing the primary variables
Exit = False
UserInputCheck = True
DoubleUserInputCheck = True
ALUPoint = False

# ROM Memory #
Documentation = ()
##############

# RAM Memory #
InstructionMemory = []
ALUInstructions = []
##############

# Registers #
RegisterA, RegisterB = float
RegisterC, RegisterD = str
RegisterE, RegisterF = bool

# PROGRAM INSTRUCTIONS #
INSTRUCTIONS = [
    "ADD 1,2",
    "SUB 1,2",
    "MUL 1,2",
    "DIV 1,2",
    "MOD 1,2",
    "FINAL SUM"]
###########################

# List of Arithmetic Commands
ArithmeticCommands = ["ADD", "SUB", "MUL", "DIV", "MOD"]

# Creating the Arithmetic Logic Unit Class
class ArithmeticLogicUnit:
    
    # Class Constructor
    def __init__(self):
        pass
    
    # The addition function that performs addition on as many numbers as you want
    def Addition(self, Numbers):
        Total = 0.0
        for Number in Numbers:
            Total += Number
        return (Total)
        
    # The subtraction function that performs subraction on as many numbers as you want
    def Subtraction(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary -= Number
        return (Primary)
        
    # The multiplication function that performs multiplication on as many numbers as you want     
    def Multiplication(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary = Primary * Number
        return (Primary)
    
    # The division function that performs division on as many numbers as you want     
    def Division(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary = Primary / Number
        return (Primary)
    
    # The modulus function that performs the modulus function on two numbers 
    def Modulus(self, NumberOne, NumberTwo):
        return (NumberOne % NumberTwo)
        
# For writing and reading data from the registers
class Register:
    
    def __init__(self):
        pass
    
    def Write(Register, Data, Overwrite=True):
        if Register != None:
            if Overwrite == True:
                Register = Data
            else:
                print("Register Full")
        else:
            Register = Data
        
    def Read(Register):
        return (Register)
    
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
InstructionCount = -1
ALUInput = None
InstructionPoint = False

FinalSum = 0
FinalSumPoint = False

while Exit != True:
    ClockCycle()
    CycleCount += 1
    
    if ALUPoint == True:
        if ALUInputPoint == True:
            # ALU Command Shell
            ALUInput = input("|ALU| --> ")
        # If the EXIT Command is entered then break from the loop
        elif "EXIT" in ALUInput:
            ALUPoint = False
            UserInputCheck = True
                
        # If the ADD Command is present, then commence the ADD Procedure
        elif ALUInput[0:3] == "ADD":
                
            # Retrieve all the numbers after the ADD Command
            AdditionNumbers = ALUInput[4:]

            # Split them into a list, based on the comma
            RawAdditionNumbers = AdditionNumbers.split(",")
            FinalAdditionNumbers = []

            # Run a loop iterating through the list, and changing their data type to a float
            for AdditionNumber in RawAdditionNumbers:
                AdditionNumber = float(AdditionNumber)

                # Then appending them into the new list, FinalAdditionNumbers which will be passed as a argument to the ALU Class
                FinalAdditionNumbers.append(float(AdditionNumber))
                
            # Call the Addition Function from the ALU Class
            Return = ALU.Addition(FinalAdditionNumbers)
            print(Return)
            
            ALUPoint = False
            ALUInputPoint = False
            DoubleUserInputCheck = False
            UserInputCheck = True
                
            # Checking if the user wants a final sum
            if FinalSumPoint == True:
                FinalSum += Return
                
        # If the SUB Command is present, then commence the SUB Procedure
        elif ALUInput[0:3] == "SUB":
                
            # Retrieve all the numbers after the SUB Command
            SubtractionNumbers = ALUInput[4:]
                
            # Split them into a list, based on the comma
            RawSubtractionNumbers = SubtractionNumbers.split(",")
            FinalSubtractionNumbers = []

            # Run a loop iterating through the list, and changing their data type to a float
            for SubtractionNumber in RawSubtractionNumbers:
                SubtractionNumber = float(SubtractionNumber)

                # Then appending them into the new list, FinalSubtractionNumbers which will be passed as a argument to the ALU Class
                FinalSubtractionNumbers.append(float(SubtractionNumber))

            # Call the Subtraction Function from the ALU Class
            Return = ALU.Subtraction(FinalSubtractionNumbers)
            print(Return)
            
            ALUPoint = False
            ALUInputPoint = False
            DoubleUserInputCheck = False
            UserInputCheck = True
            
            # Checking if the user wants a final sum
            if FinalSumPoint == True:
                FinalSum += Return
                
        # If the MUL Command is present, then commence the MUL Procedure
        elif ALUInput[0:3] == "MUL":
                
            # Retrieve all the numbers after the MUL Command
            MultiplicationNumbers = ALUInput[4:]
                
            # Split them into a list, based on the comma
            RawMultiplicationNumbers = MultiplicationNumbers.split(",")
            FinalMultiplicationNumbers = []

            # Run a loop iterating through the list, and changing their data type to a float
            for MultiplicationNumber in RawMultiplicationNumbers:
                MultiplicationNumber = float(MultiplicationNumber)

                # Then appending them into the new list, FinalMultiplicationNumbers which will be passed as a argument to the ALU Class
                FinalMultiplicationNumbers.append(float(MultiplicationNumber))

            # Call the Multiplication Function from the ALU Class
            Return = ALU.Multiplication(FinalMultiplicationNumbers)
            print(Return)
            
            ALUPoint = False
            ALUInputPoint = False
            DoubleUserInputCheck = False
            UserInputCheck = True
            
            # Checking if the user wants a final sum
            if FinalSumPoint == True:
                FinalSum += Return
                
        # If the DIV Command is present, then commence the DIV Procedure
        elif ALUInput[0:3] == "DIV":
                
            # Retrieve all the numbers after the DIV Command
            DivisionNumbers = ALUInput[4:]
            
            # Split them into a list, based on the comma
            RawDivisionNumbers = DivisionNumbers.split(",")
            FinalDivisionNumbers = []

            # Run a loop iterating through the list, and changing their data type to a float
            for DivisionNumber in RawDivisionNumbers:
                DivisionNumber = float(DivisionNumber)

                # Then appending them into the new list, FinalDivisionNumbers which will be passed as a argument to the ALU Class
                FinalDivisionNumbers.append(float(DivisionNumber))

            # Call the Division Function from the ALU Class
            Return = ALU.Division(FinalDivisionNumbers)
            print(Return)
            
            ALUPoint = False
            ALUInputPoint = False
            DoubleUserInputCheck = False
            UserInputCheck = True
                
            # Checking if the user wants a final sum
            if FinalSumPoint == True:
                FinalSum += Return
                
        # If the MOD Command is present, then commence the MOD Procedure
        elif ALUInput[0:3] == "MOD":
                
            # Retrieve all the numbers after the MOD Command
            ModulusNumbers = ALUInput[4:]
                
            # Split them into a list, based on the comma
            RawModulusNumbers = ModulusNumbers.split(",")
            FinalModulusNumbers = []

            # Run a loop iterating through the list, and changing their data type to a float
            for ModulusNumber in RawModulusNumbers:
                ModulusNumber = float(ModulusNumber)

                # Then appending them into the new list, FinalModulusNumbers which will be passed as a argument to the ALU Class
                FinalModulusNumbers.append(float(ModulusNumber))

            # Call the Modulus Function from the ALU Class
            Return = ALU.Modulus(FinalModulusNumbers[0], FinalModulusNumbers[1])
            print(Return)
            
            ALUPoint = False
            ALUInputPoint = False
            DoubleUserInputCheck = False
            UserInputCheck = True
            
            # Checking if the user wants a final sum
            if FinalSumPoint == True:
                FinalSum += Return
     
    # If the UserInputCheck Variable
    elif UserInputCheck == True:
        
        # Checking for if the CPU should collect User Input:
        if DoubleUserInputCheck == True:
            UserInput = input("### ")
        
        # If the user wants to load the program from their file, then...
        if UserInput == "LOAD INSTRUCTIONS":
            # Appending the User's Instructions into the Instruction Memory
            for Instruction in INSTRUCTIONS:
                InstructionMemory.append(Instruction)
                
            # Printing a header, to signify the start of the user defined program
            print((len(InstructionMemory[0])+2) * "#")
            
            for Instruction in InstructionMemory:
                print(Instruction)
                
            # Printing a footer to signify the end of the user defined program
            print((len(InstructionMemory[0])+2) * "#")
            
        # If the user wants to excecute the user defined program
        if UserInput == "EXCECUTE INSTRUCTIONS":
            for Command in ArithmeticCommands:
                for Instruction in InstructionMemory:
                    if Command in Instruction:
                        ALUInstructions.append(Instruction)
            if InstructionMemory[-1] == "FINAL SUM":
                FinalSumPoint = True
            if ALUInstructions != None:
                ALUPoint = True
                ALUInputPoint = False
            InstructionPoint = True
        
        if InstructionPoint == True:
            InstructionCount += 1
            ALUInput = InstructionMemory[InstructionCount]
            
            if InstructionCount >= (len(InstructionMemory) - 1):
                InstructionPoint = False
                DoubleUserInputCheck = True
                ALUPoint = False
        
                if FinalSumPoint == True:
                    print("Final Sum -->", FinalSum)
                    FinalSum = 0
                    InstructionCount = -1
                    FinalSumPoint = False
            
        # If the 'EXIT' command is entered then set the Exit variable to True
        elif UserInput == "EXIT" :
            Exit = True

        # Allows the user to directly accesss the ALU itself
        elif UserInput == "|ALU|":
            ALUPoint = True
            ALUInputPoint = True
            UserInputCheck = False
        
        # Print the number of clock cycles completed
        elif UserInput == "ClockCycleCount_Show":
            print("Excecuted Clock Cycles:", CycleCount)
            
    else:
        print("Soon to be Error Handeling")
