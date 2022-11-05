from playsound import playsound
import time


start = time.time()
print(open("ascii_stills/0.txt").read())

playsound('audio.m4a', False)
x = input("Say something: ")
print(x)

end = time.time()


print(open("ascii_stills/"+str(int((end-start)/10)*10)+".txt").read())
print(end - start)