# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from model.model import Model


class Controller:
    def __init__(self):
        self.model = Model()

        self.filter = {'typ': '%', 'kategorie': '%', 'raum': '%', 'zustand': '%', 'anzahl_von': '%', 'anzahl_bis': '%',
                       'ausleibahrkeit': '%'}
        self.such = ""

    def getData(self) -> dict[str, dict[int, str]]:
        abfrage = self.model.getInventory()
        erg = [[spalte] for spalte in
               ['ID', 'Name', 'Typ', 'Kategorie', 'Raum', 'Ausgeliehen', 'Status', 'Anzahl', 'Bemerkung']]
        for liste in abfrage:
            for i, element in enumerate(liste):
                erg[i].append(element)
        return {zeile[0] if len(zeile) > 0 else print(len(zeile)): {i: spalte for i, spalte in enumerate(zeile[1:])} for
                zeile in erg}

    def saveObject(self, newObject: dict) -> bool:
        if newObject.get("name") is None or newObject.get("typ") is None or newObject.get("kategorie") is None or \
                newObject.get("raum"):
            raise Exception('Missing arguments')
        else:
            if newObject.get("ID") is not None:
                self.model.updateInventory(newObject.get("ID"), newObject.get("name"), newObject.get("typ"),
                                           newObject.get("kategorie"), newObject.get("raum"),
                                           newObject.get("ausgeliehen"), newObject.get("status"),
                                           newObject.get("anzahl"), newObject.get("bemerkung"))
                return True
            else:
                return self.existsObject(self.model.addInventory(newObject.get("name"), newObject.get("typ"),
                                                                 newObject.get("kategorie"), newObject.get("raum"),
                                                                 newObject.get("ausgeliehen"), newObject.get("status"),
                                                                 newObject.get("anzahl"), newObject.get("bemerkung")))

    def existsObject(self, ID: int) -> bool:
        if self.model.getData(ID):
            return False
        else:
            return True

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
        return self.existsObject(ID)

    def getKategorie(self):
        return [i[0] for i in self.model.getKategorien()]

    def filterSpeichern(self, filterDict: dict[str, str]) -> dict[str, any]:
        stehtfuer={"kein Filter":"%","":"%","Gebrauch":"Gg","Verbrauch":"Vg"}
        for i in filterr:
            if filterr[i] in stehtfuer:
                self.filter[i]=stehtfuer[filterr[i]]
            else:
                self.filter[i]=filterr[i]
        return self.getData()

    def suche(self, suchbegriff: str) -> dict[dict]:
        self.such = "%" + suchbegriff + "%"
        return self.getData()


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
