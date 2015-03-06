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

class checkin:
    u, d, l, r = True, True, True, True

def check(i, j, ch):
    if abs(i) + abs(j) < 2:
        if i > 0:
            ch.d = False
                            
        if i < 0:
            ch.u = False
                        
        if j > 0:
            ch.r = False       
                        
        if j < 0:
            ch.l = False  

def clean(printed, panel, health_pan, mana_pan, stamina_pan, knight, right_hand):
    panel.delete(health_pan)
    panel.delete(mana_pan)
    panel.delete(stamina_pan)
    panel.delete(right_hand)    
    
    for i in range(len(knight.printed_loot)):
        panel.delete(knight.printed_loot[i])
    
    for i in range(len(printed)):
        panel.delete(printed[i])
    
    printed = [] 
    return printed, panel

def repaint(knight, panel, level, ch, health_pan, mana_pan, stamina_pan, v_loot, printed, images, floar, stone, r_h):
    
    printed, panel = clean(printed, panel, health_pan, mana_pan, stamina_pan, knight, r_h)
    
    health_pan = panel.create_rectangle(347, 149, 333, 63 + ((100 - knight.health )/ 100) * 86, fill="red")
    mana_pan = panel.create_rectangle(379, 149, 365, 63 + ((100 - knight.mana )/ 100) * 86, fill="blue")
    stamina_pan = panel.create_rectangle(411, 149, 399, 63 + ((100 - knight.stamina )/ 100) * 86, fill="green")    
    ch = checkin() 
    
    if knight.right_hand != None:
        r_h = panel.create_text(270, 220, text=knight.right_hand.name, fill="blue", anchor=NW)        
    
    for i in range(len(knight.loot)):
        knight.printed_loot.append(panel.create_image(222 + 17 * i, 166, anchor=NE, image=v_loot[knight.loot[i].image]))
        
    
    for i in range(-5, 6):
        for j in range(-5, 6):
            x = 107 + j * 16
            y = 91 + i * 16
            if level[knight.y + i][knight.x + j] == '.':
                printed.append(panel.create_image(x, y, anchor=NE, image=images[floar]))
            if level[knight.y + i][knight.x + j] == 'K':
                printed.append(panel.create_image(x, y, anchor=NE, image=images[floar]))
                check(i, j, ch)
                printed.append(panel.create_image(x, y, anchor=NE, image=images[8]))                    
            if level[knight.y + i][knight.x + j] == '#':                   
                check(i, j, ch)
                printed.append(panel.create_image(x, y, anchor=NE, image=images[stone]))
            if level[knight.y + i][knight.x + j] == '_':  
                printed.append(panel.create_image(x, y, anchor=NE, image=images[5]))                
            if i == 0 and j == 0:
                printed.append(panel.create_image(x, y, anchor=NE, image=images[1]))
            if level[knight.y + i][knight.x + j] == 'T':
                printed.append(panel.create_image(x, y, anchor=NE, image=images[floar]))                
                check(i, j, ch)
                printed.append(panel.create_image(x, y, anchor=NE, image=images[3]))
            if level[knight.y + i][knight.x + j] == '>':
                printed.append(panel.create_image(x, y, anchor=NE, image=images[stone]))                
                check(i, j, ch)                
                printed.append(panel.create_image(x, y, anchor=NE, image=images[4]))  
            if level[knight.y + i][knight.x + j] == 'F':
                printed.append(panel.create_image(x, y, anchor=NE, image=images[floar])) 
                check(i, j, ch)
                printed.append(panel.create_image(x, y, anchor=NE, image=images[11]))   
                
    return printed, ch, knight, health_pan, mana_pan, stamina_pan, r_h
