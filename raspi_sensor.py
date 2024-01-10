import Adafruit_DHT

# Sensor-Typ und GPIO-Pin festlegen
sensor = Adafruit_DHT.DHT22
pin = 4  # Beispiel-GPIO-Pin

# Daten auslesen
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(f"Aktuelle Temperatur: {temperature}°C")
    print(f"Aktuelle Luftfeuchtigkeit: {humidity}%")
else:
    print("Fehler beim Auslesen des Sensors.")
