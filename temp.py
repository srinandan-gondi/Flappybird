import pygame
import os
pygame.init()

DISP_WINDOW = pygame.display.set_mode((500,500))
pygame.display.set_caption("Multi-Player Flappy Bird Game")
FLAPPY_BIRD_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Media","flappy bird.jpg")), (50,50))          
WHITE = (255,255,255)
FLAPPY_BIRD_X, FLAPPY_BIRD_Y = 200,200


def drawer(coordinates):
    DISP_WINDOW.fill(WHITE)
    DISP_WINDOW.blit(FLAPPY_BIRD_IMG,(coordinates.x,coordinates.y))
    pygame.display.update()


clock = pygame.time.Clock()

pressed_keys = pygame.key.get_pressed()
# print(pressed_keys)

coordinates = pygame.Rect(200,200,50,50)
# coordinates.y += 10
# print(coordinates)
# print(coordinates.y)
# print(coordinates.x)

def main():
    temp = True
    while temp:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                temp = False
        
        if pressed_keys[pygame.K_UP]:
            coordinates.y += 10
            print(coordinates)
        drawer(coordinates)        
        
        # FLAPPY_BIRD_Y += 1
    # elif pressed_keys[pygame.K_s]:    
    #     FLAPPY_BIRD_Y -= 1
    
    

    
    


    pygame.quit()    











if __name__ == "__main__":
    main()


# screen = pygame.display.set_mode([500,500])


# font = pygame.font.Font('freesansbold.ttf', 32)

# text = font.render("Hey There!",True,(0,55,0),(255,255,255))
# textRect = text.get_rect()

# temp = True
# while temp:
#     screen.fill((255,255,255))
    
#     screen.blit(text,textRect) 


#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             temp = False

        
               

    

#     # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

#     pygame.display.flip()

# pygame.quit()




