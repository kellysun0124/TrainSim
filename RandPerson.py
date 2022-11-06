import random
import time
from Person import Person

genderList = ["male", "female"]
girlNameList = ["Alice", "Kelly", "Pheobe", "Judy", "Lisa", "Tasha", "Rachel", "Jennie", "Natalie", "Sophia"]
boyNameList = ["Bob", "Roger", "Yvan", "Liam", "Lucas", "James", "Quinn", "Ross", "Jaden", "Ash"]
stationDict = {
    "Toyosu" : 0,
    "Shin Toyosu" : 3,
    "Shijo Mae" : 4,
    "Ariake Tennis No Mori" : 6,
    "Ariake" : 8,
    "Tokyo Big Sight" : 10,
    "Aomi" : 12,
    "Telecom Center" : 14,
    "Tokyo International Cruise Terminal" : 16,
    "Daiba" : 17,
    "Odaiba Kaihinkoen" : 19,
    "Shibaura-Futo" : 25,
    "Hinode" : 26,
    "Takeshiba" : 28,
    "Shiodome" : 31,
    "Shimbashi" : 33
}
moodList = ["angry", "sad", "happy"]

class RandPerson(Person):
    def __init__(self, start_time):
        #randome age
        age = random.randint(5, 90)
        #set gender and name based on gender
        gender = random.choice(genderList)
        if gender == genderList[1]:
            name = random.choice(girlNameList)
        else:
            name = random.choice(boyNameList)
        #set origin and destination
        now_time = time.time()
        past_station_times = [station_time for station_time in stationDict.values() if station_time < (now_time - start_time)/60 ]
        stationList = list(stationDict)
        current_station_index = len(past_station_times)
        origin = random.choice(stationList[:current_station_index])
        destination = random.choice(stationList[current_station_index:])

        #mood
        mood = random.choice(moodList)

        super().__init__(name, gender, age, origin, destination, mood)


