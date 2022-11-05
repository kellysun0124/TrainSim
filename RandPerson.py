import random
import time
from Person import Person

genderList = ["male", "female"]
girlNameList = ["Alice", "Kelly", "Pheobe", "Judy", "Lisa", "Tasha", "Rachel", "Jennie", "Natlie", "Sophia"]
boyNameList = ["Bob", "Roger", "Yvan", "Liam", "Lucas", "James", "Quinn", "Ross", "Jaden", "Ash"]
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
moodList = ["angry", "sad"]

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
        past_station_times = [station_time if station_time < now_time - start_time for station_time in stationDict.values()]
        stationList = list(stationDict)
        current_station_index = len(past_station_times)
        origin = random.choice(stationList[:current_station_index])
        destination = random.choice(stationList[current_station_index:])

        #mood
        mood = random.choice(moodList)

        super().__init__(name, gender, age, origin, destination, mood)


