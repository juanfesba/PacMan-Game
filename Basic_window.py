#===============================================================================
# En este espacio solo se van a realizar importaciones de librerias o modulos
#===============================================================================
import sys, pygame, os, random
from pygame.locals import *
from Utilidades import *
from Tkinter import *
from copy import deepcopy

#===============================================================================
# Constantes
#===============================================================================

# Esta declaracion siempre va aqui ---------------------------------------------
pygame.init()

pygame.mixer.music.load("Thexxintro.ogg")
pygame.mixer.music.play(-1)
# Pantalla ---------------------------------------------------------------------
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_FLAGS = FULLSCREEN #0
DISPLAY_DEPTH = 32 #Opcional

# Cuadros por segundo ----------------------------------------------------------
FPS = 100
fpsClock = pygame.time.Clock()

# Inicializacion de la pantalla ------------------------------------------------
x = pygame.display.mode_ok((DISPLAY_WIDTH,DISPLAY_HEIGHT),DISPLAY_FLAGS,DISPLAY_DEPTH)
DISPLAY_SURF = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT),DISPLAY_FLAGS,DISPLAY_DEPTH)

#Inicializacion de superficie de juego

DISPLAY_GAME = Sup(800,600)
DISPLAY_GAME.rect.top = 60
DISPLAY_GAME.rect.left = 165

DISPLAY_BAR = Sup(150,720)
DISPLAY_BAR.rect.top = 0
DISPLAY_BAR.rect.left = 1130

DISPLAY_FONT = Sup(1130,720)
DISPLAY_FONT.rect.top = 0
DISPLAY_FONT.rect.left = 0
DISPLAY_FONT.surf.blit(pygame.image.load("Menu.png"),(0,0))

# Superficie para el fondo


# Titulo del juego --------------------------------------------------------
pygame.display.set_caption("Aleph")
# Icono ------------------------------------------------------------------------
pygame.display.set_icon(pygame.image.load('WhiteBoss.png'))
# Pacman -----------------------------------------------------------------------

pac=Pacman("AvatarP1.png","AvatarP2.png")
pac.position(50,50)

# Fantasmas --------------------------------------------------------------------

ghost=Obj("WhiteBoss.png")
ghosts=[Obj("WhiteBoss.png") for e in range (0)]

# Monedas

#coins=Coins("coins.png",DISPLAY_GAME.rect.width,DISPLAY_GAME.rect.height,1,l_texto)

#Fuente

fontObj = pygame.font.Font('Pacman1.ttf', 32)
fontObj1 = pygame.font.Font('Pacman1.ttf', 100)
fontObj2 = pygame.font.Font('Pacman1.ttf', 70)

#Enemigos Nivel 1

E702530F=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(700,250),300,700,False,2)
E10401540T=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(100,400),150,450,True,2)
E30353075F=eneMovR(["Nivel1/Lobo2.png","Nivel1/Lobo3.png"],(300,350),300,700,False,2)
E704545100T=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(700,450),450,1000,True,2)
E60204060F=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(600,200),400,600,False,2)
E3010045100T=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(300,1000),450,1000,True,2)
E10601090F=eneMovR(["Nivel1/Lobo2.png","Nivel1/Lobo3.png"],(100,600),100,900,False,2)
E90401545T=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(900,400),150,450,True,2)
E107070100T=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(100,700),700,1000,True,2)
E9010070100T=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(900,1000),700,1000,True,2)
E30703070F=eneMovR(["Nivel1/Lobo2.png","Nivel1/Lobo3.png"],(300,700),300,700,False,2)
E40804060F=eneMovR(["Nivel1/Lobo2.png","Nivel1/Lobo3.png"],(400,800),400,600,False,2)
E70903070F=eneMovR(["Nivel1/Oso1.png","Nivel1/Oso2.png"],(700,900),300,700,False,2)
ENEMIGOS = [E702530F.rect,E10401540T.rect,E30353075F.rect,E704545100T.rect,E60204060F.rect,E3010045100T.rect,E10601090F.rect,E90401545T.rect,E107070100T.rect,E9010070100T.rect,E30703070F.rect,E40804060F.rect,E70903070F.rect]
ENEMIGOSj = [E702530F.juan,E10401540T.juan,E30353075F.juan,E704545100T.juan,E60204060F.juan,E3010045100T.juan,E10601090F.juan,E90401545T.juan,E107070100T.juan,E9010070100T.juan,E30703070F.juan,E40804060F.juan,E70903070F.juan]
ENEMIGOSjj = [E702530F,E10401540T,E30353075F,E704545100T,E60204060F,E3010045100T,E10601090F,E90401545T,E107070100T,E9010070100T,E30703070F,E40804060F,E70903070F]

#Meta 1

metacol=pygame.image.load("Target.png")
metacolrect=metacol.get_rect()
metacolrect.top=50
metacolrect.left=500
metarect=metacol.get_rect()
metarect.top=50
metarect.left=500

#Muros Nivel 1
l_texto = ["##22255522#22555222##",
           "# ##2555221225552####",
           "# ###51112121115##3##",
           "#    51222122215   3#",
           "3# # 51211111215 # #3",
           "3#   51111111115   #3",
           "## # 51112121115 # ##",
           "3# # 51111111115 # #3",
           "3#   54555255545   #3",
           "##                 ##",
           "#3# #  # #3# #  # #33",
           "### ##         ## ##3",
           "##                 ##",
           "33# ## ## # ## ## #33",
           "##   #         #   ##",
           "## #   ## # ##   # ##",
           "3# # # #     # # # #3",
           "##   # # #3# # #   #3",
           "3# # #         # # #3",
           "## #   #3##3##   # ##",
           "3#   #         #   #3",
           "###3#3###3#####3#3###",
           "##3###33##3#3#33###3#"]
    
DISPLAY_BACKGROUND = Sup(len(l_texto[0]*50),len(l_texto*50))
DISPLAY_BACKGHOSTS = Sup(len(l_texto[0]*50),len(l_texto*50))  

l_muros = [pygame.image.load("Nivel1/Pasto1.png"),pygame.image.load("Nivel1/Arbol1.png"),pygame.image.load("Nivel1/Pasto4.png"),pygame.image.load("Nivel1/Arbol2.png"),pygame.image.load("Nivel1/Arbol3.png"),pygame.image.load("Nivel1/Madera.png"),pygame.image.load("Nivel1/Rio2.png"),pygame.image.load("Target.png"),pygame.image.load("Nivel2/Cannon2.png"),pygame.image.load("Nivel2/Cannon3.png")]
muros = Muros(l_muros,DISPLAY_BACKGROUND,l_texto)

