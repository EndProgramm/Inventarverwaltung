# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from model.datenbank import DB


class Controller:
    def __init__(self):
        self.model = DB()

    def getData(self) -> dict[dict]:
        abfrage = self.model.getAll()
        erg = [[spalte] for spalte in ['ID', 'Name', 'Typ', 'Kategorie', 'Raum', 'Ausgeliehen', 'Status', 'Anzahl', 'Bemerkung']]
        for liste in abfrage:
            for i, element in enumerate(liste):
                erg[i].append(element)
        return {zeile[0] if len(zeile) > 0 else print(len(zeile)): {i: spalte for i, spalte in enumerate(zeile[1:])} for zeile in erg}

    def saveUses(self) -> bool:
        pass


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
