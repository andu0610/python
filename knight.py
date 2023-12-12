from npc import NPC
from stats import *


class Knight(NPC):
    def __init__(self):
        super().__init__(NPCHealth.knightHealth,NPCDamage.knightDamage,NPCArmour.knightArmour,NPCMagic.knightMagic,NPCHunger.knightHunger, NPCMagicResistance.knightMagicRessistance)