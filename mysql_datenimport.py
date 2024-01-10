import mysql.connector

# Verbindung zur Datenbank herstellen
connection = mysql.connector.connect(
    host="dein_host",
    user="dein_benutzername",
    password="dein_passwort",
    database="deine_datenbank"
)

# Ein Cursor-Objekt erstellen
cursor = connection.cursor()

# Beispiel-Daten
vorname = "Max"
nachname = "Mustermann"
alter = 30

# SQL-Befehl zum Einfügen von Daten
sql_befehl = "INSERT INTO deine_tabelle (vorname, nachname, alter) VALUES (%s, %s, %s)"

# Daten einfügen
daten = (vorname, nachname, alter)
cursor.execute(sql_befehl, daten)

# Änderungen in der Datenbank speichern
connection.commit()

# Verbindung schließen
cursor.close()
connection.close()
