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

class sword:
    damage = None
    health = None
    image = None    
    itype = 'sword'
    name = None
    
    def __init__(self, damage, health, image, name):
        self.damage = damage
        self.health = health
        self.image = image
        self.name = name
        
class heal:
    heal = None
    image = None
    itype = 'heal'
    
    def __init__(self, heal, image):
            self.heal = heal 
            self.image = image

class helmet:
    armory = None
    name = None
    itype = "helmet"
    image = None
    health = None
    
    def __init__(self, armor, health, image, name):
        self.armory = armor
        self.name = name
        self.image = image
        self.health = health
        
def lvl(const):
    if const == 1:
        
        f_r = open('./levels/level_1.txt', 'r')
        lvl1 = []
        
        for i in range(25):
            lvl1.append(list(f_r.readline()))
        
        f_r.close()
        return lvl1, 5, 12, [[17, 5, sword(20, 50, 0, "usual sword")], [17, 19, heal(50, 1)]], (-1, -1), (18, 12), 2, 0
    elif const == 2:
        
        f_r = open('./levels/level_2.txt', 'r')
        lvl2 = []
                
        for i in range(25):
            lvl2.append(list(f_r.readline()))
                
        f_r.close()        
        return lvl2, 5, 12, [], (4, 12), (11, 20), 6, 7
    elif const == 3:
        
        f_r = open('./levels/level_3.txt', 'r')
        lvl3 = []
                        
        for i in range(25):
            lvl3.append(list(f_r.readline()))
                        
        f_r.close()          
        return lvl3, 6, 5, [[5, 19, helmet(10, 100, 2, "usual helmet")]], (6, 4), (6, 20), 9, 10     

