# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung
import pprint

from model.model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.filter = {'typ': '%', 'kategorie': '%', 'raum': '%', 'zustand': '%', 'anzahl_von': '%', 'anzahl_bis': '%',
                       'ausleibahrkeit': '%'}
        self.such = ""

    def getData(self) -> dict[dict]:
        abfrage = self.model.getInventory()
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
        material = self.model.getData(ID)
        if material:
            return {'ID': ID, 'Name': material[0][1], 'Type': material[0][2], 'Kategorie': material[0][3],
                    'Ausgeliehen': material[0][4], 'Status': material[0][5],
                    'Anzahl': material[0][6], 'Bemerkung': material[0][7]}
        else:
            return {'ID': ID, 'Name': "null", 'Type': "null", 'Kategorie': "null", 'Ausgeliehen': "null",
                    'Status': "null",
                    'Anzahl': "null", 'Bemerkung': "null"}

    def delObject(self, ID: int) -> bool:
        self.model.deleteInventory(ID)
        pass

    def getKategorie(self):
        return [i[0] for i in self.model.getKategorien()]

    def filterSpeichern(self, filterr):
        for i in filterr:
            if filterr[i] == "kein Filter" or filterr[i] == "":
                self.filter[i] = "%"
            else:
                self.filter[i] = filterr[i]
        return self.getData()

    def suche(self, suchbegriff):
        self.such = "%" + str(suchbegriff) + "%"
        return self.getData()


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
    c.getKategorie
