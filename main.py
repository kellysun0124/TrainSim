import RandPerson
from playsound import playsound
import time
from Dialog import Dialog

def OpenScript():
    print("Hello! This is a text based real time train simulation made by Kelly Sun and Yvan Quinn.")
    print("The views out the window and sounds are based in real time and real life.")
    print("Hello! You are currently at Toyosu Station, a terminal stop of the Yurikamome Line.\nThe New Transit Yurikamome is a driverless, automated transit service linking Shimbashi to Toyosu, via Odaiba across the Rainbow Bridge in Tokyo.\nYou are on your way to visit Grandma, so you'll want to get off at Shimbashi station.")

def GetOnTrain():
    print("The train has arrived, it brings about a blast of wind as it slows to a stop at the station.  The automatic doors open with a whoosh.")
    GetOnTrain = input("Would you like to get on the train?\n")
    while True:
        if GetOnTrain.lower() == "yes":
            break
        else:
            print("The automatic doors closes with a snap, and the train begins to leave the station.")
            print("You bailed on visiting Grandma.\nGAME OVER.")
            exit()
    playsound('audio.mp3', False)
    start = time.time()
    while(time.time() - start < 2000):
        Interaction(start)
    print("You missed your stop, the train has turned arround. You'll spend the next half our riding the train home in shame.")
    print("Grandma will be very disappointed.\nGAME OVER>")
    exit()



    

def Interaction(start):
    print("You look around and see many passangers around you, some reading, others with earphones on.")
    print("Sitting across from of you is a young woman and young man.")
    print("To look around at any point please type 'look out' or 'look out the window'.")
    print("To talk to one of the passangers, please input 'talk to someone'")
    print("To get off the train at any point, please input 'get off' or 'get off the train'")
    action = input("what would you like to do?\n").lower
    if "talk" in action:
        Dialog(start)
    if "look" in action:
        windowView(start)
    


def windowView(start):
    print(open("ascii_stills/"+str(int((time.time()-start)/10)*10)+".txt").read())


def main():
    OpenScript()
    GetOnTrain()
    
main()

    

main()
