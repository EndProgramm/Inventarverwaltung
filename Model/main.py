# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

import sqlite3 as sqlite


class Model:
    def suchanfrage_GLEICH(self, tabelle, spalte, wert):
        con = sqlite.connect(self.db)
        cur = con.cursor()
        sql = f"SELECT {spalte} FROM {tabelle} WHERE {spalte} = {wert}"



if __name__ == '__main__':
    # Für tests am Model
    pass
