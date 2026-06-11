from utilities.Colors import C
from utilities.teams import S
import time
import random

def open_menu():
    menu =  str(input(""" 
                ╔══════════════════════════════════════╗
                ║           MENU                       ║
                ║       ▶ Quit                         ║  
                ║       ▶ Continue                     ║  
                ╚══════════════════════════════════════╝   
                        Please select an option: """)) 
    if menu.lower() == 'quit':
        print(C.clr("Thank you for trying out the simulator! See you next time!", C.RED, C.BG_BLACK, C.BOLD))
        exit()

def continue_game(answer):
    response = input(answer)

    if response.lower() == 'm':
        open_menu()
        return continue_game(answer)
    return response
    
def test123():
    print(("""
                ╔══════════════════════════════════════╗
                ║         MADDEN FOOTBALL '26          ║
                ║       Python Simulator Edition       ║
                ╚══════════════════════════════════════╝  
                """))
    

    print(C.clr("Welcome to a Python Madden 26 simulator!", C.RED, C.BG_BLACK, C.BOLD))
    time.sleep(1)
    print(C.clr("Here you will experience the game Madden 26 but in Python!", C.RED, C.BG_BLACK, C.BOLD))
    time.sleep(1)
    print(C.clr("Now Get ready to dive into the world of Python Madden 26!", C.RED, C.BG_BLACK, C.BOLD))
    time.sleep(1)

    invalid_input = 0
    invalid_menu_input = 0
    
    user_input = continue_game(C.clr("Press 'e' to continue or press 'm' to open the menu: ", C.YELLOW, C.BG_BLACK, C.BOLD))
    while user_input.lower() not in ['e', 'm']:
        print(C.clr(f"Invalid input. Please try again. You have {3 - invalid_input} remaining attempts left.", C.RED, C.BG_BLACK, C.BOLD))
        user_input = continue_game(C.clr("Press 'e' to continue or press 'm' to open the menu: ", C.YELLOW, C.BG_BLACK, C.BOLD))
        invalid_input += 1
        if invalid_input >= 3:
            print(C.clr("Too many invalid attempts. Restarting the simulator.", C.RED, C.BG_BLACK, C.BOLD))
            test123()

    a = (continue_game(C.clr("How long do you want the game to last? (in minutes): ", C.YELLOW, C.BG_BLACK, C.BOLD)))
    print(a)
    game_time = int(a)
    while game_time == 0 is True:
        print(C.clr("Invalid input. Please enter a valid number for the game time.", C.RED, C.BG_BLACK, C.BOLD))
        a = (continue_game(C.clr("How long do you want the game to last? (in minutes): ", C.YELLOW, C.BG_BLACK, C.BOLD)))
        game_time = int(a)

    print(C.clr("Now its time to choose your team!"), C.GREEN, C.BG_BLACK, C.BOLD)
    print(C.clr("Here are the teams you can choose from:", C.GREEN, C.BG_BLACK, C.BOLD))
    seen = set()
    for team_name, ovr in S.teams.values():
        if team_name not in seen:
            print(C.clr(
                f"▶ {team_name} (OVR {ovr})",
                C.GREEN,
                C.BG_BLACK,
                C.BOLD
            ))
            seen.add(team_name)
    team_input = continue_game("Please enter the name of the team you want to play as: ")
    while team_input.lower() not in S.teams:
        print(C.clr("Invalid team name. Please try again.", C.RED, C.BG_BLACK, C.BOLD))
        team_input = continue_game(C.clr("Please enter the name of the team you want to play as: ", C.YELLOW, C.BG_BLACK, C.BOLD))
    print(C.clr(f"You have chosen to play as the {team_input}!", C.GREEN, C.BG_BLACK, C.BOLD))
    time.sleep(1)
    print(C.clr("Now let's get started!", C.GREEN, C.BG_BLACK, C.BOLD))
    computer_team = random.choice(list(S.teams.values()))
    print(C.clr(f"You will be playing against the {computer_team[0]} who has an OVR of {computer_team[1]}!", C.GREEN, C.BG_BLACK, C.BOLD))
    time.sleep(1)
    print(C.clr("Let the game begin!", C.GREEN, C.BG_BLACK, C.BOLD))
    HALF_TIME = 0
    QUARTER = 1

    game_clock = game_time * 60
    while game_clock > 0:
        print(C.clr(f"Current Quarter: {QUARTER} | Time Remaining: {game_clock // 60}:{game_clock % 60}", C.YELLOW, C.BG_BLACK, C.BOLD))
        time.sleep(1)
        game_clock -= 10
        if game_clock <= (game_time * 60) / 2 and HALF_TIME == 0:
            print(C.clr("Half Time! Take a break and get ready for the second half!", C.GREEN, C.BG_BLACK, C.BOLD))
            time.sleep(2)
            HALF_TIME = 1
        if game_clock <= (game_time * 60) / 4 and QUARTER == 1:
            print(C.clr("End of the first quarter!", C.GREEN, C.BG_BLACK, C.BOLD))
            time.sleep(2)
            QUARTER = 2
        if game_clock <= (game_time * 60) / 2 and QUARTER == 2:
            print(C.clr("End of the second quarter!", C.GREEN, C.BG_BLACK, C.BOLD))
            time.sleep(2)
            QUARTER = 3
        if game_clock <= (game_time * 60) * (3/4) and QUARTER == 3:
            print(C.clr("End of the third quarter!", C.GREEN, C.BG_BLACK, C.BOLD))
            time.sleep(2)
            QUARTER = 4
    