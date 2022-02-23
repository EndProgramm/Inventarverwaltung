import sqlite3


class Model:
    
    def daten_updaten(self,id, name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung): #Values as String with Value, Empty → None
        con = sqlite3.connect('inventar.db')
        cur = con.cursor()
        cur.execute('UPDATE "Material" SET Name = ?, Typ = ?, Kategorie = ?, Raum = ?, Ausgeliehen = ?, Status = ?, Anzahl = ?, Bemerkung = ? WHERE MID = ?;', (name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung,id))
        con.commit()
        con.close()
        
