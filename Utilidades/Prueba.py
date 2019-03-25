#if not g_modulo:
                #for g in ghosts:
                    #g.rect.left,g.rect.top=random.randint(0,DISPLAY_GAME.rect.width-100),random.randint(0,DISPLAY_GAME.rect.height-100)
                #g_modulo=50
            #g_modulo-=1

        #koin=pygame.transform.scale(pygame.image.load(imagen),(13,21))
        #koin=koin.get_rect()
        #if self.amount<=((d_width/koin.width)*(d_height/koin.height)):
            #c=self.amount
            #self.coins=[]
            #for ev in range (0,d_height-koin.height,koin.height):
                #for eve in range (0,d_width-koin.width,koin.width):
                    #if c:
                        #c-=1
                        #self.coins.append(CoinOrd(imagen,eve,ev))
        #else:
            #self.coins=[Coin(imagen,d_width,d_height) for e in range(amount)]