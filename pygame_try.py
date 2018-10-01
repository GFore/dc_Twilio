import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
nlist = [2, 1, 9, 10, 18, 4, 12, 5, 11]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE) # This is a tuple!
    # pygame.draw.circle(screen, (255, 0, 0), (250, 100), 50, 0)
    end_pos = len(nlist)-1

    while end_pos > 1:
        offset = 0
        for i in range(end_pos):
            if nlist[i] > nlist[i+1]:  # then swap them
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
            #print(num_list, end_pos)
        for x in nlist:
            pygame.draw.rect(screen, BLACK, [75 + offset, 100, 20, 20*x], 2)   # Draw a rectangle outline
            offset += 25
        pygame.display.update()            #and show it all
        pygame.time.delay(500)
        end_pos -= 1
     
    # Draw a solid rectangle
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    pygame.display.update()
    clock.tick(60)
pygame.quit()