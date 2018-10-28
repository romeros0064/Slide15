# imports from pygame library
import random, time, pygame, sys, copy
from pygame.locals import *

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#Define Global constants
width, height = 320, 320
numRowsCols = 4 # must be square for this game...

def main():
    # Initialize the game screen
    pygame.init()
    gameScreen=pygame.display.set_mode((width, height))
    #print ("hello world")
    
    #initialize the blocks
    gameGrid = makeGrid(numRowsCols,numRowsCols)
    printGrid(gameGrid)
    
    #draw one block
    blockWidth=width/numRowsCols
    blockHeight=height/numRowsCols
    pygame.draw.rect(gameScreen, RED, [0, 0, blockWidth, blockHeight])
    #block = pygame.Surface((blockWidth,blockHeight). 0, screen)
    pygame.draw.rect(gameScreen, WHITE, [0, 0, blockWidth, blockHeight], int(blockWidth*0.05))
    
    #draw text over the block
    #pygame.font.init()  # If you've already called pygame.init() in your program, you don't have to call pygame.font.init()
    blockFont = pygame.font.SysFont(pygame.font.get_default_font(), 28, True, False)
    blockTextSurface = blockFont.render(str(gameGrid[0][0].numValue), False, WHITE)
    gameScreen.blit(blockTextSurface, ((blockWidth - blockTextSurface.get_rect().width) / 2, (blockHeight - blockTextSurface.get_rect().height) / 2))
    
    gameGrid[1][0].DrawBlock(gameScreen, 1, 0)
    
    DrawGrid(gameScreen,gameGrid)
    pygame.display.flip()
    
    #main game loop
    endGame=False
    while (1):
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
            grid[i].append(SlidingBlock(numbers[x]))
            x=x+1
                    
    return grid

# object type for the block
class SlidingBlock:
    def __init__(self,value):
        self.numValue=value  # number on block; 0 denotes empty space
        
    # screen is screen to draw on
    # (i,j) is the col and row of the position of the block in the grid
    def DrawBlock(self, screen, i, j):
        #draw one block
        blockWidth=width/numRowsCols
        blockHeight=height/numRowsCols
        pygame.draw.rect(screen, RED, [j*blockWidth, i*blockHeight, blockWidth, blockHeight])
        #block = pygame.Surface((blockWidth,blockHeight). 0, screen)
        pygame.draw.rect(screen, WHITE, [j*blockWidth, i*blockHeight, blockWidth, blockHeight], int(blockWidth*0.05))
        
        #draw text over the block
        #pygame.font.init()  # If you've already called pygame.init() in your program, you don't have to call pygame.font.init()
        blockFont = pygame.font.SysFont(pygame.font.get_default_font(), 28, True, False)
        blockTextSurface = blockFont.render(str(self.numValue), False, WHITE)
        screen.blit(blockTextSurface, (j*blockWidth + ((blockWidth - blockTextSurface.get_rect().width) / 2), i*blockHeight + ((blockHeight - blockTextSurface.get_rect().height) / 2)))
        
        #don't flip here; let the calling function flip so the blocks all update together!
        #pygame.display.flip()

def printGrid(grid):
    for i in range(numRowsCols):
        row = ""
        for j in range(numRowsCols):
            row += str(grid[i][j].numValue) + "  "
        print (row)

def DrawGrid(screen, grid):
    for i in range(numRowsCols):
        for j in range(numRowsCols):
            if(grid[i][j].numValue == 0):
                grid[i][j].DrawBlock(screen,i,j)
            #else do nothing because position 0 is the empty spot
        #print (row)

if __name__ == '__main__':
    main()