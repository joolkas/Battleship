"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""


class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    # TODO: copy your Character class implementation from
    #       the previous assignment here and implement the
    #       following new methods.
    #
    #       Also note, that you have to modify at least
    #       __init__ and printout methods to conform with
    #       the new bahavior of the class.

    def __init__(self, title, points):

        if not isinstance(title, str):
            raise TypeError

        self.__title = title
        self.__DB = {}
        self.__index = 0
        self.__points = points

    def get_name(self):
        return self.__title

    def give_item(self, item):
        if item in self.__DB:
            self.__DB[item]+=1
        else:
            up_dict = {item:1}
            self.__DB.update(up_dict)

    def remove_item(self, item):
        if item in self.__DB:
            if self.__DB[item]>1:
                self.__DB[item]-=1
            else:
                del self.__DB[item]

    def printout(self):
        print("Name:", self.__title)
        print("Hitpoints:", self.__points)

        for element, idx in sorted(self.__DB.items()):
            print(" ", idx, element)

    def has_item(self, name):
        if name not in self.__DB:
            return False
        else:
            return True

    def how_many(self, itemName):
        if itemName in self.__DB:
            return self.__DB[itemName]
        else:
            return 0

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """
        if self.has_item(item):
            self.remove_item(item)
            target.give_item(item)

        # TODO: implementation of the method

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.


        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.
        """
        if weapon not in WEAPONS:
            print("Attack fails: unknown weapon \"", weapon, "\".", sep='')
        elif target == self:
            print("Attack fails:", self.__title, "can't attack him/herself.")
        elif not self.has_item(weapon):
            print("Attack fails: ", self.__title, " doesn't have \"", weapon, "\".", sep='')
        else:
            damage = WEAPONS[weapon]
            print(self.__title, "attacks", target.__title, "delivering", damage, "damage.")
            target.__points = target.__points - damage
            if target.__points <= 0:
                print(self.__title," successfully defeats ", target.__title,".", sep='')

        """
        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # TODO: the implementation of the method


WEAPONS = {
    # Weapon          Damage
    # --------------   ------
    "elephant gun": 15,
    "gun": 5,
    "light saber": 50,
    "sword": 7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword")  # Conan doesn't have a sword.
    conan.attack(conan, "gun")  # A character is not allowed to attack himself.
    conan.attack(conan, "pen")  # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")  # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword")  # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")  # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
