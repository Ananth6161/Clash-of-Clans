from colorama import Fore, Back, Style
import numpy as np
import os
import time
from src.buildings import Building, Town_Hall, Hut, Wall, Cannon,Wizard_Tower
from src.troops import Attackers, Barbarians, King,Archers,Balloons,Queen
from src.tiles import Tile
from src.changes import set_colors
from src.input import *
from src.utils import *
l = 30
b = 50
level=1
health=100
h=[0,0,0]
print("enter which charachter u would like to select to play \nenter 1 for king and 0 for queen:",end="")
p=input()
print(Back.BLACK+"\n", end="")
os.system('clear')
print(" ")
king = King(1000, l-1, int(b/2))
queen=Queen(900, l-1, int(b/2))
tiles = np.empty((l, b), dtype=object)
for i in range(l):
    for j in range(b):
        tiles[i, j] = Tile("BLUE", i, j)
num=[0,0,0]
barbarians = np.array([Barbarians(250, -1, -1) for _ in range(6)])
archers = np.array([Archers(125, -1, -1) for _ in range(6)])
balloons = np.array([Balloons(250, -1, -1) for _ in range(3)])
walls = np.array([Wall(100, _ ,8) for _ in range(l)])
tiles[3, 5].color = "CYAN"
tiles[24, 10].color = "CYAN"
tiles[2, 48].color = "CYAN"
tiles[15,15].color="CYAN"
tiles[28,2].color="CYAN"
tiles[8,40].color="CYAN"
tiles[20,49].color="CYAN"
tiles[28,30].color="CYAN"
tiles[6,14].color="CYAN"
huts = np.empty((6), dtype=object)
huts[0] = Hut(250, int((3*l)/8), int(b/4)-2, 0)
huts[1] = Hut(250, int((5*l)/8), int(b/4), 1)
huts[2] = Hut(250, int(l/4), int(b/2), 2)
huts[3] = Hut(250, int((3*l)/4), int(b/2), 3)
huts[4] = Hut(250, int((3*l)/8), int((3*b)/4), 4)
huts[5] = Hut(250, int((5*l)/8), int((3*b)/4), 5)
cannons = np.empty((6), dtype=object)
cannons[0] = Cannon(300, 16, 5, 30, 0)
cannons[1] = Cannon(300, 12, 34, 30, 1)
cannons[2] = Cannon(300, 22, 32, 30, 2)
cannons[3] = Cannon(300, 28, 40, 30, 3)
cannons[4] = Cannon(0, 12, 3, 30, 4)
cannons[5] = Cannon(0, 1, 12, 30, 5)
wizard_towers = np.empty((4), dtype=object)
wizard_towers[0] = Wizard_Tower(300, 15,35, 30, 0)
wizard_towers[1] = Wizard_Tower(300, 22, 22, 30, 1)
wizard_towers[2] = Wizard_Tower(0, 4,44, 30, 2)
wizard_towers[3] = Wizard_Tower(0, 10, 4, 30, 3)
town_hall = Town_Hall(350, int(l/2)-2, int(b/2)-2)
set_buildings(cannons,wizard_towers, huts, town_hall, tiles,walls)
set_colors(p,huts,queen, king, town_hall, tiles, cannons,wizard_towers,walls , l, b)
print_in_terminal(tiles, l, b)
while(1):
    func = Get().__call__
    a = input_to(func)
    if(a == 'q'):
        break
    cannons_reset(cannons)
    wizard_towers_reset(wizard_towers)
    set_buildings(cannons,wizard_towers, huts, town_hall, tiles,walls)
    king_queen_position_update(p,a, king,queen, tiles, barbarians,archers,balloons, num)
    king_queen_hp_update(p,king,queen, cannons)
    barbarian_position_update(barbarians, tiles, huts,
                              town_hall, cannons,wizard_towers,walls, l, b)
    archer_position_update(archers, tiles, huts,
                              town_hall, cannons,wizard_towers,walls, l, b)
    balloon_position_update(balloons, tiles, huts,
                              town_hall, cannons,wizard_towers,walls, l, b)
    troops_hp_update(barbarians,archers,balloons, cannons,wizard_towers,king,queen,p)
    buildings_hp_update(p,barbarians, king,queen, tiles, huts, cannons,wizard_towers, town_hall,walls,l,b)
    if(a=='b'):
        queen_attack(p,queen,huts,cannons,wizard_towers,town_hall,walls,2,8)
    if(a==' '):
        if(p=='1'):
            AoE('0',huts,cannons,wizard_towers,town_hall,walls,1,king.damage_rate,king.x,king.y)
    if(a=='c'):
        h[2]=1
    else:
        h[2]=0
    if(h[0]==1):
        queen_attack(p,queen,huts,cannons,wizard_towers,town_hall,walls,4,16)
    set_colors(p,huts,queen, king, town_hall, tiles, cannons,wizard_towers,walls , l, b)
    print_changes(tiles, l, b,cannons,wizard_towers)
    h[0]=h[1]
    h[1]=h[2]
    if(p=='1'):
        health=king.hp/10
    if(p=='0'):
        health=queen.hp/9
    print(" LEVEL: ",level,"                                                                                                                                                                              HEALTH: ",health,"%")
    if(endings(barbarians, king,queen,archers,balloons, huts, cannons, town_hall,wizard_towers,p) == 1):
        if(level==1):
            reset(huts,cannons,walls,wizard_towers,town_hall,barbarians,king,queen,balloons,archers,l,b)
            cannons[5].hp=0
            wizard_towers[3].hp=0
            num=[0,0,0]
            print("")
            set_buildings(cannons,wizard_towers, huts, town_hall, tiles,walls)
            set_colors(p,huts,queen, king, town_hall, tiles, cannons,wizard_towers,walls , l, b)
            print_in_terminal(tiles, l, b)
        if(level==2):
            reset(huts,cannons,walls,wizard_towers,town_hall,barbarians,king,queen,balloons,archers,l,b)
            num=[0,0,0]
            print("")
            set_buildings(cannons,wizard_towers, huts, town_hall, tiles,walls)
            set_colors(p,huts,queen, king, town_hall, tiles, cannons,wizard_towers,walls , l, b)
            print_in_terminal(tiles, l, b)
        if(level==3):
            print("_____________VICTORY!!!!!!!_____________")
            break
        level=level+1
    if(endings(barbarians, king,queen,archers,balloons, huts, cannons, town_hall,wizard_towers,p) == 0):
        print("_____________YOU HAVE BEEN DEFEATED!!!!!!_____________")
        break
    time.sleep(0.5)
