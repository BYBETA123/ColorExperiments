import pygame
display_score_y=0
# Define some variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE=(0,0,255)
LIGHT_BLUE=(0,226,226)
PURPLE=(128,0,90)
square_x=50
square_y=50
player_rect=pygame.Rect(square_x,square_y,50,50)
def player_icon(screen, x, y):
    pygame.draw.rect(screen,LIGHT_BLUE, [square_x,square_y,50,50])
# def player_icon_hitbox(screen,x,y):
#     # left  
#     pygame.draw.line(screen, GREEN, [square_x, square_y], [square_x, square_y+50], 1)
#     # right
#     pygame.draw.line(screen, GREEN, [square_x+50, square_y], [square_x+50, square_y+50], 1)
#     # top
#     pygame.draw.line(screen, GREEN, [square_x, square_y], [square_x+50, square_y], 1)
#     # bottom
#     pygame.draw.line(screen, GREEN, [square_x+50, square_y+50], [square_x, square_y+50], 1)
enemy_square_x=1000
enemy_square_y=350
enemy_rect=pygame.Rect(enemy_square_x,enemy_square_y,50,50)
def enemy_icon(screen,x,y):
    pygame.draw.rect(screen,GREEN, [enemy_square_x,enemy_square_y,50,50])
    
# def enemy_icon_hitbox(screen,x,y):
#     # left
#     pygame.draw.line(screen,GREEN,[enemy_square_x,enemy_square_y],[enemy_square_x,enemy_square_y+25],1)
#     # right
#     pygame.draw.line(screen,GREEN,[enemy_square_x+25,enemy_square_y],[enemy_square_x+25,enemy_square_y+25],1)
#     # top
#     pygame.draw.line(screen,GREEN,[enemy_square_x,enemy_square_y],[enemy_square_x+25,enemy_square_y],1)
#     # bottom
#     pygame.draw.line(screen,GREEN,[enemy_square_x+25,enemy_square_y+25],[enemy_square_x,enemy_square_y+25],1)
# Setup
pygame.init()
# length_of_screen=1366
# height_of_screen=768
# Set the width and height of the screen [width,height]
# size = [length_of_screen, height_of_screen]
# screen = pygame.display.set_mode(size)
screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
collide = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Hide the mouse cursor
pygame.mouse.set_visible(0)
# Speed in pixels per frame
square_change_x=0
square_change_y=0
enemy_square_change_y=0
enemy_square_change_x=0
# Current position
x_coord=0
y_coord=0
score_x=0
score_y=0
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=True
                # User pressed down on a key
    if enemy_square_y>square_y:
        square_y=square_y+10
    if enemy_square_y<square_y:
        square_y=square_y-10
    if enemy_square_x>square_x:
        square_x=square_x+10
    if enemy_square_x<square_x:
        square_x=square_x-10
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        # if event.key == pygame.K_LEFT:
        #     square_change_x=-10
        # elif event.key == pygame.K_RIGHT:
        #     square_change_x=10
        # elif event.key == pygame.K_UP:
        #     square_change_y=-10
        # elif event.key == pygame.K_DOWN:
        #     square_change_y=10
        if event.key == pygame.K_a:
            enemy_square_change_x=-10
        elif event.key == pygame.K_d:
            enemy_square_change_x=10
        elif event.key == pygame.K_w:
            enemy_square_change_y=-10
        elif event.key == pygame.K_s:
            enemy_square_change_y=10
    # User let up on a key
    elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
        if event.key == pygame.K_a or event.key == pygame.K_d:
            enemy_square_change_x = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            enemy_square_change_y = 0
        # elif event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
        #     square_change_x=0
        # elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
        #     square_change_y=0

    square_x=square_x+square_change_x
    if square_x>=1200:
        square_x=1200
    if square_x<=50:
        square_x=50
    square_y=square_change_y+square_y
    if square_y>=500:
        square_y=500
    if square_y<=50:
        square_y=50
    enemy_square_y=enemy_square_y+enemy_square_change_y
    if enemy_square_y<=50:
        enemy_square_y=50
    if enemy_square_y>=500:
        enemy_square_y=500
    enemy_square_x=enemy_square_x+enemy_square_change_x
    if enemy_square_x>=1200:
        enemy_square_x=1200
    if enemy_square_x<=50:
        enemy_square_x=50
    # --- Game Logic
    # Move the object according to the speed vector.
    # --- Drawing Code
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    font = pygame.font.SysFont('Calibri', 200, True, False)
    text = font.render(str(score_x),True,LIGHT_BLUE)
    screen.blit(text,[500,570])
    font = pygame.font.SysFont('Calibri', 200, True, False)
    text = font.render("-",True,PURPLE)
    screen.blit(text,[620,555])
    font = pygame.font.SysFont('Calibri', 200, True, False)
    text = font.render(str(display_score_y),True,GREEN)
    screen.blit(text,[700,570])
    for l in range(50,1300,50):
        pygame.draw.line(screen,WHITE,[l,0],[l,550],1)
    # 
    for k in range(50,600,50):
        pygame.draw.line(screen, WHITE, [0,k], [1300,k],1)
    pygame.draw.line(screen,BLACK,[0,0],[1300,0],99)
    pygame.draw.line(screen,BLACK,[0,0],[0,700],99)
    pygame.draw.line(screen,BLACK,[1300,0],[1300,700],99)
    # pygame.draw.line(screen,GREEN,[square_x-1400,square_y],[square_x+1400,square_y])
    # pygame.draw.line(screen,GREEN,[square_x-1400,square_y+50],[square_x+1400,square_y+50])
    # pygame.draw.line(screen,GREEN,[square_x,square_y-700],[square_x,square_y+700])
    # pygame.draw.line(screen,GREEN,[square_x+50,square_y-700],[square_x+50,square_y+700])
    # pygame.draw.line(screen,GREEN,[enemy_square_x-1400,enemy_square_y],[enemy_square_x+1400,enemy_square_y])
    # pygame.draw.line(screen,GREEN,[enemy_square_x-1400,enemy_square_y+50],[enemy_square_x+1400,enemy_square_y+50])
    # pygame.draw.line(screen,GREEN,[enemy_square_x,enemy_square_y-700],[enemy_square_x,enemy_square_y+700])
    # pygame.draw.line(screen,GREEN,[enemy_square_x+50,enemy_square_y-700],[enemy_square_x+50,enemy_square_y+700])
    player_icon(screen, x_coord, y_coord)
    enemy_icon(screen, x_coord, y_coord)
    if enemy_square_x>=square_x and enemy_square_x<=square_x+50:
        if enemy_square_y>=square_y and enemy_square_y<=square_y+50:
            score_x+=1
            square_x=50
            square_y=50
            enemy_square_x=1000
            enemy_square_y=350
    score_y+=1
    if score_y<100:
        display_score_y=0
    elif score_y<200:
        display_score_y=1
    elif score_y<300:
        display_score_y=2
    elif score_y<400:
        display_score_y=3
    elif score_y<500:
        display_score_y=4
    elif score_y<600:
        display_score_y=5
    elif score_y<700:
        display_score_y=6
    elif score_y<800:
        display_score_y=7
    elif score_y<900:
        display_score_y=8
    elif score_y<1000:
        display_score_y=9
    elif score_y<1100:
        display_score_y=10
    elif score_y<1200:
        display_score_y=11
    elif score_y<1300:
        display_score_y=12
    elif score_y<1400:
        display_score_y=13
    elif score_y<1500:
        display_score_y=14
    elif score_y<1600:
        display_score_y=15
    elif score_y<1700:
        display_score_y=16
    elif score_y<1800:
        display_score_y=17
    elif score_y<1900:
        display_score_y=18
    elif score_y<2000:
        display_score_y=19
    elif score_y<2100:
        display_score_y=20
    elif score_y<2200:
        display_score_y=21
    elif score_y<2300:
        display_score_y=22
    elif score_y<2400:
        display_score_y=23
    elif score_y<2500:
        display_score_y=24
    elif score_y<2600:
        display_score_y=25
    elif score_y<2700:
        display_score_y=26
    elif score_y<2800:
        display_score_y=27
    elif score_y<2900:
        display_score_y=28
    elif score_y<3000:
        display_score_y=29
    elif score_y<3100:
        display_score_y=30
    elif score_y<3200:
        display_score_y=31
    elif score_y<3300:
        display_score_y=32
    elif score_y<3400:
        display_score_y=33
    elif score_y<3500:
        display_score_y=34
    elif score_y<3600:
        display_score_y=35
    elif score_y<3700:
        display_score_y=36
    elif score_y<3800:
        display_score_y=37
    elif score_y<3900:
        display_score_y=38
    elif score_y<4000:
        display_score_y=39
    elif score_y<4100:
        display_score_y=40
    elif score_y<4200:
        display_score_y=41
    elif score_y<4300:
        display_score_y=42
    elif score_y<4400:
        display_score_y=43
    elif score_y<4500:
        display_score_y=44
    elif score_y<4600:
        display_score_y=45
    elif score_y<4700:
        display_score_y=46
    elif score_y<4800:
        display_score_y=47
    elif score_y<4900:
        display_score_y=48
    elif score_y<5000:
        display_score_y=49
    elif score_y<5100:
        display_score_y=50
    elif score_y<5200:
        display_score_y=51
    elif score_y<5300:
        display_score_y=52
    elif score_y<5400:
        display_score_y=53
    elif score_y<5500:
        display_score_y=54
    elif score_y<5600:
        display_score_y=55
    elif score_y<5700:
        display_score_y=56
    elif score_y<5800:
        display_score_y=57
    elif score_y<5900:
        display_score_y=58
    elif score_y<6000:
        display_score_y=59
    else:
        display_score_y=60
    if score_x>5:
        screen.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 200, True, False)
        text = font.render(str("PLAYER 1 WON"),True,LIGHT_BLUE)
        screen.blit(text,[50,200])
    if score_y>6000:
        screen.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 200, True, False)
        text = font.render(str("PLAYER 2 WON"),True,GREEN)
        screen.blit(text,[50,200])
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()