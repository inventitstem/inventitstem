import turtle
import math
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
pixelDiameterMm = 3
holeDiameterMm=1.75 # in mm Could be 1.5mm but with korf of laser tight on the other side
pixelSpaceMm = 2

mmFactor = (90.1/23.839) # As measured
 # 197.87365241830616 pixel = 53.7mm
pixelSpace = pixelSpaceMm*mmFactor
pixelDiameter= pixelDiameterMm*mmFactor
holeDiameter=holeDiameterMm*mmFactor

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
def curve(origin,radius,angleStart,angleTotal,steps):
    pen.up()
    angleStep=(angleTotal)/steps
    angle=angleStart
    pen.goto(origin[0]+math.sin(angle)*radius,origin[1]+math.cos(angle)*radius)
    pen.down() 
    for i in range(steps): 
        angle=angle+angleStep
        pen.goto(origin[0]+math.sin(angle)*radius,origin[1]+math.cos(angle)*radius)
    #pen.up()

def curveLine(start,end,radius,steps):
    #Get length of line
    opposite = (end[1]-start[1])
    adjacent = (end[0]-start[0])
    length = (adjacent^2 + opposite^2)^-1
    angle = math.asin(opposite/length)
    stepX = adjacent/steps
    stepY = opposite/steps

    # TBD remaining
    # pen.up()
    #pen.goto(start)
    #pen.down()
    #for i in range(steps):

    #
  
# Defining method to draw a full heart 
def heart(): 
  
    # Set the fill color to red 
    pen.fillcolor('red') 
  
    # Start filling the color 
    #pen.begin_fill() 
  
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
    #pen.end_fill() 

# Defining method to draw a square
def square(origin,x,y,color,radius):
    pen.color(color)
    pen.up()
    locationX=(-origin[0]-x/2)
    locationY=(-origin[1]-y/2)
    #print(str(x-radius-radius))
    pen.goto(locationX,locationY+radius) # Bottom left
    pen.down()
     # Top Left
    locationY=locationY+y
    pen.goto(locationX,locationY-radius)
    curve((locationX+radius,locationY-radius),radius,1.5*math.pi,0.5*math.pi,10)
     # Top Right
    locationX=locationX+x
    pen.goto(locationX-radius,locationY)
    curve((locationX-radius,locationY-radius),radius,0*math.pi,0.5*math.pi,10)
     # Bottom Right
    locationY=locationY-y
    pen.goto(locationX,locationY+radius)
    curve((locationX-radius,locationY+radius),radius,0.5*math.pi,0.5*math.pi,10)
     # Bottom Left
    locationX=locationX-x
    pen.goto(locationX+radius,locationY)
    curve((locationX+radius,locationY+radius),radius,1*math.pi,0.5*math.pi,10)
    #Add Curved Edges
    #curve((0,0),1,0*math.pi,2*math.pi,10)
    pen.up()

def circleCentre(origin,r,color):
    pen.color(color)
    pen.up()
    pen.goto(origin[0],origin[1]-r)
    pen.down()
    pen.circle(r)

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
            x=crossStitchFont[text[j]][i][0]*pixelDiameter + xCursor # Cursor position in pixel
            y=crossStitchFont[text[j]][i][1]*pixelDiameter + yCursor # Cursor position in pixel
            pixelMatrix.append((x,y))
            if(x > xPixelMax):
                xPixelMax = x
            if(y > yPixelMax):
                yPixelMax = y
    return [pixelMatrix,xPixelMax,yPixelMax]

