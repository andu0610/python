from archer import Archer
from knight import Knight
from pykeman import Pykeman
from wizard import Wizard

def game():
    knight=Knight()
    archer = Archer()
    pykeman = Pykeman()
    wizard = Wizard()


    print(f"stats knight --> HP:{knight.hp}, DMG:{knight.damage}, ARMOUR:{knight.armour}, MAGIC:{knight.magic}, HUNGER:{knight.hunger}")



if __name__=="__main__":
    game()