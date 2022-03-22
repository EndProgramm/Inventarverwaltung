# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from model.model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.filter = {'typ': '%', 'kategorie': '%', 'raum': '%', 'zustand': '%', 'anzahl_von': '%', 'anzahl_bis': '%',
                       'ausleibahrkeit': '%'}
        self.such = ""
        self.sortierung = "ID"
        self.direction = "asc"
        print(self.filter["ausleibahrkeit"])

    def getData(self) -> dict[dict]:
        abfrage = self.model.filterAll("", self.such, self.filter["typ"], self.filter["kategorie"], self.filter["raum"],
                                       self.filter["ausleibahrkeit"], self.filter["zustand"], self.filter['anzahl_von'],
                                       self.filter['anzahl_bis'], self.sortierung, self.direction)
        erg = [[spalte] for spalte in
               ['ID', 'Name', 'Typ', 'Kategorie', 'Raum', 'Ausgeliehen', 'Zustand', 'Anzahl', 'Bemerkung']]
        for liste in abfrage:
            for i, element in enumerate(liste):
                erg[i].append(element)
        return {zeile[0] if len(zeile) > 0 else print(len(zeile)): {i: spalte for i, spalte in enumerate(zeile[1:])} for
                zeile in erg}

    def saveObject(self, newObject: dict) -> bool:
        if newObject.get("ID") is not None:
            self.model.updateInventory(str(newObject.get("ID")), newObject.get("name"), newObject.get("typ"),
                                       newObject.get("kategorie"), newObject.get("raum"),
                                       newObject.get("ausgeliehen"), newObject.get("zustand"),
                                       newObject.get("anzahl"), newObject.get("bemerkung"))
            return True
        else:
            if newObject.get("bemerkung")==None or newObject.get("bemerkung")=="None":
                newObject["bemerkung"]=""
            if newObject.get("kategorie")=="Gg":
                newObject["anzahl"]=1
            if newObject.get("name") == "":
                return "name"
            if newObject.get("raum") == "":
                return "raum"
            if newObject.get("kategorie") == "":
                return "kategorie"
            return self.existsObject(self.model.addInventory(newObject.get("name"), newObject.get("typ"),
                                                             newObject.get("kategorie"), newObject.get("raum"),
                                                             newObject.get("ausgeliehen"), newObject.get("zustand"),
                                                             newObject.get("anzahl"), newObject.get("bemerkung")))

    def existsObject(self, ID: int) -> bool:
        if self.model.getData(ID):
            return False
        else:
            return True

    def getObjectByID(self, ID: int) -> dict:
        material = self.model.getData(str(ID))
        if material:
            return {'ID': ID, 'name': material[0][1], 'typ': material[0][2], 'kategorie': material[0][3],
                    'raum': material[0][4], 'ausgeliehen': material[0][5], 'zustand': material[0][6],
                    'anzahl': material[0][7], 'bemerkung': material[0][8]}
        else:
            return {'ID': ID, 'name': "null", 'typ': "null", 'kategorie': "null", 'raum': 'null',
                    'ausgeliehen': "null", 'zustand': "null", 'anzahl': "null", 'bemerkung': "null"}

    def delObject(self, ID: int) -> bool:
        self.model.deleteInventory(ID)
        return self.existsObject(ID)

    def getKategorie(self):
        return [i[0] for i in self.model.getKategorien()]

    def sortBy(self, sortierung: str) -> dict[dict]:
        if self.sortierung == sortierung:
            if self.direction == "ASC":
                self.direction = "DESC"
            else:
                self.direction = "ASC"
        else:
            self.sortierung = sortierung
            self.direction = "ASC"
        return self.getData()

    def filterSpeichern(self, filterDict: dict[str, str]) -> dict[dict]:
        stehtfuer = {"kein Filter": "%", "": "%", "Gebrauch": "Gg", "Verbrauch": "Vg", "funktionsfähig": "True",
                     "defekt": "False"}
        for i in filterDict:
            if filterDict[i] in stehtfuer:
                self.filter[i] = stehtfuer[filterDict[i]]
            else:
                self.filter[i] = filterDict[i]
        return self.getData()

    def suche(self, suchbegriff: str) -> dict[dict]:
        self.such = f"%{suchbegriff}%"
        return self.getData()

    def getFilter(self):
        stehtfuerrueckwarts = {"%": "kein Filter", "Gg": "Gebrauch", "Vg": "Verbrauch", "True": "funktionsfähig",
                               "False": "defekt"}
        filterDict = {'typ': '%', 'kategorie': '%', 'raum': '%', 'zustand': '%', 'anzahl_von': '%', 'anzahl_bis': '%',
                      'ausleibahrkeit': '%'}
        for i in self.filter:
            if self.filter[i] in stehtfuerrueckwarts:
                filterDict[i] = stehtfuerrueckwarts[self.filter[i]]
            else:
                filterDict[i] = self.filter[i]
        if filterDict["anzahl_von"] == "kein Filter":
            filterDict["anzahl_von"] = ""
        if filterDict["anzahl_bis"] == "kein Filter":
            filterDict["anzahl_bis"] = ""
        return filterDict

    def defektmelden(self, mID):
        x = self.model.filterAll(mID, "%", "%", "%", "%", "%", "%", "%", "%", self.sortierung, self.direction)
        self.model.updateInventory(mID, x[0][1], x[0][2], x[0][3], x[0][4], x[0][5], "False", x[0][7], x[0][8])


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
