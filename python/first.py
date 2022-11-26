
import pygame
import os

from pygame.locals import *
pygame.init()



screen = pygame.display.set_mode((600,700))
'''Setting the screen size'''

pygame.display.set_caption("Whacky Wheels 2.0")
'''Setting tab description'''

FPS = 60

bike_scale_x, bike_scale_y = 55,40
'''setting bike scale'''

'''tree_scale_x, tree_scale_y = 50,60'''



santa_on_bike_image = pygame.image.load(os.path.join('Images','santa_bike.png'))
'''opening the bike image'''



'''tree_image = pygame.image.load(os.path.join('Images', 'tree.png'))'''


santa_on_bike = pygame.transform.rotate(
    pygame.transform.scale(
        santa_on_bike_image,(bike_scale_x,bike_scale_y)), 0)
'''Rotate by value of 0, transform by called scale value'''

'''tree = pygame.transform.scale(
        tree_image,(tree_scale_x, tree_scale_y))'''



def draw(bike):
    screen.fill((0,200,0)) ,'''BACKGROUND COLOR (Green) '''

    screen.blit(santa_on_bike, (bike.x, bike.y))
    '''DRAWING BIKE'''

    '''screen.blit(tree, (100, 100))'''


    pygame.display.update()
    '''Updates display after drawing'''

def main():
    bike = pygame.Rect(100, 700, bike_scale_x, bike_scale_y)
    '''tree = pygame.Rect(100, 700, tree_scale_x, tree_scale_y)'''

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS) 
        ''' Makes sure that it runs at a stable FPS '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        '''Makes sure it continues running'''

        bike.y += -1
        '''Makes bike go up'''

        '''tree.y += -1'''

        draw(bike)

    pygame.quit()




if __name__ == "__main__":
    main()

'''forgot what this does, but it breaks the code without it'''