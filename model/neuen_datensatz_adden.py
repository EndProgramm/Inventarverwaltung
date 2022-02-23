import sqlite3


class Model:
    
    def daten_eintragen(self, name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung): #Values as String with Value, Empty → None
        con = sqlite3.connect('inventar.db')
        cur = con.cursor()
        cur.execute('INSERT INTO "Material" (Name, Typ, Kategorie, Raum, Ausgeliehen, Status, Anzahl, Bemerkung) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung))
        id = cur.lastrowid
        con.commit()
        con.close()
        return(id)