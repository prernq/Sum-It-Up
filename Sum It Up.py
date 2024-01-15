#Date: 2019-12-17
#Description: A game where the user plays against the computer where 4 die are rolled, in which 2 are chosen to create a sum and fill a slot of a rack. The fastest player to fill their rack wins.
#Test Cases: Spent a lot of time trying to error check the game. Gave the game to different students in class to see if they could properly use it from a user standpoint.
#           Asked if they ran into any errors or whether there any way it can make the game better. Feedback was record, and worked on the next day.


#main lists

rack_slots = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
user_rack = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#index        0    1    2    3    4    5    6    7    8    9    10   11   12   13   14
#rack no.     2    3    4    5    6    7    8    9    10   11   12   13   14   15   16
comp_rack = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


#functions begin here
def start_up():
    from time import sleep
    sleep(0.2)
    print("L", end ="")
    sleep(0.2)
    print("O", end ="")
    sleep(0.2)
    print("A", end ="")
    sleep(0.2)
    print("D", end ="")
    sleep(0.2)
    print("I", end ="")
    sleep(0.2)
    print("N", end ="")
    sleep(0.2)
    print("G", end ="")
    sleep(0.2)
    print(".", end ="")
    sleep(0.2)
    print(".", end ="")
    sleep(0.2)
    print(".\n")
    print('                                                                        _______')
    print('███████╗██╗   ██╗███╗   ███╗    ██╗████████╗    ██╗   ██╗██████╗       /\ o o o\'')
    print('██╔════╝██║   ██║████╗ ████║    ██║╚══██╔══╝    ██║   ██║██╔══██╗     /o \ o o o\_______')
    print('███████╗██║   ██║██╔████╔██║    ██║   ██║       ██║   ██║██████╔╝    (    )------)   o /|')
    print('╚════██║██║   ██║██║╚██╔╝██║    ██║   ██║       ██║   ██║██╔═══╝      \ o/  o   /_____/o|')
    print('███████║╚██████╔╝██║ ╚═╝ ██║    ██║   ██║       ╚██████╔╝██║           \/______/     |oo|')
    print('╚══════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝   ╚═╝        ╚═════╝ ╚═╝                 |   o   |o/')
    print('                                                                             |_______|/')
    print('\nWelcome to Sum it Up!!')
    rules()
    


def rules():
    print("\nThe rules are as follows:")
    print("The objective of the game is to fill up every slot within your rack before the computer does, in order to win the game.")
    print("1) Once you begin, you will be prompted to roll 4 die.")
    print("2) From the die you rolled, choose 2 different die that add up to one of the unfilled slots on your rack.")
    print("3) Pick the die by entering a number according to the order it was rolled.")
    print("4) If you are able to choose 2 die that add up to one of the numbers on the rack, you will have completed that slot.")
    print("5) If you are unable to fill a slot on your rack with the die you roll, your turn will be skipped.")
    print("6) The first player to fill up every slot in the rack wins the game.")
    start_game()


    
def start_game():
    input("\nPress Enter to begin the game: ")
    print("\nYOUR RACK LOOKS LIKE:")
    display_user_rack()
    user_dice()



def display_user_rack():
    print("\nUSER RACK:")
    print("\n   |   ", end="")
    for x in range (0, 15):
        print((rack_slots[x]).ljust(4), end = "")
        print("|".ljust(4), end = '')

    print("\n   +", end ='')
    for z in range(len(user_rack)):
        print("-------+".ljust(8), end = "")
        
    #for x in range(len(user_rack)):
    print("\n   |   ", end='')
    for y in range(15):
        print((user_rack[y]).ljust(4), end='')
        print("|".ljust(4), end = '')
    print("\n\n")



def user_dice():
    import random
    from time import sleep
    die1 = random.randint(1, 8)
    die2 = random.randint(1, 8)
    die3 = random.randint(1, 8)
    die4 = random.randint(1, 8)

    input("\n\n\nPress Enter to roll the die: ")
    sleep(0.2)
    display_user_dice(die1, die2, die3, die4)


    
