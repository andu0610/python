from npc import NPC
from stats import *

class Wizard(NPC):
    def __init__(self):
        super().__init__(NPCHealth.wizardHealth,NPCDamage.wizardDamage,NPCArmour.wizardArmour,NPCMagic.wizardMagic,NPCHunger.wizardHunger, NPCMagicResistance.wizardMagicRessistance, NPCMana.wizardMana)