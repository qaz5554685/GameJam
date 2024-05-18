import sys

import pygame
from GameClass import *
from GameFunction import *
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
#test

start_button = Button("Start",650,500,300,100,(0,0,0),60)
quit_button = Button("Quit",650,650,300,100,(0,0,0),60)
Game_Name = Text("BuckShot",800,400,150,(0,0,0))
player = Player("Player",100,800,100,(0,0,0),0,800)
enemy = Player("Enemy",1500,50,100,(0,0,0),1400,50)

Turn = 0 # 0=Player1,1=Player2

dialog = DialogBar()
dialog_show = 0
choose = 0
gun = Gun("GameJam/assets/gun.png",680,280,320,320)

# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    if game_status == 0:
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
                    initialGame(player,enemy,dialog)
                    dialog.txt = "Your Turn!"
                    dialog_show = 1
                    continue
        bg.fill((221,221,221))
        window_surface.fill((221, 221, 221))
        start_button.DrawButton(bg,window_surface)
        quit_button.DrawButton(bg,window_surface)
        
        start_button.DrawTxT(window_surface)
        quit_button.DrawTxT(window_surface)
        Game_Name.DrawTxT(window_surface)

        pygame.display.update()
    elif game_status == 1:
        
        skip = Button("Skip",0,400,200,100,(0,0,0),60)
        dialog_surface = pygame.Surface((1600,900),pygame.SRCALPHA)
        dialog_surface.convert()
        dialog_surface.fill((221,221,221,0))
        dialog_surface.set_alpha(256)
        



        

        
        if Turn == 0:
            if player.hand ==1:
                player.hand =0
                dialog.txt = "你被綁了!"
                dialog.DrawBackground(dialog_surface,window_surface)
                dialog.DrawTxT(window_surface)
                pygame.display.update()
                pygame.time.delay(1000)
                Turn = 1
                dialog.txt = "Enemy Turn!"
                dialog_show = 1
                Turn_initial(enemy,dialog)
                continue

            if player.action == 0:
                Turn = 1
                Turn_initial(enemy,dialog)
                continue


            if choose == 0:
                for event in pygame.event.get():
                # 當使用者結束視窗，程式也結束
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for i in range(6):
                            if player.slot[i]!=None and mouse_x >= player.slot[i].x and mouse_x <= player.slot[i].x+player.slot[i].x_size and mouse_y >= player.slot[i].y and mouse_y <= player.slot[i].y+player.slot[i].y_size:
                                if player.slot[i].__class__.__name__ == 'solid_ammo':
                                    check = player.slot[i].use(gun)
                                    if check == 1:
                                        player.slot[i] = None
                                        arrange(player.slot)
                                        player.action-=1
                                elif player.slot[i].__class__.__name__ == 'hollow_ammo':
                                    check = player.slot[i].use(gun)
                                    if check == 1:
                                        player.slot[i] = None
                                        arrange(player.slot)
                                        player.action-=1
                                elif player.slot[i].__class__.__name__ == 'armor':
                                    player.slot[i].use(player)
                                    player.slot[i] = None
                                    arrange(player.slot)
                                    player.action-=1
                                elif player.slot[i].__class__.__name__ == 'drink':
                                    player.slot[i].use(gun)
                                    player.slot[i] = None
                                    arrange(player.slot)
                                    player.action-=1
                                elif player.slot[i].__class__.__name__ == 'look':
                                    dialog.txt = player.slot[i].use(gun)
                                    player.slot[i] = None
                                    arrange(player.slot)
                                    player.action-=1
                                    dialog_show=1
                                elif player.slot[i].__class__.__name__ == 'hand':
                                    player.slot[i].use(enemy)
                                    player.slot[i] = None
                                    arrange(player.slot)
                                    player.action-=1
                                    for j in range(6):
                                        if enemy.slot[j].__class__.__name__ == 'key':
                                            enemy.slot[j].use(enemy)
                                            enemy.slot[j] = None
                                            arrange(enemy.slot)

                                break
                        if mouse_x>=skip.x and mouse_x<=skip.x+skip.x_size and mouse_y>= skip.y and mouse_y <= skip.y + skip.y_size:
                            player.action = 0
                        if mouse_x>=720 and mouse_x<=900 and mouse_y>= 380 and mouse_y <= 500 and player.action==2:
                            choose = 1
                            dialog_show = 1
                            dialog.txt = "選擇第一槍的目標"


            window_surface.fill((221, 221, 221))
            for i in range(6):
                if player.slot[i] != None:
                    player.slot[i].DrawImage(window_surface)
            for i in range(6):
                if enemy.slot[i] != None:
                    enemy.slot[i].DrawImage(window_surface)
            player.DrawHeart(window_surface)
            enemy.DrawHeart(window_surface)
            skip.DrawButton(dialog_surface,window_surface)
            gun.DrawImage(window_surface)
            player.DrawTxT(window_surface)
            enemy.DrawTxT(window_surface)
            skip.DrawTxT(window_surface)
            
            if dialog_show == 1 and choose == 1:
                dialog.DrawBackground(dialog_surface,window_surface)
                dialog.DrawTxT(window_surface)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if mouse_x>=0 and mouse_x<=200 and mouse_y>= 750 and mouse_y <= 820:
                            choose = 0
                            gun.shoot("Player",player,enemy)
                            player.action=0
                        if mouse_x>=1400 and mouse_x<=1600 and mouse_y>= 0 and mouse_y <= 70:
                            choose = 0
                            gun.shoot("Enemy",player,enemy)
                            player.action=0
            elif dialog_show == 1:
                dialog.DrawBackground(dialog_surface,window_surface)
                dialog.DrawTxT(window_surface)
                pygame.display.update()
                pygame.time.delay(1000)
                dialog_show=0
                continue
                
            
                
        
        elif Turn == 1:
            if enemy.hand == 1:
                enemy.hand = 0
                window_surface.fill((0,0,0))
                dialog.txt = "敵人被綁了!"
                dialog.DrawBackground(dialog_surface,window_surface)
                dialog.DrawTxT(window_surface)
                pygame.display.update()
                pygame.time.delay(1000)
                Turn = 0
                dialog_show = Turn_initial(player,dialog)
                continue
            for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            dialog.txt = "Enemy Turn!"
            dialog_show = 1
            window_surface.fill((0,0,0))
            dialog.DrawBackground(dialog_surface,window_surface)
            dialog.DrawTxT(window_surface)

            action_array = AI_action(enemy,gun,player)
            for i in action_array:
                if i == 'hand':
                    for j in range(6):
                        if player.slot[j].__class__.__name__ == 'key':
                            player.slot[j].use(player)
                            player.slot[j] = None
                            arrange(player.slot)
            pygame.display.update()
            pygame.time.delay(1000)
            print(action_array)
            Turn = 0
            dialog_show = Turn_initial(player,dialog)



        
        

        pygame.display.update()