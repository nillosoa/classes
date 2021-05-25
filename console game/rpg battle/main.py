from classes.game import person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 624, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

#Create White Magic
cure = Spell("Cure", 25, 624, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 500, "white")

#Create some items
potion = Item("Potion", "potion", "Heals 50 HP.", 50)
hipotion = Item("HiPotion", "potion", "Heals 100 HP.", 100)
superpotion = Item("SuperPotion", "potion", "Heals 1000 HP.", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member.", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP.", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage.", 500)

#Instantiate People
player_magic = [fire, thunder, blizzard, meteor, curaga]
enemy_spells = [fire, meteor, cure]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 10},
                {"item": superpotion, "quantity": 3}, {"item": elixir, "quantity": 3},
                {"item": hielixir, "quantity": 2}, {"item": grenade, "quantity": 20}]

player1 = person("Valos:", 3260, 132, 300, 34, player_magic, player_items)
player2 = person("Nick :", 4160, 188, 300, 34, player_magic, player_items)
player3 = person("Robot:", 3089, 174, 288, 34, player_magic, player_items)

enemy1  = person("Imp   ", 1250, 130, 560, 325, enemy_spells, [])
enemy2  = person("Magnus", 11200, 701, 525, 25, enemy_spells, [])
enemy3  = person("Imp   ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=" * 10)
    print("\n\n")

    print("NAME                HP                                  MP")
    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose action:")
        print("\n")
        index = (int(choice) - 1)

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked", enemies[enemy].name.replace(" ", ""), "for", str(dmg), "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", ""), "has died.")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP.\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to", enemies[enemy].name.replace(" ", "") + "." + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", ""), "has died.")
                    del enemies[enemy]


        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item:")) - 1

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] <= 0:
                print(bcolors.FAIL + "\nNone left." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "points." + bcolors.ENDC)
            elif item.type == "elixir":

                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damange to", enemies[enemy].name.replace(" ", "") + "." + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", ""), "has died.")
                    del enemies[enemy]

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player or enemy won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + 'You Win' + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False

    # Enemy attack phase
    print("\n")
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        target = random.randrange(0, 3)

        if enemy_choice == 0:
            # Chose attack
            enemy_damage = enemies[0].generate_damage()

            players[target].take_damage(enemy_damage)
            print(bcolors.FAIL + enemy.name.replace(" ", "") + " attacks " +
                  players[target].name.replace(":", "").replace(" ", "") + " for " +  str(enemy_damage) + "." + bcolors.ENDC)
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.FAIL + enemy.name.replace(" ", "") + " heals for", str(magic_dmg), "HP with", spell.name + bcolors.ENDC)
            elif spell.type == "black":
                players[target].take_damage(magic_dmg)
                print(bcolors.FAIL + enemy.name.replace(" ", "") + " uses " + spell.name +
                      " dealing ", str(magic_dmg), "points of damage to", players[target].name.replace(":", "").replace(" ", "") + "." + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", ""), "has died.")
                    del players[target]
