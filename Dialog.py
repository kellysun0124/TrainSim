from RandPerson import RandPerson
from random import randint, choice

def Dialog(start_time):
    stranger = RandPerson(start_time)
    name = stranger.get_name()
    if stranger.get_gender() == "male":
        pronoun = "he"
        possessive = "his"
        label = "man"
    else:
        pronoun = "she"
        possessive = "her"
        label = choice(['woman','lady'])

    age = stranger.get_age()
    if age < 30:
        age = "young "
    elif age < 55:
        age = ""
    elif age < 85:
        age = "old "
    else:
        age = "ancient "

    i = randint(0,4)
    match stranger.get_mood():
        case "angry":
            if(i==0):
                print("'The "+age+"stranger seems to look right through you.")
                input("'Yes?!?' \n")
                input("'I really don't have time for this, but I could use some advice. What's the best way to get back at someone?'\n")
                print("The "+age+label+" stranger doesn't seem to hear what you say, and continues on.")
                if(age == "young "):
                    partner = choice(["girlfriend", "boyfriend", "fiancee"])
                else:
                    partner = choice(["wife, husband"])
                haha = choice([("BITCH","she"),("ASSHOLE","he")])
                input("'If that " + haha[0] + " thinks " + haha[1] + " can sleep with my " + partner + " and get away with it "+ haha[1] + "'s got another thing coming.'\n")
                print("'I don't need your USELESS FUCKING INPUT on this, why don't you mind your own GODDAMN BUSINESS!'")
                print("You hastily back away before the angry "+age+label+" takes a swing at you.")
            elif (i == 1 or age == "old "):
                print("The "+age+"stranger jerks " + possessive + " head up and glares at you for a moment.")
                angryconvo = input("'What?'' \n")
                print("'Well that's nice. Stop bothering me.'")
                print("The "+age+label+" goes back to what " + pronoun + " was doing and ignores you.")
            elif (i == 2):
                print("The "+age+"stranger briefly takes " + possessive + " eyes off " + possessive + " phone and grunts")
                angryconvo = input("'Huh? Can't you see I'm busy?'\n")
                print("'Well go bother someone else, ok?'")
                print("The "+age+label+"stranger takes out a pair of earphones, puts them on and returns to " + possessive + " phone.")
            elif (i == 3):
                print("The "+age+"stranger continues listen to music with headphones on, but glances over at you.")
                angryconvo = input("'What do you want?'\n")
                print("The "+age+label+" shrugs and looks away from you. Ignoring you.")
                print("You don't know if " + pronoun + " even heard you...")

        case "sad":
            match i%2:
                case 0:
                    print("The stranger stares blankly out of the window, as if " + pronoun + " is a thousand miles away. \nAt your greeting " + pronoun + " blinks and stares at you startled.")
                    username = input("'Oh...Hi, where are my manners. I'm sorry about that. My name is " + name + ".  What is your name?' \n")
                    visit = input("'Nice to meet you " + username + ". Are you visiting someone?' \n")
                    if visit.lower() == "y":
                        yesvisit = input("'Oh, who are you visiting?' \n")
                        if "gran" in yesvisit.lower():
                            print(name + " chokes, 'Oh... I'm on my way to visit mine too... in the hospital... \nMy Gran Gran is dying from cancer...'")
                        else:
                            print(name + "chokes, 'Oh... I'm on my way to my grandmother... in the hospital...\nShe's dying from cancer...'")
                        print("You offer your condolences, but an awkward silence falls.\n" + name + " starts to cry quietly and looks off into the distance...")
                case 1:
                    if age == "young ":
                        print("The "+age+"stranger looks at you and sniffles.  You notice that "+possessive+" eyes are also red and puffy.")
                        tissue = input("Would you like to offer some tissues? ")
                        if "y" in tissue.lower():
                            print(pronoun+" thanks you and blows loudly into the tissue.")
                            print("*sniffles*")
                            print("'You're so kind' "+pronoun+" pockets the now soaked and wrinkly tissue.")
                            user = input("Would you like to ask "+possessive+" what is wrong?\n")
                            if "y" in user.lower():
                                print(pronoun.capitalize()+" looked down and says")
                                print("'I um....I got dumped today...' "+possessive+" voice quivering as "+pronoun+" trails off.")
                                print("'I don't know what I'm going to do now...We've been together for 10 months...10 WHOLE months!'")
                                console = input("Would you like to try and help?\n")
                                if "y" in user.lower():
                                    print("You give a consoling pat on "+possessive+" shoulder, and awkwardly say")
                                    print("'You'll be ok...there there...' and hand over more tissues...")
                                else:
                                    print("You tuck away the rest of your tissues and pretend to be on your phone...")
                            else:
                                print("You stare awkwardly at the "+age+label+"...")
                        else:
                            print("You play with your pack of tissues awkwardly, while "+pronoun+" gives you dagger eyes.")
                    else:
                        print("The stranger sniffles loudly, and blows into "+possessive+" t-shirt.\nYou drop your phone and "+pronoun+" makes eye contact with you...")
                        tissue = input("Would you like to offer some tissues? ")
                        if "y" in tissue.lower():
                            print(pronoun+" thanks you and takes the tissue.")
                            print("*sniffles*")
                            print("'You're so kind' "+pronoun+" wipes the tears off "+possessive+" face.")
                            user = input("Would you like to ask "+possessive+" where "+pronoun+" is going? ")
                            if "y" in user.lower():
                                print(pronoun.capitalize()+" looked down and says")
                                print("'I'm just going home, I got fired today...' "+possessive+" voice quivering as "+pronoun+" trails off.")
                                print("'I don't know what I'm going to do now...I've been working at this company for 8 years...'")
                                print(pronoun.capitalize()+" sighs heavily.  And looks defeated...")
                        else:
                            print("You try to not stare while "+pronoun+" cries...")

        case "happy":
            match i % 2:
                case 0:
                    dest = stranger.get_destination()
                    if dest == "Shimbashi":
                        username = input("The "+age+"stranger looks at you and asks you in a giddy voice: \n'Hello stranger, what's your name?' \n")
                        visit = input("'Nice to meet you " + username + ", I'm " + name + ". Where are you going?' \n").lower()
                        if "shimbashi" in visit:
                            print(name + " laughs happily. \n'Me too! I'm gonna go shopping in the Ginza district!'")
                        else:
                            print(name + " laughs happily. \n'I'm gonna go shopping in the Ginza district!'")
                        print(name + " looks around and leans in to whisper... \n'I JUST WON THE LOTTERY!!!'")
                        print(possessive.capitalize() + " phone rings, so " + pronoun + " answers it and get to chatting excitedly...")
                    else:
                        response = input("The "+age+"stranger greets you with a smile and asks, 'What can I do for you?'\n")
                        print("'I'm not sure if I can really help you with that, you see I've found myself in a bit of a conundrum.'")
                        print("'There's a friend of mine I'd like to visit, but I've never been to " +possessive+" place. And I left my phone at home!'")
                        print("'I do remember the address, but I'm not so good with maps. I think I'm supposed to get off at "+ dest+" Station?'")
                        username = input("'Where are my manners, what's your name?' ")
                        print("'It's great to mee you " + username + ", I'm "+ stranger.get_name()+"!'")
                        station = input("'If you don't mind me asking, where are you getting off?' ")
                        if dest.lower() in station.lower():
                            input("'Wow! What a coincidence! That's so great! Would you mind showing me around?' ")
                        else:
                            print("'Oh I love that area! It's just a ten minute walk to some really nice clubs.'")
                            print("'I know, why don't I show you around? My other friend's lame anyways, " + pronoun+ " never knows how to have a good time.'")
                            input("'What do you say?' ")
                        input("'Ha! I knew you'd say yes, I'm so excited to hit the town with my new best friend! "+stranger.get_name()+" and " +username+", name a more dynamic duo!'\n")
                        print("'Well when you put it like that...'")

                case 1:
                    print("Before you get a chance to introduce yourself, the "+age+"stranger grabs you by the hand and asks you,")
                    ans = input("'Have you ever been in love?'\n")
                    print("'\""+ans+"!\" That's rich! I tell you what, I feel like I've just been given a second chance at life.")
                    print("Trust me, you've never met such a gorgeous "+choice(["man", "woman"])+", and hot DAMN what an ass!")
                    print("You look away uncomfortably as the "+age+label+"'s eyes glaze over and "+pronoun+" starts to make groping motions with "+ possessive+ " hands.")
