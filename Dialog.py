from RandPerson import RandPerson
from random import randint

def Dialog(start_time):
    stranger = RandPerson(start_time)
    name = stranger.get_name()
    if stranger.get_gender() == "male":
        pronoun = "he"
        possessive = "his"
    else:
        pronoun = "she"
        possessive = "her"
    i = randint(1, 3)
    match stranger.get_mood():
        case "angry":
            if (i == 1):
                print("The stranger jerks " + possessive + " head up and glares at you for a moment.")
                angryconvo = input("What? \n")
                print("'Well that's nice. Stop bothering me.'")
                print("'The stranger goes back to what " + pronoun + " was doing and ignores you.'")
            if (i == 2):
                print("The stranger briefly takes " + possessive + " eyes off " + possessive + " phone and grunts")
                angryconvo = input("'Huh? Can't you see I'm busy?'\n")
                print("'Well go bother someone else, ok?'")
                print("The stranger takes out a pair of earphones, puts them on and returns to " + possessive + " phone.")
            if (i == 3):
                print("The stranger continues listen to music with headphones on, but glances over at you.")
                angryconvo = input("'What do you want?'\n")
                print("The stranger shrugs and looks away from you. Ignoring you.")
                print("You don't know if " + pronoun + " even heard you...")

        case "sad":
            print("The stranger stares blankly out of the window, as if " + pronoun + " are a thousand miles away. \nAt your greeting " + pronoun + " blinks and stares at you startled.")
            username = input("'Oh...Hi, where are my manners. I'm sorry about that. My name is " + name + ".  What is your name?'' \n")
            visit = input("'Nice to meet you " + username + ". Are you visiting someone?'' \n")
            if visit.lower() == "yes":
                yesvisit = input("Oh, who are you visiting? \n")
                if "gran" in yesvisit.lower():
                    print(name + " chokes, 'Oh... I'm on my way to visit mine too... in the hospital... \nShe's dying from cancer...'")
                else:
                    print(name + "chokes, 'Oh... I'm on my way to my Gran Gran... in the hospital...\nShe's dying from cancer...'")
            else:
                print(name + "chokes, 'Oh... I'm on my way to my Granmother... in the hospital...\nShe's dying from cancer...")
            print("You offer your condolences, but an awkward silence falls.\n" + name + " starts to cry quietly and moves away from you...")           
        case "happy":
            username = input("The stranger looks at you and asks you in a giddy voice. \n'Hello stranger, what's your name?'' \n")
            visit = input("'Nice to meet you " + username + ", I'm " + name + ". Where are you going?' \n")
            print(name + " laughs happily. \n'I'm gonna go shopping in the Ginza district!'")
            print(name + " looks around and leans in to whisper... \n'I JUST WON THE LOTTERY!!!'")
            print(possessive + " phone rings, so " + pronoun + " answers it and get to chatting excitedly...")