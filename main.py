import RandPerson
import Dialog

def OpenScript():
    print("Hello! This is a text based real time train simulation made by Kelly Sun and Yvan Quinn.")
    print("The views out the window and sounds are based in real time and real life.")
    print("Hello! You are currently at Toyosu Station, a terminal stop of the Yurikamome Line.\n The New Transit Yurikamome is a driverless, automated transit service linking Shimbashi to Toyosu, via Odaiba across the Rainbow Bridge in Tokyo.\nYou are on your way to visit your grandma, so you'll want to get off at Shimbashi station.")

def GetOnTrain():
    print("The train has arrived, it brings about a blast of wind as it slows to a stop at the station.  The automatic doors open with a whoosh.")
    GetOnTrain = input("Would you like to get on the train?\n")
    while True:
        if GetOnTrain.lower() == "yes":
            break
        else:
            print("The automatic doors closes with a snap, and the train begins to leave the station.")
            print("You bailed on visiting grandma. \nGAME OVER.")
            exit()

    

def Interaction():
    OpenScript()
    print("You look around and see many passangers around you, some reading, others with earphones on.")
    print("To look around at any point please input 'look out' or 'look out the window'.")
    print("To talk to one of the passangers, please input 'talk to someone' or 'have a conversation with someone'.")
    print("To get off the train at any point, please input 'get off' or 'get off the train'")
    action = input("what would you like to do?")
    if "talk" || "conversation" in action:
        Dialog() 
    


def main():
    OpenScript()
    GetOnTrain()
    
main()

    


