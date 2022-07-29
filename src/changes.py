from src.buildings import Building, Town_Hall, Hut, Wall, Cannon
from src.troops import Attackers, Barbarians, King
from src.tiles import Tile
import os
from colorama import Fore, Back, Style


def set_colors(p,huts,queen, king, town_hall, tiles, cannons,wizard_towers,walls, l, b):
    for i in range(l):
        for j in range(b):
            tiles[i, j].color = "BLUE"
    tiles[3, 5].color = "CYAN"
    tiles[24, 10].color = "CYAN"
    tiles[2, 48].color = "CYAN"
    tiles[15,15].color="CYAN"
    tiles[28,2].color="CYAN"
    tiles[8,40].color="CYAN"
    tiles[20,49].color="CYAN"
    tiles[28,30].color="CYAN"
    tiles[6,14].color="CYAN"
    for W in walls:
        if(W.hp>0):
           a=W.x
           b=W.y
           tiles[a, b].color = "CYAN"
    for H in huts:
        a = H.x
        b = H.y
        if(H.hp > 125):
            c = "GREEN"
        elif(H.hp > 50):
            c = "YELLOW"
        elif(H.hp > 0):
            c = "RED"
        else:
            c = "BLUE"
        tiles[a, b].color = c
        tiles[a+1, b+1].color = c
        tiles[a+1, b].color = c
        tiles[a, b+1].color = c
    a = town_hall.x
    b = town_hall.y
    if(town_hall.hp > 175):
        c = "GREEN"
    elif(town_hall.hp > 70):
        c = "YELLOW"
    elif(town_hall.hp > 0):
        c = "RED"
    else:
        c = "BLUE"
    tiles[a, b].color = c
    tiles[a, b+1].color = c
    tiles[a, b+2].color = c
    tiles[a+1, b+1].color = c
    tiles[a+2, b+1].color = c
    tiles[a+3, b+1].color = c
    tiles[a+1, b].color = c
    tiles[a+2, b].color = c
    tiles[a+3, b].color = c
    tiles[a+1, b+2].color = c
    tiles[a+2, b+2].color = c
    tiles[a+3, b+2].color = c
    for C in cannons:
        a = C.x
        b = C.y
        if(C.hp > 0):
            c = "RED"
        else:
            c = "BLUE"
        tiles[a, b].color = c
    for C in wizard_towers:
        a = C.x
        b = C.y
        if(C.hp > 0):
            c = "RED"
        else:
            c = "BLUE"
        tiles[a, b].color = c
    if(p=='1'):
        if(king.hp > 0):
            tiles[king.x, king.y].color = "YELLOW"
        else:
            tiles[king.x, king.y].color = "BLUE"
            tiles[king.x, king.y].is_king = 0
    if(p=='0'):
        if(queen.hp > 0):
            tiles[queen.x, queen.y].color = "YELLOW"
        else:
            tiles[queen.x, queen.y].color = "BLUE"
            tiles[queen.x, queen.y].is_queen = 0


def dist(a, b, c, d):
    x = a-c
    y = b-d
    if(x < 0):
        x = -x
    if(y < 0):
        y = -y
    if(x > y):
        return x
    else:
        return y


def min_distance(B, a, b, sx, sy):
    min = 12345
    for i in range(sx):
        for j in range(sy):
            if(dist(a+i, b+j, B.x, B.y) < min):
                min = dist(a+i, b+j, B.x, B.y)
    return min

# def barbarians_update(huts, barbarians, king, town_hall, tiles):

def damage(a,b,c,cannons,wizard_towers,huts,town_hall,walls):
    for H in huts:
        for i in range(2):
            for j in range(2):
                if(H.x+i==a and H.y+j == b and H.hp>0):
                    H.hp=H.hp-c
                    return 1
    for H in cannons:
        if(H.x==a and H.y== b and H.hp>0):
            H.hp=H.hp-c
            return 1
    for H in wizard_towers:
        if(H.x==a and H.y== b and H.hp>0):
            H.hp=H.hp-c
            return 1
    for H in walls:
        if(H.x==a and H.y== b and H.hp>0):
            H.hp=H.hp-c
            return 1
    for i in range(4):
        for j in range(3):
            if(town_hall.x+i==a and town_hall.y+j == b and town_hall.hp>0):
                town_hall.hp=town_hall.hp-c
                return 1
    return 0

def wall_damage(a,b,c,walls):
    for H in walls:
        if(H.x==a and H.y== b and H.hp>0):
            H.hp=H.hp-c
            return 1
    return 0
    
def set_target(B,huts, town_hall, cannons,wizard_towers):
    min = 12345
    type = ""
    if(B.hp<=0):
        B.target=-1
    else:
        if(min_distance(B, town_hall.x, town_hall.y, 4, 3) < min and town_hall.hp > 0):
            type = "Town_Hall"
            min = min_distance(B, town_hall.x, town_hall.y, 4, 3)
            B.targetx = town_hall.x
            B.targety = town_hall.y
            B.target = 1
        for H in huts:
            if(min_distance(B, H.x, H.y, 2, 2) < min and H.hp > 0):
                type = "Hut"
                min = min_distance(B, H.x, H.y, 2, 2)
                B.targetx = H.x
                B.targety = H.y
                B.target = 1
        for C in cannons:
            if(min_distance(B, C.x, C.y, 1, 1) < min and C.hp > 0):
                type = "Cannon"
                min = min_distance(B, C.x, C.y, 1, 1)
                B.targetx = C.x
                B.targety = C.y
                B.target = 1
        for C in wizard_towers:
            if(min_distance(B, C.x, C.y, 1, 1) < min and C.hp > 0):
                type = "Wizard_Towers"
                min = min_distance(B, C.x, C.y, 1, 1)
                B.targetx = C.x
                B.targety = C.y
                B.target = 1

