# Importing Modules
from machine import Pin
from time import sleep

# Initializing the primary variables
Exit = False
ALUPoint = False
RegisterPoint = False

# Count of program cycles
CycleCount = 0

# Final Sum of all operations
FinalSum = 0

"""
InstructionMemory = (
    "ADD 1,2",
    "SUB 1,2",
    "MUL 1,2",
    "DIV 1,2",
    "MOD 1,2",
    "FINAL SUM")
"""

# The programs instruction memory. Where the user writes their instructions
InstructionMemory = (
    "READ RegisterA",
    "WRITE RegisterA Starbucks",
    "READ RegisterA",
    "READ RegisterB",
    "WRITE RegisterB Subway",
    "READ RegisterB",
    "READ RegisterC",
    "WRITE RegisterC TacoBell",
    "READ RegisterC",
    "READ RegisterD",
    "WRITE RegisterD Chaat Bhavan",
    "READ RegisterD",
    "CycleCount")

# ArithmeticLogicUnit class containing Arithmetic and Logic Operations
class ArithmeticLogicUnit:
    
    # Class Constructor
    def __init__(self):
        pass
    
    # Addition Function, takes as many amount of numbers as the user desires
    def Addition(self, Numbers):
        Total = 0.0
        for Number in Numbers:
            Total += Number
        return (Total)

    # Subtraction Function, takes as many amount of numbers as the user desires
    def Subtraction(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary -= Number
        return (Primary)
    
    # Multiplication Function, takes as many amount of numbers as the user desires
    def Multiplication(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary = Primary * Number
        return (Primary)
  
    # Division Function, takes as many amount of numbers as the user desires
    def Division(self, Numbers):
        Primary = Numbers[0]
        Numbers.pop(0)
        for Number in Numbers:
            Primary = Primary / Number
        return (Primary)

    # Modulus Function, takes 2 numbers and returns the remainders
    def Modulus(self, NumberOne, NumberTwo):
        return (NumberOne % NumberTwo)
      
    # Yes Logic Gate
    def Yes(Bit):
        if Bit == 0:
            return 0
        if Bit == 1:
            return 1
        
    # NOT Logic Gate
    def NOT(Bit):
        if Bit == 0:
            return 1
        elif Bit == 1:
            return 0
        
    # AND Logic Gate
    def AND(BitA, BitB):
        if (BitA and BitB) == 0:
            return 0
        elif (BitA and BitB) == 1:
            return 1
        elif (BitA == 1) or (BitB == 0):
            return 0
        
    # OR Logic Gate
    def OR(BitA, BitB):
        if (BitA == 1) or (BitB == 1):
            return 1
        elif (BitA and BitB) == 0:
            return 0
        elif (BitA and BitB) == 1:
            return 1
        
    # XOR Logic Gate
    def XOR(BitA, BitB):
        if (BitA and BitB) == 1:
            return 0
        elif (BitA == 1) or (BitB == 1):
            return 1
        elif (BitA and BitB) == 0:
            return 0
        
    # NAND Logic Gate
    def NAND(BitA, BitB):
        if (BitA and BitB) == 1:
            return 0
        if (BitA and BitB) == 0:
            return 1
        elif (BitA == 1) or (BitB == 1):
            return 1
        
    # NOR Logic Gate
    def NOR(BitA, BitB):
        if (BitA == 1) or (BitB == 1):
            return 0
        elif (BitA and BitB) == 1:
            return 0
        elif (BitA == 0) and (BitB == 0):
            return 1
        
    # XNOR Logic Gate
    def XNOR(BitA, BitB):
        if (BitA == 0) and (BitB == 0):
            return 1
        elif (BitA and BitB) == 1:
            return 1
        elif (BitA == 1) or (BitB == 1):
            return 0
         
class Register:
    
    def __init__(self, InitValue):
        self.RegisterA = InitValue
        self.RegisterB = InitValue
        self.RegisterC = InitValue
        self.RegisterD = InitValue
        self.RegisterE = InitValue
        self.RegisterF = InitValue
    
    def Write(self, Register, Data):
        if Register == "RegisterA":
            self.RegisterA = Data
            return (self.RegisterA)
        
        elif Register == "RegisterB":
            self.RegisterB = Data
            return (self.RegisterB)
        
        elif Register == "RegisterC":
            self.RegisterC = Data
            return (self.RegisterC)
        
        elif Register == "RegisterD":
            self.RegisterD = Data
            return (self.RegisterD)
        
        elif Register == "RegisterE":
            self.RegisterE = Data
            return (self.RegisterE)
        
        elif Register == "RegisterF":
            self.RegisterF = Data
            return (self.RegisterF)
        
    def Read(self, Register):
        if Register == "RegisterA": return (self.RegisterA)
        elif Register == "RegisterB": return (self.RegisterB)
        elif Register == "RegisterC": return (self.RegisterC)
        elif Register == "RegisterD": return (self.RegisterD)
        elif Register == "RegisterE": return (self.RegisterE)
        elif Register == "RegisterF": return (self.RegisterF)
        else: return ("Register does not exist")
    
LEDPin25 = Pin(25, Pin.OUT)

ALU = ArithmeticLogicUnit()
RegisterControl = Register("")

ClockSpeed = float(input("DEFINE CLOCK SPEED [HERTZ]: "))
def ClockCycle():
    Speed = 1 / float(ClockSpeed)
    LEDPin25.toggle()
    sleep(Speed/2)
    LEDPin25.toggle()
    sleep(Speed/2)

# Interating through each line of the InstructionMemory
for Line in InstructionMemory:
    
    # Clock Cycle
    ClockCycle()
    CycleCount += 1
    
    # Printing the number of excecuted clock cycles
    if Line == "CycleCount":
        print(CycleCount)
        
    # ALU Interface
    if Line == "FINAL SUM":
        print(FinalSum)
    
    # If the ADD Command is present, then commence the ADD Procedure
    if Line[0:3] == "ADD":
                
        # Retrieve all the numbers after the ADD Command
        AdditionNumbers = Line[4:]

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
        LinePoint = False
        DoubleUserInputCheck = False
        UserInputCheck = True
                
        FinalSum += Return
                
    # If the SUB Command is present, then commence the SUB Procedure
    if Line[0:3] == "SUB":
                
        # Retrieve all the numbers after the SUB Command
        SubtractionNumbers = Line[4:]
                
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
        LinePoint = False
        DoubleUserInputCheck = False
        UserInputCheck = True
            
        FinalSum += Return
                
    # If the MUL Command is present, then commence the MUL Procedure
    if Line[0:3] == "MUL":
                
        # Retrieve all the numbers after the MUL Command
        MultiplicationNumbers = Line[4:]
                
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
        LinePoint = False
        DoubleUserInputCheck = False
        UserInputCheck = True
            
        FinalSum += Return
                
    # If the DIV Command is present, then commence the DIV Procedure
    if Line[0:3] == "DIV":
                
        # Retrieve all the numbers after the DIV Command
        DivisionNumbers = Line[4:]
        
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
        LinePoint = False
        DoubleUserInputCheck = False
        UserInputCheck = True
                
        FinalSum += Return
                
    # If the MOD Command is present, then commence the MOD Procedure
    if Line[0:3] == "MOD":
                
        # Retrieve all the numbers after the MOD Command
        ModulusNumbers = Line[4:]
                
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
        LinePoint = False
        DoubleUserInputCheck = False
        UserInputCheck = True
            
        FinalSum += Return

    if Line[0:4] == "READ":
        RegisterOutput = RegisterControl.Read(Line[5:])
        print(Line[5:], "-->", RegisterOutput)
            
    if Line[0:5] == "WRITE":
        RegisterOutput = RegisterControl.Write(Line[6:15], Line[16:])
