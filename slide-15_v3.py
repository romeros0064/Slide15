# imports from pygame library
import random, time, pygame, sys, copy, math
from pygame.locals import *

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

LEFT = "Left"
RIGHT = "Right"
UP = "Up"
DOWN = "Down"

#Define Global constants
width, height = 320, 320
numRowsCols = 5 # must be square for this game...
blockWidth=width/numRowsCols
blockHeight=height/numRowsCols

def main():
    # Initialize the game screen
    pygame.init()
    gameScreen=pygame.display.set_mode((width, height))
    #print ("hello world")
    
    #initialize the blocks
    gameGrid = makeGrid(numRowsCols,numRowsCols)
    printGrid(gameGrid)
    DrawGrid(gameScreen,gameGrid)
    
    #gameGrid[0][0].DrawBlock(gameScreen)
    pygame.display.flip()
    
    #main game loop
    endGame=False
    while (True):
        if (endGame==True):
            #any other cleanup can go here
            break
        
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button 
            if event.type==pygame.QUIT:
##                # if it is quit the game and everything
                pygame.quit()
                endGame=True
            
            elif event.type==pygame.MOUSEBUTTONUP:
                # if (event.button == 1)    # only for left click?
                # find out which block
                print( "pos= " + str(event.pos) + "; btn= " + str(event.button) )
                mousex, mousey = event.pos
                x = math.floor((mousex / width) * numRowsCols)
                y = math.floor((mousey / height) * numRowsCols)
                print( "(" + str(x) + ", " + str(y) + ")" )
                # if next to a zero, move to the zero
                TryToMoveBlock(gameGrid,x,y)
                DrawGrid(gameScreen,gameGrid)
                
                
    

            
# Creates a 2D List of 0's, nCols x nRows large, and fills with SlidingBlock type objects
def makeGrid(nCols,nRows):
    grid = []
    numbers=[]
    for x in range(0,nCols*nRows):
        numbers.append(x)
    random.shuffle(numbers)
    x=0
    print(numbers)
    
    for i in range(nRows):
        # Create an empty list for each row
        grid.append([])
        for j in range(nCols):
            # Pad each column in each row with a 0
            grid[i].append(SlidingBlock(numbers[x],i,j))
            x=x+1
                    
    return grid

# object type for the block
class SlidingBlock:
    def __init__(self,value,i,j):
        self.numValue=value  # number on block; 0 denotes empty space
        self.row=i
        self.col=j
        self.color = RED
        
        self.UpdateBlock()
        
        
    def UpdateBlock(self): 
        # +1 because the grid starts at (0,0) but the correct game position starts at 1
        if (self.numValue==0):
            self.color = BLACK
        elif ( self.numValue == numRowsCols*self.row + self.col + 1 ):  
            self.color = GREEN
        else:
            self.color = RED
        
        self.blockSurface = pygame.Surface((blockWidth, blockHeight))
        self.blockSurfacePos = self.blockSurface.get_rect().move(self.col*blockWidth,self.row*blockHeight)
        self.blockSurface.fill(self.color)
        pygame.draw.rect(self.blockSurface, WHITE, self.blockSurface.get_rect(), int(blockWidth*0.05))
        self.blockTextSurface = pygame.font.SysFont(pygame.font.get_default_font(), 28, True, False).render(str(self.numValue), False, WHITE)
        if(self.numValue != 0):
            self.blockSurface.blit(self.blockTextSurface, ((self.blockSurface.get_rect().width/2) - (self.blockTextSurface.get_rect().width/2), (self.blockSurface.get_rect().height/2) - (self.blockTextSurface.get_rect().height / 2)))
        
     
    # screen is screen to draw on
    # (i,j) is the col and row of the position of the block in the grid
    def DrawBlock(self, screen):
        screen.blit(self.blockSurface, self.blockSurfacePos)
        #don't flip here; let the calling function flip so the blocks all update together!
        #pygame.display.flip()

    

def TryToMoveBlock(grid, x, y):
    move= ""
    if ( x > 0 ):
        if ( grid[y][x-1].numValue==0 ):  # check left
            print("move left")
            move= LEFT
            
            #swap the values
            grid[y][x-1].numValue=grid[y][x].numValue
            grid[y][x].numValue=0
            grid[y][x-1].UpdateBlock()
            grid[y][x].UpdateBlock()
    if ( x < numRowsCols-1 ):
        if ( grid[y][x+1].numValue==0 ):  # check right
            print("move right")
            move= RIGHT
            
            #swap the values
            grid[y][x+1].numValue=grid[y][x].numValue
            grid[y][x].numValue=0
            grid[y][x+1].UpdateBlock()
            grid[y][x].UpdateBlock()
    if ( y > 0 ):
        if ( grid[y-1][x].numValue==0 ):  # check up
            print("move up")
            move= UP
            
            #swap the values
            grid[y-1][x].numValue=grid[y][x].numValue
            grid[y][x].numValue=0
            grid[y-1][x].UpdateBlock()
            grid[y][x].UpdateBlock()
    if ( y < numRowsCols-1 ):
        if ( grid[y+1][x].numValue==0 ):  # check down
            print("move down")
            move= DOWN
            
            #swap the values
            grid[y+1][x].numValue=grid[y][x].numValue
            grid[y][x].numValue=0
            grid[y+1][x].UpdateBlock()
            grid[y][x].UpdateBlock()
    if ( move == "" ):                     # otherwise, indicate can't move somehow?
        print("don't move")


def printGrid(grid):
    for i in range(numRowsCols):
        row = ""
        for j in range(numRowsCols):
            row += str(grid[i][j].numValue) + "  "
        print (row)

def DrawGrid(screen, grid):
    for i in range(numRowsCols):
        for j in range(numRowsCols):
            grid[i][j].DrawBlock(screen)
            #else do nothing because position 0 is the empty spot
        #print (row)
    pygame.display.flip()

if __name__ == '__main__':
    main()