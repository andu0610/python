from npc_states import *
from stats import *

class NPC(object):

    def __init__(self, hp, damage, armour, magic, hunger, magic_resistance):
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.magic = magic
        self.hunger = hunger
        self.magic_resistance = magic_resistance
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
                    self.hp -=NPCDeBuffDamage.fireDamage
                    print("BURNING!!!")
                    return
                case NPCdebuff.Starving:
                    self.hp -=NPCDeBuffDamage.starvingDamage
                    print("STARVING!!!")
                    return
                case NPCdebuff.Poisoned:
                    self.hp -=NPCDeBuffDamage.poisonDamage
                    print("POISONED!!!")
                    return
                case _:
                    print("I am healthy")
                    return
