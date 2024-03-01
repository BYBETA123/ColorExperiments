import pygame
import random
# Define some variables
color_x=255
color_y=0
color_z=0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE=(0,0,255)
LIGHT_BLUE=(0,226,226)
PURPLE=(128,0,90)
COLOR=(color_x,color_y,color_z)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARK_BLUE = (0, 0, 255)
INDIGO = (46, 43, 95)
VIOLET = (139, 0, 255)
square_x=50
square_y=50
enemy_square_x=1000
enemy_square_y=350
player_rect=pygame.Rect(square_x,square_y,50,50)
enemy_rect=pygame.Rect(enemy_square_x,enemy_square_y,50,50)
display_score_y=0
clock_tick=132
counter=0
def check_score(score_y):
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
    return display_score_y

def player_icon(screen, x, y):
    pygame.draw.rect(screen,COLOR, [square_x,square_y,50,50])

def player_icon_hitbox(screen,x,y):
    # left  
    pygame.draw.line(screen, BLACK, [square_x, square_y], [square_x, square_y+50], 1)
    # right
    pygame.draw.line(screen, BLACK, [square_x+50, square_y], [square_x+50, square_y+50], 1)
    # top
    pygame.draw.line(screen, BLACK, [square_x, square_y], [square_x+50, square_y], 5)
    # bottom
    pygame.draw.line(screen, BLACK, [square_x+50, square_y+50], [square_x, square_y+50], 1)

def enemy_icon(screen,x,y):
    pygame.draw.rect(screen,GREEN, [enemy_square_x,enemy_square_y,50,50])

def enemy_icon_hitbox(screen,x,y):
    # left
    pygame.draw.line(screen,COLOR,[enemy_square_x,enemy_square_y],[enemy_square_x,enemy_square_y+50],1)
    # right
    pygame.draw.line(screen,COLOR,[enemy_square_x+50,enemy_square_y],[enemy_square_x+50,enemy_square_y+50],1)
    # top
    pygame.draw.line(screen,COLOR,[enemy_square_x,enemy_square_y],[enemy_square_x+50,enemy_square_y],1)
    # bottom
    pygame.draw.line(screen,COLOR,[enemy_square_x+50,enemy_square_y+50],[enemy_square_x,enemy_square_y+50],1)
# Setup
pygame.init()
# length_of_screen=1366
# height_of_screen=768
# Set the width and height of the screen [width,height]
# size = [length_of_screen, height_of_screen]
# screen = pygame.display.set_mode(size)
screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Loop until the user clicks the close button.
done = False
finished = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Hide the mouse cursor
pygame.mouse.set_visible(0)
# Speed in pixels per frame
square_change_x=0
square_change_y=0
enemy_square_change_y=0
enemy_square_change_x=0
color_game_tick=0
# Current position
x_coord=0
y_coord=0
score_x=0
score_y=0
array=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing --- 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=True

    if enemy_square_y>square_y:
        square_y=square_y+4
    if enemy_square_y<square_y:
        square_y=square_y-4
    if enemy_square_x>square_x:
        square_x=square_x+4
    if enemy_square_x<square_x:
        square_x=square_x-4

# track key inputs
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            enemy_square_change_x=-10
        elif event.key == pygame.K_d:
            enemy_square_change_x=10
        elif event.key == pygame.K_w:
            enemy_square_change_y=-10
        elif event.key == pygame.K_s:
            enemy_square_change_y=10

    if event.type==pygame.KEYDOWN:    
        if event.key == pygame.K_LEFT:
            enemy_square_change_x=-10
        elif event.key == pygame.K_RIGHT:
            enemy_square_change_x=10
        elif event.key == pygame.K_UP:
            enemy_square_change_y=-10
        elif event.key == pygame.K_DOWN:
            enemy_square_change_y=10

    # User let up on a key
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d:
            enemy_square_change_x = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            enemy_square_change_y = 0
        elif event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
            square_change_x=0
        elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            square_change_y=0

# if the key events are randomised
        # random_choice=random.choice(array)
        # if random_choice == 1:
        #     enemy_square_change_x=0
        #     enemy_square_change_y=0

    square_x=square_x+square_change_x
    if square_x>=1250:
        square_x=1250
    if square_x<=50:
        square_x=50
    square_y=square_change_y+square_y
    if square_y>=500:
        square_y=500
    if square_y<=50:
        square_y=50

    enemy_square_y=enemy_square_y+enemy_square_change_y
    enemy_square_x=enemy_square_x+enemy_square_change_x
    if enemy_square_y<=50:
        enemy_square_y=51
    if enemy_square_x>=1250:
        enemy_square_x=1250
    if enemy_square_x<=50:
        enemy_square_x=51
    if enemy_square_y>=500:
        enemy_square_y=500



