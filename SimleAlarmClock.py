import time
import datetime
import winsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    if datetime.datetime.now().strftime("%H:%M:%S") == alarm_time:
        print("Wake up!")
        winsound.Beep(2000, 2000) 
        break
