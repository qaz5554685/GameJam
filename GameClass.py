import pygame
import queue

class Text():
    def __init__(self,txt,x,y,size,color):
        self.txt = txt
        self.txt_x =x
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

    #def shoot(self):




        

        
        