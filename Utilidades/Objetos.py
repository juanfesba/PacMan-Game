import pygame
from random import randint
from copy import copy
class Obj():
    #Variables de movimiento
    
    def imagenes(self,image):
        pacman1=pygame.image.load(image)
        pacman1=pygame.transform.scale(pacman1,(50,50)) #volver relativo NO gracias
#        pacman1=pacman1.convert()
        return pacman1
    def __init__(self,imagen):
        self.imagen=self.imagenes(imagen)
        self.rect=self.imagen.get_rect()
        
    def imagenes4040(self,image_surf):
        pacman2=pygame.transform.scale(image_surf,(40,40)) #volver relativo NO gracias
        return pacman2

class Sup(pygame.Surface):
    
    def __init__(self,width,height):
        self.surf=pygame.Surface((width,height))
        self.rect=self.surf.get_rect()

class MouseRect(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class MenuLevels():
    def __init__(self,matriztriple):
        self.C_dinamicos=matriztriple
        self.default = pygame.image.load("Menu.png").convert_alpha()
        self.Surf = pygame.Surface((1280,720))
        self.Surfx = self.Surf.get_rect()
        
    def update(self):
        MouseRect=pygame.Rect(pygame.mouse.get_pos(),(1,1))
        self.Surf.blit(self.default,(0,0))
        for e in self.C_dinamicos:
            if MouseRect.colliderect(e[1]):
                self.Surf.blit(pygame.image.load(e[2]),(0,0))
        for e in self.C_dinamicos:
            if MouseRect.colliderect(e[1]):
                self.Surf.blit(pygame.image.load(e[3]).convert_alpha(),(e[1].left,e[1].top-10))
            else:
                self.Surf.blit(pygame.image.load(e[0]).convert_alpha(),e[1])
        
class Botones():
    def __init__(self,imageorig,imageedit,x,y):
        self.imgoriginal=imageorig
        self.imgeditada=imageedit
        self.imgreal=self.imgoriginal
        self.imgpos=self.imgoriginal.get_rect()
        self.imgpos.left,self.imgpos.top=(x,y)

    def update(self,surface,cursor):
        if cursor.colliderect(self.imgpos):
            self.imgreal=self.imgeditada
        else: 
            self.imgreal=self.imgoriginal
        surface.blit(self.imgreal,self.imgpos)

class Pacman(Obj):
    def __init__(self,imagen00,imagen01):
        pacman00=self.imagenes(imagen00)
        pacman01=self.imagenes(imagen01)
        pacman10=pygame.transform.flip(pacman00,True,False)
        pacman11=pygame.transform.flip(pacman01,True,False)
        pacmanA=pygame.transform.rotate(pacman00,90)
        pacmanA1=pygame.transform.rotate(pacman01,90)
        pacmanB=pygame.transform.rotate(pacman00,270)
        pacmanB1=pygame.transform.rotate(pacman01,270)
        self.pacmans=[[pacman00,pacman01],[pacman10,pacman11],[pacmanA,pacmanA1],[pacmanB,pacmanB1]]
        self.rect=pacman00.get_rect()
        self.rect1=pacman00.get_rect()
        self.rect1.width*=0.8
        self.rect1.height*=0.8
        self.rect1.center=(self.rect.width/2,self.rect.height/2)
        self.modulo=0
        self.direccion=1
        self.coins_eaten=0
        self.life_surf=self.imagenes4040(pacman00)
        self.lifes=3
        self.lifesurf=[[self.life_surf,self.life_surf.get_rect()] for e in range (self.lifes)]
        self.limitleft=0
        self.limittop=0
        
    def position(self,x,y):
        self.rect.top= y
        self.rect.left= x
        self.rect1.top= y+5
        self.rect1.left= x+5
        
    def upgrade(self,surf,Coin_obj,Wall_Obj):
        im_pacman=self.pacmans[self.direccion-1][1 if self.modulo<25 else 0]
        self.modulo=self.modulo+1 if  self.modulo<50 else 0
        surf.surf.blit(im_pacman,self.rect)
        self.collideCoins(Coin_obj)
        self.transport(surf.rect.width,surf.rect.height)
        posx,posy=self.rect.left,self.rect.top
        posx1,posy1=self.rect1.left,self.rect1.top
        
        if self.direccion==1:
            self.rect.left+=surf.rect.width/400
            self.rect1.left+=surf.rect.width/400
        elif self.direccion==2:
            self.rect.left-=surf.rect.width/400
            self.rect1.left-=surf.rect.width/400
        elif self.direccion==3:
            self.rect.top-=surf.rect.height/300
            self.rect1.top-=surf.rect.height/300
        elif self.direccion==4:
            self.rect.top+=surf.rect.height/300
            self.rect1.top+=surf.rect.height/300
        for g in Wall_Obj.final_wall:
            if self.rect1.colliderect(g):
                self.rect.left,self.rect.top=posx,posy
                self.rect1.left,self.rect1.top=posx1,posy1
            
        
    def transport(self,width,height):
        if self.rect.left>=width+5:
            self.rect.left=self.rect.width*-1
            self.rect1.left=self.rect1.width*-1-5
        if self.rect.left<=self.rect.width*-1-5:
            self.rect.left=width
            self.rect1.left=width+5
        if self.rect.top>=height+5:
            self.rect.top=self.rect.height*-1
            self.rect1.top=self.rect1.height*-1-5
        if self.rect.top<=self.rect.width*-1-5:
            self.rect.top=height
            self.rect1.top=height+5
    
    def collideCoins(self,Coins_obj):
        x=self.rect1.collidelistall(Coins_obj.rects)
        for e in sorted(x,reverse=True):
            Coins_obj.coins.pop(e)
            Coins_obj.rects.pop(e)
            self.coins_eaten+=1
            Coins_obj.amount-=1
        
    def collideGhosts(self,List):
        #return True if self.rect1.collidelist(List)>-1 else False
        for g in List:
            if self.rect1.colliderect(g.rect):
                return True
        return False
        
class Coin(Obj):
    def __init__(self,imagen,contadorj,contadori):
        self.imagen=pygame.transform.scale(pygame.image.load(imagen),(13,21))
        self.rect=self.imagen.get_rect()
        #self.rect.top=randint(0,d_height-21)
        #self.rect.left=randint(0,d_width-13)
        self.rect.left=contadorj*50+19
        self.rect.top=contadori*50+15
        
    def upgrade(self,surf):
        surf.blit(self.imagen,self.rect)
        
class CoinOrd(Coin):
    def __init__(self,imagen,ev,eve):
        self.imagen=pygame.transform.scale(pygame.image.load(imagen),(13,21))
        self.rect=self.imagen.get_rect()
        self.rect.top=eve
        self.rect.left=ev
        
class Coins(Coin):
    def __init__(self,imagen,d_width,d_height,amount,text):
        self.amount=amount
        self.coins=[]
        contadori=0
        for e in text:
            contadorj=0
            for ev in e:
                if ev==" ":
                    self.coins.append(Coin(imagen,contadorj,contadori))
                contadorj+=1
            contadori+=1
        
        self.coinsave=[]
        contadorisave=0
        for e in text:
            contadorjsave=0
            for ev in e:
                if ev==" ":
                    self.coinsave.append(Coin(imagen,contadorjsave,contadorisave))
                contadorjsave+=1
            contadorisave+=1
        self.rectsave=[e.rect for e in self.coinsave]
        self.rects=[e.rect for e in self.coins]
        
    def upgrades(self,surf):
        for e in self.coins:
            e.upgrade(surf)

class Muros():
    def __init__(self,muros,surf,texto):
        self.muro = []
        width = surf.rect.width
        height = surf.rect.height
        x= {" ":muros[0],"#":muros[1],"1":muros[2],"2":muros[3],"3":muros[4],"4":muros[5],"5":muros[6],"+":muros[7],"6":muros[8],"7":muros[9]}
        cant_x = width/len(texto[0])
        cant_y = height/len(texto)
        acumx = 0
        acumy = 0
        self.r_wall=[]
        self.r1_wall=[]
        for linea in texto:
            l_wall=[]
            l_width=0
            for c in linea:
                imagen = x[c]
                imagenr = imagen.get_rect()
                imagenr.left = acumx
                imagenr.top = acumy
                acumx += imagenr.width
                self.muro.append([imagen,imagenr])
                if imagen==x["#"] or imagen==x["2"] or imagen==x["3"] or imagen==x["5"] or imagen==x["6"] or imagen==x["7"]:
                    l_width+=imagenr.width
                if imagen==x[" "] or imagen==x["1"] or imagen==x["4"] or imagen==x["+"]:
                    if l_width:
                        l_wall.append(pygame.Rect(acumx-l_width-imagenr.width,acumy,l_width,imagenr.height))
                        l_width=0
            if l_width:
                l_wall.append(pygame.Rect(acumx-l_width,acumy,l_width,imagenr.height))
            self.r_wall+=l_wall
            acumy += imagenr.height
            acumx = 0
            
        self.final_wall=[]
        self.l_height=imagenr.height
        while self.r_wall:
            self.left1=self.r_wall[0].left
            top1=self.r_wall[0].top
            height1=self.r_wall[0].height
            self.width1=self.r_wall[0].width
            i=1
            y=len(self.r_wall)-1
            while i <= y:
                x=self.r_wall[i]
                if self.left1==x.left and self.width1==x.width  and x.top-top1==imagenr.height:
                    self.l_height+=imagenr.height
                    top1+=imagenr.height
                    del self.r_wall[i]
                    y-=1
                    i-=1
                i+=1
            self.final_wall.append(pygame.Rect(self.left1,self.r_wall[0].top,self.width1,self.l_height))
            self.l_height=imagenr.height
            del self.r_wall[0]

    def update(self,surf):
        for e in self.muro:
            surf.surf.blit(e[0],e[1])
            
    def MuroColli(self):
        self.x=[e[1] for e in self.muro]
        #for e in self.muro:
            #x.append(e[1])
          
class LifeUp():
    def __init__(self,pos,imagen):
        self.img=pygame.image.load(imagen)
        self.rect=self.img.get_rect()
        self.rect.left=pos[0]
        self.rect.top=pos[1]
        self.rect1=self.img.get_rect()
        self.rect1.left=pos[0]
        self.rect1.top=pos[1]
        self.flag=True
        
    def update(self,surf):
        surf.surf.blit(self.img,self.rect)

class eneMovR():
    def __init__(self,Image_l,pos,min,max,vertical,v):
        self.image = [pygame.image.load(e) for e in Image_l]
        self.actual = self.image[0]
        self.rect = self.actual.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
        self.juan=self.actual.get_rect()
        self.juan.top = pos[1]
        self.juan.left = pos[0]
        self.vx = 0
        self.vy = 0
        self.direccion = True
        self.velocidad = v
        self.modulo = 30
        self.vertical=vertical
        self.min=min
        self.max=max
        
        self.copyjuanmin=min
        self.copyjuanmax=max
        
        self.juanmin=min
        self.juanmax=max
        if self.juanmin==pos[0] or self.juanmin==pos[1]:
            self.dirjuan=True
        else:
            self.dirjuan=False
    
    def Mov_juan(self):
        if self.vertical:
            if self.juanmax>self.juan.top and self.dirjuan:
                self.juan.top+=2
            else:
                self.dirjuan=False
                self.juan.top-=2
                if self.juanmin==self.juan.top:
                    self.dirjuan=True
        else:
            if self.juanmax>self.juan.left and self.dirjuan:
                self.juan.left+=2
                if self.juanmax==self.juan.left:
                    self.image[0]=pygame.transform.flip(self.image[0],True,False)
                    self.image[1]=pygame.transform.flip(self.image[1],True,False)
            else:
                self.dirjuan=False
                self.juan.left-=2
                if self.juanmin==self.juan.left:
                    self.image[0]=pygame.transform.flip(self.image[0],True,False)
                    self.image[1]=pygame.transform.flip(self.image[1],True,False)
                    self.dirjuan=True
    def cambiar(self):
        if not(self.modulo):
            self.modulo = 30
            self.actual = self.image[0]
        
        elif self.modulo == 15:
            self.actual = self.image[1]
            
        self.modulo -= 1
        
    
    def Mov_enemie(self):
        self.cambiar()
        if self.vertical:
            if self.rect.top <= self.min:
                self.direccion = False
            elif self.rect.top >= self.max:
                self.direccion = True
            
            if self.direccion:
                self.vy=-self.velocidad
            else:
                self.vy=self.velocidad
        else:
            if self.rect.left <= self.min:
                self.direccion = False
            elif self.rect.left >= self.max:
                self.direccion = True
            
            if self.direccion:
                self.vx=-self.velocidad
            else:
                self.vx=self.velocidad
        self.rect.move_ip(self.vx,self.vy)
        