import pygame, sys
import time
import random

pygame.init()

#Image Loader
def load_image(name):
    image = pygame.image.load(name)
    return image

#Animation Images
imageone = load_image('walkrightonesword.png')
imagetwo = load_image('walkrighttwosword.png')
imagethree = load_image('walkrightthreesword.png')
imagefour = load_image('standingsword.png')
imagefive = load_image('walkleftonesword.png')
imagesix = load_image('walklefttwosword.png')
imageseven = load_image('walkleftthreesword.png')
imageeight = load_image('forwardonesword.png')
imagenine = load_image('forwardtwosword.png')
imageten = load_image('forwardthreesword.png')
imageeleven = load_image('forwardfoursword.png')
imagetwelve = load_image('forwardfivesword.png')
imagethirteen = load_image('forwardsixsword.png')
imagefourteen = load_image('backonesword.png')
imagefifteen = load_image('backtwosword.png')
imagesixteen = load_image('backthreesword.png')
imageseventeen = load_image('backfoursword.png')
imageeighteen = load_image('backfivesword.png')
imagenineteen = load_image('backsixsword.png')
imagetwenty = load_image('standingbacksword.png')

#Smoke Images
smokeone = load_image('smokeone.png')
smoketwo = load_image('smoketwo.png')
smokethree = load_image('smokethree.png')
smokefour = load_image('smokefour.png')
smokefive = load_image('smokefive.png')
smokesix = load_image('smokesix.png')

#Into Images
dragon = load_image('dragon.png')
flyingdragon = load_image('dragonflying.png')
dragonhalf = load_image('dragonhalf.png')
dragonclosed = load_image('dragonclosed.png')
dragonopen = load_image('dragonopen.png')
son = load_image('son.png')
doorone = load_image('doorone.png')
doortwo = load_image('doortwo.png')
doorthree = load_image('doorthree.png')
doorfour = load_image('doorfour.png')
mage = load_image('mage.png')
holdsword = load_image('holdingsword.png')
firstpicture = load_image('walkrighttwo.png')

#Background Images
bgstart = load_image('bgstart.png')

#TileMap Images
BERRYBUSH = load_image('berrybushtile.png')
BUSH = load_image('bushtile.png')
GRAVEL = load_image('graveltile.png')
MOSSYSTONE = load_image('mossystonetile.png')
STONE = load_image('stonetile.png')
WATER = load_image('watertile.png')
GRASS = load_image('grasstile.png')
HOUSE = load_image('housetile.png')
ROCK = load_image('rocktile.png')
TREE = load_image('treetile.png')
STAIR = load_image('staircasetile.png')

#spritemask = pygame.mask.from_surface(imagefour)

#Basic Widths + Heights
display_width = 1120
display_height = 880
tile_size = 80
MAPWIDTH = 14
MAPHEIGHT = 11

#Colours
black = (0, 0, 0)
gray = (50, 50, 50)
blue = (0, 206, 209)
hoverblue = (95, 158, 160)
cream = (245, 245, 245)

#Tile association numbers
RBUSH = 0
GBUSH = 1
GGRAVEL = 2
MSTONE = 3
GSTONE = 4
BWATER = 5
GGRASS = 6
BHOUSE = 7
BROCK = 8
GTREE = 9
DSTAIR = 10

#All Tiles
tiles = {
    RBUSH : BERRYBUSH,
    GBUSH : BUSH,
    GGRAVEL : GRAVEL,
    MSTONE : MOSSYSTONE,
    GSTONE : STONE,
    BWATER : WATER,
    GGRASS : GRASS,
    BHOUSE : HOUSE,
    BROCK : ROCK,
    GTREE : TREE,
    DSTAIR : STAIR
    }

