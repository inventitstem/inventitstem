import turtle
from svg_turtle import SvgTurtle

#########################################################
# Script to create an svg image of cross-stitch text    #
# PIXELS are organised to create shapes and text        #
# Each PIXEL consists of a square arrangement of HOLES  #
# Each HOLE has a diameter of HOLEDIAMETER and are on   #
# grid of GRIDCENTRE. All measurements are in mm which  #
# are scaled appropiatley using adapted script.         #
# Text is stored in a library. Image is fed into a      #
# matrix first and then converted to mm.
# 1) Write Text into matrix                             #
# 2) Determine size of matrix                           #
# 3) Draw surrounding shape                             #
# 4) Scale and print matrix                             #
# 5) Convert to svg                                     #
#########################################################

#File setup

# Parameter setup #
pixelDiameter = 1
holeDiameter=2 # in mm
gridCentre=2.5 # in mm
holeR=holeDiameter/2
canvasSize=(150,150) #in mm
#max=(75,30) #in mm
mmFactor = (90.1/23.839) # As measured
pixelSpace = 2
  
# Creating a turtle object(pen) 
pen = SvgTurtle(canvasSize[0]*mmFactor,canvasSize[1]*mmFactor)

# Library for text
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
    "L":[(0,0),(1,0),(2,0),(3,0),(4,0),(1,1),(5,1),(1,2),(1,3),(0,4),(1,4),(2,4)],
    "M":[(0,0),(1,0),(2,0),(5,0),(6,0),(1,1),(6,1),(1,2),(3,2),(4,2),(6,2),(1,3),(2,3),(5,3),(6,3),(0,4),(1,4),(6,4)],
    "N":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "O":[(1,0),(2,0),(3,0),(0,1),(4,1),(0,2),(4,2),(0,3),(4,3),(1,4),(2,4),(3,4)],
    "P":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "Q":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "R":[(0,0),(1,0),(2,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(1,3),(5,3),(0,4),(1,4),(2,4),(3,4),(4,4)],
    "S":[(0,0),(1,0),(2,0),(3,0),(4,1),(1,2),(2,2),(3,2),(0,3),(1,4),(1,4),(2,4),(3,4),(4,4)],
    "T":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "U":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "V":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "W":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "X":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "Y":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "Z":[(0,0),(1,0),(2,0),(4,0),(5,0),(1,1),(5,1),(1,2),(2,2),(3,2),(4,2),(5,2),(1,3),(5,3),(0,4),(1,4),(2,4),(4,4),(5,4)],
    "'":[(0,3),(0,4)]

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

# Defining method to draw a square
def square(origin,x,y,color):
    pen.color(color)
    pen.width(0.1)
    pen.up()
    pen.goto(origin[0]-x/2, origin[1]-y/2)
    pen.down()
    pen.goto(origin[0]-x/2, origin[1]+y/2)
    pen.goto(origin[0]+x/2, origin[1]+y/2)
    pen.goto(origin[0]+x/2, origin[1]-y/2)
    pen.goto(origin[0]-x/2, origin[1]-y/2)
    pen.up()

def calibrate(origin,scale,length):
    # Canvas width 100. Length 90. Line width 0.1. Length is 90.1 pixel, 23.839
    # Canvas width 150. Length 90. Line width 0.1. Length is 90.1 pixel, 23.839
    # Canvas width 150. Length 45. Line width 0.1. Length is 45.1 pixel, 11.933
    pen.color('blue')
    pen.width(0.1)
    pen.up()
    pen.goto(origin)
    pen.down()
    pen.goto(origin[0]+length*scale,origin[1])
    pen.up()
  
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
    
def xStitchWord(text,origin):
    pixelMatrix =[] # Matrix to store the pixels
    xCursor = origin[0] # cursor to increment so that letters don't overlap
    yCursor = origin[1] # cursor to increment. Should not increment as all on single line
    xPixelMax=0
    yPixelMax=0
    for j in range(len(text)):
        #pen.clear()
        xCursor = xPixelMax + pixelSpace # Update the cursor ready for the next letter
        for i in range(len(crossStitchFont[text[j]])):
            #print (crossStitchFont[text][i])
            #print(text[j] + " " + crossStitchFont[text[j]])
            x=crossStitchFont[text[j]][i][0] + xCursor
            y=crossStitchFont[text[j]][i][1] + yCursor
            pixelMatrix.append((x,y))
            if(x > xPixelMax):
                xPixelMax = x
            if(y > yPixelMax):
                yPixelMax = y
    return [pixelMatrix,xPixelMax,yPixelMax]


#defining method to write cross-stitch text pixels
def xstitch1():
    #text="RICH"
    #holeLoc =[]
    #stitchLoc=[]

    cursor = (0,0)
    #offset = (-10*mmFactor,5*mmFactor)

    #pen.speed(0)

    #xCursor = 0
    #yCursor = 0
    #xMax=0
    #yMax=0

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

def pixelToHole(pixelMatrix,origin):
    pen.color('red')
    pen.width(0.1)
    for i in range(len(pixelMatrix)):
        print(pixelMatrix[i])
        pen.up()
        pen.goto(pixelMatrix[i][0]+origin[0],pixelMatrix[i][1]+origin[1])
        pen.down()
        pen.circle(pixelDiameter/2)


# Draw a heart 
#heart() 
  
# Write text 
#txt() 
#pen.up()
#pen.goto((-canvasSize[0]/2+5)*mmFactor,(canvasSize[1]/2-5)*mmFactor)

#pen.down()
#pen.forward(max[0]*mmFactor)
#pen.right(90)
#pen.forward(max[1]*mmFactor)
#pen.right(90)
#pen.forward(max[0]*mmFactor)
#pen.right(90)
#pen.forward(max[1]*mmFactor)

# To hide turtle 
#pen.ht() 
text=["CHARLIE'S","ROOM"]
pixelWord=[]
xPixelMax=0
yPixelMax=0


for i in range(len(text)):
    pixelWord.append(xStitchWord(text[i],(0,0)))
    if pixelWord[i][1] > xPixelMax: # Get the maximum width of the text
        xPixelMax=pixelWord[i][1]
    yPixelMax=yPixelMax+pixelWord[i][2] # Get the total height of the text

# Print the holes centered around origin
# Gap from text to shape
# Gap from text to outline
pixelHeightMax = yPixelMax+(len(text)-1)*pixelSpace # max text height with spacing
yPixelCursor = pixelHeightMax/2 #
for i in range(len(text)):
    yPixelCursor = yPixelCursor-pixelWord[0][2]
    pixelToHole(pixelWord[i][0],(-pixelWord[0][1]/2,yPixelCursor))
    yPixelCursor = yPixelCursor-pixelSpace

# Draw the surrounding shape to be cut
square((0,0),(xPixelMax+2*pixelSpace),(2*4+3*pixelSpace),'blue')

# Draw the surrounding shape to be cut
square((0,0),(xPixelMax+5*pixelSpace),(2*4+5*pixelSpace),'red')

calibrate((-45,45),mmFactor,20)



pen.save_as('example.svg')
#wait=input()