def display_user_dice(die1, die2, die3, die4):
    from time import sleep    
    print("\n(1) The first dice rolled is:", die1)
    sleep(0.2)
    print("(2) The second dice rolled is:", die2)
    sleep(0.2)
    print("(3) The third dice rolled is:", die3)
    sleep(0.2)
    print("(4) The forth dice rolled is:", die4)

    sum1 = die1 + die2
    sum2 = die1 + die3
    sum3 = die1 + die4
    sum4 = die2 + die3
    sum5 = die2 + die4
    sum6 = die3 + die4

    if user_rack[sum1 - 2] == '.':
        choose_die(die1, die2, die3, die4)

    elif user_rack[sum2 - 2] == '.':
        choose_die(die1, die2, die3, die4)
        
    elif user_rack[sum3 - 2] == '.':
        choose_die(die1, die2, die3, die4)

        
    elif user_rack[sum4 - 2] == '.':
        choose_die(die1, die2, die3, die4)

        
    elif user_rack[sum5 - 2] == '.':
        choose_die(die1, die2, die3, die4)
        
    elif user_rack[sum6 - 2] == '.':
           choose_die(die1, die2, die3, die4)

    else:
        print("\nSorry! You cannot fill an empty slot with the die you rolled!")
        display_comp_rack()
        comp_dice()


    
def choose_die(die1, die2, die3, die4):
    dicevalue1 = 0
    dicevalue2 = 0
    while True:
        try:
            dicechoice1 = int(input("\nEnter the first dice you'd like to use (1-4): "))
            
            if dicechoice1 == 1:
                dicevalue1 = die1
                break
            elif dicechoice1 == 2:
                dicevalue1 = die2
                break
            elif dicechoice1 == 3:
                dicevalue1 = die3
                break
            elif dicechoice1 == 4:
                dicevalue1 = die4
                break
            else:
                print("Input a valid value for a dice.")
        except:
            print("Please enter an integer between 1-4!")
        
    while True:
        try:
            dicechoice2 = int(input("\nEnter the second dice you'd like to use (1-4): "))

            if dicechoice2 == dicechoice1:
                print("\nThat was your first dice choice, try again!")

            elif dicechoice2 != dicechoice1:
                if dicechoice2 == 1:
                    dicevalue2 = die1
                    break
                elif dicechoice2 == 2:
                    dicevalue2 = die2
                    break
                elif dicechoice2 == 3:
                    dicevalue2 = die3
                    break
                elif dicechoice2 == 4:
                    dicevalue2 = die4
                    break
                else:
                    print("Input a valid value for a dice.")
            else:
                print("Input a valid value for a dice.")
        except:
            print("Please enter an integer between 1-4!")

    fill_user_rack(die1, die2, die3, die4, dicevalue1, dicevalue2)



def fill_user_rack(die1, die2, die3, die4, first_dice, second_dice):
    dicesum = (first_dice + second_dice)
    print("\nThe sum is:", dicesum)

    rack_index = (dicesum - 2)
    availability = user_rack[rack_index]
    #print(availability)

    if availability == '.':
        user_rack[rack_index] = 'X'
        
        #print(user_rack)
        counter = 0
        for f in range(0,15):
            if user_rack[f] == 'X':
                counter += 1
                if counter == 15:
                    print("\n __  ______  __  __  _      ______  _  ____\n \ \/ / __ \/ / / / | | /| / / __ \/ |/ / /\n  \  / /_/ / /_/ /  | |/ |/ / /_/ /    /_/\n  /_/\____/\____/   |__/|__/\____/_/|_(_)")
                                           
                    end_game()
            elif user_rack[f] == '.':
                display_user_rack()
                display_comp_rack()
                comp_dice()
                break
            
       
        
    elif availability == 'X':
        print("\nThe slot you are trying to fill is already completed. Choose 2 other die.\n")
        display_user_dice(die1, die2, die3, die4)
        
    else:
        print("Error 404: Something went wrong. Try again or restart the program.")



#Computer Plays

