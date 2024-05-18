from GameClass import *
import random


def Draw_Card(player):
    if player.txt == "Player":
        for i in range(6):
            if player.slot[i] == None:
                num = random.randint(0,6)
                if num==0:
                    player.slot[i] = Card_Place(i,"GameJam/assets/solid.jpg",300,600)
                elif num==1:
                    player.slot[i] = Card_Place(i,"GameJam/assets/hollow.jpg",300,600)
                elif num==2:
                    player.slot[i] = Card_Place(i,"GameJam/assets/look.jpg",300,600)
                elif num==3:
                    player.slot[i] = Card_Place(i,"GameJam/assets/drink.jpg",300,600)
                elif num==4:
                    player.slot[i] = Card_Place(i,"GameJam/assets/key.jpg",300,600)
                elif num==5:
                    player.slot[i] = Card_Place(i,"GameJam/assets/armor.jpg",300,600)
                elif num==6:
                    player.slot[i] = Card_Place(i,"GameJam/assets/hand.jpg",300,600)
    elif player.txt == "Enemy":
        for i in range(6):
            if player.slot[i] == None:
                num = random.randint(0,6)
                if num==0:
                    player.slot[i] = Card_Place(i,"GameJam/assets/solid.jpg",0,0)
                elif num==1:
                    player.slot[i] = Card_Place(i,"GameJam/assets/hollow.jpg",0,0)
                elif num==2:
                    player.slot[i] = Card_Place(i,"GameJam/assets/look.jpg",0,0)
                elif num==3:
                    player.slot[i] = Card_Place(i,"GameJam/assets/drink.jpg",0,0)
                elif num==4:
                    player.slot[i] = Card_Place(i,"GameJam/assets/key.jpg",0,0)
                elif num==5:
                    player.slot[i] = Card_Place(i,"GameJam/assets/armor.jpg",0,0)
                elif num==6:
                    player.slot[i] = Card_Place(i,"GameJam/assets/hand.jpg",0,0)

def Card_Choose(image_path,x,y,x_size,y_size):
    if image_path == "GameJam/assets/solid.jpg":
        card = solid_ammo(image_path,x,y,x_size,y_size)
    elif image_path == "GameJam/assets/hollow.jpg":
        card = hollow_ammo(image_path,x,y,x_size,y_size)
    elif image_path == "GameJam/assets/look.jpg":
        card = look(image_path,x,y,x_size,y_size)
    elif image_path == "GameJam/assets/drink.jpg":
        card = drink(image_path,x,y,x_size,y_size)
    elif image_path == "GameJam/assets/armor.jpg":
        card = armor(image_path,x,y,x_size,y_size)
    elif image_path == "GameJam/assets/key.jpg":
        card = key(image_path,x,y,x_size,y_size)
    elif image_path == "GameJam/assets/hand.jpg":
        card = hand(image_path,x,y,x_size,y_size)
    return card

def Card_Place(i,image_path,x,y):
    if  i == 0:
        card = Card_Choose(image_path,x,y,200,290)
    elif i == 1:
        card = Card_Choose(image_path,x+200,y,200,290)
    elif i == 2:
        card = Card_Choose(image_path,x+400,y,200,290)
    elif i == 3:
        card = Card_Choose(image_path,x+600,y,200,290)
    elif i == 4:
        card = Card_Choose(image_path,x+800,y,200,290)
    elif i == 5:
        card = Card_Choose(image_path,x+1000,y,200,290)
    return card

def initialGame(player,enemy,dialog):
    player.slot[4] = None
    player.slot[5] = None
    player.slot[3] = None
    player.slot[2] = None
    player.slot[1] = None
    player.slot[0] = Card_Place(0,"GameJam/assets/hand.jpg",300,600)
    enemy.slot[4] = None
    enemy.slot[5] = None
    enemy.slot[3] = None
    enemy.slot[2] = None
    enemy.slot[1] = None
    enemy.slot[0] = Card_Place(0,"GameJam/assets/key.jpg",0,0)
    Turn_initial(player,dialog)

def arrange(slot):
    num = 0
    for i in range (6):
        if slot[i] == None:
            num = i
            break
    for i in range(num,6,1):
        if i == 5 or slot[i+1] == None:
            num = i
            break
        else:
            slot[i+1].x -=200
            slot[i] = slot[i+1]
    slot[num] = None
            
def Turn_initial(player,dialog):
    Draw_Card(player)
    player.action = 2
    player.armor = 0
    if player.txt == "Player":
        dialog.txt = "Your Turn!"
        return 1
    return 0

def FindSlot(slot,card):
    for i in range(6):
        if slot[i].__class__.__name__ == card:
            return i
    return -1


def AI_action(enemy,gun,player):
    action = []
    if enemy.life==3:
        if gun.ammo.empty() == False:
            action.append('shoot player')
            gun.shoot("Player",player,enemy)
            enemy.action-=2
        else:
            for i in range(2):
                card = FindSlot(enemy.slot,'solid_ammo')
                if card != -1 and gun.ammo.qsize()!=6:
                    action.append('solid_ammo')  
                    check = enemy.slot[card].use(gun)
                    if check == 1:
                        enemy.slot[card] = None
                        arrange(enemy.slot)
                        enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'hollow_ammo')
                if card != -1 and gun.ammo.qsize()!=6:
                    action.append('hollow_ammo')
                    check = enemy.slot[card].use(gun)
                    if check == 1:
                        enemy.slot[card] = None
                        arrange(enemy.slot)
                        enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'hand')
                if card != -1:
                    action.append('hand')
                    enemy.slot[card].use(player)
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'look')
                if card != -1:
                    action.append('look')
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'armor')
                if card != -1:
                    action.append('armor')
                    enemy.slot[card].use(enemy)
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'drink')
                if card != -1:
                    action.append('drink')
                    enemy.slot[card].use(gun)
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
            enemy.action = 0
        
    else:
        dice = random.randint (0,1)
        if dice > 0:
            dice = random.randint (0,1)
            if dice:
                action.append('shoot Enemy')
                gun.shoot("Enemy",player,enemy)
                enemy.action-=2
            else:
                action.append('shoot Player')
                gun.shoot("Player",player,enemy)
                enemy.action-=2
        else:
            for i in range(2):
                card = FindSlot(enemy.slot,'solid_ammo')
                if card != -1 and gun.ammo.qsize()!=6:  
                    action.append('solid_ammo')
                    check = enemy.slot[card].use(gun)
                    if check == 1:
                        enemy.slot[card] = None
                        arrange(enemy.slot)
                        enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'hollow_ammo')
                if card != -1 and gun.ammo.qsize()!=6:
                    action.append('hollow_ammo')
                    check = enemy.slot[card].use(gun)
                    if check == 1:
                        enemy.slot[card] = None
                        arrange(enemy.slot)
                        enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'hand')
                if card != -1:
                    action.append('hand')
                    enemy.slot[card].use(player)
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'look')
                if card != -1:
                    action.append('look')
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'armor')
                if card != -1:
                    action.append('armor')
                    enemy.slot[card].use(enemy)
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
                card = FindSlot(enemy.slot,'drink')
                if card != -1:
                    action.append('drink')
                    enemy.slot[card].use(gun)
                    enemy.slot[card] = None
                    arrange(enemy.slot)
                    enemy.action-=1
                    continue
            enemy.action = 0
    return action
                