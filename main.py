import pygame
import time
import random

pygame.init()
pygame.font.init()

POINT_FONT = pygame.font.SysFont('comicsans', 40)
TIMEUP_FONT = pygame.font.SysFont('comisans', 60)

WHITE = (255, 255, 255)

FPS = 60

HEIGHT = 500
WIDTH = 500

IMAGE_HEIGHT = 400
IMAGE_WIDTH = 400

TIME_FOR_ONE_ROUND = 2

point = 0

window = pygame.display.set_mode((WIDTH,HEIGHT))


clock = pygame.time.Clock()

timestart = time.time()


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

def timesUp():
    window.fill((0, 0, 0)) 
    timeuptext = TIMEUP_FONT.render("Times up", 1, WHITE)
    timesup = TIMEUP_FONT.render("Try Again", 1, WHITE)
    window.blit(timeuptext,(0,100))
    window.blit(timesup, (0, 150))
    pygame.display.update()
    time.sleep(2)
    main()


def urNotFan(Preference):
    window.fill((0, 0, 0))
    urnotfantext = TIMEUP_FONT.render("You are not fan of " +str(Preference), 1, WHITE)
    timetext = TIMEUP_FONT.render("You have survived "+str(round(time.time()-timestart))+" secs", 1, WHITE)
    window.blit(urnotfantext,(0, 100))
    window.blit(timetext,(0, 150))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

def notLoyalToActor(Preference):
    window.fill((0, 0, 0))
    urnotfantext = TIMEUP_FONT.render("You are not loyal to " +str(Preference), 1, WHITE)
    timetext = TIMEUP_FONT.render("You have survived "+str(round(time.time()-timestart))+" secs", 1, WHITE)
    window.blit(urnotfantext,(0, 100))
    window.blit(timetext,(0, 150))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

def drawWindow(imageRect, AJITH_IMAGE, point, elapsedTime):
    window.fill((0,0,0))
    window.blit(AJITH_IMAGE, (imageRect.x, imageRect.y))
    pointText = POINT_FONT.render(str(point), 1, WHITE)
    window.blit(pointText,(0,0))
    timeText = POINT_FONT.render(str(round(elapsedTime)), 1, WHITE)
    window.blit(timeText,(450,0))
    pygame.display.update()


startTime = time.time()
survivedTime = time.time()
def main():
    global startTime
    startTime = time.time()

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

        elapsedTime = time.time() - startTime
        if elapsedTime > TIME_FOR_ONE_ROUND:
            point = 0
            print("Time's Up")
            timesUp()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if point < 0 :
                timesUp()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    if Correct: # showed preferred photo
                        urNotFan(Preference)
                    else: # showed unpreferred photo
                        main()
                elif event.key == pygame.K_SPACE:
                    if Correct: # shown preferred photo
                        point+=1                       
                    else: # showed unpreferred photo
                        notLoyalToActor(Preference)
                    main()

        drawWindow(imageRect, IMAGE, point, elapsedTime)    


    print("done")


if __name__ == "__main__":
    main()