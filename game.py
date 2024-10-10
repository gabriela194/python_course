import random 

from objects.hero_class import HeroFactory
from objects.inventory_class import Item

def game():
    hero_factory = HeroFactory()
    hero_classes = {1: "warrior", 2: "mage"}
    print("\nWelcome to the heroes versus monsters game! \nChoose your hero class (1, 2): ")
    
    for key in hero_classes.keys():
        print(key, ". ", hero_classes[key])

    while True:
        try:
            hero_class = hero_classes[int(input())]
            hero = hero_factory.create_hero(hero_class)
            break
        except (KeyError, ValueError):
            print("Invalid input. Please try again.")

    monsters_defeated = 0

    while monsters_defeated < 3:
        monster = hero_factory.create_monster()
        print(f"\nA dangerous {monster.monster_type} monster appears!")

        while True:  
            if hero.dead():
                print(f"\n{hero.hero_class.capitalize()} died :(Game Over.")
                return  

            if monster.dead():
                print(f"{monster.monster_type.capitalize()} monster is defeated!")
                print(f"Health of {hero.hero_class} is {hero.health}.")
                monsters_defeated += 1
                break  

            available_attacks = {1: "sword"}
            if hero.inventory.get("bow"):
                available_attacks[2] = "bow"
            if hero.inventory.get("spellbook"):
                available_attacks[3] = "magic"  

            print("\nChoose your attack type:")
            for key, value in available_attacks.items():
                print(key, ". ", value)

            while True:
                try:
                    attack_choice = int(input())
                    if attack_choice in available_attacks:
                        attack_type = available_attacks[attack_choice]
                        break
                    else:
                        print("Invalid choice. Please select a valid attack type.")
                except ValueError:
                    print("Invalid input. Please try again.")

            if hero_class == "warrior":
                    if attack_choice == 1:
                        damage = random.randint(hero.attack - 2, hero.attack)
                        print(f"\n{hero.hero_class.capitalize()} causes {damage} damage to the {monster.monster_type} monster.")
                        monster.damage_taken(damage)
                        print(f"Health of {monster.monster_type} is {monster.health}.")
                    elif attack_choice == 2:
                        damage = random.randint(hero.attack // 2, hero.attack)
                        print(f"\n{hero.hero_class.capitalize()} causes {damage} damage to the {monster.monster_type} monster.")
                        monster.damage_taken(damage)
                        print(f"Health of {monster.monster_type} is {monster.health}.") 
                    elif attack_choice == 3:
                        damage = random.randint(hero.attack // 3, hero.attack)
                        print(f"\n{hero.hero_class.capitalize()} causes {damage} damage to the {monster.monster_type} monster.")
                        monster.damage_taken(damage)
                        print(f"Health of {monster.monster_type} is {monster.health}.")  

            if hero_class == "mage":
                    if attack_choice == 1:
                        damage = random.randint(hero.attack // 3, hero.attack)
                        print(f"\n{hero.hero_class.capitalize()} causes {damage} damage to the {monster.monster_type} monster.")
                        monster.damage_taken(damage)
                        print(f"Health of {monster.monster_type} is {monster.health}.")
                    elif attack_choice == 2:
                        damage = random.randint(hero.attack // 2, hero.attack)
                        print(f"\n{hero.hero_class.capitalize()} causes {damage} damage to the {monster.monster_type} monster.")
                        monster.damage_taken(damage)
                        print(f"Health of {monster.monster_type} is {monster.health}.") 
                    elif attack_choice == 3:
                        damage = random.randint(hero.attack - 2, hero.attack)
                        print(f"\n{hero.hero_class.capitalize()} causes {damage} damage to the {monster.monster_type} monster.")
                        monster.damage_taken(damage)
                        print(f"Health of {monster.monster_type} is {monster.health}.")                 

            if monster.dead():
                continue  

            damage = random.randint(monster.attack // 2, monster.attack)
            print(f"{monster.monster_type.capitalize()} monster causes {damage} damage to {hero.hero_class}.")
            hero.damage_taken(damage)
            print(f"Health of {hero.hero_class} is {hero.health}.")

            if hero.dead():
                print(f"\n{hero.hero_class.capitalize()} died :( Game Over.")
                return 

    print("\nCongratulations! You defeated all the monsters!")