# heroes
    # warrior, mage
# monsters 
    # ogre, dragon

# defining class Character

class Character:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def damage_taken(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def dead(self):
        return self.health == 0

# defining subclass Hero within Character

class Hero(Character):
    def __init__(self, hero_class, health, attack):
        super().__init__(health, attack)
        self.hero_class = hero_class
        self.inventory = {"sword": True, "bow": True, "spellbook": True}

    def pick_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            raise ValueError("Invalid item")

# defining subclasses within Hero

class Warrior(Hero):
    def __init__(self):
        super().__init__("warrior", 40, 10)

class Mage(Hero):
    def __init__(self):
        super().__init__("mage", 40, 20)

# defining subclass Monster within Character

class Monster(Character):
    def __init__(self, monster_type, health, attack):
        super().__init__(health, attack)
        self.monster_type = monster_type

# defining subclasses within Monster

class Ogre(Monster):
    def __init__(self):
        super().__init__("ogre", 20, 12)

class Dragon(Monster):
    def __init__(self):
        super().__init__("dragon", 20, 10)