# Monedas 1

coins=Coins("coins.png",DISPLAY_GAME.rect.width,DISPLAY_GAME.rect.height,174,l_texto)

# Cargar el fondo a la superficie fondo
DISPLAY_BACKGROUND.surf.fill(WHITE)
muros.update(DISPLAY_BACKGROUND)

#Bounus 1

BonusV1=LifeUp([400,100],"Lifeup.png")
BonusV2=LifeUp([600,100],"Lifeup.png")

#Enemigos 2

E157457157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,457),157,607,False,2)
E607457157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,457),157,607,False,2)
E157507157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,507),157,607,False,2)
E607557157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,557),157,607,False,2)
E157307157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,307),157,607,False,2)
E157257157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,257),157,607,False,2)
E157207157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,207),157,607,False,2)
E157157157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,157),157,607,False,2)
E607257157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,257),157,607,False,2)
E607207157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,207),157,607,False,2)
E607157157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,157),157,607,False,2)
E4075757707T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(407,57),57,707,True,2)
E3575757707T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(357,57),57,707,True,2)

E2578078071207T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(257,807),807,1207,True,2)
E4578078071207T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(457,807),807,1207,True,2)
E607307157607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,307),157,607,False,2)
E257807257507F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(257,807),257,507,False,2)
E207907207607F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(207,907),207,607,False,2)
E557857207557F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(557,857),207,557,False,2)
E55795757557F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(557,957),57,557,False,2)
E1571057207457F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,1057),157,457,False,2)
E2571107157257F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(257,1107),157,257,False,2)
E3571157357457F=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(357,1157),357,457,False,2)

E1575757307T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(157,57),57,307,True,2)
E6075757307T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(607,57),57,307,True,2)
E20730757307T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(207,307),57,307,True,2)
E557307557307T=eneMovR(["Nivel2/CannonBall.png","Nivel2/CannonBall.png"],(557,307),57,307,True,2)

E707207157607F=eneMovR(["Nivel2/Soldier1.png","Nivel2/Soldier2.png"],(707,207),707,1057,False,2)
E7076571571057F=eneMovR(["Nivel2/Soldier1.png","Nivel2/Soldier2.png"],(707,657),707,1057,False,2)

ENEMIGOS2 = [E157457157607F.rect,E607457157607F.rect,E157507157607F.rect,E607557157607F.rect,E157307157607F.rect,E157257157607F.rect,E157207157607F.rect,E157157157607F.rect,E607257157607F.rect,E607207157607F.rect,E607157157607F.rect,E4075757707T.rect,E2578078071207T.rect,E4578078071207T.rect,E3575757707T.rect,E607307157607F.rect,E257807257507F.rect,E207907207607F.rect,E557857207557F.rect,E55795757557F.rect,E1571057207457F.rect,E2571107157257F.rect,E3571157357457F.rect,E1575757307T.rect,E6075757307T.rect,E20730757307T.rect,E557307557307T.rect,E707207157607F.rect,E7076571571057F.rect]
ENEMIGOSj2 = [E157457157607F.juan,E607457157607F.juan,E157507157607F.juan,E607557157607F.juan,E157307157607F.juan,E157257157607F.juan,E157207157607F.juan,E157157157607F.juan,E607257157607F.juan,E607207157607F.juan,E607157157607F.juan,E4075757707T.juan,E2578078071207T.juan,E4578078071207T.juan,E3575757707T.juan,E607307157607F.juan,E257807257507F.juan,E207907207607F.juan,E557857207557F.juan,E55795757557F.juan,E1571057207457F.juan,E2571107157257F.juan,E3571157357457F.juan,E1575757307T.juan,E6075757307T.juan,E20730757307T.juan,E557307557307T.juan,E707207157607F.juan,E7076571571057F.juan]
ENEMIGOSjj2 = [E157457157607F,E607457157607F,E157507157607F,E607557157607F,E157307157607F,E157257157607F,E157207157607F,E157157157607F,E607257157607F,E607207157607F,E607157157607F,E4075757707T,E2578078071207T,E4578078071207T,E3575757707T,E607307157607F,E257807257507F,E207907207607F,E557857207557F,E55795757557F,E1571057207457F,E2571107157257F,E3571157357457F,E1575757307T,E6075757307T,E20730757307T,E557307557307T,E707207157607F,E7076571571057F]

#Meta 2

metacol2=pygame.image.load("Target.png")
metacolrect2=metacol.get_rect()
metacolrect2.top=50
metacolrect2.left=650
metarect2=metacol.get_rect()
metarect2.top=50
metarect2.left=650

#Muros Nivel 2

l_texto2 = ["##2#####2#####55##2######",
            "#1#44444444444####55##2##",
            "#1#4444444444##5#########",
            "2154444444444###2####2###",
            "#1#4444444444#         ##",
            "51#4444444444# ## # ## #2",
            "#124444444444# #  #  # ##",
            "#1#4444444444#    #    #5",
            "#1#44444444445 #     # 5#",
            "#154444444444# # ### # ##",
            "21#4444444444# #     # #2",
            "#124444444444#    #    ##",
            "#124444444444#2 # # 5 #5#",
            "51#4444444444#          #",
            "#1#4444444444## 2 # # ##5",
            "#1#5#7#1#7#5##          #",
            "#1##3111111#2## # 5 # #2#",
            "#1#2111111116#    5     #",
            "#1#31111111112 #     # ##",
            "5111111111116# # 2#2 # ##",
            "#52111#1#1#5## #     # #5",
            "##311111112#11   2##   2#",
            "###1116111211# #  #  # 2#",
            "#5#1113111#1## 5# # 5# ##",
            "#5#111#11111##         #2",
            "##5###2#55###5####2###2##",
            "###2####22####55########5",]

DISPLAY_BACKGROUND2 = Sup(len(l_texto2[0]*50),len(l_texto2*50))
DISPLAY_BACKGHOSTS2 = Sup(len(l_texto2[0]*50),len(l_texto2*50))