# drawing the grid and adjustments
    screen.fill(BLACK)
    for l in range(50,1350,50):
        pygame.draw.line(screen,COLOR,[l,0],[l,550],1)
    for k in range(50,600,50):
        pygame.draw.line(screen, COLOR, [0,k], [1300,k],1)
    pygame.draw.line(screen,COLOR,[0,0],[1400,0],99)
    pygame.draw.line(screen,COLOR,[0,0],[0,700],99)
    pygame.draw.line(screen,COLOR,[1400,0],[1400,700],200)
    pygame.draw.line(screen,COLOR,[1400,800],[0,800],500)
    pygame.draw.line(screen,COLOR,[375,660],[925,660],180)
    font = pygame.font.SysFont('Calibri', 200, True, False)
    text = font.render((str(0)+str(score_x)),True,WHITE)
    screen.blit(text,[400,570])
    font = pygame.font.SysFont('Calibri', 200, True, False)
    text = font.render("-",True,WHITE)
    
    # color of background
    if color_game_tick<255:
        color_y=color_y+1
        color_game_tick=color_game_tick+1
        COLOR=(color_x,color_y,color_z)
    elif color_game_tick<510:
        color_x=color_x-1
        color_game_tick=color_game_tick+1
        COLOR=(color_x,color_y,color_z)
    elif color_game_tick<765:
        color_y=color_y-1
        color_z=color_z+1
        color_game_tick=color_game_tick+1
        COLOR=(color_x,color_y,color_z)
    elif color_game_tick<1020:
        color_z=color_z-1
        color_x=color_x+1
        color_game_tick=color_game_tick+1
        COLOR=(color_x,color_y,color_z)
    elif color_game_tick>=1020:
        color_game_tick=0
    
    # check_score(score_y)
    if check_score(score_y)<10:
        screen.blit(text,[620,555])
        font = pygame.font.SysFont('Calibri', 200, True, False)
        text = font.render((str(0)+str(check_score(score_y))),True,WHITE)
        screen.blit(text,[700,570])
    else:
        screen.blit(text,[620,555])
        font = pygame.font.SysFont('Calibri', 200, True, False)
        text = font.render(str(check_score(score_y)),True,WHITE)
        screen.blit(text,[700,570])
    
    # draw the player icons
    player_icon(screen, x_coord, y_coord)
    enemy_icon(screen, x_coord, y_coord)
    # player_icon_hitbox(screen, x_coord, y_coord)
    # enemy_icon_hitbox(screen, x_coord, y_coord)
    # check if the squares are touching

    if enemy_square_x>=square_x and enemy_square_x<=square_x+50:
        if enemy_square_y>=square_y and enemy_square_y<=square_y+50:
            score_x+=1
            square_x=50
            square_y=50
            enemy_square_x=1000
            enemy_square_y=350
    if enemy_square_x+50>=square_x and enemy_square_x+50<=square_x+50:
        if enemy_square_y>=square_y and enemy_square_y<=square_y+50:
            score_x+=1
            square_x=50
            square_y=50
            enemy_square_x=1000
            enemy_square_y=350
    if enemy_square_x+50>=square_x and enemy_square_x+50<=square_x+50:
        if enemy_square_y+50>=square_y and enemy_square_y+50<=square_y+50:
            score_x+=1
            square_x=50
            square_y=50
            enemy_square_x=1000
            enemy_square_y=350
    if enemy_square_x>=square_x and enemy_square_x<=square_x+50:
        if enemy_square_y+50>=square_y and enemy_square_y+50<=square_y+50:
            score_x+=1
            square_x=50
            square_y=50
            enemy_square_x=1000
            enemy_square_y=350
    score_y+=1
    # changing player score

    if score_x>=5:
        screen.fill(BLACK)
        clock_tick=10000000
        font = pygame.font.SysFont('Calibri', 200, True, False)
        text = font.render(str("THE COMPUTER"),True,COLOR)
        text2 = font.render(str("WON"),True,COLOR)
        screen.blit(text,[20,200])
        screen.blit(text2,[450,400])
        score_y=0
    if score_y>6000:
        screen.fill(BLACK)
        clock_tick=10000000
        font = pygame.font.SysFont('Calibri', 200, True, False)
        text = font.render(str("YOU WON"),True,COLOR)
        screen.blit(text,[250,200])
        square_x=50
        square_y=50
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit frames per second
    clock.tick(clock_tick)

# Close the window and quit.
pygame.quit()