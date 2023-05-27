from py.class_setup import BasePiece, Player, Enemy
from py.save_manip import save, load

gameplay_stats = {
    'enemies_defeated' : 0,
    'kill_streak' : 0,
    'times_died' : 0
}

def menu():
    You = Player("", [100, 100], 5, 0, ['potion'], 200, 0, [1, 25, 0]) # name, hp (current, max), atk, status id, inventory, gold, buff, level (level, exp needed, current exp)
    print("Hello player, and welcome to this little RPG I've made!")
    You.name = input("What is your name, player? ")
    print(f"Alright, hello then, {You.name}!")

    print("Testing saving data...")
    try:
        save(You)
        print("All done! Check the json folder to see your data :3")
    
    except Exception as error:
        print(error)

    print("Let's get into the actual game now, yeah?")
    

    combat_loop(You)


def enemy_generation():
    pass


def combat_loop(player : object, enemy : object):
    pass

menu()
