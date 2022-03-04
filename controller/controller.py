# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from model.model import Model


class Controller:
    def __init__(self):
        self.model = Model()

    def getData(self) -> dict[dict]:
        abfrage = self.model.getAll()
        erg = [[spalte] for spalte in
               ['ID', 'Name', 'Typ', 'Kategorie', 'Raum', 'Ausgeliehen', 'Status', 'Anzahl', 'Bemerkung']]
        for liste in abfrage:
            for i, element in enumerate(liste):
                erg[i].append(element)
        return {zeile[0] if len(zeile) > 0 else print(len(zeile)): {i: spalte for i, spalte in enumerate(zeile[1:])} for
                zeile in erg}

    def saveObejct(self, newObject: []) -> bool:
        if len(newObject) < 8:  # Number is not correct - Just a test value
            raise Exception('Missing arguments')
        else:
            # run model
            # if object exists update object, if not insert it
            pass

    def getObjectByID(self, ID: int) -> dict:
        return {'ID': ID, 'Name': "null", 'Type': "null", 'Kategorie': "null", 'Ausgeliehen': "null", 'Status': "null",
                'Anzahl': "null", 'Bemerkung': "null"}

    def delObject(self) -> bool:
        pass


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
