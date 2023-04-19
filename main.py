import pygame
from threading import Thread
import time
import random

pygame.init()
pygame.font.init()

POINT_FONT = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)

FPS = 60

HEIGHT = 500
WIDTH = 500

IMAGE_HEIGHT = 400
IMAGE_WIDTH = 400

point = 0

window = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def countDown():
    global myTimer

    myTimer = 5
    for x in range(5):
        myTimer-=1
        time.sleep(1)
    print("time out")



def stop():
    global point
    point -=1
    main()

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
        addrs = randomLine("RajiniKanth.txt")
    elif rnum == 3:
        #Vijay
        if Preference == "Vijay":
            Correct = True
        addrs = randomLine("Vijay.txt")
    
    return addrs,Correct


def drawWindow(imageRect, AJITH_IMAGE, point):

    window.blit(AJITH_IMAGE, (imageRect.x, imageRect.y))
    global startTime
    startTime = time.time()
    pointText = POINT_FONT.render(str(point), 1, WHITE)
    window.blit(pointText,(0,0))
    pygame.display.update()

# countDownThread = Thread(target=countDown)
# countDownThread.start()

def main():
    window.fill((0,0,0))
    global point

    Correct = False
    Preference = "Vijay"


    addrs, Correct = chooseRandomImage(Correct,Preference)
    IMAGE = pygame.transform.scale(pygame.image.load(addrs), (IMAGE_WIDTH,IMAGE_HEIGHT))
    
    imageRect = pygame.Rect(50,50, 400, 400)

    clock.tick(FPS)

    running = True
    while running:
        global startTime
        elapsedTime = time.time() - startTime
        if elapsedTime > 5:
            point = 0
            print("Time's Up")
            main()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #correct
                    if Correct:
                        point+=2
                    else:
                        point-=1
                    # myTimer = 0
                    main()
                if event.key == pygame.K_LCTRL: #others
                    if Correct:
                        point-=5
                    else:
                        point+=1
                    # myTimer = 0
                    main()

        drawWindow(imageRect, IMAGE, point)      
    print("done")


if __name__ == "__main__":
    main()