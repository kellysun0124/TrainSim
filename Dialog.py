import RandPerson
import random

def Dialog(start_time):
    stranger = RandPerson(start_time)
    match stranger.mood:
        case "angry":
            print("The stranger jerks their head up and stared at you for a moment.")
            angryconvo = input("What? \n")
            print("Well thats nice. Stop bothering me.")
            print("The stranger goes back to what they were doing and ignores you")
        case "sad":
            print("The stranger was staring blankly out of the window, as if they were a thousand miles away. \nAt your greeting they blink and stare at you startled.")
            username = input("Oh...Hi, where are my manners. I'm sorry about that. My name is" + stranger.name + ".  What is your name?")
            visit = input("Nice to meet you" + username + ". Are you visiting someone?")
            if visit.lower == "yes":
                yesvisit = input("Oh, who are you visiting?")
                if "grandma" in yesvisit.lower:
                    print(stranger.name + "choked, oh... I'm on my way to visit mine too... in the hospital...\nShe's dying from cancer...")
                    print("You offer your condolences, but an awkward silence falls.\nThe stranger starts to cry quietly and moves away from you...")
                else:
                    print(stranger.name + "choked, oh... I'm on my way to my Granmother... in the hospital...\nShe's dying from cancer...")
                    print("You offer your condolences, but an awkward silence falls.\nThe stranger starts to cry quietly and moves away from you...")
            else:
                print(stranger.name + "choked, oh... I'm on my way to my Granmother... in the hospital...\nShe's dying from cancer...")
                print("You offer your condolences, but an awkward silence falls.\nThe stranger starts to cry quietly and moves away from you...")
        case "happy":
            username = input("The stranger looked at you and asks you in a giddy voice.\n'Hello stranger, what's your name?")
            visit = input("Nice to meet you" + username + ". I'm " + stranger.name + "Where are you going?")
            print("The stranger laughs happily.\n'I'm gonna go shopping in Ginza!'")
            print(stranger.name + "looks around and lean in to whisper\n'I just won the lottery!!!'")
            print("The strangers phone rings so they answered it excitedly and got to chatting on the phone...")
            
