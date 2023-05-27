from py.class_setup import Player, Enemy
from py.save_manip import file_save, file_load
from os import listdir
from json import load
from random import randint

gameplay_stats = {
    'enemies_defeated' : 0,
    'kill_streak' : 0,
    'times_died' : 0,
    'unlocked_areas' : ['forest']
}

You = Player("", [50, 50], 7, 0, ['potion'], 250, 0, [1, 25, 0]) # name, hp (current, max), atk, status id, inventory, buff, level (level, exp needed, current exp)

def menu():
    opt = ""
    while True:
        print("[New Game] or [Load] player data?")
        opt = input("Input: ").lower()

        match opt:
            case 'new game':
                name = input("Enter name: ").lower()
                global You
                You.name = name
                print("Testing saving file... ")
                print(file_save(You, gameplay_stats))
                hub()
            case 'load':
                name = input("Enter name: ").lower()
                print("Attempting to load player data... ")
                try:
                    player_dict = file_load(name)[0]
                    You = Player(player_dict['name'], player_dict['hp'], player_dict['atk'], player_dict['status'], player_dict['inventory'], player_dict['gold'], player_dict['buff'], player_dict['level'])
                    hub()
                except UnboundLocalError:
                    print("Save data not found. Check for spelling errors!")



def hub():
    while True:
        print("\nYou are currently in a small town. Would you like to visit the [shop], go [explore], or go [home]?")
        visit = input("Input: ").lower()
        match visit:
            case 'shop':
                print("lower is working :3")
            case 'explore':
                if You.hp[0] <= 0:
                    print("You need to heal up first. Head [home] to do so!")
                else:
                    print("\n ok im gonna put u in forest cuz i gotta debug thanks bbgorl")
                    area = 'forest'
                    CurrentEnemy = enemy_generation(area)
                    combat_loop(You, CurrentEnemy)
            case 'home':
                You.hp[0] = You.hp[1]
                print("\nYou go home and your mother feeds you the most scrumptious meal of your life. Your health is now full!")



def enemy_generation(area : str):
    for filename in listdir("./json"):
        filename = str(filename)
        if area in filename.lower():

            with open(f"json/{filename}", "r") as save_data:
                save_data = load(save_data)    

    enemy = randint(0, 50)
    enemy_dict = save_data[enemy]
    CurrentEnemy = Enemy(enemy_dict['name'], enemy_dict['hp'], enemy_dict['atk'], enemy_dict['status'])

    return CurrentEnemy


def combat_loop(player : object, enemy : object):
    action = ""
    earned_exp = round((enemy.hp[1] + enemy.atk)/3)
    while True:
        print(f"\nYou are fighting a {enemy.name}.")
        action = input("What do you want to do? [attack, inspect, use item] ")
        match action:
            case 'attack':
                print(player.attack(enemy))
                
        if enemy.hp[0] <= 0:
            print(f"\n{player.name} has successfully defeated the {enemy.name} and earned {earned_exp} EXP!")
            player.level[2] += earned_exp
            player.level_up()
            break
        elif enemy.status != 0:
            print(f"\nThe {enemy.name} is unable to attack!")
        else:
            print(enemy.attack(player))

        if player.hp[0] <= 0:
            print(f"\n{player.name} has been defeated... Heading back to the town now.")

menu()