def display_comp_rack():
    print("\n\nCOMPUTER RACK:")
    print("\n   |   ", end="")
    for x in range (0,15):
        print((rack_slots[x]).ljust(4), end = "")
        print("|".ljust(4), end = '')
        
    print("\n   +", end ='')
    for z in range(len(comp_rack)):
        print("-------+".ljust(8), end = "")
    
    #for x in range(len(user_rack)):
    print("\n   |   ", end='')
    for y in range(0,15):
        print((comp_rack[y]).ljust(4), end = "")
        print("|".ljust(4), end = '')
    print("\n\n")



def comp_dice():
    import random
    from time import sleep
    die1 = random.randint(1, 8)
    die2 = random.randint(1, 8)
    die3 = random.randint(1, 8)
    die4 = random.randint(1, 8)

    print("\nThe Computer rolled:")
    sleep(0.2)
    print("1:", die1)
    sleep(0.2)
    print("2:", die2)
    sleep(0.2)
    print("3:", die3)
    sleep(0.2)
    print("4:", die4)
    sleep(0.5)
    
    #die sums
    sum1 = die1 + die2
    sum2 = die1 + die3
    sum3 = die1 + die4
    sum4 = die2 + die3
    sum5 = die2 + die4
    sum6 = die3 + die4

    if comp_rack[sum1 - 2] == '.':
        print("\nDice 1 and 2 were chosen.")
        sleep(0.2)
        fill_comp_rack(sum1-2)

    elif comp_rack[sum2 - 2] == '.':
        print("\nDice 1 and 3 were chosen.")
        sleep(0.2)
        fill_comp_rack(sum2-2)
        
    elif comp_rack[sum3 - 2] == '.':
        print("\nDice 1 and 4 were chosen.")
        sleep(0.2)
        fill_comp_rack(sum3-2)
        
    elif comp_rack[sum4 - 2] == '.':
        print("\nDice 2 and 3 were chosen.")
        sleep(0.2)
        fill_comp_rack(sum4-2)
        
    elif comp_rack[sum5 - 2] == '.':
        print("\nDice 2 and 4 were chosen.")
        sleep(0.2)
        fill_comp_rack(sum5-2)
        
    elif comp_rack[sum6 - 2] == '.':
        print("\nDice 3 and 4 were chosen.")
        sleep(0.2)
        fill_comp_rack(sum6-2)
    else:
        print("\nThe computer couldn't fill a slot!")
        sleep(0.2)
        display_comp_rack()
        display_user_rack()
        user_dice()



def fill_comp_rack(index):
    comp_rack[index] = 'X'

    counter = 0
    for f in range(0,15):
        if comp_rack[f] == 'X':
            counter += 1
            if counter == 15:
                #print("\n\nCOMPUTER WINS!")
                print("\n  _________  __  ______  __  _______________  _      _______  ________")
                print(" / ___/ __ \/  |/  / _ \/ / / /_  __/ __/ _ \  | | /| / /  _/ |/ / __/ /")
                print("/ /__/ /_/ / /|_/ / ___/ /_/ / / / / _// , _/  | |/ |/ // //    /\ \/_/ ")
                print("\___/\____/_/  /_/_/   \____/ /_/ /___/_/|_|   |__/|__/___/_/|_/___(_)  ")
                                                                        
                end_game()
        elif comp_rack[f] == '.':
            display_comp_rack()
            display_user_rack()
            user_dice()
            break
        
#End Game AND restart
def end_game():
    from time import sleep
    print("\nThanks for playing!")

    while True:
        try:
            answer = input("\nWould you like to play again? Enter 'y' or 'n':")
            if answer == 'y':
                sleep(0.3)
                print("\nCLEARING RACKS...\n")
                for x in range (0,15):
                    user_rack[x] = '.'
                    comp_rack[x] = '.'
                sleep(0.5)
                start_game()
                break

            elif answer == 'n':
                print("\nAlright, see you later!")
                break

            else:
                print("That is not a valid answer, try again!")
        except:
            print("That is not a valid answer, try again!")
#main
start_up()
