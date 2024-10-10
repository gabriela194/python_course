import random
from typing import Any

from objects.create_class import AbstractFactory
from objects.character_class import Warrior, Mage, Ogre, Dragon

class HeroFactory(AbstractFactory):
    def create_hero(self, hero_class) -> Any:
        if hero_class not in ["warrior", "mage"]:
            raise ValueError("Invalid hero class")
        elif hero_class == "warrior":
            return Warrior()
        elif hero_class == "mage":
            return Mage()

    def create_monster(self) -> Any:
        monster_type = random.choice(["ogre", "dragon"])
        if monster_type == "ogre":
            return Ogre()
        elif monster_type == "dragon":
            return Dragon()