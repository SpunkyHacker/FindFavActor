import pygame
import os
import random

pygame.init()

FPS = 60

HEIGHT = 500
WIDTH = 500

IMAGE_HEIGHT = 400
IMAGE_WIDTH = 400



window = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def chooseRandomImage(Correct,Preference):

    def randomLine(fname):
        lines = open(fname).read().splitlines()
        return random.choice(lines)

    rnum = random.randint(1,3)
    if rnum == 1:
        #ajith
        if Preference == "Ajith":
            Correct = True
        addrs = randomLine("Ajith.txt")
    elif rnum == 2:
        #rajinikanth
        if Preference == "Rajinikanth":
            Correct = True
        addrs = randomLine("RanjiniKanth.txt")
    elif rnum == 3:
        #Vijay
        if Preference == "Vijay":
            Correct = True
        addrs = randomLine("Vijay.txt")
    
    return addrs,Correct


def drawWindow(imageRect, AJITH_IMAGE):
    window.blit(AJITH_IMAGE, (imageRect.x, imageRect.y))

    pygame.display.update()

def main():

    Correct = False
    Preference = "Vijay"

    addrs, Correct = chooseRandomImage(Correct,Preference)
    AJITH_IMAGE = pygame.transform.scale(pygame.image.load(addrs), (IMAGE_WIDTH,IMAGE_HEIGHT))
    
    imageRect = pygame.Rect(50,50, 400, 400)

    clock.tick(FPS)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        drawWindow(imageRect, AJITH_IMAGE)      
    print("done")


if __name__ == "__main__":
    main()