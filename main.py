import RandPerson
from playsound import playsound
import time
from Dialog import Dialog

duration = 2000

def OpenScript():
    print("Hello! This is a text based real time train simulation made by Kelly Sun and Yvan Quinn.")
    print("The views out the window and sounds are based in real time and real life.")
    print("Please turn up your volume.")
    print("\nHello! You are currently at Toyosu Station, a terminal stop of the Yurikamome Line.\nThe New Transit Yurikamome is a driverless, automated transit service linking Shimbashi to Toyosu, via Odaiba across the Rainbow Bridge in Tokyo.\nYou are on your way to visit Grandma, so you'll want to get off at Shimbashi station.")

def bail():
    print("The automatic doors closes with a snap, and the train begins to leave the station.")
    print("You bailed on visiting Grandma. She will be very disappointed.\nGAME OVER.")
    exit()

def GetOnTrain():
    print("The train has arrived, it brings about a blast of wind as it slows to a stop at the station.  The automatic doors open with a whoosh.")
    GetOnTrain = input("Would you like to get on the train?\n")
    while True:
        if "y" in GetOnTrain.lower():
            break
        else:
            bail()
    playsound('audio.mp3', False)
    start = time.time()
    Interaction(start)


stationDict = {
    "Toyosu" : 0,
    "Shin_Toyosu" : 3,
    "Shijo_Mae" : 4,
    "Ariake_Tennis_No_Mori" : 6,
    "Ariake" : 8,
    "Tokyo_Big_Sight" : 10,
    "Aomi" : 12,
    "Telecom_Center" : 14,
    "Tokyo_International_Cruise_Terminal" : 16,
    "Daiba" : 17,
    "Odaiba_Kaihinkoen" : 19,
    "Shibaura-Futo" : 25,
    "Hinode" : 26,
    "Takeshiba" : 28,
    "Shiodome" : 31,
    "Shimbashi" : 33
}

    

def Interaction(start):
    print("\nYou look around and see many passangers around you, some reading, others with earphones on.")
    print("Sitting across from of you is a young woman and young man.")
    print("To look around at any point please type 'look out' or 'look out the window'.")
    print("To talk to one of the passangers, please input 'talk to someone'")
    print("To get off the train at any point, please input 'get off' or 'get off the train'")

    while(time.time() - start < duration):
        action = input("\nWhat would you like to do?\n")
        action = action.lower()
        if "talk" in action:
            Dialog(start)
        elif "look" in action:
            windowView(start)
        elif "get off" in action:
            elapsed = time.time() - start
            if elapsed > duration-30:
                print("You step off the train into the bustling Shimbashi Station. You can't wait to give Grandma a big hug!")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~ YOU WIN ~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            elif int(elapsed / 60) in stationDict.values():
                if(elapsed < 60): bail()
                print("You step off the train into the wrong station.")
                print("The automatic doors closes with a snap, and the train begins to leave.")
                print("You'll spend the next " + str(2*int((duration - elapsed)/60)) + " minutes waiting around for the train to take you home.")
                print("Grandma will be disappointed, she was really looking forward to seeing you.\nGAME OVER.")
                exit()
            else:
                print("You can't do that, the doors are closed.")
        else:
            print("Invalid action, please try again.")

    print("\nYou missed your stop, the train has turned arround. You'll spend the next half our riding the train home in shame.")
    print("Grandma will be disappointed, she was really looking forward to seeing you. \nGAME OVER>")
    exit()


    


def windowView(start):
    print(open("ascii_stills/"+str(int((time.time()-start)/10)*10)+".txt").read())


def main():
    OpenScript()
    GetOnTrain()
    
main()

    

main()
