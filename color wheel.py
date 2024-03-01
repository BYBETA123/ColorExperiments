import pygame
done=False
pygame.init()
screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
color_game_tick=0
color_x=255
color_y=0
color_z=0
BLACK=(0,0,0)
WHITE=(255,255,255)
COLOR=(color_x,color_y,color_z)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=True
    # screen.fill(BLACK)
    # pygame.display.flip()
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
    color_game_tick+=1
    # screen.fill(WHITE)
    screen.fill(COLOR)
    pygame.display.flip()