#First Map
tilemapone = [
    [GTREE, BWATER, BWATER, BWATER, GTREE, BROCK, GGRASS, BROCK, GTREE, BROCK, GTREE, BROCK, BROCK, BROCK],
    [BWATER, BWATER, BWATER, BWATER, BWATER, GGRASS, GGRASS, GGRASS, GGRASS, GTREE, GGRASS, GTREE, BROCK, BROCK],
    [BWATER, BWATER, BWATER, BWATER, RBUSH, RBUSH, BHOUSE, GGRAVEL, RBUSH, GGRASS, GGRASS, GGRASS, GTREE, BROCK],
    [BROCK, BWATER, GBUSH, GGRASS, GTREE, GGRASS, GGRASS, GGRAVEL, GBUSH, BHOUSE, RBUSH, BHOUSE, GBUSH, BROCK],
    [GGRASS, GGRASS, BHOUSE, GGRASS, GBUSH, BHOUSE, GGRASS, GGRAVEL, GGRASS, GGRAVEL, GGRASS, GGRAVEL, GGRAVEL, GTREE],
    [GTREE, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GGRAVEL, GTREE, GGRASS],
    [GTREE, GGRASS, GGRASS, BHOUSE, GGRAVEL, GBUSH, GGRASS, GGRAVEL, GGRASS, GGRASS, GGRAVEL, GGRASS, GGRASS, GGRASS],
    [BROCK, GTREE, RBUSH, GGRAVEL, GGRAVEL, GGRASS, GGRASS, GGRAVEL, GGRASS, GBUSH, GGRAVEL, BHOUSE, GTREE, GTREE],
    [BROCK, BROCK, GTREE, GGRASS, GBUSH, GGRASS, RBUSH, GGRAVEL, BHOUSE, BHOUSE, GGRAVEL, GGRAVEL, GGRAVEL, GTREE],
    [BROCK, BROCK, BROCK, GGRASS, GGRASS, GTREE, GTREE, GGRAVEL, GGRAVEL, GGRAVEL, GBUSH, GGRASS, RBUSH, BROCK],
    [BROCK, BROCK, BROCK, BROCK, GTREE, GTREE, GTREE, GTREE, GTREE, GGRASS, GTREE, BROCK, BROCK, BROCK]
]

#Second Map
tilemaptwo = [
    [GTREE, BROCK, BWATER, BWATER, BWATER, BWATER, GTREE, GTREE, BROCK, GTREE, BROCK, GTREE, BROCK, BROCK],
    [BROCK, GTREE, GTREE, BWATER, BWATER, GGRASS, GTREE, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, BROCK, BROCK],
    [BROCK, GTREE, RBUSH, GGRASS, GGRASS, GGRASS, RBUSH, GGRASS, GGRASS, GGRASS, BROCK, GGRASS, GGRASS, BROCK],
    [GTREE, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GBUSH, GGRASS, GGRASS, BROCK, DSTAIR, BROCK, GTREE],
    [BROCK, GGRASS, GBUSH, GGRASS, BWATER, RBUSH, GGRASS, GGRASS, GTREE, GGRASS, BROCK, BROCK, BROCK, GTREE],
    [GTREE, RBUSH, GBUSH, BWATER, BWATER, GGRASS, GGRASS, GGRASS, GGRASS, RBUSH, GGRASS, GGRASS, GGRASS, GTREE],
    [GTREE, GGRASS, GGRASS, BWATER, BWATER, GBUSH, GTREE, RBUSH, GGRASS, GGRASS, GTREE, RBUSH, GGRASS, BROCK],
    [BROCK, GTREE, BWATER, BWATER, BWATER, GGRASS, GGRASS, GGRASS, GGRASS, GBUSH, GGRASS, BROCK, GGRASS, BROCK],
    [BROCK, GTREE, BWATER, BWATER, GGRASS, GTREE, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, BROCK, GGRASS, GTREE],
    [BROCK, BWATER, BWATER, GTREE, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, GGRASS, BROCK, BROCK],
    [BWATER, BWATER, BWATER, BROCK, GTREE, GTREE, GGRASS, GBUSH, BROCK, BROCK, GTREE, RBUSH, BROCK, BROCK],
]

#Useful definitions
smallText = pygame.font.Font('ARCADECLASSIC.ttf', 25)
GAMEDISPLAY = pygame.display.set_mode((MAPWIDTH * tile_size, MAPHEIGHT * tile_size))
event = pygame.event.poll()
clock = pygame.time.Clock()

#Functions
def character(x, y):
    GAMEDISPLAY.blit(imagefour, (x, y))

def quitgame():
    pygame.quit()
    quit()

def message_display(text, fontsize, timer, colour):
    largeText = pygame.font.Font('ARCADECLASSIC.ttf', fontsize)
    TextSurf, TextRect = text_objects(text, largeText, colour)
    TextRect.center = ((display_width / 2), 780)
    GAMEDISPLAY.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(timer)

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def intro_images():
    displayBackground(tilemapone)
    GAMEDISPLAY.blit(son, (160, 400))

def more_images():
    GAMEDISPLAY.blit(mage, (240, 400))
    GAMEDISPLAY.blit(firstpicture, (80, 400))
    
