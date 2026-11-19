import random
import settings
from main2 import words, playround


def multiplayer():
    word1, word2 = random.sample(words[settings.difficulty], 2)

    print("\nPlayer 1's turn")
    p1 = playround(word1)

    input("\nPress Enter to pass the game to Player 2...")
    print("\n" * 3) 

    print("Player 2's turn")
    p2 = playround(word2)

    print("\n RESULTS ")
    if p1 is None:
        print("Player 1: failed")
    else:
        print(f"Player 1: {p1} tries")
        
    if p2 is None:
        print("Player 2: failed")
        
    else:
        print(f"Player 2: {p2} tries")


    if p1 is None and p2 is None:
        print("Nobody got their word. Its a draw")
        
    elif p1 is None:
        print("Player 2 wins!")
        
    elif p2 is None:
        print("Player 1 wins!")
        
    elif p1 < p2:
        print("Player 1 wins!")
        
    elif p2 < p1:
        print("Player 2 wins!")
        
    else:
        print("It's a tie!")
