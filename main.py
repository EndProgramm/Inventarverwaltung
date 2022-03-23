# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

"""
Beschreibung: \n
Basis der UI, implementiert mit UIApp
"""
import time

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from controller.controller import Controller

control = Controller()
id: int = 0


class AddInv(Screen):
    addUses = ObjectProperty()
    addConsum = ObjectProperty()
    showAll = ObjectProperty()


class AddConsum(Screen):
    def saveInv(self):
        popup = Popup(title='Gespeichert',
                      content=Label(text="Neues Verbrauchsmaterial\nwurde gespeichert!"),
                      size_hint=(None, None), size=(200, 100))
        popup.open()


class Popups(FloatLayout): # Popup von Button 'Filter'
    popupClose = ObjectProperty(None)
    refreshTable = ObjectProperty(None)

    # Eingabe wird gespeichert:
    typSpinner = ObjectProperty()
    kategorieSpinner = ObjectProperty()
    raumEnt = ObjectProperty()
    zustandSpinner = ObjectProperty()
    anzahlVonEnt = ObjectProperty()
    anzahlBisEnt = ObjectProperty()
    ausleihbarSpinner = ObjectProperty()

    def kategorie(self): # gibt alle Kategorien zurück
        return control.getKategorie()

    def speichern(self):
        # ausgewählte Filter werden gespeichert
        dict = {
            "typ": self.typSpinner.text,
            "kategorie": self.kategorieSpinner.text,
            "raum": self.raumEnt.text,
            "zustand": self.zustandSpinner.text,
            "anzahl_von": self.anzahlVonEnt.text,
            "anzahl_bis": self.anzahlBisEnt.text,
            "ausleibahrkeit": self.ausleihbarSpinner.text
        }
        return control.filterSpeichern(dict) #In der Datenbank wird mit Filtern gesucht


class PopupAddGG(FloatLayout):  # Gebrauchsgegenstand hinzufügen
    popupAddGGClose = ObjectProperty(None)

    # Eingabe wird gespeichert:
    nameEnt = ObjectProperty()
    kategorieEnt = ObjectProperty()
    raumEnt = ObjectProperty()
    zustandSpinner = ObjectProperty()
    bemerkungEnt = ObjectProperty()
    ausleihbarCheckbox = ObjectProperty()

    def speichern(self):
        dict = {
            "name": self.nameEnt.text,
            "typ": "Gg",
            "kategorie": self.kategorieEnt.text,
            "raum": self.raumEnt.text,
            "ausleibahrkeit": self.ausleihbarCheckbox.active,
            "zustand": self.zustandSpinner.text,
            "bemerkung": self.bemerkungEnt.text
        }
        fehlermeldung = control.saveObject(dict)
        if fehlermeldung:
            popup = Popup(title='Fehler', title_align="center",
                          content=Label(text=fehlermeldung),
                          size_hint=(None, None), size=(200, 100))
            popup.open()


class PopupAddVG(FloatLayout):  # Verbrauchsgegenstand
    popupAddVGClose = ObjectProperty(None)
    nameEnt = ObjectProperty()
    kategorieEnt = ObjectProperty()
    raumEnt = ObjectProperty()
    zustandSpinner = ObjectProperty()
    bemerkungEnt = ObjectProperty()
    anzahlEnt = ObjectProperty()

    def speichern(self):
        dict = {
            "name": self.nameEnt.text,
            "typ": "Vg",
            "kategorie": self.kategorieEnt.text,
            "raum": self.raumEnt.text,
            "anzahl": self.anzahlEnt.text,
            "zustand": self.zustandSpinner.text,
            "bemerkung": self.bemerkungEnt.text
        }
        fehlermeldung = control.saveObject(dict)
        if fehlermeldung:
            popup = Popup(title='Fehler', title_align="center",
                          content=Label(text=fehlermeldung),
                          size_hint=(None, None), size=(200, 100))
            popup.open()


class ShowAll(Screen):
    pass

class Einzelansicht(FloatLayout):
    # self.texte: dict[str, any] = {'None': None}
    closeEinzelansicht = ObjectProperty(None)
    entryId = ObjectProperty()
    entryName = ObjectProperty()
    entryAnzahl = ObjectProperty()
    entryKategorie = ObjectProperty()
    entryAusgeliehen = ObjectProperty()
    entryBemerkung = ObjectProperty()
    entryRaum = ObjectProperty()
    entryTyp = ObjectProperty()
    entryZustand = ObjectProperty()

    def entryFill(self):
        global mid
        self.texte = control.getObjectByID(int(mid))
        self.entryId.text = str(self.texte.get("ID", "None"))
        self.entryName.text = str(self.texte.get("name", "None"))
        self.entryRaum.text = str(self.texte.get("raum", "None"))
        self.entryTyp.text = str(self.texte.get("typ", "None"))
        self.entryKategorie.text = str(self.texte.get("kategorie", "None"))
        self.entryAusgeliehen.text = str(self.texte.get("ausgeliehen", "None"))
        self.entryZustand.text = str(self.texte.get("zustand", "None"))
        self.entryAnzahl.text = str(self.texte.get("anzahl", "None"))
        self.entryBemerkung.text = str(self.texte.get("bemerkung", "None"))

    def speichern(self):
        dataNew = {'ID': int(self.entryId.text),
                   'name': self.entryName.text,
                   'raum': self.entryRaum.text,
                   'typ': self.entryTyp.text,
                   'kategorie': self.entryKategorie.text,
                   'ausgeliehen': self.entryAusgeliehen.text,
                   'zustand': self.entryZustand.text,
                   'anzahl': self.entryAnzahl.text,
                   'bemerkung': self.entryBemerkung.text}
        control.saveObject(dataNew)

    def kategorie(self):
        return control.getKategorie()

    def defektmelden(self):
        # control.defektmelden(int(self.ids.entryId.text))
        pass


