""" "Legend of ponomar" - a rpg
Copyright (C) 2015 Alex Ponomarev

Это свободная программа; вы можете повторно распространять ее и/или
модифицировать ее в соответствии с Универсальной Общественной Лицензией
GNU, опубликованной Фондом Свободного ПО; либо версии 2, либо (по вашему
выбору) любой более поздней версии.

Эта программа распространяется в надежде, что она будет полезной, но БЕЗ
КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемых гарантий КОММЕРЧЕСКОЙ
ЦЕННОСТИ или ПРИГОДНОСТИ ДЛЯ КОНКРЕТНОЙ ЦЕЛИ.  Для получения подробных
сведений смотрите Универсальную Общественную Лицензию GNU.

Вы должны были получить копию Универсальной Общественной Лицензии GNU
вместе с этой программой; если нет, напишите в Free Software Foundation,
Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"""

from tkinter import *
from level import *
from  repaint import *
import math, threading, time

def update():
    global printed, ch, knight, health_pan, mana_pan, stamina_pan, images, floar, right_hand
    
    printed, ch, knight, health_pan, mana_pan, stamina_pan, right_hand =  repaint(knight, panel, level, ch, health_pan, mana_pan, stamina_pan, v_loot, printed, images, floar, stone, right_hand)

class mob:
    global knight, level
    health = 50
    x, y = None, None
    
    def __init__(self, x, y):
        while self.health > 0:
            while abs(knight.x - end[0]) + abs(knight.y - end[1]) <= 2:
                return

class hero:
    global check_u, check_d, check_l, check_r
    
    helmet = None
    armory = None
    boats = None
    left_hand = None
    right_hand = None
    
    armor = 0
    health = 100
    mana = 100
    damage = 10
    stamina = 100
    loot = []
    printed_loot = []
    level = 1
    levels_gone = [None] * 100
    x, y = None, None
    
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
    
    def up(self, event):
        if ch.u and self.stamina > 0:
            self.y -= 1
            self.stamina -= 1
        update()
        
    def down(self, event):
        if ch.d and self.stamina > 0:
            self.y += 1
            self.stamina -= 1
            
        update()
        
    def left(self, event):
        if ch.l and self.stamina > 0:
            self.x -= 1
            self.stamina -= 1
            
        update()
        
    def right(self, event):
        if ch.r and self.stamina > 0:
            self.x += 1
            self.stamina -= 1
            
        update()
    def relax(self, event):
        self.stamina = min(100, self.stamina + 5)
        update()
    
    def interact(self, event):
        delete = []
        global level, x, y, chests, start, end, floar, stone
        
        if abs(self.x - end[0]) + abs(self.y - end[1]) <= 1:
            self.levels_gone[self.level] = [level, self.x, self.y, chests, start, end, floar, stone]
            level, x, y, chests, start, end, floar, stone = lvl(self.level + 1)
            self.x = x
            self.y = y
            self.level += 1
            
            time.sleep(0.5)
            return update()
        
        if abs(self.x - start[0]) + abs(self.y - start[1]) <= 1:                    
            level, x, y, chests, start, end, floar, stone = self.levels_gone[self.level - 1]
            self.x = x
            self.y = y
            self.level -= 1
            
            time.sleep(0.5)
            return update()        
        
        for i in range(len(chests)):
            if abs(self.x - chests[i][0]) + abs(self.y - chests[i][1]) <= 1:
                for j in range(2, len(chests[i])):
                    if len(self.loot) < 12:
                        self.loot.append(chests[i][j])
                        delete.append((i, j))
                        
        for i in delete:
            del(chests[i[0]][2])
            
        update()
        
    def using(self, event):
        if int(event.keysym) <= len(self.loot):
            if self.loot[int(event.keysym) - 1].itype == "sword":
                if self.right_hand == None:
                    self.right_hand = self.loot[int(event.keysym) - 1]
                    del(self.loot[int(event.keysym) - 1])
                    self.damage += self.right_hand.damage
                    print(self.damage)
                else:
                    self.damage -= self.right_hand.damage
                    self.loot.append(self.right_hand)
                    self.right_hand = self.loot[int(event.keysym) - 1]                    
                    del(self.loot[int(event.keysym) - 1])
                    self.damage += self.right_hand.damage
                    print(self.damage)   
            elif self.loot[int(event.keysym) - 1].itype == "helmet":
                if self.helmet == None:
                    self.helmet = self.loot[int(event.keysym) - 1]
                    del(self.loot[int(event.keysym) - 1])
                    self.armor += self.helmet.armory
                    print(self.armor)
                else:
                    self.armor -= self.helmet.armory
                    self.loot.append(self.helmet)
                    self.helmet = self.loot[int(event.keysym) - 1]                    
                    del(self.loot[int(event.keysym) - 1])
                    self.armor += self.helmet.armory
                    print(self.armor)   
            elif self.loot[int(event.keysym) - 1].itype == "heal":
                self.health = min(100, self.health + self.loot[int(event.keysym) - 1].heal)
                del(self.loot[int(event.keysym) - 1])
                    
        update()
        
