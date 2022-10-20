from abc import ABC, abstractmethod
from curses.ascii import isdigit
import math

# Squad-asl
# By : Abdelrahman Mohamed Essam
class Polygon(ABC) :
    @abstractmethod
    def area(self) :
        pass
    @abstractmethod
    def perimeter(self) :
        pass
    @abstractmethod
    def Draw(self) :
        pass

class Triangle(Polygon) :
    def __init__(self,side1,side2,side3) :
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3  
    def perimeter(self) :
        return (self._side1 + self.side2 + self._side3)
    def area(self) :
        p = 0.5 * self.perimeter()
        a = p*(p-self._side1)(p-self.side2)(p-self._side3)
        return ( math.sqrt(a) )
    @abstractmethod
    def Draw(self) :
        pass 

class Quadrilateral(Polygon) :
    def __init__(self,side1,side2,side3,side4) :
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3  
        self.__side4 = side4 
    def perimeter(self) :
        return (self._side1 + self.side2 + self.side3 + self._side4)
    @abstractmethod
    def area(self) :
        pass
    @abstractmethod
    def Draw(self) :
        pass 
class Pentagon(Polygon) :
    def __init__(self,SideLength):
        self.__SideLength = SideLength
    def area(self) :
        return (0.25 * self.__SideLength * math.sqrt(5*(5+(2*math.sqrt(5)))) )
    def perimeter(self) :
        return(5*self.__SideLength)
    def Draw(self) :
        a = math.ceil(abs(0.5877*self.__SideLength))
        height = a
        for i in range(height):
            printed =""
            j = height-i-1
            while(j>0):
                printed += "  "
                j-=1
            k = (i+1)*2-1
            while(k>0) :
                printed +=2*"*" 
                k-=1
            print(printed)
        height =(a*2) - 1
        printed =" "
        for i in range(height-1,a,-1):
            j = height-i-1
            while(j>0):
                printed += " "
                j-=1
            k = (i*2)
            while(k>0) :
                printed +="*" 
                k-=1
            print(printed)
            printed =" "
        print("\n")
class Hexagon(Polygon) :
    def __init__(self,SideLength):
        self.__SideLength = SideLength
    def area(self) :
        return (0.25 * self.__SideLength * math.sqrt(5*(5+(2*math.sqrt(6)))) )
    def perimeter(self) :
        return(6*self.__SideLength)
    def Draw(self) :
        height = int(self.__SideLength / 2)
        for i in range(height,height*2,1):
            printed =""
            j = (2*height) - i - 1
            while(j>0):
                printed += " "
                j-=1
            k = ( (i+1)*2-2 ) 
            while(k>0) :
                printed +="*" 
                k-=1
            print(printed)
        printed = ""
        for i in range( (height*2 - 2 ),height-1,-1):
            printed =""
            j = height*2 - i - 1
            while(j>0):
                printed += " "
                j-=1
            k = ( (i+1)*2-2 ) 
            while(k>0) :
                printed +="*" 
                k-=1
            print(printed)
class Octagon(Polygon) :
    def __init__(self,SideLength):
        self.__SideLength = SideLength
    def area(self) :
        return (0.25 * self.__SideLength * math.sqrt(5*(5+(2*math.sqrt(8)))) )
    def perimeter(self) :
        return(8*self.__SideLength)
    def Draw(self) :
        height = int(self.__SideLength/2)
        a = round(2.414*height)
        for i in range(height,a,1):
            printed =""
            j = a-i-1
            while(j>0):
                printed += " "
                j-=1
            k = (i+1)*2-1
            while(k>0) :
                printed +="*" 
                k-=1
            print(printed)
        for i in range(height-1):
            print(printed)
        for i in range(a-1,height-1,-1):
            printed =""
            j = a-i-1
            while(j>0):
                printed += " "
                j-=1
            k = (i+1)*2-1
            while(k>0) :
                printed +="*" 
                k-=1
            print(printed)
        print("\n")
class Square(Quadrilateral) :
    def __init__(self,SideLength):
        self.__SideLength = SideLength
    def area(self) :
        return (self.__SideLength * self.__SideLength)
    def perimeter(self):
        return(4*self.__SideLength)
    def Draw(self) :
        for i in range(self.__SideLength):
            printed =""
            for j in range(self.__SideLength):
                printed += "* "
            print(printed)
        print("\n")
        