l_muros2 = [pygame.image.load("Nivel2/Calle1.png"),pygame.image.load("Nivel2/House2.png"),pygame.image.load("Nivel2/Calle2.png"),pygame.image.load("Nivel2/House1.png"),pygame.image.load("Nivel2/Cannon1.png"),pygame.image.load("Nivel2/Calle3.png"),pygame.image.load("Nivel2/House3.png"),pygame.image.load("Target.png"),pygame.image.load("Nivel2/Cannon2.png"),pygame.image.load("Nivel2/Cannon3.png")]
muros2 = Muros(l_muros2,DISPLAY_BACKGROUND2,l_texto2)

#Monedas2

coins2=Coins("coins.png",DISPLAY_GAME.rect.width,DISPLAY_GAME.rect.height,138,l_texto2)

#Cargar el fondo 2

DISPLAY_BACKGROUND2.surf.fill(WHITE)
muros2.update(DISPLAY_BACKGROUND2)

# animacion --------------------------------------------------------------------
g_modulo=0
alpha=255
i=1

#prints

#Intro

xxintro = pygame.image.load("Intro.png").convert()
introm=0

def xxIntro(intromod):
    DISPLAY_INTRO = Sup(1280,720)
    DISPLAY_INTRO.rect.top = 0
    DISPLAY_INTRO.rect.left = 0
    DISPLAY_INTRO.surf.blit(xxintro,(0,0))
    if intromod>=50:
        textSurfaceObj = fontObj.render("Press Enter to Start", True, GREEN) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_INTRO.rect.width/2,600)
        DISPLAY_INTRO.surf.blit(textSurfaceObj,textRectObj)
    return DISPLAY_INTRO

#Mouse

MouseR=MouseRect()

#Menu

MenuMode=0

xxmenu = pygame.image.load("Menu.png").convert_alpha()
xxhistoria = pygame.image.load("Historia.png").convert_alpha()
xxhistoria2 = pygame.image.load("Historia2.png").convert_alpha()
xxhistoria3 = pygame.image.load("Historia3.png").convert_alpha()
historia2posx=640
historia3posx=510

MatrizNiveles=[["Nivel1.png",pygame.Rect(600,200,620,50),"Nivel1Font.png","Nivel1b.png"],
               ["Nivel2.png",pygame.Rect(620,270,620,50),"Nivel2Font.png","Nivel2b.png"],
               ["Nivel3.png",pygame.Rect(610,340,620,50),"Nivel3Font.png","Nivel3b.png"],
               ["Nivel4.png",pygame.Rect(612,410,620,50),"Nivel4Font.png","Nivel4b.png"],
               ["Nivel5.png",pygame.Rect(730,480,620,50),"Nivel5Font.png","Nivel5b.png"]]

MenuL=MenuLevels(MatrizNiveles)

BotNormal = Botones(pygame.image.load("NormalMode1.png").convert_alpha(),pygame.image.load("NormalMode2.png").convert_alpha(),375,200)
BotClassic = Botones(pygame.image.load("ClassicMode1.png").convert_alpha(),pygame.image.load("ClassicMode2.png").convert_alpha(),375,270)
BotSurvival = Botones(pygame.image.load("SurvivalMode.png").convert_alpha(),pygame.image.load("SurvivalMode1.png").convert_alpha(),375,340)
BotInfo = Botones(pygame.image.load("Info.png").convert_alpha(),pygame.image.load("Info1.png").convert_alpha(),100,410)
BotScores = Botones(pygame.image.load("Scores.png").convert_alpha(),pygame.image.load("Scores1.png").convert_alpha(),100,480)
BotOptions = Botones(pygame.image.load("Options1.png").convert_alpha(),pygame.image.load("Options2.png").convert_alpha(),100,550)
BotCredits = Botones(pygame.image.load("Credits.png").convert_alpha(),pygame.image.load("Credits1.png").convert_alpha(),100,620)
BotPlay = Botones(pygame.image.load("Play.png").convert_alpha(),pygame.image.load("Play1.png").convert_alpha(),100,255)

BotBack = Botones(pygame.image.load("Back.png").convert_alpha(),pygame.image.load("Back1.png").convert_alpha(),100,620)
BotReturn = Botones(pygame.image.load("Return.png").convert_alpha(),pygame.image.load("Return1.png").convert_alpha(),530,680)
BotStart = Botones(pygame.image.load("Start.png").convert_alpha(),pygame.image.load("Start1.png").convert_alpha(),530,20)

def xxMenu():
    DISPLAY_MENU = Sup(1280,720)
    DISPLAY_MENU.rect.top = 0
    DISPLAY_MENU.rect.left = 0
    DISPLAY_MENU.surf.blit(xxmenu,(0,0))
    return DISPLAY_MENU

def xxHistoria():
    DISPLAY_MENU = Sup(1280,720)
    DISPLAY_MENU.rect.top = 0
    DISPLAY_MENU.rect.left = 0
    DISPLAY_MENU.surf.fill(BLACK) #DISPLAY_MENU.surf.blit(xxhistoria,(0,0))
    return DISPLAY_MENU

def HistTexto(texto,y):
    textSurfaceObj = fontObj.render(texto, True, BLACK) #Estilizar fondo de letras
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.left,textRectObj.top = 110,y
    xxhistoria.blit(textSurfaceObj,textRectObj)

