from npc import NPC
from stats import *

class Archer(NPC):
    def __init__(self):
        super().__init__(NPCHealth.archerHealth,NPCDamage.archerDamage,NPCArmour.archerArmour,NPCMagic.archerMagic,NPCHunger.archerHunger, NPCMagicResistance.archerMagicRessistance)