class Rectangle(Quadrilateral) :
    def __init__(self,Length,Width):
        self.__Length = Length
        self.__Width = Width
    def area(self) :
        return (self.__Length * self.__Width)
    def perimeter(self):
        return(2*( self.__Length + self.__Width))
    def Draw(self) :
        for i in range(self.__Width):
            printed =""
            for j in range(self.__Length):
                printed += "* "
            print(printed)
        print("\n")

# By : Daniel Adel
class isoscelesTriangle(Triangle):
    def __init__(self,height):
        self.__Height = height
    def area(self) :
        return (0.5*self.__Height * ((2*self.__Height)-1))
    def perimeter(self):
        return(((2*self.__Height)-1)+(2*self.__Height))
    def Draw(self) :
        k = 0
        for i in range(1, self.__Height+1):
            for space in range(1, (self.__Height-i)+1):
                print(end="  ")
        
            while k!=(2*i-1):
                print("* ", end="")
                k += 1       
            k = 0
            print()   
class equilateralTriangle(Triangle):
    def __init__(self,SideLength):
        self.__SideLength = SideLength
    def area(self) :
        return (float((math.sqrt(3)/4)*(self.__SideLength)*(self.__SideLength)) )
    def perimeter(self):
        return(3 * self.__SideLength)
    def Draw(self) :
        k = self.__SideLength - 1
        for i in range(0, self.__SideLength):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i+1):
                print("* ", end="")
            print("\n")    

def checkLength(length):
    while not length.isdigit:
            print("invalid input!")
            length = input("Please enter the shape Length: ")

while True:
    print("Hello!, please input the shapes from the following list: ")
    print("      s -> square \n      r -> Rectangle \n      e -> Equilateral triangle \n      i -> Isosceles triangle \n      p -> Pentagon\n      h -> Hexagon\n      o -> Octagon \n ")
    name = input("please enter the shape name: ")
    while name not in "sreipho":
        print("invalid input!")
        name = input("please enter the shape name: ")
    print("What would you like to do?\n      p -> know the perimeter \n      a -> know the area \n      d -> draw the shape \n")
    operation = input("please enter the operation you would like: ")
    while operation not in "pad":
        print("invalid input")
        operation = input("please enter the operation you would like: ")
    
    if name == "s":
        height = input("Please enter the shape Length: ")
        checkLength(height)
        square = Square(int(height))
        if operation == "p":
            print(square.perimeter())
        elif operation == "a":
            print(square.area())
        elif operation == "d":
            square.Draw()        
    if name == "r":
        length = input("Please enter the shape Length: ")
        while not length.isdigit:
            print("invalid input!")
            length = input("Please enter the shape Length: ")
        width = input("Please enter the shape Width: ")
        while not width.isdigit:
            print("invalid input!")
            width = input("Please enter the shape Width: ")    
        rect = Rectangle(int(length),int(width))
        if operation == "p":
            print(rect.perimeter())
        elif operation == "a":
            print(rect.area())
        elif operation == "d":
            rect.Draw()        
    if name == "e":
        length = input("Please enter the shape Length: ")
        checkLength(length)
        equ = equilateralTriangle(int(length))
        if operation == "p":
            print(equ.perimeter())
        elif operation == "a":
            print(equ.area())
        else:
            equ.Draw()      
    if name == "i":
        length = input("Please enter the shape Length: ")
        checkLength(length) 
        iso = isoscelesTriangle(int(length))
        if operation == "p":
            print(iso.perimeter())
        elif operation == "a":
            print(iso.area())
        else:
            iso.Draw()   
    if name == "p":
        length = input("Please enter the shape Length: ")
        checkLength(length)
        pent = Pentagon(int(length))
        if operation == "p":
            print(pent.perimeter())
        elif operation == "a":
            print(pent.area())
        else:
            pent.Draw() 
    if name == "h":
        length = input("Please enter the shape Length: ")
        checkLength(length)  
        hex = Hexagon(int(length))
        if operation == "p":
            print(hex.perimeter())
        elif operation == "a":
            print(hex.area())
        else:
            hex.Draw()    
    if name == "o":
        length = input("Please enter the shape Length: ")
        checkLength(length) 
        oct = Octagon(int(length))
        if operation == "p":
            print(oct.perimeter())
        elif operation == "a":
            print(oct.area())
        else:
            oct.Draw()              
    Continue = input("do you want to continue? press n to exit and press any other key to continue :  ")                  
    if Continue == "n":
        exit()

