# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

import sqlite3 as sqlite


class Model:
    def suchanfrage_GLEICH(self, tabelle, spalte, wert):
        con = sqlite.connect(self.db)
        cur = con.cursor()
        sql = f"SELECT {spalte} FROM {tabelle} WHERE {spalte} = {wert}"
    
    def datensatz_loeschen(self, mId):
        connection = sql.connect("Inventar.db")
        cursor = connection.cursor()
        sql="DELETE FROM Material WHERE id='"+mId+"';"
        cursor.execute(sql)
        connection.commit()
        connection.close()



if __name__ == '__main__':
    # Für tests am Model
    pass
