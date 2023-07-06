# Importing Modules
from machine import Pin
from time import sleep

# Initializing the primary variables
Exit = False
RegisterPoint = False

# Count of program cycles
CycleCount = 0

# Final Sum of all operations
FinalSum = 0

# Dictionary to parse comparision commands

# The programs instruction memory. Where the user writes their instructions
InstructionMemory = (
    "ADD 1,2",
    "SUB 1,2",
    "MUL 1,2",
    "DIV 1,2",
    "MOD 1,2",
    "FINAL SUM",
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
    "CycleCount",
    "YES 1",
    "NOT 0",
    "AND 1,0",
    "OR 1,0",
    "XOR 1,0",
    "NAND 1,0",
    "NOR 1,0",
    "XNOR 1,0",
    "CollectINT BroWSG ",
    "CollectSTRING BroWSG ",
    "CollectFLOAT BroWSG ",
    "CollectBOOLEAN BroWSG ",
    "READ InputRegister",
    "CompareN=5,5",
    "CompareR=A,F")

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
    def Yes(self, Bit):
        if Bit == 0:
            return 0
        if Bit == 1:
            return 1
        
    # NOT Logic Gate
    def NOT(self, Bit):
        if Bit == 0:
            return 1
        elif Bit == 1:
            return 0
        
    # AND Logic Gate
    def AND(self, BitA, BitB):
        if (BitA and BitB) == 0:
            return 0
        elif (BitA and BitB) == 1:
            return 1
        elif (BitA == 1) or (BitB == 0):
            return 0
        
    # OR Logic Gate
    def OR(self, BitA, BitB):
        if (BitA == 1) or (BitB == 1):
            return 1
        elif (BitA and BitB) == 0:
            return 0
        elif (BitA and BitB) == 1:
            return 1
        
    # XOR Logic Gate
    def XOR(self, BitA, BitB):
        if (BitA and BitB) == 1:
            return 0
        elif (BitA == 1) or (BitB == 1):
            return 1
        elif (BitA and BitB) == 0:
            return 0
        
    # NAND Logic Gate
    def NAND(self, BitA, BitB):
        if (BitA and BitB) == 1:
            return 0
        if (BitA and BitB) == 0:
            return 1
        elif (BitA == 1) or (BitB == 1):
            return 1
        
    # NOR Logic Gate
    def NOR(self, BitA, BitB):
        if (BitA == 1) or (BitB == 1):
            return 0
        elif (BitA and BitB) == 1:
            return 0
        elif (BitA == 0) and (BitB == 0):
            return 1
        
    # XNOR Logic Gate
    def XNOR(self, BitA, BitB):
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
        self.InputRegister = InitValue
    
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
        
        elif Register == "InputRegister":
            self.InputRegister = Data
            return (self.InputRegister)
        
    def Read(self, Register):
        if Register == "RegisterA": return (self.RegisterA)
        elif Register == "RegisterB": return (self.RegisterB)
        elif Register == "RegisterC": return (self.RegisterC)
        elif Register == "RegisterD": return (self.RegisterD)
        elif Register == "RegisterE": return (self.RegisterE)
        elif Register == "RegisterF": return (self.RegisterF)
        elif Register == "InputRegister": return (self.InputRegister)
        else: return ("Register does not exist")
    
# Comparision Registers
ComparisionRegisterA = False
ComparisionRegisterB = False
ComparisionRegisterC = False

# Comparision Unit
class Comparision:
    
    def __init__(self, InitValue):
        pass
    
    def GreaterThan(self, Object1, Object2):
        Result = ((Object1) > (Object2))
        self.ComparisionRegisterA = Result
        return Result
    
    def LessThan(self, Object1, Object2):
        Result = ((Object1) < (Object2))
        self.ComparisionRegisterB = Result
        return Result
    
    def EqualTo(self, Object1, Object2):
        Result = ((Object1) == (Object2))
        self.ComparisionRegisterC = Result
        return Result
    
LEDPin25 = Pin(25, Pin.OUT)


