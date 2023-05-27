from json import dump, load
from os import listdir, remove

def file_save(player : object, gameplay : dict):
    player_dict = vars(player)
    player_name = player.name.lower()

    with open(f"json/saves/{player_name}.json", "w") as save_data:
        save_data.write('[ \n')
        dump(player_dict, save_data)
        save_data.write(', \n')
        dump(gameplay, save_data)
        save_data.write('\n ]')
    
    return f"Data of '{player_name}' successfully saved to json/saves/{player_name}.json!"


def file_load(player_name : str):
    player_name = player_name.lower()

    for filename in listdir("./json"):
        filename = str(filename)
        if player_name in filename.lower():

            with open(f"json/saves/{player_name}.json", "r") as save_data:
                player_dict = load(save_data)

    return player_dict, f"Data of '{player_name}' successfully loaded from json/saves/{player_name}.json!"


def file_delete(player_name : str):
    player_name = player_name.lower()

    for filename in listdir("./json/saves"):
        filename = str(filename)
        if player_name in filename.lower():

            while True:
                double_check = input(f"Are you sure you want to delete the data of '{player_name}? Y/N")

                if double_check.upper() == "Y":

                    while True:
                        double_check = input(f"Type in '{player_name}' to fully confirm. Type 'cancel' to cancel.")
                        if double_check == player_name:
                            remove(f"json/saves/{player_name}.json")
                            return f"Data of '{player_name}' has successfully been deleted."                
                        elif double_check == "cancel":
                            return 0
                        
                elif double_check.upper() == "N":
                    return 0
                    
