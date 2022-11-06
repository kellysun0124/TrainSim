from RandPerson import RandPerson
import random

def Dialog(start_time):
    stranger = RandPerson(start_time)
    name = stranger.get_name()
    match stranger.get_mood():
        int i = random.ranint(1, 3)
        case "angry":
            if (i == 1):
                print("The stranger jerks their head up and stares at you for a moment.")
                angryconvo = input("What? \n")
                print("Well thats nice. Stop bothering me.")
                print("The stranger goes back to what they were doing and ignores you.")
            if (i == 2):
                print("The stranger took off his eyes off his phone and grunts")
                angryconvo = input("Huh? Can't you see I'm busy?\n")
                print("Well go bother someone else, ok?")
                print("The stranger took out a pair of earphones and puts them on and returns to his phone.")
            if (i == 3):
                print("The stranger continues listen to music with headphones on, but glances over at you.")
                angryconvo = input("What would you like to say?\n")
                print("The stranger shrugs and looks away from you. Ignoring you.")
                print("You don't know if the stranger even heard you...")

        case "sad":
            if (int i == 1):
                print("The stranger was staring blankly out of the window, as if they were a thousand miles away. \nAt your greeting they blink and stare at you startled.")
                username = input("Oh...Hi, where are my manners. I'm sorry about that. My name is " + name + ".  What is your name? \n")
                visit = input("Nice to meet you" + username + ". Are you visiting someone? \n")
                if visit.lower() == "yes":
                    yesvisit = input("Oh, who are you visiting? \n")
                    if "gran" in yesvisit.lower():
                        print(name + "choked, oh... I'm on my way to visit mine too... in the hospital... \nShe's dying from cancer...")
                        print("You offer your condolences, but an awkward silence falls. \nThe stranger starts to cry quietly and moves away from you...")
                    else:
                        print(name + "choked, oh... I'm on my way to my Granmother... in the hospital...\nShe's dying from cancer...")
                        print("You offer your condolences, but an awkward silence falls. \nThe stranger starts to cry quietly and moves away from you...")
                else:
                    print(name + "choked, oh... I'm on my way to my Granmother... in the hospital...\nShe's dying from cancer...")
                    print("You offer your condolences, but an awkward silence falls.\nThe stranger starts to cry quietly and moves away from you...")
                
        
        case "happy":
            username = input("The stranger looked at you and asks you in a giddy voice. \n'Hello stranger, what's your name? \n")
            visit = input("Nice to meet you " + username + ", I'm " + name + ". Where are you going? \n")
            print("The stranger laughs happily. \n'I'm gonna go shopping in the Ginza district!'")
            print(name + " looks around and leans in to whisper... \nI JUST WON THE LOTTERY!!!")
            print(name + "'s phone rings, so they answer it and get to chatting excitedly...")
            
