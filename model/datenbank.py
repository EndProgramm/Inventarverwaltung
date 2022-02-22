# -*- coding: utf-8 -*-

"""
Beschreibung: \n
API für die Datenbank
"""

import sqlite3 as sqlite


class DB:
    """
    API für die Datenbank
    """
    def __init__(self, db_name="inventar.db"):
        self.name = db_name

    def getAll(self) -> tuple[tuple]:
        """
        Gibt alle Daten aus der Gegenstandstabelle zurück
        """
        return cur.fetchall()

    def suchanfrage_GLEICH(self, tabelle: str, attribut: str, wert: str) -> list[tuple]:
        """
        Suchanfrage nach identischen Wert von wert zu attribut\n
        Alle Parameter sollten als str gegeben sein \n(werden aber auch gecasted)\n
        gibt alle Zeilen, bei denen das gesuchte Attribut mit dem Wert übereinstimmt mit allen ihren Attributen
        """
        con = sqlite.connect(self.name)
        cur = con.cursor()

        sql = f"SELECT * FROM {tabelle} WHERE {attribut} = {wert}"
        cur.execute(sql)

        return cur.fetchall()  # rückgabe in form [("Zeile1", "Attribut2", ...), ("Zeile2", ...), ...]

    def suchanfrage_LIKE(self, tabelle: str, attribut: str, wert: str) -> list[tuple]:
        """
        Suchanfrage nach ähnlichem Wert von wert zu attribut\n
        Alle Parameter sollten als str gegeben sein \n(werden aber auch gecasted)\n
        gibt alle Zeilen, bei denen das gesuchte Attribut mit dem Wert übereinstimmt mit allen ihren Attributen
        """
        con = sqlite.connect(self.name)
        cur = con.cursor()

        sql = f"SELECT * FROM {tabelle} WHERE {attribut} LIKE {wert}"
        cur.execute(sql)
        return cur.fetchall()  # rückgabe in form [("Zeile1", "Attribut2", ...), ("Zeile2", ...), ...]

    def datensatz_loeschen(self, mId):
        connection = sqlite.connect(self.name)
        cursor = connection.cursor()
        sql = "DELETE FROM Material WHERE id='"+mId+"';"
        cursor.execute(sql)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    # Für tests
    pass