def pixelToHole(pixelMatrix,origin):
    #Each pixel has a hole in each corner Co-ordinates for each circle are from centre bottom
    #print(str(len(pixelMatrix)*4))
    #Draw pixels as circles
    #pen.color('green')
    #for i in range(len(pixelMatrix)):
    #    #print(pixelMatrix[i])
    #    pen.up()
    #    pen.goto(pixelMatrix[i][0]+origin[0],pixelMatrix[i][1]+origin[1]-pixelDiameter/2) # Each Circle is referenced from bottom mid.
    #    pen.down()
    #    pen.circle(pixelDiameter/2)

    #Draw pixels as the cross-stitch
    pen.color('blue')
    pen.width(1)
    holeMatrix=[]
    f=1000000000000 # factor to remove float inaccuracies. Set as high as possible
    for i in range(len(pixelMatrix)):
        #print(pixelMatrix[i])
        pen.up()
        # Goto top right of pixel
        holeLocation = (math.ceil((pixelMatrix[i][0]+origin[0]-pixelDiameter/2)*f)/f,math.ceil((pixelMatrix[i][1]+origin[1]+pixelDiameter/2)*f)/f)
        holeMatrix.append(holeLocation) if holeLocation not in holeMatrix else holeMatrix
        pen.goto(holeLocation)
        pen.down()
        # Bottom Left Pixel
        holeLocation = (math.ceil((pixelMatrix[i][0]+origin[0]+pixelDiameter/2)*f)/f,math.ceil((pixelMatrix[i][1]+origin[1]-pixelDiameter/2)*f)/f)
        holeMatrix.append(holeLocation) if holeLocation not in holeMatrix else holeMatrix
        pen.goto(holeLocation)
        pen.up()
        #Top Left of pixel
        holeLocation = (math.ceil((pixelMatrix[i][0]+origin[0]-pixelDiameter/2)*f)/f,math.ceil((pixelMatrix[i][1]+origin[1]-pixelDiameter/2)*f)/f)
        holeMatrix.append(holeLocation) if holeLocation not in holeMatrix else holeMatrix
        pen.goto(holeLocation)
        pen.down()
        #Bottom right
        holeLocation = (math.ceil((pixelMatrix[i][0]+origin[0]+pixelDiameter/2)*f)/f,math.ceil((pixelMatrix[i][1]+origin[1]+pixelDiameter/2)*f)/f)
        holeMatrix.append(holeLocation) if holeLocation not in holeMatrix else holeMatrix
        pen.goto(holeLocation)
        pen.up()

    print(str(len(holeMatrix)))
    #Draw the holes for the cross-stitch
    pen.color('red')
    pen.width(width)
    for i in range(len(holeMatrix)):
        #print(holeMatrix[i])
        pen.up()
        pen.goto(holeMatrix[i][0],holeMatrix[i][1]-holeDiameter/2)
        pen.down()
        pen.circle(holeDiameter/2)

# To hide turtle 
#pen.ht() 
text=["G"]
pixelWord=[]
xPixelMax=0
yPixelMax=0

#Generate pixel matrix
for i in range(len(text)):
    print("Generating: " + text[i])
    pixelWord.append(xStitchWord(text[i],(0,0)))
    if pixelWord[i][1] > xPixelMax: # Get the maximum width of the text
        xPixelMax=pixelWord[i][1]
    yPixelMax=yPixelMax+pixelWord[i][2] # Get the total height of the text

#Get Maximum size
pixelHeightMax = (yPixelMax+(len(text)-1)*pixelSpace)#*pixelDiameter # max text height is number of lines -1 as space between each space
#borderDimensions = ((xPixelMax+0*pixelSpace),(2*4+3*pixelSpace))# Border shape (a rectangle for now with pixel space boundary)
borderDimensions = ((xPixelMax+2*pixelSpace),(2*4*pixelDiameter+3*pixelSpace))# Border shape (a rectangle for now with pixel space boundary)
outlineDimensions = ((xPixelMax+5*pixelSpace),(2*4*pixelDiameter+5*pixelSpace)) # Outline shape (a rectangle for now with Pixel Space boundary)

#########
# Print #
#########

# Creating a turtle object(pen)
x=100
y=18
width=0.1 # Its assumed a width of 1mm
offset = ((1-1)/2,(1-1)/2)
margin = 10

pen = SvgTurtle(outlineDimensions[0]+margin,outlineDimensions[1]+margin)
pen.width(width)

yPixelCursor = pixelHeightMax/2 #
for i in range(len(text)):
    yPixelCursor = yPixelCursor-pixelWord[0][2]
    pixelToHole(pixelWord[i][0],(-pixelWord[i][1]/2-offset[0]-pixelSpace/2,yPixelCursor))
    yPixelCursor = yPixelCursor-pixelSpace

# Draw the surrounding shape to be cut
square(offset,(borderDimensions[0]),(borderDimensions[1]),'blue',5)

# Draw the surrounding shape to be cut
square(offset,outlineDimensions[0],outlineDimensions[1],'red',5)

# Draw heart around the text
#curve((0,0),10,1.5*math.pi,1*math.pi,10)

#Calibration
#calibrate((-45,45),mmFactor,20)
#circleCentre(inkscapeOriginOffset,1,"blue")
#square(pen,(0,0),x,y,'red')

pen.save_as('_'.join(text) + '.svg')
#wait=input()