#Daten aus der Datenbank auslesen
#Lisa-Marie Frauböse, Malte Reimer

import os, sqlite3

def sql(command):
    # Herstellen der Verbindung mit der Datenbank
    connection = sqlite3.connect("Inventar.db")
    # Über den sogenannten Cursor können Anfragen an die Datenbank gestellt werden
    cursor = connection.cursor()
    # Tabellen erzeugen
    sql = command
    # Hier wird über den Cursor den Anfrage gestellt
    cursor.execute(sql)
    # Im ergebnis speichern wir das, was wir vom Curser zurück erhalten
    ergebnis = cursor.fetchall()
    # commit schließt die Transaktion ab und speichert die Änderung dauerhaft
    connection.commit()
    # Schließen der Datenbankverbindung
    connection.close()
    if ergebnis:
        return ergebnis
    else:
        return None
    
def alleDaten():
    return sql("SELECT * FROM Material")
    
