
from knight import Knight


from npc_states import *


def game():
    knight = Knight()


    print(f"stats knight --> HP:{knight.hp}, DMG:{knight.damage}, ARMOUR:{knight.armour}, MAGIC:{knight.magic}, HUNGER:{knight.hunger}, MANA:{knight.mana}")

    knight.takeDamage(NPCdebuff.Burning)

    print(f"stats knight --> HP:{knight.hp}, DMG:{knight.damage}, ARMOUR:{knight.armour}, MAGIC:{knight.magic}, HUNGER:{knight.hunger}, MANA:{knight.mana}")

    knight.healing()

    print(f"stats knight --> HP:{knight.hp}, DMG:{knight.damage}, ARMOUR:{knight.armour}, MAGIC:{knight.magic}, HUNGER:{knight.hunger}, MANA:{knight.mana}")


if __name__ == "__main__":
    game()
