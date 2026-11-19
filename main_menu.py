import main2
import settings
import multi


def main_menu():
    while True:
        print("""
    WORDLE
    1- START
    2- MULTIPLAYER
    3- SETTINGS
    4- EXIT
    """)
        
        userinput=input("Select an option: ").strip()
        
        if userinput == "1":
            main2.singleplayer()
            
        elif userinput == "2":
            multi.multiplayer()
            
        elif userinput == "3":
            settings.open_settings()
            
        elif userinput == "4":
            print("Goodbye")
            break
        
        else:
            print("Invalid option, please choose a valid number")
        
main_menu()
    

