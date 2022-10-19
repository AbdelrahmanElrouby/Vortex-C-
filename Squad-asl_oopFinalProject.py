from abc import ABC, abstractmethod
import math

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
        return (self.__side1 + self.__side2 + self.__side3)
    def area(self) :
        p = 0.5 * self.perimeter()
        a = p*(p-self.__side1)*(p-self.__side2)*(p-self.__side3)
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
        return (self.__side1 + self.__side2 + self.__side3 + self.__side4)
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





