import turtle
from svg_turtle import SvgTurtle

holeDiameter=2 # in mm
gridCentre=2.5 # in mm
holeR=holeDiameter/2
canvasSize=(100,100) #in mm
max=(75,30) #in mm
mmFactor = 1#300/79 # 1mm
  
# Creating a turtle object(pen) 
pen = SvgTurtle(canvasSize[0]*mmFactor,canvasSize[1]*mmFactor)

crossStitchFont = {
    # https://i0.wp.com/lordlibidan.com/wp-content/uploads/2019/04/5a-Minature-Cross-Stitch-Alphabet-Pattern-Free-Download.png?ssl=1
    "A":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(2,2),(3,2),(4,2),(2,3),(4,3),(3,4)],
    "B":[(0,0),(1,0),(2,0),(3,0),(4,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(1,3),(5,3),(0,4),(1,4),(2,4),(3,4),(4,4)],
    "C":[(1,0),(2,0),(3,0),(4,0),(0,1),(4,1),(0,2),(0,3),(4,3),(1,4),(2,4),(3,4),(4,4)],
    "D":[(0,0),(1,0),(2,0),(3,0),(4,0),(1,1),(5,1),(1,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(3,4),(4,4)],
    "E":[(0,0),(1,0),(2,0),(3,0),(4,0),(1,1),(5,1),(1,2),(2,2),(3,2),(1,3),(5,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)],
    "F":[(0,0),(1,0),(2,0),(1,1),(1,2),(2,2),(3,2),(1,3),(5,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)],
    "G":[(1,0),(2,0),(3,0),(4,0),(0,1),(4,1),(0,2),(3,2),(4,2),(0,3),(1,4),(2,4),(3,4),(4,4)],
    "H":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "I":[(0,0),(1,0),(2,0),(1,1),(1,2),(1,3),(0,4),(1,4),(2,4)],
    "J":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "K":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "L":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "M":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "N":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "O":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "P":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "Q":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "R":[(0,0),(1,0),(2,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(1,3),(5,3),(0,4),(1,4),(2,4),(3,4),(4,4)],
    "S":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "T":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "U":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "V":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "W":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "X":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "Y":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "Z":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)]

}
  
# Defining a method to draw curve 
def curve(): 
    for i in range(200): 
  
        # Defining step by step curve motion 
        pen.right(1) 
        pen.forward(1) 
  
# Defining method to draw a full heart 
def heart(): 
  
    # Set the fill color to red 
    pen.fillcolor('red') 
  
    # Start filling the color 
    pen.begin_fill() 
  
    # Draw the left line 
    pen.left(140) 
    pen.forward(113) 
  
    # Draw the left curve 
    curve() 
    pen.left(120) 
  
    # Draw the right curve 
    curve() 
  
    # Draw the right line 
    pen.forward(112) 
  
    # Ending the filling of the color 
    pen.end_fill() 
  
# Defining method to write text 
def txt(): 
  
    # Move turtle to air 
    pen.up() 
  
    # Move turtle to a given position 
    pen.setpos(-68, 95) 
  
    # Move the turtle to the ground 
    pen.down() 
  
    # Set the text color to lightgreen 
    pen.color('lightgreen') 
  
    # Write the specified text in  
    # specified font style and size 
    pen.write("Georgie is a Poo", font=( 
      "Verdana", 12, "bold")) 

text="RICH"
holeLoc =[]
stitchLoc=[]

cursor = (0,0)
offset = (-10*mmFactor,5*mmFactor)

pen.speed(0)

xCursor = 0
yCursor = 0
xMax=0
yMax=0

for j in range(len(text)):
    #pen.clear()
    if j > 0:
        test=0
    holeLoc =[]
    stitchLoc=[]
    xCursor = xMax + 2
    xMax=0
    yMax=0
    for i in range(len(crossStitchFont[text[j]])):
        #print (crossStitchFont[text][i])
        x=crossStitchFont[text[j]][i][0] + xCursor
        y=crossStitchFont[text[j]][i][1]
        holeLoc.append((x,y))
        holeLoc.append((x+1,y))
        holeLoc.append((x,y+1))
        holeLoc.append((x+1,y+1))

        #Get the width and height of the character
        if x > xMax:
            xMax = x

        if y > yMax:
            yMax = y

        #Draw crosses
        pen.color('blue')
        pen.width(3)
        pen.up()
        pen.goto((x*gridCentre+offset[0])*mmFactor,(y*gridCentre+holeR+offset[1])*mmFactor)
        pen.down()
        pen.goto(((x+1)*gridCentre+offset[0])*mmFactor,((y+1)*gridCentre+holeR+offset[1])*mmFactor)
        pen.up()
        pen.goto(((x+1)*gridCentre+offset[0])*mmFactor,(y*gridCentre+holeR+offset[1])*mmFactor)
        pen.down()
        pen.goto((x*gridCentre+offset[0])*mmFactor,((y+1)*gridCentre+holeR+offset[1])*mmFactor)

    print("XMax = " + str(xMax) + "\t yMax = " + str(yMax))
    #Draw holes
    pen.color('red')
    pen.width(1)
    for i in range(len(holeLoc)):
        pen.up()
        pen.goto((holeLoc[i][0]*gridCentre+offset[0])*mmFactor,(holeLoc[i][1]*gridCentre+offset[1])*mmFactor)
        pen.down()
        pen.circle(holeR*mmFactor)

# Draw a heart 
#heart() 
  
# Write text 
#txt() 
pen.up()
pen.goto((-canvasSize[0]/2+5)*mmFactor,(canvasSize[1]/2-5)*mmFactor)

pen.down()
pen.forward(max[0]*mmFactor)
pen.right(90)
pen.forward(max[1]*mmFactor)
pen.right(90)
pen.forward(max[0]*mmFactor)
pen.right(90)
pen.forward(max[1]*mmFactor)

# To hide turtle 
pen.ht() 

pen.save_as('example.svg')
wait=input()