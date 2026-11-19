import random
import settings
words={
        "easy":  ["LAMP", "FISH", "TREE", "MOON", "BOOK", "CAKE", "RAIN", "SAND", "WIND", "STAR", "DOOR", "FIRE", "LEAF", "BIRD", "SHIP"],
        "normal": ["BREAD", "SMILE", "PLANT", "LIGHT", "WATER", "HOUSE","CHAIR", "DREAM", "STORM", "HAPPY", "BEACH", "FLAME", "CLOUD", "GRAIN", "HEART", "MUSIC", "NIGHT", "PEACH", "RIVER", "SHIRT", "TABLE", "TRAIN", "WORLD", "APPLE", "BRUSH", "CANDY", "DRIVE", "EARTH", "FRUIT", "GREEN"],
        "hard": ["BALANCE", "CAPTAIN", "DOLPHIN", "KITCHEN", "LANTERN", "MONSTER", "PICTURE", "RAINBOW", "SUNRISE", "TEACHER", "WEATHER", "JOURNEY", "MACHINE", "FREEDOM", "HARVEST"],
        }

def playround(secretword):
    guesses=0 
    rules=settings.DIFFICULTIES[settings.difficulty]
    length=rules["length"]
    attempts=rules["attempts"]
    
   
    def show_hint(secretword):
        num_hints = 1
        positions = random.sample(range(length) , num_hints)
    
        display_hint = []
        for i in range(0,length):
            if i in positions:
                display_hint.append(secretword[i])
            else:
                display_hint.append("_")
                
        print(' '.join(display_hint))
        
    
    
    wordleword=random.choice(words[settings.difficulty])
    if settings.hints_enabled == True:
        show_hint(wordleword)
        
    while attempts != guesses: 
        userguess=input("guess the word ").strip().upper()
        
        if len(userguess) != length:
            print(f"your guess needs to be {length} letters")
            continue
        
        guesses+=1
        position = 0
        clue = ""
        for letter in userguess:
            if letter == wordleword[position]:
                clue += "\033[32m◼\033[0m"
                
            elif letter in wordleword:
                clue += "\033[33m◼\033[0m"
        
            else: 
                clue += "\033[30m◼\033[0m"
            position += 1
            
        print(clue)    
        if userguess==wordleword:
            print("correct")
            return guesses
        
        if attempts <= guesses:
            print("game over")
            return None
            
def singleplayer():
    word = random.choice(words[settings.difficulty])
    playround(words)
    
    
    
    
    
    
    
    
    
    
    