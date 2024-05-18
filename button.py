import pygame

class Button():
    def __init__(self,txt,x,y,x_size,y_size,color):
        self.txt = txt
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.color = color

    def DrawButton(self,surface,screen):
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.x+self.x_size, self.y), 4)
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.x, self.y+self.y_size), 4)
        pygame.draw.line(surface, self.color, (self.x, self.y+self.y_size), (self.x+self.x_size, self.y+self.y_size), 4)
        pygame.draw.line(surface, self.color, (self.x+self.x_size, self.y), (self.x+self.x_size, self.y+self.y_size), 4)
        screen.blit(surface,(0,0))

    def DrawTxT(self,surface,screen,font):
        text_surface = font.render(self.txt,True,self.color)
        text_rect = text_surface.get_rect(center=(self.x+(self.x_size//2),self.y+(self.y_size//2)+(self.y_size//20)))
        screen.blit(text_surface, text_rect)
        

        
        