def set_target_archer(B,huts, town_hall, cannons,wizard_towers):
    min = 12345
    type = ""
    if(B.hp<=0):
        B.target=-1
    else:
        if(min_distance(B, town_hall.x, town_hall.y, 4, 3) < min and town_hall.hp > 0):
            type = "Town_Hall"
            min = min_distance(B, town_hall.x, town_hall.y, 4, 3)
            B.targetx = town_hall.x
            B.targety = town_hall.y
            B.target = 1
            if(min<=9):
                B.target_in_range=1
        for H in huts:
            if(min_distance(B, H.x, H.y, 2, 2) < min and H.hp > 0):
                type = "Hut"
                min = min_distance(B, H.x, H.y, 2, 2)
                B.targetx = H.x
                B.targety = H.y
                B.target = 1
                if(min<=9):
                    B.target_in_range=1
        for C in cannons:
            if(min_distance(B, C.x, C.y, 1, 1) < min and C.hp > 0):
                type = "Cannon"
                min = min_distance(B, C.x, C.y, 1, 1)
                B.targetx = C.x
                B.targety = C.y
                B.target = 1
                if(min<=9):
                    B.target_in_range=1
        for C in wizard_towers:
            if(min_distance(B, C.x, C.y, 1, 1) < min and C.hp > 0):
                type = "Wizard_Towers"
                min = min_distance(B, C.x, C.y, 1, 1)
                B.targetx = C.x
                B.targety = C.y
                B.target = 1
                if(min<=9):
                    B.target_in_range=1
def set_target_balloon(B,huts, town_hall, cannons,wizard_towers):
    min = 12345
    type = ""
    k=0
    if(B.hp<=0):
        B.target=-1
    else:
        for C in cannons:
            if(min_distance(B, C.x, C.y, 1, 1) < min and C.hp > 0):
                type = "Cannon"
                min = min_distance(B, C.x, C.y, 1, 1)
                B.targetx = C.x
                B.targety = C.y
                B.target = 1
                k=1
        for C in wizard_towers:
            if(min_distance(B, C.x, C.y, 1, 1) < min and C.hp > 0):
                type = "Wizard_Tower"
                min = min_distance(B, C.x, C.y, 1, 1)
                B.targetx = C.x
                B.targety = C.y
                B.target = 1
                k=1
        if(min_distance(B, town_hall.x, town_hall.y, 4, 3) < min and town_hall.hp > 0 and k==0):
            type = "Town_Hall"
            min = min_distance(B, town_hall.x, town_hall.y, 4, 3)
            B.targetx = town_hall.x
            B.targety = town_hall.y
            B.target = 1
        for H in huts:
            if(min_distance(B, H.x, H.y, 2, 2) < min and H.hp > 0 and k==0):
                type = "Hut"
                min = min_distance(B, H.x, H.y, 2, 2)
                B.targetx = H.x
                B.targety = H.y
                B.target = 1
def barbarian_moments(barbarians, tiles, huts, town_hall, cannons,wizard_towers):
    for B in barbarians:
        if(B.x != -1 and B.y != -1 and B.hp>0):
            set_target(B, huts, town_hall, cannons,wizard_towers)
def archer_moments(archers, tiles, huts, town_hall, cannons,wizard_towers):
    for B in archers:
        if(B.x != -1 and B.y != -1 and B.hp>0 and B.hp>0):
            set_target_archer(B, huts, town_hall, cannons,wizard_towers)
def balloon_moments(balloons,tiles,huts,town_hall,cannons,wizard_towers):
    for B in balloons:
        if(B.x != -1 and B.y != -1 and B.hp>0):
            set_target_balloon(B, huts, town_hall, cannons,wizard_towers)

def endings(barbarians, king,queen,archers,balloons, huts, cannons, town_hall,wizard_towers,p):
    x = 0
    y = 0
    for B in barbarians:
        if(B.hp > 0):
            x = 1
    for B in archers:
        if(B.hp > 0):
            x = 1
    for B in balloons:
        if(B.hp > 0):
            x = 1
    if(king.hp > 0 and p=='1'):
        x = 1
    if(queen.hp > 0 and p=='0'):
        x = 1
    for C in cannons:
        if(C.hp > 0):
            y = 1
    for C in wizard_towers:
        if(C.hp > 0):
            y = 1
    for C in huts:
        if(C.hp > 0):
            y = 1
    if(town_hall.hp > 0):
        y = 1
    if(x == 0):
        print(Back.BLACK+"\n", end="")
        os.system('clear')
        return 0
    if(y == 0):
        print(Back.BLACK+"\n", end="")
        os.system('clear')
        return 1
    return 2
def reset(huts,cannons,walls,wizard_towers,town_hall,barbarians,king,queen,balloons,archers,l,b):
    for H in huts:
        H.hp=250
    for H in cannons:
        H.hp=300
    for H in walls:
        H.hp=100
    for H in wizard_towers:
        H.hp=300
    for H in barbarians:
        H.hp=250
        H.x=-1
        H.y=-1
        H.targetx = -1
        H.targety = -1
        H.target = 0
    for H in balloons:
        H.hp=250
        H.x=-1
        H.y=-1
        H.targetx = -1
        H.targety = -1
        H.target = 0
    for H in archers:
        H.hp=125
        H.x=-1
        H.y=-1
        H.targetx = -1
        H.targety = -1
        H.target = 0
        H.target_in_range=0
    town_hall.hp=350
    king.hp=1000
    king.x=l-1
    king.y= int(b/2)
    queen.hp=900
    queen.x=l-1
    queen.y= int(b/2)
    