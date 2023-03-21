from gpiozero import Button
import time
import math

wind_count = 0       # Counts how many half-rotations
radius_cm = 9.0 # Radius of your anemometer
wind_interval = 5    # How often (secs) to report speed

# Every half-rotation, add 1 to count
def spin():
	global wind_count
	wind_count = wind_count + 1
	# print("spin" + str(wind_count))

# Calculate the wind speed
def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0

    dist_km = (circumference_cm * rotations) / 100000.0

    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * 3600

    return km_per_hour * 1.18


wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

# Loop to measure wind speed and report at 5-second intervals
while True:
        wind_count = 0
        time.sleep(wind_interval)
        print( calculate_speed(wind_interval), "cm/h")

def reset_wind():
    global wind_count
    wind_count = 0