#===============================================================================
# Circuito principal
ControladorP = 0 #CONTROLADOR PRINCIPAL
LvlState=0
#===============================================================================
while True:
    #DISPLAY_SURF.fill(BLACK)
    DISPLAY_SURF.blit(DISPLAY_FONT.surf,(0,0))
    DISPLAY_GAME.surf.fill(WHITE)
    #EL CONTROLADORP DICE EN QUE ESTADO DEL JUEGO ESTAMOS
    if ControladorP==4:
        #"Scroll"
        
        E702530F.Mov_enemie()
        E10401540T.Mov_enemie()
        E30353075F.Mov_enemie()
        E704545100T.Mov_enemie()
        E60204060F.Mov_enemie()
        E3010045100T.Mov_enemie()
        E10601090F.Mov_enemie()
        E90401545T.Mov_enemie()
        E107070100T.Mov_enemie()
        E9010070100T.Mov_enemie()
        E30703070F.Mov_enemie()
        E40804060F.Mov_enemie()
        E70903070F.Mov_enemie()
        
        E702530F.Mov_juan()
        E10401540T.Mov_juan()
        E30353075F.Mov_juan()
        E704545100T.Mov_juan()
        E60204060F.Mov_juan()
        E3010045100T.Mov_juan()
        E10601090F.Mov_juan()
        E90401545T.Mov_juan()
        E107070100T.Mov_juan()
        E9010070100T.Mov_juan()
        E30703070F.Mov_juan()
        E40804060F.Mov_juan()
        E70903070F.Mov_juan()
        
        DISPLAY_BACKGHOSTS.surf.blit(DISPLAY_BACKGROUND.surf,(0,0))
        
        DISPLAY_BACKGHOSTS.surf.blit(E702530F.actual,E702530F.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E10401540T.actual,E10401540T.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E30353075F.actual,E30353075F.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E704545100T.actual,E704545100T.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E60204060F.actual,E60204060F.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E3010045100T.actual,E3010045100T.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E10601090F.actual,E10601090F.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E90401545T.actual,E90401545T.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E107070100T.actual,E107070100T.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E9010070100T.actual,E9010070100T.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E30703070F.actual,E30703070F.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E40804060F.actual,E40804060F.rect)
        DISPLAY_BACKGHOSTS.surf.blit(E70903070F.actual,E70903070F.rect)
        
        DISPLAY_BACKGHOSTS.surf.blit(metacol,metacolrect)
        
        if BonusV1.flag:
            BonusV1.update(DISPLAY_BACKGHOSTS)
            if pac.rect1.colliderect(BonusV1.rect1):
                BonusV1.flag=False
                pac.lifes+=1
                pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
                
        if BonusV2.flag:
            BonusV2.update(DISPLAY_BACKGHOSTS)
            if pac.rect1.colliderect(BonusV2.rect1):
                BonusV2.flag=False
                pac.lifes+=1
                pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
        #for e in ENEMIGOS:
            #pygame.draw.rect(DISPLAY_BACKGHOSTS.surf,BLUE,e,3)
        #for e in ENEMIGOSj:
            #pygame.draw.rect(DISPLAY_BACKGHOSTS.surf,RED,e,2)
        if pac.rect.left>=DISPLAY_GAME.rect.width/2 and pac.direccion==1 and pac.limitleft<=(50*len(l_texto[0])-DISPLAY_GAME.rect.width):
            DISPLAY_BACKGHOSTS.rect.left -= DISPLAY_GAME.rect.width/400
            pac.rect.left -= 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.left -= 2 #DISPLAY_GAME.rect.width/400
            pac.limitleft += 2 #DISPLAY_GAME.rect.width/400
            for e in muros.final_wall:
                e.left -= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj:
                e.left-=2
            for e in ENEMIGOSjj:
                if not e.vertical:
                    e.juanmin-=2
                    e.juanmax-=2
            for e in coins.coins:
                e.rect.left-=2
            metarect.left-=2
            BonusV1.rect1.left-=2
            BonusV2.rect1.left-=2
            
        if pac.rect.left<=DISPLAY_GAME.rect.width/2 and pac.direccion==2 and pac.limitleft>=0:
            DISPLAY_BACKGHOSTS.rect.left += DISPLAY_GAME.rect.width/400
            pac.rect.left += 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.left += 2 #DISPLAY_GAME.rect.width/400
            pac.limitleft -= 2 #DISPLAY_GAME.rect.width/400
            for e in muros.final_wall:
                e.left+= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj:
                e.left+=2
            for e in ENEMIGOSjj:
                if not e.vertical:
                    e.juanmin+=2
                    e.juanmax+=2
            for e in coins.coins:
                e.rect.left+=2
            metarect.left+=2
            BonusV1.rect1.left+=2
            BonusV2.rect1.left+=2
        if pac.rect.top<=DISPLAY_GAME.rect.height/2 and pac.direccion==3 and pac.limittop>=0:
            DISPLAY_BACKGHOSTS.rect.top += DISPLAY_GAME.rect.height/300
            pac.rect.top += 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.top += 2 #DISPLAY_GAME.rect.width/400
            pac.limittop-= 2 #DISPLAY_GAME.rect.width/400
            for e in muros.final_wall:
                e.top+= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj:
                e.top+=2
            for e in ENEMIGOSjj:
                if e.vertical:
                    e.juanmin+=2
                    e.juanmax+=2
            for e in coins.coins:
                e.rect.top+=2
            metarect.top+=2
            BonusV1.rect1.top+=2
            BonusV2.rect1.top+=2
        if pac.rect.top>=DISPLAY_GAME.rect.height/2 and pac.direccion==4 and pac.limittop<=(50*len(l_texto)-DISPLAY_GAME.rect.height):
            DISPLAY_BACKGHOSTS.rect.top -= 2
            pac.rect.top -= 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.top -= 2 #DISPLAY_GAME.rect.width/400
            pac.limittop += 2 #DISPLAY_GAME.rect.width/400
            for e in muros.final_wall:
                e.top-= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj:
                e.top-=2
            for e in ENEMIGOSjj:
                if e.vertical:
                    e.juanmin-=2
                    e.juanmax-=2
            for e in coins.coins:
                e.rect.top-=2
            metarect.top-=2
            BonusV1.rect1.top-=2
            BonusV2.rect1.top-=2

        DISPLAY_GAME.surf.blit(DISPLAY_BACKGHOSTS.surf,DISPLAY_BACKGHOSTS.rect)
        
        coins.upgrades(DISPLAY_GAME.surf)
        
        DISPLAY_BAR.surf.fill(YELLOW)

        if pac.lifes:
        
            if pac.rect1.collidelistall(ENEMIGOSj):
                
                for e in ENEMIGOSj:
                    e.left+=pac.limitleft
                    e.top+=pac.limittop
                for e in ENEMIGOSjj:
                    e.juanmin=e.copyjuanmin
                    e.juanmax=e.copyjuanmax
                
                for e in coins.coins:
                    e.rect.left+=pac.limitleft
                for e in coins.coins:
                    e.rect.top+=pac.limittop
                BonusV1.rect1.left+=pac.limitleft
                BonusV1.rect1.top+=pac.limittop
                BonusV2.rect1.left+=pac.limitleft
                BonusV2.rect1.top+=pac.limittop
                pac.direccion=1
                pac.lifesurf.pop()
                pac.lifes-=1
                pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
                pac.position(50,50)
                DISPLAY_BACKGHOSTS.rect.top=0
                DISPLAY_BACKGHOSTS.rect.left=0
                for e in muros.final_wall:
                    e.top+=pac.limittop
                    e.left+=pac.limitleft
                metarect.top+=pac.limittop
                metarect.left+=pac.limitleft
                pac.limitleft=0
                pac.limittop=0
            
            if coins.amount==0 and pac.rect1.colliderect(metarect):
                metarect.top+=pac.limittop
                metarect.left+=pac.limitleft
                ControladorP=3
                LvlState=2
                historia2posx=640
                historia3posx=510
                xxhistoria = pygame.image.load("Historia.png").convert_alpha()
                coins.coins=[]
                coins.rects=[]
                coins.amount=174
                pac.coins_eaten=0
                pac.lifes=3
                pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
                pac.position(50,50)
                DISPLAY_BACKGROUND.rect.top=0
                DISPLAY_BACKGROUND.rect.left=0

            if pac.collideGhosts(ghosts):

                pac.lifes-= 1

                #textSurfaceObj = fontObj1.render("Perdiste", True, YELLOW, BLACK)
                #textRectObj = textSurfaceObj.get_rect()
                #textRectObj.center=(DISPLAY_GAME.rect.width/2,DISPLAY_GAME.rect.height/2)
                #DISPLAY_GAME.surf.blit(textSurfaceObj,textRectObj)

                #for g in ghosts:
                    #g.rect.left,g.rect.top=random.randint(0,DISPLAY_GAME.rect.width-100),random.randint(0,DISPLAY_GAME.rect.height-100)

            else:
                #for g in ghosts:
                    #DISPLAY_GAME.surf.blit(g.imagen,g.rect)

                #for e in muros.final_wall:
                    #pygame.draw.rect(DISPLAY_GAME.surf,GREEN,e,2)

                pac.upgrade(DISPLAY_GAME,coins,muros)
                #pygame.draw.rect(DISPLAY_GAME.surf,RED,pac.rect,5)
                #pygame.draw.rect(DISPLAY_GAME.surf,BLUE,pac.rect1,5)

                textSurfaceObj = fontObj.render(str(pac.coins_eaten), True, YELLOW, BLACK)
                textRectObj = textSurfaceObj.get_rect()
                DISPLAY_GAME.surf.blit(textSurfaceObj,textRectObj)
        else:
            BonusV1.flag=True
            BonusV2.flag=True
            metarect.top+=pac.limittop
            metarect.left+=pac.limitleft
            coins.coins=coins.coinsave
            coins.rects=coins.rectsave
            coins.amount=174
            pac.coins_eaten=0
            pac.lifes=3
            pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
            pac.position(50,50)
            DISPLAY_BACKGROUND.rect.top=0
            DISPLAY_BACKGROUND.rect.left=0
            for e in muros.final_wall:
                e.top+=pac.limittop
                e.left+=pac.limitleft
            pac.limitleft=0
            pac.limittop=0
            ControladorP=3
            LvlState=7
            historia2posx=640
            historia3posx=510
            xxhistoria = pygame.image.load("Historia.png").convert_alpha()

        textSurfaceObj = fontObj.render("Score", True, BLACK) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,50)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)

        textSurfaceObj = fontObj.render(str(pac.coins_eaten*50), True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,100)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)

        textSurfaceObj = fontObj.render("Lifes", True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,150)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj.render("Time", True, BLACK) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,320)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj.render(str(pygame.time.get_ticks()/1000.0), True, BLACK) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,350)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)

        for e in pac.lifesurf:
            if i==1:
                e[1].top=200
                e[1].left=15
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==2:
                e[1].top=200
                e[1].left=55
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==3:
                e[1].top=200
                e[1].left=95
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==4:
                e[1].top=250
                e[1].left=15
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==5:
                e[1].top=250
                e[1].left=55
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==6:
                e[1].top=250
                e[1].left=95
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
        i=1
        
        #Nivel 2
        
    if ControladorP==5:
        #"Scroll"
        
        E157457157607F.Mov_enemie()
        E607457157607F.Mov_enemie()
        E157507157607F.Mov_enemie()
        E607557157607F.Mov_enemie()
        E157307157607F.Mov_enemie()
        E157257157607F.Mov_enemie()
        E157207157607F.Mov_enemie()
        E157157157607F.Mov_enemie()
        E607257157607F.Mov_enemie()
        E607207157607F.Mov_enemie()
        E607157157607F.Mov_enemie()
        E4075757707T.Mov_enemie()
        E3575757707T.Mov_enemie()
        E2578078071207T.Mov_enemie()
        E4578078071207T.Mov_enemie()
        E607307157607F.Mov_enemie()
        E257807257507F.Mov_enemie()
        E207907207607F.Mov_enemie()
        E557857207557F.Mov_enemie()
        E55795757557F.Mov_enemie()
        E1571057207457F.Mov_enemie()
        E2571107157257F.Mov_enemie()
        E3571157357457F.Mov_enemie()
        E1575757307T.Mov_enemie()
        E6075757307T.Mov_enemie()
        E20730757307T.Mov_enemie()
        E557307557307T.Mov_enemie()
        E707207157607F.Mov_enemie()
        E7076571571057F.Mov_enemie()
        
        E157457157607F.Mov_juan()
        E607457157607F.Mov_juan()
        E157507157607F.Mov_juan()
        E607557157607F.Mov_juan()
        E157307157607F.Mov_juan()
        E157257157607F.Mov_juan()
        E157207157607F.Mov_juan()
        E157157157607F.Mov_juan()
        E607257157607F.Mov_juan()
        E607207157607F.Mov_juan()
        E607157157607F.Mov_juan()
        E4075757707T.Mov_juan()
        E3575757707T.Mov_juan()
        E2578078071207T.Mov_juan()
        E4578078071207T.Mov_juan()
        E607307157607F.Mov_juan()
        E257807257507F.Mov_juan()
        E207907207607F.Mov_juan()
        E557857207557F.Mov_juan()
        E55795757557F.Mov_juan()
        E1571057207457F.Mov_juan()
        E2571107157257F.Mov_juan()
        E3571157357457F.Mov_juan()
        E1575757307T.Mov_juan()
        E6075757307T.Mov_juan()
        E20730757307T.Mov_juan()
        E557307557307T.Mov_juan()
        E707207157607F.Mov_juan()
        E7076571571057F.Mov_juan()
        
        DISPLAY_BACKGHOSTS2.surf.blit(DISPLAY_BACKGROUND2.surf,(0,0))
        
        DISPLAY_BACKGHOSTS2.surf.blit(E157457157607F.actual,E157457157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E607457157607F.actual,E607457157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E157507157607F.actual,E157507157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E607557157607F.actual,E607557157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E157307157607F.actual,E157307157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E157257157607F.actual,E157257157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E157207157607F.actual,E157207157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E157157157607F.actual,E157157157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E607257157607F.actual,E607257157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E607207157607F.actual,E607207157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E607157157607F.actual,E607157157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E4075757707T.actual,E4075757707T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E3575757707T.actual,E3575757707T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E2578078071207T.actual,E2578078071207T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E4578078071207T.actual,E4578078071207T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E607307157607F.actual,E607307157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E257807257507F.actual,E257807257507F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E207907207607F.actual,E207907207607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E557857207557F.actual,E557857207557F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E55795757557F.actual,E55795757557F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E1571057207457F.actual,E1571057207457F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E2571107157257F.actual,E2571107157257F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E3571157357457F.actual,E3571157357457F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E1575757307T.actual,E1575757307T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E6075757307T.actual,E6075757307T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E20730757307T.actual,E20730757307T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E557307557307T.actual,E557307557307T.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E707207157607F.actual,E707207157607F.rect)
        DISPLAY_BACKGHOSTS2.surf.blit(E7076571571057F.actual,E7076571571057F.rect)
        
        DISPLAY_BACKGHOSTS2.surf.blit(metacol2,metacolrect2)
        
        #DISPLAY_BACKGHOSTS.surf.blit(E702530F.actual,E702530F.rect)
        if pac.rect.left>=DISPLAY_GAME.rect.width/2 and pac.direccion==1 and pac.limitleft<=(50*len(l_texto2[0])-DISPLAY_GAME.rect.width):
            DISPLAY_BACKGHOSTS2.rect.left -= DISPLAY_GAME.rect.width/400
            pac.rect.left -= 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.left -= 2 #DISPLAY_GAME.rect.width/400
            pac.limitleft += 2 #DISPLAY_GAME.rect.width/400
            for e in muros2.final_wall:
                e.left -= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj2:
                e.left-=2
            for e in ENEMIGOSjj2:
                if not e.vertical:
                    e.juanmin-=2
                    e.juanmax-=2
            for e in coins2.coins:
                e.rect.left-=2
            metarect2.left-=2
            
        if pac.rect.left<=DISPLAY_GAME.rect.width/2 and pac.direccion==2 and pac.limitleft>=0:
            DISPLAY_BACKGHOSTS2.rect.left += DISPLAY_GAME.rect.width/400
            pac.rect.left += 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.left += 2 #DISPLAY_GAME.rect.width/400
            pac.limitleft -= 2 #DISPLAY_GAME.rect.width/400
            for e in muros2.final_wall:
                e.left+= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj2:
                e.left+=2
            for e in ENEMIGOSjj2:
                if not e.vertical:
                    e.juanmin+=2
                    e.juanmax+=2
            for e in coins2.coins:
                e.rect.left+=2
            metarect2.left+=2
        if pac.rect.top<=DISPLAY_GAME.rect.height/2 and pac.direccion==3 and pac.limittop>=0:
            DISPLAY_BACKGHOSTS2.rect.top += DISPLAY_GAME.rect.height/300
            pac.rect.top += 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.top += 2 #DISPLAY_GAME.rect.width/400
            pac.limittop-= 2 #DISPLAY_GAME.rect.width/400
            for e in muros2.final_wall:
                e.top+= 2 #DISPLAY_GAME.rect.width/400
            for e in coins2.coins:
                e.rect.top+=2
            metarect2.top+=2
            for e in ENEMIGOSj2:
                e.top+=2
            for e in ENEMIGOSjj2:
                if e.vertical:
                    e.juanmin+=2
                    e.juanmax+=2
        if pac.rect.top>=DISPLAY_GAME.rect.height/2 and pac.direccion==4 and pac.limittop<=(50*len(l_texto2)-DISPLAY_GAME.rect.height):
            DISPLAY_BACKGHOSTS2.rect.top -= 2
            pac.rect.top -= 2 #DISPLAY_GAME.rect.width/400
            pac.rect1.top -= 2 #DISPLAY_GAME.rect.width/400
            pac.limittop += 2 #DISPLAY_GAME.rect.width/400
            for e in muros2.final_wall:
                e.top-= 2 #DISPLAY_GAME.rect.width/400
            for e in ENEMIGOSj2:
                e.top-=2
            for e in ENEMIGOSjj2:
                if e.vertical:
                    e.juanmin-=2
                    e.juanmax-=2
            for e in coins2.coins:
                e.rect.top-=2
            metarect2.top-=2

        DISPLAY_GAME.surf.blit(DISPLAY_BACKGHOSTS2.surf,DISPLAY_BACKGHOSTS2.rect)
        coins2.upgrades(DISPLAY_GAME.surf)
        DISPLAY_BAR.surf.fill(YELLOW)

        if pac.lifes:
            
            if pac.rect1.collidelistall(ENEMIGOSj2):
                
                for e in ENEMIGOSj2:
                    e.left+=pac.limitleft
                    e.top+=pac.limittop
                for e in ENEMIGOSjj2:
                    e.juanmin=e.copyjuanmin
                    e.juanmax=e.copyjuanmax
                
                for e in coins2.coins:
                    e.rect.left+=pac.limitleft
                for e in coins2.coins:
                    e.rect.top+=pac.limittop
                pac.direccion=1
                pac.lifesurf.pop()
                pac.lifes-=1
                pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
                pac.position(50,50)
                DISPLAY_BACKGHOSTS2.rect.top=0
                DISPLAY_BACKGHOSTS2.rect.left=0
                for e in muros2.final_wall:
                    e.top+=pac.limittop
                    e.left+=pac.limitleft
                metarect2.top+=pac.limittop
                metarect2.left+=pac.limitleft
                pac.limitleft=0
                pac.limittop=0
            
            if coins2.amount==0 and pac.rect1.colliderect(metarect2):
                metarect2.top+=pac.limittop
                metarect2.left+=pac.limitleft
                ControladorP=3
                LvlState=3
                historia2posx=640
                historia3posx=510
                xxhistoria = pygame.image.load("Historia.png").convert_alpha()
                coins2.coins=[]
                coins2.rects=[]
                coins2.amount=138
                pac.coins_eaten=0
                pac.lifes=3
                pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
                pac.position(50,50)
                DISPLAY_BACKGROUND2.rect.top=0
                DISPLAY_BACKGROUND2.rect.left=0

            pac.upgrade(DISPLAY_GAME,coins2,muros2)
            #pygame.draw.rect(DISPLAY_GAME.surf,RED,pac.rect,5)
            #pygame.draw.rect(DISPLAY_GAME.surf,BLUE,pac.rect1,5)

            textSurfaceObj = fontObj.render(str(pac.coins_eaten), True, YELLOW, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            DISPLAY_GAME.surf.blit(textSurfaceObj,textRectObj)
        else:
            metarect2.top+=pac.limittop
            metarect2.left+=pac.limitleft
            coins2.coins=coins2.coinsave
            coins2.rects=coins2.rectsave
            coins2.amount=138
            pac.coins_eaten=0
            pac.lifes=3
            pac.lifesurf=[[pac.life_surf,pac.life_surf.get_rect()] for e in range (pac.lifes)]
            pac.position(50,50)
            DISPLAY_BACKGROUND2.rect.top=0
            DISPLAY_BACKGROUND2.rect.left=0
            for e in muros2.final_wall:
                e.top+=pac.limittop
                e.left+=pac.limitleft
            pac.limitleft=0
            pac.limittop=0
            ControladorP=3
            LvlState=7
            historia2posx=640
            historia3posx=510
            xxhistoria = pygame.image.load("Historia.png").convert_alpha()

        textSurfaceObj = fontObj.render("Score", True, BLACK) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,50)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)

        textSurfaceObj = fontObj.render(str(pac.coins_eaten*50), True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,100)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)

        textSurfaceObj = fontObj.render("Lifes", True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,150)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj.render("Time", True, BLACK) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,320)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)
        
        textSurfaceObj = fontObj.render(str(pygame.time.get_ticks()/1000.0), True, BLACK) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (DISPLAY_BAR.rect.width/2,350)
        DISPLAY_BAR.surf.blit(textSurfaceObj,textRectObj)

        for e in pac.lifesurf:
            if i==1:
                e[1].top=200
                e[1].left=15
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==2:
                e[1].top=200
                e[1].left=55
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==3:
                e[1].top=200
                e[1].left=95
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==4:
                e[1].top=250
                e[1].left=15
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==5:
                e[1].top=250
                e[1].left=55
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
            elif i==6:
                e[1].top=250
                e[1].left=95
                DISPLAY_BAR.surf.blit(e[0],e[1])
                i+=1
        i=1
    
    #Circuito de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            print ("QUIT event has occurred!")
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print ("ESCAPE event has occurred!")
                pygame.quit()
                sys.exit()
            if event.key == K_RIGHT:
                pac.direccion=1
            elif event.key == K_LEFT:
                pac.direccion=2
            elif event.key == K_UP:
                pac.direccion=3
            elif event.key == K_DOWN:
                pac.direccion=4
            if event.key == K_RETURN and ControladorP==0:
                ControladorP=1
        elif event.type==pygame.MOUSEBUTTONDOWN and ControladorP==1:
            if MouseR.colliderect(BotNormal.imgpos):
                ControladorP=2
            if MouseR.colliderect(BotPlay.imgpos):
                if MenuMode!=1:
                    MenuMode=1
                else:
                    MenuMode=0
            if MouseR.colliderect(BotCredits.imgpos):
                if MenuMode!=3:
                    MenuMode=3
                else:
                    MenuMode=0
            if MouseR.colliderect(BotInfo.imgpos):
                if MenuMode!=4:
                    MenuMode=4
                else:
                    MenuMode=0
        elif event.type==pygame.MOUSEBUTTONDOWN and ControladorP==2:
            if MouseR.colliderect(MatrizNiveles[0][1]):
                ControladorP=3
                LvlState=1
            if MouseR.colliderect(MatrizNiveles[1][1]):
                ControladorP=3
                LvlState=2
            if MouseR.colliderect(MatrizNiveles[2][1]):
                ControladorP=3
                LvlState=3
            if MouseR.colliderect(MatrizNiveles[3][1]):
                ControladorP=3
                LvlState=4
            if MouseR.colliderect(MatrizNiveles[4][1]):
                ControladorP=3
                LvlState=5
            if MouseR.colliderect(BotBack.imgpos):
                MenuMode=0
                ControladorP=1
        elif event.type==pygame.MOUSEBUTTONDOWN and ControladorP==3:
            if MouseR.colliderect(BotStart.imgpos):
                if LvlState==7:
                    ControladorP=1
                    MenuMode=0
                    historia2posx=640
                    historia3posx=510
                    xxhistoria = pygame.image.load("Historia.png").convert_alpha()
                if LvlState==1:
                    ControladorP=4
                if LvlState==2:
                    ControladorP=5
                #Aqui va el controlador del boton start que esta encima de los pergaminos, este redirige a cada nivel. Ej.
                #if LvlState==2:
                    #ControladorP=5
                #if LvlState==3:
                    #ControladorP=6
                #if LvlState==4:
                    #ControladorP=7
                #if LvlState==5:
                    #ControladorP=8
            if MouseR.colliderect(BotReturn.imgpos):
                ControladorP=2
                #IMPORTANTE E   AL GANAR O PERDER UN NIVEL HAY QUE PONER ESTAS LINEAS LAS CUALES REINICIAN LOS PERGAMINOS
                historia2posx=640
                historia3posx=510
                xxhistoria = pygame.image.load("Historia.png").convert_alpha()

    DISPLAY_SURF.blit(DISPLAY_GAME.surf,DISPLAY_GAME.rect)
    DISPLAY_SURF.blit(DISPLAY_BAR.surf,DISPLAY_BAR.rect)
    if ControladorP==0:
        introm+=1
        if introm==125:
            introm=0
        xIntro=xxIntro(introm)
        DISPLAY_SURF.blit(xIntro.surf,xIntro.rect)
    if ControladorP==1:
        MouseR.update()
        xMenu=xxMenu()
        if MenuMode!=4:
            if MenuMode==1:
                BotNormal.update(xMenu.surf,MouseR)
                BotClassic.update(xMenu.surf,MouseR)
                BotSurvival.update(xMenu.surf,MouseR)
            BotScores.update(xMenu.surf,MouseR)
            BotOptions.update(xMenu.surf,MouseR)
            BotCredits.update(xMenu.surf,MouseR)
            BotPlay.update(xMenu.surf,MouseR)

            if MenuMode==3:
                textSurfaceObj = fontObj1.render("Michael G.", True, YELLOW) #Estilizar fondo de letras
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = ((xMenu.rect.width/2)+200,360)
                xMenu.surf.blit(textSurfaceObj,textRectObj)

                textSurfaceObj = fontObj1.render("Juan Fer. E.", True, YELLOW) #Estilizar fondo de letras
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = ((xMenu.rect.width/2)+200,460)
                xMenu.surf.blit(textSurfaceObj,textRectObj)

                textSurfaceObj = fontObj1.render("Jan P.", True, YELLOW) #Estilizar fondo de letras
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = ((xMenu.rect.width/2)+200,560)
                xMenu.surf.blit(textSurfaceObj,textRectObj)
                
        textSurfaceObj = fontObj1.render("Aleph", True, YELLOWS) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (xMenu.rect.width/2,100)
        xMenu.surf.blit(textSurfaceObj,textRectObj)
        BotInfo.update(xMenu.surf,MouseR)
        DISPLAY_SURF.blit(xMenu.surf,xMenu.rect)
    
    if ControladorP==2:
        MouseR.update()
        MenuL.update()
        
        textSurfaceObj = fontObj2.render("Normal Mode", True, YELLOWS) #Estilizar fondo de letras
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (MenuL.Surfx.width*3/4-50,100)
        MenuL.Surf.blit(textSurfaceObj,textRectObj)
        
        BotBack.update(MenuL.Surf,MouseR)
        
        DISPLAY_SURF.blit(MenuL.Surf,(0,0))
        
    if ControladorP==3:
        MouseR.update()
        xHistoria=xxHistoria()
        BotStart.update(xHistoria.surf,MouseR)
        BotReturn.update(xHistoria.surf,MouseR)
        DISPLAY_SURF.blit(xHistoria.surf,xHistoria.rect)
        if historia3posx==70:
            DISPLAY_SURF.blit(xxhistoria,(130,80))
            if LvlState==1:
                HistTexto("Lvl 1",70)
                HistTexto("Cuenta la leyenda que el hechicero",120)
                HistTexto("del reino mato al rey y secuestro a",150)
                HistTexto("la princesa en su propio castillo,",180)
                HistTexto("ademas de apoderarse del pueblo.",210)
                HistTexto("Con el fin de que nadie le hiciera",260)
                HistTexto("frente, exilio a los mas fuertes del",290)
                HistTexto("reino en el bosque, esperando que las",320)
                HistTexto("bestias se los comiesen.",350)
                HistTexto("Tu aventura comienza aqui. Eres el",400)
                HistTexto("ultimo sobreviviente, escapa del",430)
                HistTexto("bosque no sin antes recoger el dinero",460)
                HistTexto("que dejaron los otros heroes.",490)
            if LvlState==2:
                HistTexto("Lvl 2",70)
                HistTexto("Lo has hecho muy bien, pero no creas",120)
                HistTexto("que derrotar al hechicero es lo mismo",150)
                HistTexto("que escapar de un simple bosque. Debes",180)
                HistTexto("hacerte mas fuerte para poder por lo",210)
                HistTexto("menos acercarte al castillo sin que.",240)
                HistTexto("el poder del hechicero te haga pedazos",270)
                HistTexto("Has escuchado rumores de un sabio que",320)
                HistTexto("puede entrenarte y guiarte y asi poder",350)
                HistTexto("conseguir el poder necesario. Pero no",380)
                HistTexto("olvides que no hay almuerzo gratis y",410)
                HistTexto("debes reunir mas dinero para pagarle.",440)
                HistTexto("Ve a la ciudad en su encuentro. Ten",470)
                HistTexto("mucho cuidado, el hechicero oyo de ti",500)
                HistTexto("y ha mandado soldados para matarte.",530)
            if LvlState==3:
                HistTexto("Lvl 3",70)
                HistTexto("Tu entrenamiento ha ido muy bien, eres",120)
                HistTexto("mas fuerte, pero no lo suficiente como",150)
                HistTexto("para acercarte al hechicero todavia.",180)
                HistTexto("El sabio te dice que en la montania mas",230)
                HistTexto("alta del reino yace una fuente de poder",260)
                HistTexto("capaz de multiplicar tus fuerzas para",290)
                HistTexto("poder hacerle frente al hechicero.",320)
                HistTexto("En tu camino escuchas rumores de que",370)
                HistTexto("casualmente el hechicero ha estado",400)
                HistTexto("transportando el tesoro del reino en",430)
                HistTexto("la montania, seguramente para robarlo.",460)
                HistTexto("Recupera el dinero tambien, pero ten",490)
                HistTexto("cuidado, seguramente esta custodiado.",520)
            if LvlState==4:
                HistTexto("Lvl 4",70)
                HistTexto("Has recorrido toda la montania y no",120)
                HistTexto("encuentras el poder prometido, de",150)
                HistTexto("igual manera notas que falta mucho",180)
                HistTexto("dinero.",210)
                HistTexto("Tal vez te han enganiado. Espera...",260)
                HistTexto("Es un hueco! La montania es un volcan",310)
                HistTexto("Internate en el y recupera lo que",360)
                HistTexto("falta del tesoro, ahi tambien debe",390)
                HistTexto("estar la fuente poder de la que",420)
                HistTexto("hablaba el sabio. Debe de estar muy",450)
                HistTexto("protegida.",480)
            if LvlState==5:
                HistTexto("Lvl 5",70)
                HistTexto("Tu aventura esta llegando a su fin.",120)
                HistTexto("Has entrado al castillo sin que el",170)
                HistTexto("poder del hechicero te afecte.",200)
                HistTexto("Esquiva todos los guardianes que",250)
                HistTexto("obstaculicen tu camino y elimina",280)
                HistTexto("al hechicero.",310)
                HistTexto("No olvides recuperar en el camino",360)
                HistTexto("la parte del tesoro que todavia",390)
                HistTexto("no habia sido transportada al",420)
                HistTexto("volcan.",450)
                HistTexto("Mucha suerte heroe, eres la gran",480)
                HistTexto("esperanza de todo el reino.",510)
            if LvlState==7:
                HistTexto("Perdiste, pero lo puedes volver",200)
                HistTexto("a intentar de nuevo",230)
        if historia3posx!=70:
            historia3posx-=5
            historia2posx+=5
        DISPLAY_SURF.blit(xxhistoria3,(historia3posx,0))
        DISPLAY_SURF.blit(xxhistoria2,(historia2posx,0))
        
    pygame.display.update()
    fpsClock.tick(FPS)
