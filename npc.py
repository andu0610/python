from npc_states import *


class NPC(object):
    def __init__(self, hp, damage, armour, magic, hunger):
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.magic = magic
        self.hunger = hunger
        self.alive = True

    def getstate(self):
        if self.alive:
            return NPCstates.ALIVE
        else:
            return NPCstates.DEAD

    def takeDamage(self, debuff, damage):
        state = self.getstate()
        if state == NPCstates.ALIVE:
            match debuff:
                case NPCdebuff.Burning:
                    self.hp -= damage
                    print("BURNING!!!")
                    return
                case NPCdebuff.Starving:
                    self.hp -= damage
                    print("STARVING!!!")
                    return
                case NPCdebuff.Poisoned:
                    self.hp -= damage
                    print("POISONED!!!")
                    return
                case _:
                    print("I am healthy")
                    return