def display_image(image, x, y, timer):
        GAMEDISPLAY.blit(image, (x, y))
        pygame.display.update()
        time.sleep(timer)

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GAMEDISPLAY, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(GAMEDISPLAY, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    GAMEDISPLAY.blit(textSurf, textRect)


def displayBackground(mapnumber):
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            GAMEDISPLAY.blit(tiles[mapnumber[row][column]], [column * tile_size, row * tile_size])
            if tiles[mapnumber[row][column]] == HOUSE:
                global housemask
                #housemask = pygame.mask.from_surface(HOUSE)

#Start Screen
def game_start():

    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        GAMEDISPLAY.blit(bgstart, (0, 0))

        largeText = pygame.font.Font('ARCADECLASSIC.ttf', 60)
        TextSurf, TextRect = text_objects("Dragon Slayer", largeText, black)
        TextRect.center = ((display_width / 2), (display_height / 4))
        GAMEDISPLAY.blit(TextSurf, TextRect)

        button(" Play!", 180, 230, 100, 50, blue, hoverblue, game_intro)
        button(" Quit!", 840, 230, 100, 50, blue, hoverblue, quitgame)

        pygame.display.update()

#Game introduction
def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        display_image(dragonclosed, 0, 0, 1.5)
        display_image(dragonhalf, 0, 0, 0.042)
        display_image(dragonopen, 0, 0, 1.2)
        GAMEDISPLAY.fill(black)
        display_image(doorone, 430, 480, 2)
        display_image(doortwo, 430, 480, 1.5)
        display_image(doorthree, 430, 480, 1.5)
        display_image(doorfour, 430, 480, 1.3)
        GAMEDISPLAY.fill(black)
        pygame.display.update()
        time.sleep(1.8)

        v = 1200
        z = 395
        v_change = 0

        flying = 0

        while flying < 50:
            v_change = -15
            v += v_change
            intro_images()
            GAMEDISPLAY.blit(flyingdragon, (v, z))
            pygame.display.update()
            time.sleep(0.10)
            flying += 1

        intro_images()
        GAMEDISPLAY.blit(dragon, (530, 350))
        pygame.display.update()
        message_display("Dragon: This world will break under my wraith!", 40, 4, cream)
        intro_images()

        v = 530
        z = 350
        v_change = 0

        flying = 0

        while flying < 67:
            v_change = -15
            v += v_change
            intro_images()
            GAMEDISPLAY.blit(flyingdragon, (v, z))
            pygame.display.update()
            time.sleep(0.10)
            flying += 1

        pygame.display.update()
        GAMEDISPLAY.blit(firstpicture, (80, 400))
        message_display("You: Oh no! My son! Why did you have to fight in the army...", 40, 5.3, cream)
        
        smoke = [smokeone, smoketwo, smokethree, smokefour, smokefive, smokesix]
        for smo in smoke:
            intro_images()
            GAMEDISPLAY.blit(firstpicture, (80, 400))
            GAMEDISPLAY.blit(smo, (240, 400))
            pygame.display.update()
            time.sleep(0.11)

        more_images()
        pygame.display.update()
        time.sleep(0.9)
        message_display("You: A mage! Do you have a spell to revive my boy?", 35, 5.8, cream)
        intro_images()
        more_images()
        message_display("Mage: I do not. Because the dragon took your son,", 35, 6, cream)
        intro_images()
        more_images()
        message_display("Mage: It is your destiny to defeat him!", 35, 6, cream)
        intro_images()
        more_images()
        message_display("Mage: Take this sword. Save the town and avenge your son!", 35, 6, cream)

        smoke = [smokeone, smoketwo, smokethree, smokefour, smokefive, smokesix]
        for smo in smoke:
            displayBackground(tilemapone)
            GAMEDISPLAY.blit(son, (160, 400))
            GAMEDISPLAY.blit(holdsword, (80, 400))
            GAMEDISPLAY.blit(smo, (240, 400))
            pygame.display.update()
            time.sleep(0.11)

        intro_images()
        
        map_one(80, 400)
        intro = False

#Loading map one
def map_one(startonex, startoney):

    x = startonex
    y = startoney
    
    while map_one:
        
        x_change = 0
        y_change = 0

        if y < 0:
            map_two(480, 800)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 30

                if event.key == pygame.K_LEFT:
                    x_change = -30

                if event.key == pygame.K_DOWN:
                    y_change = 30

                if event.key == pygame.K_UP:
                    y_change = -30

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0
            
        displayBackground(tilemapone)
                
        x += x_change
        y += y_change 
        GAMEDISPLAY.blit(son, (160, 400))
        character(x, y)
        pygame.display.update()
        clock.tick()

#Loading map two
def map_two(starttwox, starttwoy):

    x = starttwox
    y = starttwoy
    
    while map_two:
        
        x_change = 0
        y_change = 0

        if y > display_height - 40:
            map_one(480, 10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 30

                if event.key == pygame.K_LEFT:
                    x_change = -30

                if event.key == pygame.K_DOWN:
                    y_change = 30

                if event.key == pygame.K_UP:
                    y_change = -30

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0
            
        displayBackground(tilemaptwo)
                
        x += x_change
        y += y_change 
        character(x, y)
        pygame.display.update()
        clock.tick()
        
game_start()

    
