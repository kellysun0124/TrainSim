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

    if stranger.get_age() < 30:
        age = "young "
    elif stranger.get_age() < 55:
        age = ""
    else:
        age = "old "
    i = randint(1, 3)
    match stranger.get_mood():
        case "angry":
            if (i == 1):
                print("The "+age+"stranger jerks " + possessive + " head up and glares at you for a moment.")
                angryconvo = input("What? \n")
                print("'Well that's nice. Stop bothering me.'")
                print("'The "+age+"stranger goes back to what " + pronoun + " was doing and ignores you.'")
            if (i == 2):
                print("The "+age+"stranger briefly takes " + possessive + " eyes off " + possessive + " phone and grunts")
                angryconvo = input("'Huh? Can't you see I'm busy?'\n")
                print("'Well go bother someone else, ok?'")
                print("The "+age+"stranger takes out a pair of earphones, puts them on and returns to " + possessive + " phone.")
            if (i == 3):
                print("The "+age+"stranger continues listen to music with headphones on, but glances over at you.")
                angryconvo = input("'What do you want?'\n")
                print("The "+age+"stranger shrugs and looks away from you. Ignoring you.")
                print("You don't know if " + pronoun + " even heard you...")

        case "sad":
            if (i == 0):
                print("The stranger stares blankly out of the window, as if " + pronoun + " are a thousand miles away. \nAt your greeting " + pronoun + " blinks and stares at you startled.")
                username = input("'Oh...Hi, where are my manners. I'm sorry about that. My name is " + name + ".  What is your name?'' \n")
                visit = input("'Nice to meet you " + username + ". Are you visiting someone?'' \n")
                if visit.lower() == "yes":
                    yesvisit = input("Oh, who are you visiting? \n")
                    if "gran" in yesvisit.lower():
                        print(name + " chokes, 'Oh... I'm on my way to visit mine too... in the hospital... \nShe's dying from cancer...'")
                    else:
                        print(name + "chokes, 'Oh... I'm on my way to my Granmother... in the hospital...\nShe's dying from cancer...")
                    print("You offer your condolences, but an awkward silence falls.\n" + name + " starts to cry quietly and looks off into the distance...")
            if (i == 2):
                if age == "young ":
                    print("The "+age+"stranger looks at you and sniffles.  You notice that "+possessive+" eyes were also red and puffy.")
                    tissue = input("Would you like to offer some tissues?")
                    if "y" in tissue.lower():
                        print(pronoun+" thanks you and blows loudly into the tissue.")
                        print("*sniffles*")
                        print("'You're so kind' "+pronoun+" pockets the now soaked and wrinkly tissue.")
                        user = input("Would you like to ask "+possessive+" what is wrong?")
                        if "y" in user.lower():
                            print(pronoun+" looked down and says")
                            print("'I um....I got dumped today...' "+possessive+" voice quivering as they trailed off.")
                            print("'I don't know what I'm going to do now...We've been together for 10 months...10 WHOLE months!'")
                            console = input("Would you like to try and help?")
                            if "y" in user.lower():
                                print("You give a consoling pat on "+possessive+" shoulder, and awkwardly say")
                                print("'You'll be ok...there there...' and hand over more tissues...")
                            else:
                                print("You tuck away the rest of your tissues and pretend to be on your phone...")
                        else:
                            print("You stare awkwardly at the stranger...")
                    else:
                        print("You play with your pack of tissues awkwardly, while they gave you dagger eyes.")
                else:
                    print("The stranger sniffles loudly, and blows into "+possessive+" t-shirt.\nYou dropped your phone and "+pronoun+" makes eye contact with you...")
                    tissue = input("Would you like to offer some tissues?")
                    if "y" in tissue.lower():
                        print(pronoun+" thanks you and takes the tissue.")
                        print("*sniffles*")
                        print("'You're so kind' "+pronoun+" wipes the tears off "+possessive+" face.")
                        user = input("Would you like to ask "+possessive+" where "+pronoun+" is going?")
                        if "y" in user.lower():
                            print(pronoun+" looked down and says")
                            print("'I'm just going home, I got fired today...' "+possessive+" voice quivering as "+pronoun+" trailed off.")
                            print("'I don't know what I'm going to do now...I've been working at this company for 8 years...'")
                            print(pronoun+" sighs heavily.  And looks defeated...")
                    else:
                        print("You try to not stare while "+pronoun+" cries...")
                        
            if (int == 3):
                if age == "young ":
                    print("You notice a child crying loudly nearby...")
                    approach = input("Would you like to approach the child and ask what's wrong?")
                    if "y" in tissue.lower():
                        print("I've lost my teddy")


            

        case "happy":
            username = input("The "+age+"stranger looks at you and asks you in a giddy voice. \n'Hello stranger, what's your name?'' \n")
            visit = input("'Nice to meet you " + username + ", I'm " + name + ". Where are you going?' \n")
            print(name + " laughs happily. \n'I'm gonna go shopping in the Ginza district!'")
            print(name + " looks around and leans in to whisper... \n'I JUST WON THE LOTTERY!!!'")
            print(possessive + " phone rings, so " + pronoun + " answers it and get to chatting excitedly...")