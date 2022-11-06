from RandPerson import RandPerson
import random

def Dialog(start_time):
    stranger = RandPerson(start_time)
    name = stranger.get_name()
    match stranger.get_mood():
        case "angry":
            print("The stranger jerks their head up and glares at you for a moment.")
            angryconvo = input("'What?' \n")
            print("'Well that's nice. Stop bothering me.'")
            print("The stranger goes back to what they were doing and ignores you.")
        case "sad":
            print("The stranger stares blankly out of the window, as if they are a thousand miles away. \nAt your greeting they blink and stare at you startled.")
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
            username = input("The stranger looked at you and asks you in a giddy voice. \n'Hello stranger, what's your name?'' \n")
            visit = input("'Nice to meet you " + username + ", I'm " + name + ". Where are you going? \n'")
            print("The stranger laughs happily. \n'I'm gonna go shopping in the Ginza district!'")
            print(name + " looks around and leans in to whisper... \n'I JUST WON THE LOTTERY!!!'")
            print(name + "'s phone rings, so they answer it and get to chatting excitedly...")
            