root = Tk()
root.title("LEGEND OF PONOMAR 2")
root.resizable(width=False, height=False)

panel = Canvas(root, width = 430, height = 280)
panel.create_rectangle(10, 10, 186, 186, fill="black")
panel.grid(row=1,column=0)

images = [PhotoImage(file="src/stones/stone.gif"), #0
          PhotoImage(file="src/mobs/hero.gif"),    #1
          PhotoImage(file="src/floar/floar.gif"),  #2
          PhotoImage(file="src/loot/chest.gif"),   #3
          PhotoImage(file="src/doors/door.gif"),   #4
          PhotoImage(file="src/floar/road.gif"),   #5
          PhotoImage(file="src/floar/floar1.gif"), #6
          PhotoImage(file="src/stones/skull.gif"), #7
          PhotoImage(file="src/floar/fire.gif"),   #8
          PhotoImage(file="src/floar/floar2.gif"), #9
          PhotoImage(file="src/stones/stone2.gif"),#10
          PhotoImage(file="src/floar/fontan.gif"), #11
          PhotoImage(file="src/loot/helmet.gif")   #12
          ]

v_loot = [PhotoImage(file="src/loot/sword1.gif"), 
          PhotoImage(file="src/loot/health1.gif"),
          PhotoImage(file="src/loot/helmet.gif")]

img = PhotoImage(file="src/system/char.gif")
panel.create_image(420, 10, anchor=NE, image=img)
printed = []

level, x, y, chests, start, end, floar, stone = lvl(1)
knight = hero(x, y)

health_pan, mana_pan, stamina_pan = None, None, None

img1 = PhotoImage(file="src/system/slot.gif")
panel.create_image(410, 165, anchor=NE, image=img1)

ch = checkin() 
panel.create_text(10, 200, text="Helmet: ", anchor=NW)
panel.create_text(10, 220, text="Armory: ", anchor=NW)
panel.create_text(10, 240, text="Boots: ", anchor=NW)
panel.create_text(10, 260, text="Jewel: ", anchor=NW)
panel.create_text(195, 200, text="Left hand: ", anchor=NW)
panel.create_text(195, 220, text="Right hand: ", anchor=NW)
panel.create_text(195, 240, text="Bow: ", anchor=NW)
right_hand = None
update()

root.bind('<e>', knight.interact)
root.bind('<r>', knight.relax)
root.bind('<d>', knight.right)
root.bind('<a>', knight.left)
root.bind('<s>', knight.down)
root.bind('<w>', knight.up)
root.bind("<KeyPress-1>", knight.using)
root.bind('<KeyPress-2>', knight.using)
root.bind('<KeyPress-3>', knight.using)
root.bind('<KeyPress-4>', knight.using)
root.bind('<KeyPress-5>', knight.using)
root.bind('<KeyPress-6>', knight.using)
root.bind('<KeyPress-7>', knight.using)
root.bind('<KeyPress-8>', knight.using)
root.bind('<KeyPress-9>', knight.using)

root.mainloop()