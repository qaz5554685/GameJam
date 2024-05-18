import sys

import pygame
from button import *
from pygame.locals import QUIT

# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
window_surface = pygame.display.set_mode((1600, 900))
# 設置視窗標題為 Hello World:)
pygame.display.set_caption('Hello World:)')
# 清除畫面並填滿背景色
font = pygame.font.Font("GameJam/assets/Silver.ttf", 60)

bg = pygame.Surface(window_surface.get_size())
bg = bg.convert()
bg.fill((221,221,221))  

game_status = 0 # 0 = menu, 1=playing


# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    if game_status == 0:
        start_button = Button("Start",650,500,300,100,(0,0,0))
        quit_button = Button("Quit",650,650,300,100,(0,0,0))
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x>=quit_button.x and mouse_x <= (quit_button.x+quit_button.x_size) and mouse_y>=quit_button.y and mouse_y <= (quit_button.y+quit_button.y_size):
                    pygame.quit()
                    sys.exit()
                if mouse_x>=start_button.x and mouse_x <= (start_button.x+start_button.x_size) and mouse_y>=start_button.y and mouse_y <= (start_button.y+start_button.y_size):
                    game_status = 1

        window_surface.fill((221, 221, 221))
        start_button.DrawButton(bg,window_surface)
        quit_button.DrawButton(bg,window_surface)
        start_button.DrawTxT(bg,window_surface,font)
        quit_button.DrawTxT(bg,window_surface,font)

        pygame.display.update()
    elif game_status == 1:
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        window_surface.fill((221, 221, 221))
        pygame.display.update()