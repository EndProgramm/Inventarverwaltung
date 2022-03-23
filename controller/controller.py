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
        """
        Gibt die Daten der Tabelle formatiert zurück
        """
        abfrage = self.model.filterAll("", self.such, self.filter["typ"], self.filter["kategorie"], self.filter["raum"],
                                       self.filter["ausleibahrkeit"], self.filter["zustand"], self.filter['anzahl_von'],
                                       self.filter['anzahl_bis'], self.sortierung,
                                       self.direction)  # die gespeicherten Filter werden angewendet
        erg = [[spalte] for spalte in
               ['ID', 'Name', 'Typ', 'Kategorie', 'Raum', 'Ausgeliehen', 'Zustand', 'Anzahl',
                'Bemerkung']]  # die Spaltennamen für die Tabelle
        for liste in abfrage:  # Daten werden formatiert, damit kivy die Daten ordentlich in dei Tabelle eintragen kann
            for i, element in enumerate(liste):
                erg[i].append(element)
        return {zeile[0] if len(zeile) > 0 else print(len(zeile)): {i: spalte for i, spalte in enumerate(zeile[1:])} for
                zeile in erg}  # Daten werden fertig formatiert und ans view zurückgegeben

    def saveObject(self, newObject: dict) -> str:
        """
        Speichert ein Objekt in der Datenbank, falls dieses bereits eine ID hat, wird dieses in der Datenbank
        aktualisiert.
        Sollte das Objekt nicht alle benötigten Argumente aufweisen oder beim Speichern zu einem Fehler kommen, so wird
        eine Fehlermeldung als String zurückgegeben.
        """
        if newObject.get("ID") is not None:
            self.model.updateInventory(str(newObject.get("ID")), newObject.get("name"), newObject.get("typ"),
                                       newObject.get("kategorie"), newObject.get("raum"),
                                       newObject.get("ausgeliehen"), newObject.get("zustand"),
                                       newObject.get("anzahl"), newObject.get("bemerkung"))
        else:
            if newObject.get("bemerkung") is None or newObject.get("bemerkung") == "None":
                newObject["bemerkung"] = ""
            if newObject.get("kategorie") == "Gg":
                newObject["anzahl"] = 1
            if newObject.get("name") == "":
                return "Es fehlt der Name!"
            if newObject.get("raum") == "":
                return "Es fehlt der Raum!"
            if newObject.get("kategorie") == "":
                return "Es fehlt die Kategorie!"
            if self.existsObject(self.model.addInventory(newObject.get("name"), newObject.get("typ"),
                                                         newObject.get("kategorie"), newObject.get("raum"),
                                                         newObject.get("ausgeliehen"), newObject.get("zustand"),
                                                         newObject.get("anzahl"), newObject.get("bemerkung"))):
                return "Unbekannter Fehler!"

    def existsObject(self, ID: int) -> bool:
        """
        Es wird geprüft, ob eine ID bereits in der Datenbank gespeichert ist.
        Returns True, wenn es vorhanden ist und False nicht.
        """
        if self.model.getData(ID):
            return False
        else:
            return True

    def getObjectByID(self, ID: int) -> dict:
        """
        Returns ein Objekt aus der Datenbank, für die gegebene ID.
        Falls für die gegebene ID kein Objekt in der Datenbank gefunden werden konnte
        """
        material = self.model.getData(str(ID))
        if material:
            return {'ID': ID, 'name': material[0][1], 'typ': material[0][2], 'kategorie': material[0][3],
                    'raum': material[0][4], 'ausgeliehen': material[0][5], 'zustand': material[0][6],
                    'anzahl': material[0][7], 'bemerkung': material[0][8]}
        else:
            return {'ID': ID, 'name': "null", 'typ': "null", 'kategorie': "null", 'raum': 'null',
                    'ausgeliehen': "null", 'zustand': "null", 'anzahl': "null", 'bemerkung': "null"}

    def delObject(self, ID: int) -> bool:
        """
        Für die gegebene ID wird der dazugehörige Datensatz in der Datenbank gelöscht.
        """
        self.model.deleteInventory(ID)
        return self.existsObject(ID)

    def getKategorie(self):
        """
        Gibt alle Werte, welche in der Spalte Kategorie stehen zurück
        """
        return [i[0] for i in self.model.getKategorien()]

    def sortBy(self, sortierung: str) -> dict[dict]:
        """
        Sortiert die Datensätze nach einer bestimmten Spalte.
        Falls diese Sortierung bereits vorhanden ist, wird sie umgedreht:
        ASC -> DESC
        DESC -> ASC
        """
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
        """
        Speichert den angegebenen Filter und wendet diesen an.
        Passt die Werte des Filters an die vorgaben der Datenbank an.
        """
        stehtfuer = {"kein Filter": "%", "": "%", "Gebrauch": "Gg", "Verbrauch": "Vg", "funktionsfähig": "True",
                     "defekt": "False"}
        for i in filterDict:
            if filterDict[i] in stehtfuer:
                self.filter[i] = stehtfuer[filterDict[i]]
            else:
                self.filter[i] = filterDict[i]
        return self.getData()

    def suche(self, suchbegriff: str) -> dict[dict]:
        """
        Die Datenbank wird nach dem Suchbegriff durchsucht und alle Ergebnisse zurückgegeben.
        Der Suchbegriff wird gespeichert.
        """
        self.such = f"%{suchbegriff}%"
        return self.getData()

    def getFilter(self):
        #der Filter wird zurück gegeben und die Formatierung der Datenbank an die Formatierung des Filters angepasst
        stehtfuerrueckwarts = {"%": "kein Filter", "Gg": "Gebrauch", "Vg": "Verbrauch", "True": "funktionsfähig",
                               "False": "defekt"}
        filterDict = {'typ': '%', 'kategorie': '%', 'raum': '%', 'zustand': '%', 'anzahl_von': '%', 'anzahl_bis': '%',
                      'ausleibahrkeit': '%'}
        for i in self.filter:
            if self.filter[i] in stehtfuerrueckwarts:
                filterDict[i] = stehtfuerrueckwarts[self.filter[i]]
            else:
                filterDict[i] = self.filter[i]
        if filterDict["anzahl_von"] == "kein Filter":#im Filter steht wenn die Anzahl nicht angeben wird nichts und nicht kein Filter wie bei den anderen
            filterDict["anzahl_von"] = ""
        if filterDict["anzahl_bis"] == "kein Filter":
            filterDict["anzahl_bis"] = ""
        return filterDict

    def defektmelden(self, mID):
        #in der Datenbank wird bei einer bestimmten ID der Zustand oder Status in defekt geändert
        x = self.model.filterAll(mID, "%", "%", "%", "%", "%", "%", "%", "%", self.sortierung, self.direction)
        self.model.updateInventory(mID, x[0][1], x[0][2], x[0][3], x[0][4], x[0][5], "False", x[0][7], x[0][8])


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
