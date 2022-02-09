# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

import sqlite3 as sqlite


class Model:
    def __init__(self, db_name="Inventar.db"):
        self.db = db_name

    def suchanfrage_GLEICH(self, tabelle, attribut, wert):
        con = sqlite.connect(self.db)
        cur = con.cursor()

        sql = f"SELECT * FROM {tabelle} WHERE {attribut} = {wert}"
        cur.execute(sql)

        return cur.fetchall()  # rückgabe in form [()]

    def suchanfrage_LIKE(self, tabelle, attribut, wert):
        con = sqlite.connect(self.db)
        cur = con.cursor()

        sql = f"SELECT * FROM {tabelle} WHERE {attribut} LIKE {wert}"
        cur.execute(sql)
        return cur.fetchall()  # rückgabe in form [()]

    def datensatz_loeschen(self, mId):
        connection = sqlite.connect(self.db)
        cursor = connection.cursor()
        sql = "DELETE FROM Material WHERE id='"+mId+"';"
        cursor.execute(sql)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    # Für tests am Model
    pass
