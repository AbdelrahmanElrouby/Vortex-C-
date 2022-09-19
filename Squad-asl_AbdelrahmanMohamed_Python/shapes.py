def Draw_Square(length):
    for i in range(length):
        printed =""
        for j in range(length):
            printed += "* "
        print(printed)
    print("\n")
def Draw_Pyramid(height):
    for i in range(height):
        printed =""
        j = height-i-1
        while(j>0):
            printed += " "
            j-=1
        k = (i+1)*2-1
        while(k>0) :
            printed +="*" 
            k-=1
        print(printed)
    print("\n")
def Draw_Circle(radius):
    printed =""
    rsq = radius * radius
    for i in range(-radius ,radius + 1):
        isq = i*i
        printed = ""
        for j in range(-radius ,radius + 1 ):
            jsq = j*j
            if( (isq+jsq>rsq-radius ) and (isq+jsq<rsq+radius )  or (isq+jsq<rsq ) ):
                printed +="**"
            else:
                printed +="  "
        print(printed)
    print("\n")
def Draw_Triangle(height):
    for i in range(height) :
        printed = ""
        for j in range(i+1) :
            printed += "* "
        print(printed)
    print("\n")

def Print_Shape(shape,h) :
    match shape.lower(): #switch case to draw the shapes
        case "pyramid":
            Draw_Pyramid(int(h))
        case "circle":
            r = int(h/2)
            Draw_Circle(r)
        case "triangle":
            Draw_Triangle(int(h))
        case "square":
            Draw_Square(int(h))
def func(tuple):
    return tuple[1]
n = input("Enter the number of shapes you want to draw : ")
Shapes_Names = [] 
Shapes_Heights = [] 

for i in range(int(n)) :
    Shapes_Names.append(input("Enter the name of shape number \"" + str(i+1)+ "\" :" ) )
    Shapes_Heights.append(int(input("Enter the height of shape number \"" + str(i+1)+ "\" :") ))
Shapes = list(zip(Shapes_Names,Shapes_Heights)) #adds shapes names and heights into tuples and add them to the list Shapes
Shapes.sort(reverse=True , key = func) #Sorts shapes descendingly acccording to their height
for i in Shapes :
    print("\n")
    Print_Shape(i[0],i[1])
