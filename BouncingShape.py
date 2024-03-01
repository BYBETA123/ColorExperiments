import pygame


def changeColor(COLOR,color_game_tick):
    color_x=COLOR[0]
    color_y=COLOR[1]
    color_z=COLOR[2]
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
    return COLOR, color_game_tick


def main():
    # Define some variables
    x=150
    y=150
    x_change=1
    y_change=-1
    speed=0
    screen_size = 600
    # Setup
    pygame.init()
    # screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((screen_size,screen_size))
    window_width=screen.get_width()
    window_height=screen.get_height()

    COLOR = (255,0,0)
    size = 50
    size_update = 0
    # Loop until the user clicks the close button.
    done = False
    color_game_tick=0
    # Hide the mouse cursor
    pygame.mouse.set_visible(0)
    speed_control=10
    # -------- Main Program Loop -----------
    while not done:
        up_coords=y
        left_coords=x
        bottom_coords=y+size
        right_coords=x+size
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True
        if right_coords>=window_width:
            # size_update=1
            x_change=-1
        elif bottom_coords>=window_height:
            # size_update=1
            y_change=-1
        elif left_coords<=0:
            # print("left")
            # print("==")
            size_update=1
            x_change=1
        elif up_coords<=0:
            # print("up")
            # print("==")
            size_update=1
            y_change=1
        if speed==speed_control:
            size+=size_update
            x+=x_change
            y+=y_change
            speed=0
            size_update = 0
            COLOR, color_game_tick = changeColor(COLOR, color_game_tick)
        if size>screen_size:
            size=screen_size
        if x<0:
            x=0
        if y<0:
            y=0
        if x>screen_size:
            x=screen_size
        if y>screen_size:
            y=screen_size
        # print(x_change,y_change, "x:",x," y:",y, "size:",size)
        # print("Up:",up_coords," Left:",left_coords," Bottom:",bottom_coords," Right:",right_coords)
        speed+=1
        # pygame.draw.rect(screen,COLOR, [x,y,square_x,square_y])
        pygame.draw.rect(screen,COLOR, [x,y,size,size])
        pygame.display.flip()
        # screen.fill(BLACK)

    # Close the window and quit.
    pygame.quit()

main()