class AddUses(Screen):
    def saveInv(self):
        if control.saveObject():  # Hier ist der Callback
            popup = Popup(title='Gespeichert',
                          content=Label(text="Neues Gebrauchsmaterial\nwurde gespeichert!"),
                          size_hint=(None, None), size=(200, 100))
        popup.open()


class TableBox(BoxLayout):
    def __init__(self, data, columns, **kwargs):
        self.tableData = data
        self.columns = columns
        super().__init__(**kwargs)
        self.columns: int = 0
        self.tableData: list = []
        self.popupWindow: Popup or None = None


class Table(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.columns: int = 0
        self.tableData: list = []
        self.popupWindow: Popup or None = None
        self.popupEinzelansicht: Popup or None = None
        self.createTableData(control.getData())

    def createTableData(self, data: dict[str, dict[int, str]]):
        columnTitles = [x for x in data.keys()]
        rowsLength = len(data[columnTitles[0]])
        self.columns = len(columnTitles)

        self.tableData = []

        for y in columnTitles:
            self.tableData.append(
                {'text': str(y), 'size_hint_y': None, 'height': 30, 'bcolor': (1.0, .31, 0.0, 1)})
        for z in range(rowsLength):
            for y in columnTitles:
                self.tableData.append(
                    {'text': str(data[y][z]), 'size_hint_y': None, 'height': 20, 'bcolor': (.06, .25, .50, 1)})

    def callbackSuche(self, text: str):
        self.refreshTable(control.suche(text))

    def refreshTable(self, tableData: dict[str, dict[int, str]]):
        self.createTableData(tableData)
        self.createTable()

    def createTable(self):
        self.clear_widgets(self.children[:1])
        self.add_widget(TableBox(self.tableData, self.columns))

    def einzelansicht(self, idInput):
        global mid
        mid = idInput
        show = Einzelansicht(closeEinzelansicht=self.closeEinzelansicht)
        self.popupEinzelansicht = Popup(title="Einzelansicht", title_align="center",
                                        content=show, auto_dismiss=True,
                                        size_hint=(None, None), size=(600, 400))
        self.popupEinzelansicht.open()
        show.entryFill()

    def filter(self):
        show = Popups(popupClose=self.popupClose, refreshTable=self.refreshTable)
        self.popupWindow = Popup(title="Filter", title_align="center",
                                 content=show, auto_dismiss=True,
                                 size_hint=(None, None), size=(300, 400))
        self.popupWindow.open()

    def addGG(self):
        show = PopupAddGG(popupAddGGClose=self.popupAddGGClose)
        self.popupWindowAddGG = Popup(title="Gebrauchsgegenstand hinzufügen", title_align="center",
                                      content=show, auto_dismiss=True,
                                      size_hint=(None, None), size=(300, 400))
        self.popupWindowAddGG.open()

    def addVG(self):
        show = PopupAddVG(popupAddVGClose=self.popupAddVGClose)
        self.popupWindowAddVG = Popup(title="Verbrauchsgegenstand hinzufügen", title_align="center",
                                      content=show, auto_dismiss=True,
                                      size_hint=(None, None), size=(300, 400))
        self.popupWindowAddVG.open()

    def popupClose(self):
        self.popupWindow.dismiss()

    def popupAddGGClose(self):
        self.popupWindowAddGG.dismiss()

    def popupAddVGClose(self):
        self.popupWindowAddVG.dismiss()

    def closeEinzelansicht(self):
        self.popupEinzelansicht.dismiss()
        self.refreshTable(control.getData())

    def sortieren(self, spalte: str):
        table = control.sortBy(spalte)
        self.refreshTable(table)


class UIApp(App):
    """
    Basis der UI
    """

    def build(self):
        Window.size = (1200, 800)
        Window.maximize()
        self.sManage = ScreenManager()
        self.sManage.add_widget(AddInv(name='addInv'))
        self.sManage.add_widget(AddConsum(name='addConsum'))
        self.sManage.add_widget(AddUses(name='addUses'))
        self.sManage.add_widget(ShowAll(name='showAll'))
        self.sManage.current = 'showAll'
        return self.sManage


if __name__ == '__main__':
    # Für tests am View
    UIApp().run()
