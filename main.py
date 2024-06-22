import pygame
import os
import random
pygame.init()

DISP_WINDOW = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Multi-Player Flappy Bird Game")
FLAPPY_BIRD_IMG1 = pygame.transform.scale(pygame.image.load(os.path.join("Media","flappy2.png")), (50,50))  
FLAPPY_BIRD_IMG2 = pygame.transform.scale(pygame.image.load(os.path.join("Media","flappy3.png")), (50,50))          
WHITE = (255,255,255)
FLAPPY_BIRD_X, FLAPPY_BIRD_Y = 200,200

bg = pygame.transform.scale(pygame.image.load(os.path.join("Media","bg.png")), (1000,505))
win_design = pygame.transform.scale(pygame.image.load(os.path.join("Media","win design.jpeg")), (1000,505))
# bg = pygame.image.load(os.path.join("Media","bg.png"))
top_obs = pygame.transform.scale(pygame.image.load(os.path.join("Media","obstacle_top.png")), (50,250))
bottom_obs = pygame.transform.scale(pygame.image.load(os.path.join("Media","obstacle_bottom.png")), (50,200))

top_obstacles = [[300,0],[500,0],[800,0]]
bottom_obstacles = [[400,400],[600,400],[900,400]]
win_des_coords = [1100,0]

FPS = 60
coordinates = pygame.Rect(200,200,50,50)



def drawer(coordinates):
    DISP_WINDOW.blit(bg,(0,0))
    
    DISP_WINDOW.blit(win_design,(win_des_coords[0],win_des_coords[1]))

    for ele in top_obstacles:
        DISP_WINDOW.blit(top_obs,ele)

    for ele in bottom_obstacles:
        DISP_WINDOW.blit(bottom_obs,ele)    
    
    DISP_WINDOW.blit(FLAPPY_BIRD_IMG1,(coordinates.x,coordinates.y))
    pygame.display.update()


def move_down(u,t,a):
    drawer(coordinates)
    coordinates.y += 0.5 * a * (t**2)
            # print(coordinates.y)
    # u += a
    # t += 1



def move_up(u1,a1):
    drawer(coordinates)
    coordinates.y -= -(u1**2)/(2*a1)
    # u1 += a1

def move_forward(coordinates):
    drawer(coordinates)
    coordinates.x += 0.5
    for ele in top_obstacles:
        ele[0] -= 0.5
    for ele in bottom_obstacles:
        ele[0] -= 0.5    
    win_des_coords[0] -= 0.5



# def play_game():
#     drawer(coordinates)
    
#     for ele in top_obstacles:
#         if coordinates.x == ele[0] and coordinates.y <= top_obs.get_height():
#             coordinates.x -= 1
#             coordinates.y -= 1
#     for ele in bottom_obstacles:
#         if coordinates.x == ele[0] and coordinates.y >= 400:
#             coordinates.x -= 1
#             coordinates.y -= 1 

#     drawer(coordinates)

def check_collision(coordinates):
    bird_rect = pygame.Rect(coordinates.x, coordinates.y, 50, 50)
    for ele in top_obstacles:
        top_rect = pygame.Rect(ele[0], ele[1], 50, 250)
        if bird_rect.colliderect(top_rect):
            return True
    for ele in bottom_obstacles:
        bottom_rect = pygame.Rect(ele[0], ele[1], 50, 200)
        if bird_rect.colliderect(bottom_rect):
            return True
    return False

def play_game(coordinates):
    if check_collision(coordinates):
        print("Collision Detected!")
        return True  # Indicate a collision
    return False


 
                   


# print(pressed_keys)

# coordinates.y += 10
# print(coordinates)
# print(coordinates.y)
# print(coordinates.x)

def main():
    clock = pygame.time.Clock() 
    game_over = False
    
    u = 0.0
    t = 1.0
    a = 0.01

    u1 = 0.07
    a1 = -0.0001
    
    # coordinates = pygame.Rect(200,200,50,50)

    while pygame.K_SPACE not in pygame.key.get_pressed():
        drawer(coordinates)
    
    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
        prev_coords = coordinates.copy()
        
        if play_game(coordinates):
            coordinates.x -= random.randint(10,70)
            coordinates.y -= random.randint(10,70)
            prev_coords = coordinates
            continue

        move_forward(coordinates)
        
        
        
        if coordinates.x >= win_des_coords[0]:
            game_over = True
        
        # if DISP_WINDOW.get_height() - coordinates.y <= 60:
        #     game_over = True
        # coordinates.x += 1
        
        
        # move_forward()
        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[pygame.K_SPACE] and coordinates.y > 0):
            move_up(u1,a1)
            u1 += a1
        if(pressed_keys[pygame.K_s]):
            u1 = 0.07
            a1 = -0.0001
        # u1 = 2.0



        
        if (pressed_keys[pygame.K_s] and u == 0) or (DISP_WINDOW.get_height() - (coordinates.y+43.9) > 0 and not pressed_keys[pygame.K_SPACE]):
            # print("hey there")
            move_down(u,t,a) 
            u += a
            t += 1           
        if pressed_keys[pygame.K_SPACE]:
            u = 0.0
            t = 1.0    
        # u = 0.0
        # t = 1.0
        # drawer(coordinates)
        
        
        # if DISP_WINDOW.get_width() - coordinates.y < 0:
        #     coordinates.y += 0.5 * a * (t**2)
        #     u += a
        #     t += 1
        #     drawer(coordinates)
            # print(coordinates)
        # drawer(coordinates)        
        
        # FLAPPY_BIRD_Y += 1
    # elif pressed_keys[pygame.K_s]:    
    #     FLAPPY_BIRD_Y -= 1
    
    game_over = True

    while game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
        drawer(coordinates)

        
    
    


    pygame.quit()    











if __name__ == "__main__":
    main()