ALU = ArithmeticLogicUnit()
RegisterControl = Register("")
ComparisionControl = Comparision("")

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
        
    # Arithmetic Unit
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
            
        FinalSum += Return
    
    # Logic Unit
    
    # YES Logic Gate
    if Line[0:3] == "YES":
        YesNumbers = Line[4:]

        RawYesNumbers = YesNumbers.split(",")
        FinalYesNumbers = []

        for YesNumber in RawYesNumbers:
            YesNumber = int(YesNumber)
            FinalYesNumbers.append(int(YesNumber))

        Return = ALU.Yes(FinalYesNumbers[0])
        print(Return)
        
    # NOT Logic Gate
    if Line[0:3] == "NOT":
        NotNumbers = Line[4:]

        RawNotNumbers = NotNumbers.split(",")
        FinalNotNumbers = []

        for NotNumber in RawNotNumbers:
            NotNumber = int(NotNumber)
            FinalNotNumbers.append(int(NotNumber))

        Return = ALU.NOT(FinalNotNumbers[0])
        print(Return)
    
    # AND Logic Gate
    if Line[0:3] == "AND":
        AndNumbers = Line[4:]

        RawAndNumbers = AndNumbers.split(",")
        FinalAndNumbers = []

        for AndNumber in RawAndNumbers:
            AndNumber = int(AndNumber)
            FinalAndNumbers.append(int(AndNumber))

        Return = ALU.AND(FinalAndNumbers[0], FinalAndNumbers[1])
        print(Return)
        
    # OR Logic Gate
    if Line[0:2] == "OR":
        OrNumbers = Line[3:]

        RawOrNumbers = OrNumbers.split(",")
        FinalOrNumbers = []

        for OrNumber in RawOrNumbers:
            OrNumber = (OrNumber)
            FinalOrNumbers.append(int(OrNumber))

        Return = ALU.OR(FinalOrNumbers[0], FinalOrNumbers[1])
        print(Return)
        
    # XOR Logic Gate
    if Line[0:3] == "XOR":
        XorNumbers = Line[4:]

        RawXorNumbers = XorNumbers.split(",")
        FinalXorNumbers = []

        for XorNumber in RawXorNumbers:
            FinalXorNumbers.append(int(XorNumber))

        Return = ALU.XOR(FinalXorNumbers[0], FinalXorNumbers[1])
        print(Return)
    
    # NAND Logic Gate
    if Line[0:4] == "NAND":
        NandNumbers = Line[5:]

        RawNandNumbers = NandNumbers.split(",")
        FinalNandNumbers = []

        for NandNumber in RawNandNumbers:
            NandNumber = int(NandNumber)
            FinalNandNumbers.append(int(NandNumber))

        Return = ALU.NAND(FinalNandNumbers[0], FinalNandNumbers[1])
        print(Return)
        
    # NOR Logic Gate
    if Line[0:3] == "NOR":
        NorNumbers = Line[4:]

        RawNorNumbers = NorNumbers.split(",")
        FinalNorNumbers = []

        for NorNumber in RawNorNumbers:
            NorNumber = int(NorNumber)
            FinalNorNumbers.append(int(NorNumber))

        Return = ALU.NOR(FinalNorNumbers[0], FinalNorNumbers[1])
        print(Return)
        
    # XNOR Logic Gate
    if Line[0:4] == "XNOR":
        XnorNumbers = Line[5:]

        RawXnorNumbers = XnorNumbers.split(",")
        FinalXnorNumbers = []

        for XnorNumber in RawXnorNumbers:
            XnorNumber = int(XnorNumber)
            FinalXnorNumbers.append(int(XnorNumber))

        Return = ALU.XNOR(FinalXnorNumbers[0], FinalXnorNumbers[1])
        print(Return)
     
    # Input Managment Unit
    if Line[0:7] == "Collect":
        if Line[7:10] == "INT":
            CollectInput = int(input(Line[11:]))
            print(CollectInput)
            
        if Line[7:13] == "STRING":
            CollectInput = input(Line[14:])
            print(CollectInput)
            
        if Line[7:12] == "FLOAT":
            CollectInput = float(input(Line[13:]))
            print(CollectInput)
            
        if Line[7:14] == "BOOLEAN":
            CollectInput = bool(input(Line[15:]))
            print(CollectInput)
            
        RegisterControl.Write("InputRegister", CollectInput)
    
    # Comparing Managment Unit
    if Line[0:7] == "Compare":
        CompInput = Line[9:]
        RawCompInput = CompInput.split(",")
        
        if RawCompInput[0] == "A":
            EndResult1 = RegisterControl.RegisterA
        if RawCompInput[0] == "B":
            EndResult1 = RegisterControl.RegisterB
        if RawCompInput[0] == "C":
            EndResult1 = RegisterControl.RegisterC
        if RawCompInput[0] == "D":
            EndResult1 = RegisterControl.RegisterD
        if RawCompInput[0] == "E":
            EndResult1 = RegisterControl.RegisterE
        if RawCompInput[0] == "F":
            EndResult1 = RegisterControl.RegisterF
        
        if RawCompInput[1] == "A":
            EndResult2 = RegisterControl.RegisterA
        if RawCompInput[1] == "B":
            EndResult2 = RegisterControl.RegisterB
        if RawCompInput[1] == "C":
            EndResult2 = RegisterControl.RegisterC
        if RawCompInput[1] == "D":
            EndResult2 = RegisterControl.RegisterD
        if RawCompInput[1] == "E":
            EndResult2 = RegisterControl.RegisterE
        if RawCompInput[1] == "F":
            EndResult2 = RegisterControl.RegisterF
        
        if Line[7] == "R":
            if Line[8] == ">":
                GreaterResult = ComparisionControl.GreaterThan(EndResult1, EndResult2)
                ComparisionRegisterA = (GreaterResult)
                print(ComparisionRegisterA)
            if Line[8] == "<":
                LessResult = ComparisionControl.LessThan(EndResult1, EndResult2)
                ComparisionRegisterB = (LessResult)
                print(ComparisionRegisterB)
            if Line[8] == "=":
                EqualResult = ComparisionControl.EqualTo(EndResult1, EndResult2)
                ComparisionRegisterC = (EqualResult)
                print(ComparisionRegisterC)
        else:
            if Line[8] == ">":
                GreaterInput = Line[9:]
                RawGreaterInput = GreaterInput.split(",")
                GreaterResult = ComparisionControl.GreaterThan(RawGreaterInput[0], RawGreaterInput[1])
                ComparisionRegisterA = (GreaterResult)
                print(ComparisionRegisterA)
            if Line[8] == "<":
                LessInput = Line[9:]
                RawLessInput = LessInput.split(",")
                LessResult = ComparisionControl.LessThan(RawLessInput[0], RawLessInput[1])
                ComparisionRegisterB = (LessResult)
                print(ComparisionRegisterB)
            if Line[8] == "=":
                EqualInput = Line[9:]
                RawEqualInput = EqualInput.split(",")
                EqualResult = ComparisionControl.EqualTo(RawEqualInput[0], RawEqualInput[1])
                ComparisionRegisterC = (EqualResult)
                print(ComparisionRegisterC)
 
    # Register Managment Unit
    if Line[0:4] == "READ":
        RegisterOutput = RegisterControl.Read(Line[5:])
        print(Line[5:], "-->", RegisterOutput)
            
    if Line[0:5] == "WRITE":
        RegisterOutput = RegisterControl.Write(Line[6:15], Line[16:])
