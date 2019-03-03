import random
import pygame
import math
from sys import exit

#värit
BLACK   = (0,   0,     0)
GREY    = (200, 200, 200)
WHITE   = (255, 255, 255)
BLUE    = (0,   102, 204)
ORANGE  = (255, 128, 9  )
VIOLET  = (127, 0,   255)
YELLOW  = (255, 255, 0  )
PINK    = (255, 0,   255)

#pelinäyttö
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
BALL_SIZE = 10

varit = [BLUE,WHITE,ORANGE,VIOLET,YELLOW,PINK] #maholliset värit pelissä

lkm = 4 #montako on per rivi
tietokone = [] #tähän tietokone randomilla valkkaapi värit
ball_list = []
ball_list_koords = []


def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    screen.fill(GREY)
    pygame.display.set_caption("MasterMind")

    clock = pygame.time.Clock()

    ####
    while len(tietokone) < lkm:
        tietokone.append(random.choice(varit))

    print("anna värit yksitellen (tai välilyönnillä erotettuna) [BLUE, WHITE, ORANGE, VIOLET, YELLOW, PINK] :")
    print("______________________")
    #peli()

    #tossa ylempänä se teki ton pelin

    clock = pygame.time.Clock()
    done1 = False
    mouseClick = False

    for i in range(6):
        ball = make_ball(i*50,0,varit[i])
        ball_list.append(ball)
        ball_list_koords.extend([[ball.x,ball.y]])
        #print(ball_list_koords[-1])
    print(*ball_list_koords,sep='\n')


    while not done1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done1 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClick = True

            if mouseClick == True:
                position = pygame.mouse.get_pos()
                mouseClick = False
                #print(position)
                #lasketaan hiiren klikkauksen matka pallon keskipisteestä
                distance = math.sqrt((position[0]-ball.x)**2 + (position[1]-ball.y)**2)
                print(distance)

                if distance < float(BALL_SIZE):
                    print("ollaan pallon sisällä")
            #VÄRI PALLOT
            """
            for i in range(6):
                ball = make_ball(i*50,0,varit[i])
                ball_list.append(ball)
                ball_list_koords.extend([ball.x,ball.y])
            print(ball_list_koords)
            """
                #ball_list_color.extend([ball.color])

            for pallo in ball_list:
                for vari in varit:

                    pygame.draw.circle(screen, pallo.color, [pallo.x, pallo.y], BALL_SIZE)

            #for i in range(len(ball_list)):
            #    pygame.draw.circle(screen, varit[i], [ball[i].x, ball[i].y], BALL_SIZE)

            clock.tick(20)
            pygame.display.flip()

            """
            while len(pallot) < 5:
                for i in range()
                ball = make_ball(0.0)
                x_1 = 100
            """



class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = None

def make_ball(x_1,y_1,vari):
    ball = Ball()
    ball.x = 100+x_1
    ball.y = 100+y_1
    ball.color = vari
    return ball

def screen():
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("MasterMind")

    tietokone = [] #tähän tietokone randomilla valkkaapi värit

    while len(tietokone) < lkm:
        tietokone.append(random.choice(varit))

    #print("")asdasdasdasd
    #print(tietokone)


def kysy_varit(varit):
    kayttaja = []

    while len(kayttaja) < lkm:
            valinta = input("anna väri rivi: ").strip().split(" ")
            if valinta[-1] == "ragequit": #Akille ragequit nappi
                exit(0)
            if valinta[-1] == "ratkaisu":
                print("Ratkaisu on: ",tietokone)

            elif len(valinta) > lkm:
                print("annoit liikaa värejä")

            elif all(elem in varit for elem in valinta):
                kayttaja.extend(valinta)
            else:
                print("Kirjoitit värin väärin")
    return kayttaja



#print("anna värit yksitellen (tai välilyönnillä erotettuna) [sininen,valkoinen,oranssi,violetti,keltainen,pinkki] :")
#print("______________________")

def peli():
    done = False
    while not done:
        arvaus = kysy_varit(varit)

        arvaus_muunnos = []
        vali_ratkaisu = []
        tulokset = []

        for i in range(len(arvaus)):
            if arvaus[i] == tietokone[i]:
                tulokset.append("red")
            else:
                arvaus_muunnos.append(arvaus[i])
                vali_ratkaisu.append(tietokone[i])

        for i in range(len(arvaus_muunnos)):
            if arvaus_muunnos[i] in vali_ratkaisu:
                tulokset.append("white")

                g = (i for i, e in enumerate(vali_ratkaisu) if e in arvaus_muunnos)
                indeksi = next(g)
                vali_ratkaisu.pop(indeksi)

        if arvaus == tietokone:
            print("voitit pelin")
            done = True
            break

        random.shuffle(tulokset)
        print("tässä rivin tulos: ",tulokset)
        print("______________________")

if __name__ == "__main__":
    main()
