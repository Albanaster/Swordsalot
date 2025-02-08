

class Entity:
    HP = 0
    def __init__(self, HP:int, SPD:int):
        self.HP = HP
        self.SPD = SPD

class Player(Entity):
    pass

class Enemy(Entity):
    pass

class NPC(Entity):
    pass