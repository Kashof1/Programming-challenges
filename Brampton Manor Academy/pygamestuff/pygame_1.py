# pygame template - BMACS 2020
import pygame  # accesses pygame files
import sys  # to communicate with windows

# game setup ################ only runs once
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1000, 800  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
screen.fill((0,0,255))
# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0,0,255)
brown = (130,70,40)

gameState = "running"  # controls which state the games is in
####### game loop #######runs 60 times a second!
while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab
    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
        if event.type == pygame.KEYDOWN:  # tests if a key has been pressed down
            if event.key == pygame.K_ESCAPE:  # tests if that pressed key is the escape key
                gameState = "exit"  # causes exit of game loop
    ####### your code starts here #######
    pygame.draw.line(screen,green,(0,450),(1000,450),10)
    pygame.draw.rect(screen,red,(300,250,450,196))
    pygame.draw.circle(screen,yellow,(100,100),70)
    pygame.draw.rect(screen,white,(600,364,30,80),4)
    pygame.draw.line(screen,brown,(280,260),(525,200),20)
    pygame.draw.line(screen,brown,(525,200),(770,260),20)
    ####### your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value

####### out of game loop #######
print("The game has closed")  # notifies user the game has ended
pygame.quit()  # stops the game engine
sys.exit()  # close operating system window