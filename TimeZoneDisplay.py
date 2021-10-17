import requests
from datetime import datetime

API = "http://worldtimeapi.org/api/timezone/America/"
city = "New_York"
response = requests.get(API + city)
data = response.json()
days = {1: 'monday', 2 : 'tuesday', 3 : 'wednesday', 4 : 'thursday', 5: 'friday', 6 : 'saturday', 7 : 'sunday'}
    

time_zone = data['abbreviation']
day_num = data['day_of_week']
day = days[day_num]
date_string = data['datetime']

year = date_string[:4]
month = date_string[5:7]
date = date_string[8:10]
time = date_string[11:19]

def format_time_details():
    time_zone_sentence = day.capitalize() + ", " + month + "/" + date + "/" + year + ", " + time + " " + time_zone
    return time_zone_sentence

print(format_time_details())

