import inquirer
from name_generator import penguin, dragon_name


while True:
    name = input("Enter name:")
    if name.lower() == 'exit':
        quit()

    month = input("Month of birth (e.g. January)")
    if month.lower() == 'exit':
        quit()

    # if name.lower().strip() == "exit":
    #     print("Bye")
    #     exit_game = True
    # else: pass


    drag_or_peng = input("Would you like to be a dragon or penguin? Enter D for dragon and P for penguin. If you dont I will feed you to my dragon.")
    if drag_or_peng == 'exit':
        quit().lower()

    if drag_or_peng == "D":
        print(dragon_name(name, month))
    else:
        print(penguin(name,month))

    # check = input("Do you want to leave?")
    # if check == "exit":
    #     exit_game= True
    # else:
    #     exit_game= False
    

