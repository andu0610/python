from enum import auto, Enum


class NPCstates(Enum):
    ALIVE = auto()
    DEAD = auto()


class NPCeffects(Enum):
    Frozen = auto()
    Starving = auto()
    Stunned = auto()
    Rage = auto()
    healing = auto()


class NPCdebuff(Enum):
    Starving = auto()
    Poisoned = auto()
    Burning = auto()
