import pygame
import queue

class Text():
    def __init__(self,txt,x,y,size,color):
        self.txt = txt
        self.txt_x = x
        self.txt_y = y
        self.txt_color = color
        self.font = pygame.font.Font("GameJam/assets/Silver.ttf", size)

    def DrawTxT(self,screen):
        text_surface = self.font.render(self.txt,True,self.txt_color)
        text_rect = text_surface.get_rect(center=(self.txt_x,self.txt_y))
        screen.blit(text_surface, text_rect)
class Button(Text):
    def __init__(self,txt,x,y,x_size,y_size,color,txtsize):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.color = color
        super().__init__(txt,self.x+(self.x_size//2),self.y+(self.y_size//2)+(self.y_size//20),txtsize,color)#txt,self.x+(self.x_size//2),(self.x+self.x_size, self.y+self.y_size),txtsize,color

    def DrawButton(self,surface,screen):
        pygame.draw.rect(surface, (221,221,221), [self.x, self.y, self.x_size, self.y_size])
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.x+self.x_size, self.y), 4)
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y+self.y_size), 4)
        pygame.draw.line(surface, self.color, (self.x, self.y+self.y_size), (self.x+self.x_size, self.y+self.y_size), 4)
        pygame.draw.line(surface, self.color, (self.x+self.x_size, self.y), (self.x+self.x_size, self.y+self.y_size), 4)
        screen.blit(surface,(0,0))

class ImageLoader():
    def __init__(self,image_path,x,y,x_size,y_size):
        self.x = x
        self.y = y
        self.x_size=x_size
        self.y_size=y_size
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(self.x_size,self.y_size))
        self.image.convert()
    
    def DrawImage(self,screen):
        screen.blit(self.image,(self.x,self.y))


class Gun(ImageLoader):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)
        self.ammo = queue.Queue()

    def shoot(self,target,player,enemy):
        if self.ammo.empty() == False:
            current_ammo = self.ammo.get()
            if current_ammo == "solid":
                if target == "Player":
                    if player.armor == 0:
                        player.life -=1
                else:
                    if enemy.armor == 0:
                        enemy.life-=1
            else:
                if self.ammo.empty() == False:
                    current_ammo = self.ammo.get()
                    if current_ammo == "solid":
                        if target == "Player":
                            if enemy.armor == 0:
                                enemy.life -=1
                        else:
                            if player.armor == 0:
                                player.life-=1


class Player(Text):
    def __init__(self,name,name_x,name_y,name_size,name_color,heart_x,heart_y):
        super().__init__(name,name_x,name_y,name_size,name_color)
        self.life = 3
        self.slot = [None,None,None,None,None,None]
        self.action = 0
        self.armor = 0
        self.hand = 0
        self.heart = pygame.image.load("GameJam/assets/heart.png")
        self.heart = pygame.transform.scale(self.heart,(100,100))
        self.heart_x = heart_x
        self.heart_y = heart_y

    def DrawHeart(self,screen):
        for i in range (self.life):
            screen.blit(self.heart,(self.heart_x+i*50,self.heart_y))
        

class Card(ImageLoader):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

class solid_ammo(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,gun):
        if gun.ammo.qsize() < 6:
            gun.ammo.put("solid")
            return 1
        else:
            return 0

class hollow_ammo(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,gun):
        if gun.ammo.qsize() < 6:
            gun.ammo.put("hollow")
            return 1
        else:
            return 0

class armor(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,player):
        player.armor = 1

class drink(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,gun):
        if gun.ammo.qsize() != 0:
            gun.ammo.get()

class hand(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,enemy):
        enemy.hand = 1

class key(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,player):
        player.hand = 0

class look(Card):
    def __init__(self,image_path,x,y,x_size,y_size):
        super().__init__(image_path,x,y,x_size,y_size)

    def use(self,gun):
        if gun.ammo.empty() == True:
            return "No Ammo!"
        return list(gun.ammo.queue)[0]

class DialogBar():
    def __init__(self):
        self.x = 600
        self.y = 250
        self.x_size = 400
        self.y_size = 300
        self.txt = ""
        self.txt_x = 800
        self.txt_y = 400
        self.font = pygame.font.Font("GameJam/assets/Silver.ttf", 80)

    def DrawBackground(self,surface,screen):
        pygame.draw.rect(surface, (221,221,221), [self.x, self.y, self.x_size, self.y_size])
        pygame.draw.line(surface, (0,0,0), (self.x, self.y), (self.x+self.x_size, self.y), 4)
        pygame.draw.line(surface, (0,0,0), (self.x, self.y), (self.x, self.y+self.y_size), 4)
        pygame.draw.line(surface, (0,0,0), (self.x, self.y+self.y_size), (self.x+self.x_size, self.y+self.y_size), 4)
        pygame.draw.line(surface, (0,0,0), (self.x+self.x_size, self.y), (self.x+self.x_size, self.y+self.y_size), 4)
        screen.blit(surface,(0,0))

    def DrawTxT(self,screen):
        text_surface = self.font.render(self.txt,True,(0,0,0))
        text_rect = text_surface.get_rect(center=(self.txt_x,self.txt_y))
        screen.blit(text_surface, text_rect)

        

        
        