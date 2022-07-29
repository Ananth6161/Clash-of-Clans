from src.buildings import Building, Town_Hall, Hut, Wall, Cannon
from src.troops import Attackers, Barbarians, King
from src.tiles import Tile
from colorama import Fore, Back, Style
from src.changes import *


def print_in_terminal(tiles, l, b):
    for i in range(l):
        for j in range(b):
            print(Back.BLACK + " ", end="")
            x = "   "
            if(tiles[i, j].color == "BLUE"):
                print(Back.BLUE + x, end="")
            if(tiles[i, j].color == "GREEN"):
                print(Back.GREEN + x, end="")
            if(tiles[i, j].color == "ORANGE"):
                print(Back.GREEN + x, end="")
            if(tiles[i, j].color == "YELLOW"):
                print(Back.YELLOW + x, end="")
            if(tiles[i, j].color == "RED"):
                print(Back.RED + x, end="")
            if(tiles[i, j].color == "CYAN"):
                print(Back.CYAN + x, end="")
        print(Back.BLACK+"\n")


def print_changes(tiles, l, b,cannons,wizard_towers):
    for i in range(l):
        for j in range(b):
            if(tiles[i, j].number_of_barbarians+tiles[i,j].number_of_archers+tiles[i,j].number_of_balloons == 0):
                x = "   "
                for C in cannons:
                    if(C.x==i and C.y==j and C.hp>0):
                        x=" C "
                        break
                for C in wizard_towers:
                    if(C.x==i and C.y==j and C.hp>0):
                        x=" W "
                        break
            if(i==3 and j==5):
                x=" "+"1"+" "
            if(i==24 and j==10):
                x=" "+"2"+" "
            if(i==2 and j==48):
                x=" "+"3"+" "
            if(i==15 and j==15):
                x=" "+"4"+" "
            if(i==28 and j==2):
                x=" "+"5"+" "
            if(i==8 and j==40):
                x=" "+"6"+" "
            if(i==20 and j==49):
                x=" "+"7"+" "
            if(i==28 and j==30):
                x=" "+"8"+" "
            if(i==6 and j==14):
                x=" "+"9"+" "
            if(tiles[i, j].number_of_barbarians+tiles[i,j].number_of_archers+tiles[i,j].number_of_balloons > 0):
                x = str(tiles[i, j].number_of_barbarians)+str(tiles[i, j].number_of_archers)+str(tiles[i, j].number_of_balloons)
            if(tiles[i, j].color == "BLUE"):
                print(Back.BLUE+"\033[%s;%sH" % (2*(i+1), 4*(j+1)-2)+x)
            if(tiles[i, j].color == "GREEN"):
                print(Back.GREEN+"\033[%s;%sH" %
                      (2*(i+1), 4*(j+1)-2)+x)
            if(tiles[i, j].color == "ORANGE"):
                print(Back.MAGENTA+"\033[%s;%sH" % (2*(i+1), 4*(j+1)-2)+x)
            if(tiles[i, j].color == "YELLOW"):
                print(Back.YELLOW+"\033[%s;%sH" % (2*(i+1), 4*(j+1)-2)+x)
            if(tiles[i, j].color == "RED"):
                print(Back.RED+"\033[%s;%sH" % (2*(i+1), 4*(j+1)-2)+x)
            if(tiles[i, j].color == "CYAN"):
                print(Back.CYAN+"\033[%s;%sH" % (2*(i+1), 4*(j+1)-2)+x)


def release_barbarians(barbarians, tiles, no_of_re_ba, a, b):
    barbarians[no_of_re_ba].x = a
    barbarians[no_of_re_ba].y = b
    no_of_re_ba = no_of_re_ba+1
    tiles[a, b].number_of_barbarians = tiles[a, b].number_of_barbarians+1
    return no_of_re_ba
def release_archers(archers, tiles, no_of_re_ar, a, b):
    archers[no_of_re_ar].x = a
    archers[no_of_re_ar].y = b
    no_of_re_ar = no_of_re_ar+1
    tiles[a, b].number_of_archers = tiles[a, b].number_of_archers+1
    return no_of_re_ar
