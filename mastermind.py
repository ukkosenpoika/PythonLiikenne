import random
import pygame
from sys import exit

#värit
BLACK   = (0,   0,   0  )
WHITE   = (255, 255, 255)
BLUE    = (0,   102, 204)
ORANGE  = (255, 128, 9  )
VIOLET  = (127, 0,   255)
YELLOW  = (255, 255, 0  )
PINK    = (255, 0,   255)

#pelinäyttö
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

varit = ["sininen","valkoinen","oranssi","violetti","keltainen","pinkki"] #maholliset värit pelissä
lkm = 4 #montako on per rivi
tietokone = [] #tähän tietokone randomilla valkkaapi värit


def main():

    while len(tietokone) < lkm:
        tietokone.append(random.choice(varit))

    print("anna värit yksitellen (tai välilyönnillä erotettuna) [sininen,valkoinen,oranssi,violetti,keltainen,pinkki] :")
    print("______________________")
    peli()
    #tossa ylempänä se teki ton pelin


    pygame.init()
    screen()
    clock = pygame.time.Clock()
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

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

main()
