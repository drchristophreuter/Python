# Beispiel zum auslesen der CPU Temperatur
# Dr. Christoph Reuter 1/2024

import psutil

def get_cpu_temperature():
    try:
        temperature = psutil.sensors_temperatures()['coretemp'][0].current
        return temperature
    except:
        return -1

temperature = get_cpu_temperature()

if temperature != -1:
    print(f"CPU-Temperatur: {temperature}°C")
else:
    print("CPU-Temperatur konnte nicht abgerufen werden.")