def release_balloons(balloons, tiles, no_of_re_bal, a, b):
    balloons[no_of_re_bal].x = a
    balloons[no_of_re_bal].y = b
    no_of_re_bal = no_of_re_bal+1
    tiles[a, b].number_of_balloons = tiles[a, b].number_of_balloons+1
    return no_of_re_bal


def king_queen_hp_update(p,king,queen, cannons):
    for C in cannons:
        if(p=='1'):
            if(C.state == 0 and king.x-C.x <= C.range and king.y-C.y <= C.range and C.x-king.x <= C.range and C.y-king.y <= C.range and C.hp>0 and king.hp>0):
                king.hp = king.hp-C.rate_of_damage
                C.state = 1
        if(p=='0'):
            if(C.state == 0 and queen.x-C.x <= C.range and queen.y-C.y <= C.range and C.x-queen.x <= C.range and C.y-queen.y <= C.range and C.hp>0 and queen.hp>0):
                queen.hp = queen.hp-C.rate_of_damage
                C.state = 1
def wizard_attack(barbarians,archers,balloons,king,queen, wizard_towers,p):
    for C in wizard_towers:
        for B in balloons:
            if(C.state == 0 and B.x-C.x <= C.range and B.y-C.y <= C.range and C.x-B.x <= C.range and C.y-B.y <= C.range and C.hp>0 and B.hp>0):
                for i in range(-1,2):
                    for j in range(-1,2):
                        for H in barbarians:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in archers:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in balloons:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        if(king.x==B.x+i and king.y==B.y+j and king.hp>0 and p=='1'):
                            king.hp=king.hp-C.rate_of_damage
                        if(queen.x==B.x+i and queen.y==B.y+j and queen.hp>0 and p=='0'):
                            queen.hp=queen.hp-C.rate_of_damage
                C.state = 1
        if(p=='1'):
            if(C.state == 0 and king.x-C.x <= C.range and king.y-C.y <= C.range and C.x-king.x <= C.range and C.y-king.y <= C.range and C.hp>0 and king.hp>0):
                for i in range(-1,2):
                    for j in range(-1,2):
                        for H in barbarians:
                            if(H.x==king.x+i and H.y==king.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in archers:
                            if(H.x==king.x+i and H.y==king.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in balloons:
                            if(H.x==king.x+i and H.y==king.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        if(king.x==king.x+i and king.y==king.y+j and king.hp>0 and p=='1'):
                            king.hp=king.hp-C.rate_of_damage
                        if(queen.x==king.x+i and queen.y==king.y+j and queen.hp>0 and p=='0'):
                            queen.hp=queen.hp-C.rate_of_damage
                C.state = 1
        if(p=='0'):
            if(C.state == 0 and queen.x-C.x <= C.range and queen.y-C.y <= C.range and C.x-queen.x <= C.range and C.y-queen.y <= C.range and C.hp>0 and queen.hp>0):
                for i in range(-1,2):
                    for j in range(-1,2):
                        for H in barbarians:
                            if(H.x==queen.x+i and H.y==queen.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in archers:
                            if(H.x==queen.x+i and H.y==queen.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in balloons:
                            if(H.x==queen.x+i and H.y==queen.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        if(king.x==queen.x+i and queen.y==B.y+j and queen.hp>0 and p=='1'):
                            king.hp=king.hp-C.rate_of_damage
                        if(queen.x==queen.x+i and queen.y==queen.y+j and queen.hp>0 and p=='0'):
                            queen.hp=queen.hp-C.rate_of_damage
                C.state = 1
        for B in barbarians:
            if(C.state == 0 and B.x-C.x <= C.range and B.y-C.y <= C.range and C.x-B.x <= C.range and C.y-B.y <= C.range and C.hp>0 and B.hp>0):
                for i in range(-1,2):
                    for j in range(-1,2):
                        for H in barbarians:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in archers:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in balloons:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        if(king.x==queen.x+i and king.y==queen.y+j and king.hp>0 and p=='1'):
                            king.hp=king.hp-C.rate_of_damage
                        if(queen.x==queen.x+i and queen.y==queen.y+j and queen.hp>0 and p=='0'):
                            queen.hp=queen.hp-C.rate_of_damage
                C.state = 1
        for B in archers:
            if(C.state == 0 and B.x-C.x <= C.range and B.y-C.y <= C.range and C.x-B.x <= C.range and C.y-B.y <= C.range and C.hp>0 and B.hp>0):
                for i in range(-1,2):
                    for j in range(-1,2):
                        for H in barbarians:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in archers:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        for H in balloons:
                            if(H.x==B.x+i and H.y==B.y+j and H.hp>0):
                                H.hp=H.hp-C.rate_of_damage
                        if(king.x==B.x+i and king.y==B.y+j and king.hp>0 and p=='1'):
                            king.hp=king.hp-C.rate_of_damage
                        if(queen.x==B.x+i and queen.y==B.y+j and queen.hp>0 and p=='0'):
                            queen.hp=queen.hp-C.rate_of_damage
                C.state = 1
        

def troops_hp_update(barbarians,archers,balloons, cannons,wizard_towers,king,queen,p):
    for C in cannons:
        for B in barbarians:
            if(C.state == 0 and B.x-C.x <= C.range and B.y-C.y <= C.range and C.x-B.x <= C.range and C.y-B.y <= C.range and B.hp>0 and C.hp>0):
                B.hp = B.hp-C.rate_of_damage
                C.state = 1
        for B in archers:
            if(C.state == 0 and B.x-C.x <= C.range and B.y-C.y <= C.range and C.x-B.x <= C.range and C.y-B.y <= C.range and B.hp>0 and C.hp>0):
                B.hp = B.hp-C.rate_of_damage
                C.state = 1
    wizard_attack(barbarians,archers,balloons,king,queen, wizard_towers,p)


def cannons_reset(cannons):
    for C in cannons:
        C.state = 0
def wizard_towers_reset(wizard_towers):
    for C in wizard_towers:
        C.state = 0

def barbarian_position_update(barbarians, tiles, huts, town_hall, cannons,wizard_towers,walls, l, b):
    barbarian_moments(barbarians, tiles, huts, town_hall, cannons,wizard_towers)
    for i in range(l):
        for j in range(b):
            tiles[i, j].number_of_barbarians = 0
    for B in barbarians:

        if(B.x != -1 and B.y != -1 and B.target > 0 and B.hp >0):
            a = B.x-B.targetx
            if(a < 0):
                moda = -a
            else:
                moda = a
            b = B.y-B.targety
            if(b < 0):
                modb = -b
            else:
                modb = b
            if(moda > modb):
                Bx = B.x-int((a/moda))
                By = B.y
            if(moda < modb):
                Bx = B.x
                By = B.y-int((b/modb))
            if(moda == modb):
                Bx = B.x-int((a/moda))
                By = B.y-int((b/modb))
            if(tiles[Bx, By].is_building == 0):
                B.x = Bx
                B.y = By
            else:
                k=wall_hp_update(Bx,By,walls)
                if(k==0):
                    tiles[Bx, By].is_building = 0
            tiles[B.x, B.y].number_of_barbarians = tiles[B.x,
                                                         B.y].number_of_barbarians+1
            # print("x")

def archer_position_update(archers, tiles, huts, town_hall, cannons,wizard_towers,walls, l, b):
    archer_moments(archers, tiles, huts, town_hall, cannons,wizard_towers)
    for i in range(l):
        for j in range(b):
            tiles[i, j].number_of_archers = 0
    for B in archers:
        if(B.x != -1 and B.y != -1 and B.target > 0 and B.hp>0):
            if(B.target_in_range==1):
                    damage(B.targetx,B.targety,5,cannons,wizard_towers,huts,town_hall,walls)  
            a = B.x-B.targetx
            if(a < 0):
                moda = -a
            else:
                moda = a
            b = B.y-B.targety
            if(b < 0):
                modb = -b
            else:
                modb = b
            if(moda > modb):
                Bx = B.x-int((a/moda))
                By = B.y
            if(moda < modb):
                Bx = B.x
                By = B.y-int((b/modb))
            if(moda == modb):
                Bx = B.x-int((a/moda))
                By = B.y-int((b/modb))
            if(tiles[Bx, By].is_building == 0):
                B.x = Bx
                B.y = By    
            else:
                k=wall_hp_update_ar(Bx,By,walls)
                if(k==0):
                    tiles[Bx, By].is_building = 0
            if(B.hp>0):
                tiles[B.x, B.y].number_of_archers = tiles[B.x,
                                                         B.y].number_of_archers+1
            # print("x")
        

def balloon_position_update(balloons, tiles, huts, town_hall, cannons,wizard_towers,walls, l, b):
    balloon_moments(balloons, tiles, huts, town_hall, cannons,wizard_towers)
    for i in range(l):
        for j in range(b):
            tiles[i, j].number_of_balloons = 0
    for B in balloons:
        if( B.x != -1 and B.y != -1 and B.target > 0 and B.targetx==B.x and B.targety==B.y and B.hp>0):
                damage(B.x,B.y,20,cannons,wizard_towers,huts,town_hall,walls)
        elif(B.x != -1 and B.y != -1 and B.target > 0 and B.hp>0):
            a = B.x-B.targetx
            if(a < 0):
                moda = -a
            else:
                moda = a
            b = B.y-B.targety
            if(b < 0):
                modb = -b
            else:
                modb = b
            if(moda > modb):
                Bx = B.x-int((a/moda))
                By = B.y
            if(moda < modb):
                Bx = B.x
                By = B.y-int((b/modb))
            if(moda == modb):
                Bx = B.x-int((a/moda))
                By = B.y-int((b/modb))
            B.x = Bx
            B.y = By
        if(B.hp>0):
           tiles[B.x, B.y].number_of_balloons = tiles[B.x,B.y].number_of_balloons+1
            
            # print("x")


def king_queen_position_update(p,a, king,queen, tiles, barbarians,archers,balloons, num):
    if(p=='1'):
        m = 0
        if(a == None):
            return
        if(a == 'a'):
            kingy = king.y-1
            kingx = king.x
            m = 1
        if(a == 'd'):
            kingy = king.y+1
            kingx = king.x
            m = 1
        if(a == 'w'):
            kingx = king.x-1
            kingy = king.y
            m = 1
        if(a == 's'):
            kingx = king.x+1
            kingy = king.y
            m = 1
        tiles[king.x, king.y].is_king = 0
        if(m == 1 and tiles[kingx, kingy].is_building == 0):
            king.x = kingx
            king.y = kingy
        tiles[king.x, king.y].is_king = 1
    if(p=='0'):
        m = 0
        if(a == None):
            return
        if(a == 'a'):
            queeny = queen.y-1
            queenx = queen.x
            queen.attack_direction='a'
            m = 1
        if(a == 'd'):
            queeny = queen.y+1
            queenx = queen.x
            queen.attack_direction='d'
            m = 1
        if(a == 'w'):
            queenx = queen.x-1
            queeny = queen.y
            queen.attack_direction='w'
            m = 1
        if(a == 's'):
            queenx = queen.x+1
            queeny = queen.y
            queen.attack_direction='s'
            m = 1
        tiles[queen.x, queen.y].is_queen = 0
        if(m == 1 and tiles[queenx, queeny].is_building == 0):
            queen.x = queenx
            queen.y = queeny
        tiles[queen.x, queen.y].is_queen = 1
    if(a == '1' and num[0] < 6):
        num[0] = release_barbarians(barbarians, tiles, num[0], 3, 5)
    if(a == '2' and num[0] < 6):
        num[0] = release_barbarians(
            barbarians, tiles, num[0], 24, 10)
    if(a == '3' and num[0] < 6):
        num[0] = release_barbarians(barbarians, tiles, num[0], 2, 48)
    if(a == '4' and num[1] < 6):
        num[1] = release_archers(archers, tiles, num[1], 15, 15)
    if(a == '5' and num[1] < 6):
        num[1] = release_archers(
            archers, tiles, num[1], 28, 2)
    if(a == '6' and num[1] < 6):
        num[1] = release_archers(archers, tiles, num[1], 8, 40)
    if(a == '7' and num[2] < 3):
        num[2] = release_balloons(balloons, tiles, num[2], 20,49)
    if(a == '8' and num[2] < 3):
        num[2] = release_balloons(
            balloons, tiles, num[2], 28, 30)
    if(a == '9' and num[2] < 3):
        num[2] = release_balloons(balloons, tiles, num[2], 6, 14)
    



def set_buildings(cannons,wizard_towers, huts, town_hall, tiles,walls):
    for C in huts:
        if(C.hp>0):
            tiles[C.x, C.y].is_building = 1
            tiles[C.x, C.y+1].is_building = 1
            tiles[C.x+1, C.y].is_building = 1
            tiles[C.x+1, C.y+1].is_building = 1
        else:
            tiles[C.x, C.y].is_building = 0
            tiles[C.x, C.y+1].is_building = 0
            tiles[C.x+1, C.y].is_building = 0
            tiles[C.x+1, C.y+1].is_building = 0
    for C in cannons:
        if(C.hp>0):
            tiles[C.x, C.y].is_building = 1
        if(C.hp<=0):
            tiles[C.x, C.y].is_building = 0
    for C in wizard_towers:
        if(C.hp>0):
            tiles[C.x, C.y].is_building = 1
        if(C.hp<=0):
            tiles[C.x, C.y].is_building = 0
    for C in walls:
        if(C.hp>0):
            tiles[C.x, C.y].is_building = 1
        if(C.hp<=0):
            tiles[C.x, C.y].is_building = 0
    if(town_hall.hp>0):
        a = town_hall.x
        b = town_hall.y
        tiles[a, b].is_building = 1
        tiles[a, b+1].is_building = 1
        tiles[a, b+2].is_building = 1
        tiles[a+1, b+1].is_building = 1
        tiles[a+2, b+1].is_building = 1
        tiles[a+3, b+1].is_building = 1
        tiles[a+1, b].is_building = 1
        tiles[a+2, b].is_building = 1
        tiles[a+3, b].is_building = 1
        tiles[a+1, b+2].is_building = 1
        tiles[a+2, b+2].is_building = 1
        tiles[a+3, b+2].is_building = 1
    if(town_hall.hp<=0):
        a = town_hall.x
        b = town_hall.y
        tiles[a, b].is_building = 0
        tiles[a, b+1].is_building = 0
        tiles[a, b+2].is_building = 0
        tiles[a+1, b+1].is_building = 0
        tiles[a+2, b+1].is_building = 0
        tiles[a+3, b+1].is_building = 0
        tiles[a+1, b].is_building = 0
        tiles[a+2, b].is_building = 0
        tiles[a+3, b].is_building = 0
        tiles[a+1, b+2].is_building = 0
        tiles[a+2, b+2].is_building = 0
        tiles[a+3, b+2].is_building = 0

def queen_attack(p,queen,huts,cannons,wizard_towers,town_hall,walls,n,d):
    if(p=='0'):
        if(queen.attack_direction=='a'):
            x=queen.x
            y=queen.y-d
        if(queen.attack_direction=='d'):
            x=queen.x
            y=queen.y+d
        if(queen.attack_direction=='w'):
            x=queen.x-d
            y=queen.y
        if(queen.attack_direction=='s'):
            x=queen.x+d
            y=queen.y
        AoE(p,huts,cannons,wizard_towers,town_hall,walls,n,queen.damage_rate,x,y)
def AoE(p,huts,cannons,wizard_towers,town_hall,walls,n,damage_rate,x,y):
    if(p=='0'):
        for H in huts:
            k=0
            for i in range(2):
                for j in range(2):
                    if(H.x+i>=x-n and H.x+i<=x+n and H.y+j>=y-n and H.y+j<=y+n and H.hp>0):
                        H.hp=H.hp-damage_rate
                        k=1    
                    if(k==1):
                        break
                if(k==1):
                    break
        for H in cannons:
            if(H.x>=x-n and H.x<=x+n and H.y>=y-n and H.y<=y+n and H.hp>0):
                H.hp=H.hp-damage_rate
        for H in wizard_towers:
            if(H.x>=x-n and H.x<=x+n and H.y>=y-n and H.y<=y+n and H.hp>0):
                H.hp=H.hp-damage_rate
        k=0
        for i in range(4):
            for j in range(3):
                if(town_hall.x+i>=x-n and town_hall.x+i<=x+n and town_hall.y+j>=y-n and town_hall.y+j<=y+n and town_hall.hp>0):
                    town_hall.hp=town_hall.hp-damage_rate
                    k=1
                if(k==1):
                    break
            if(k==1):
                break
        for H in walls:
            if(H.x>=x-n and H.x<=x+n and H.y>=y-n and H.y<=y+n and H.hp>0):
                H.hp=H.hp-damage_rate
                
            
            
        


def buildings_hp_update(p,barbarians, king,queen, tiles, huts, cannons,wizard_towers, town_hall,walls,leng,bred):
    for W in walls:
        if(W.hp<=0):
            tiles[W.x, W.y].is_building = 0
    for C in huts:
        if(C.hp>0):
            x = 0
            y = 0
            for i in range(-1, 3):
                for j in range(-1, 3):
                    x = x+tiles[C.x+i, C.y+j].number_of_barbarians
                    if(p=='1'):
                        y = y+tiles[C.x+i, C.y+j].is_king
            C.hp = C.hp-(x*barbarians[0].damage_rate+0*king.damage_rate)
            if(C.hp<=0):
                tiles[C.x, C.y].is_building = 0
                tiles[C.x, C.y+1].is_building = 0
                tiles[C.x+1, C.y].is_building = 0
                tiles[C.x+1, C.y+1].is_building = 0
    for C in cannons:
        if(C.hp>0): 
            x = 0
            y = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    x = x+tiles[C.x+i, C.y+j].number_of_barbarians
                    if(p=='1'):
                        y = y+tiles[C.x+i, C.y+j].is_king
            C.hp = C.hp-(x*barbarians[0].damage_rate+0*king.damage_rate)
            if(C.hp<=0):
                tiles[C.x, C.y].is_building = 0
    for C in wizard_towers: 
        if(C.hp>0):
            x = 0
            y = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    x = x+tiles[C.x+i, C.y+j].number_of_barbarians
                    if(p=='1'):
                        y = y+tiles[C.x+i, C.y+j].is_king
            C.hp = C.hp-(x*barbarians[0].damage_rate+0*king.damage_rate)
            if(C.hp<=0):
                tiles[C.x, C.y].is_building = 0
    # for C in walls:
    #     x = 0
    #     y = 0
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
    #             if(C.x+i>=0 and C.x+i<leng and C.y+i>=0 and C.y+i<bred):
    #                 # print(C.x," ",C.y)
    #                 x = x+tiles[C.x+i, C.y+j].number_of_barbarians
    #                 y = y+tiles[C.x+i, C.y+j].is_king
    #     C.hp = C.hp-(x*barbarians[0].damage_rate+y*king.damage_rate)
    #     if(C.hp<=0):
    #         tiles[C.x, C.y].is_building = 0
    if(town_hall.hp>0):
        x = 0
        y = 0
        for i in range(-1, 5):
            for j in range(-1, 4):
                x = x+tiles[town_hall.x+i, town_hall.y+j].number_of_barbarians
                if(p=='1'):
                    y = y+tiles[town_hall.x+i, town_hall.y+j].is_king
        town_hall.hp = town_hall.hp - \
            (x*barbarians[0].damage_rate+0*king.damage_rate)
        if(town_hall.hp<=0):
            a = town_hall.x
            b = town_hall.y
            tiles[a, b].is_building = 0
            tiles[a, b+1].is_building = 0
            tiles[a, b+2].is_building = 0
            tiles[a+1, b+1].is_building = 0
            tiles[a+2, b+1].is_building = 0
            tiles[a+3, b+1].is_building = 0
            tiles[a+1, b].is_building = 0
            tiles[a+2, b].is_building = 0
            tiles[a+3, b].is_building = 0
            tiles[a+1, b+2].is_building = 0
            tiles[a+2, b+2].is_building = 0
            tiles[a+3, b+2].is_building = 0
    # for i in range(-1,2):
    #     for j in range(-1,2):
    #         if(i== 0 or j==0):
    #             l=wall_damage(king.x+i,king.y+j,king.damage_rate,walls)
    #             if(l==1):
    #                 tiles[king.x+i,king.y+j].is_building=0
    #                 break
    #     if(l==1):
    #         break

def wall_hp_update(a,b,walls):
    for w in walls:
        if(w.x==a and w.y==b and w.hp>0):
            w.hp=w.hp-10
            # print("x")
            if(w.hp<=0):
                return 0
            else:
                return 1
def wall_hp_update_ar(a,b,walls):
    for w in walls:
        if(w.x==a and w.y==b and w.hp>0):
            w.hp=w.hp-20
            # print("x")
            if(w.hp<=0):
                return 0
            else:
                return 1
