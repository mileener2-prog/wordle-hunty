hints_enabled = False
difficulty = "normal"

DIFFICULTIES = { "easy": {"length": 4, "attempts": 8},
                "normal": {"length": 5, "attempts": 6},
                "hard": {"length": 7, "attempts": 3},
                }

def open_settings():
    global hints_enabled, difficulty
    while True:
        status = "ON" if hints_enabled else "OFF"
        print("\n--- SETTINGS ---")
        print(f"1 - Toggle Hints (Currently: {status})")
        print(f"2 - Difficulty (easy / normal / hard)")
        print("3 - Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            hints_enabled = not hints_enabled  
            print(f"Hints are now {'ON' if hints_enabled else 'OFF'}!")
        elif choice == "2":
            diff = input("Choose a difficulty: ").strip().lower()
            if diff in ("easy", "normal", "hard"):
                difficulty=diff
                print(f"Difficulty set to {difficulty}")
            else:
                print("Invalid choice.")
        
        elif choice == "3":
            break
            
        else:
            print("Invalid option, try again.")
