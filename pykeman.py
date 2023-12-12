from npc import NPC
from stats import *


class Pykeman(NPC):
    def __init__(self):
        super().__init__(NPCHealth.pykemanHealth,NPCDamage.pykemanDamage,NPCArmour.pykemanArmour,NPCMagic.pykemanMagic,NPCHunger.pykemanHunger, NPCMagicResistance.pykemanMagicRessistance)