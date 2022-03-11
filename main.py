# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

"""
Beschreibung: \n
Basis der UI, implementiert mit UIApp
"""
import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

from controller.controller import Controller

control = Controller()


class AddInv(Screen):
    addUses = ObjectProperty()
    addConsum = ObjectProperty()
    showAll = ObjectProperty()
    einzelansicht = ObjectProperty()


class AddConsum(Screen):
    def saveInv(self):
        popup = Popup(title='Gespeichert',
                      content=Label(text="Neues Verbrauchsmaterial\nwurde gespeichert!"),
                      size_hint=(None, None), size=(200, 100))
        popup.open()


class Popups(FloatLayout):
    popup_close = ObjectProperty(None)
    typ_spinner = ObjectProperty()
    kategorie_spinner = ObjectProperty()
    raum_ent = ObjectProperty()
    zustand_spinner = ObjectProperty()
    anzahl_von_ent = ObjectProperty()
    anzahl_bis_ent = ObjectProperty()
    ausleihbar_spinner = ObjectProperty()

    def kategorie(self):
        return control.getKategorie()

    def speichern(self):
        dict = {
            "typ": self.typ_spinner.text,
            "kategorie": self.kategorie_spinner.text,
            "raum": self.raum_ent.text,
            "zustand": self.zustand_spinner.text,
            "anzahl_von": self.anzahl_von_ent.text,
            "anzahl_bis": self.anzahl_bis_ent.text,
            "ausleibahrkeit": self.ausleihbar_spinner.text
        }

class Popup_add_GG(FloatLayout): #Gebrauchsgegenstand
    popup_add_GG_close = ObjectProperty(None)
    name_ent=ObjectProperty()
    kategorie_ent=ObjectProperty()
    raum_ent=ObjectProperty()
    zustand_spinner=ObjectProperty()
    bemerkung_ent=ObjectProperty()
    ausleihbar_checkbox = ObjectProperty()
    def speichern(self):
        dict = {
            "name": self.name_ent.text,
            "typ": "Gg",
            "kategorie": self.kategorie_ent.text,
            "raum": self.raum_ent.text,
            "ausleibahrkeit": self.ausleihbar_checkbox.active, #Wert zurückbekommen (sowas wie self.kategorie.text)
            "zustand": self.zustand_spinner.text,
            "Bemerkung": self.bemerkung_ent.text
        }
        print(dict)


class ShowAll(Screen):
    pass

class Einzelansicht(Screen):
    pass

class AddUses(Screen):
    def saveInv(self):
        if control.saveObejct():  # Hier ist der Callback
            popup = Popup(title='Gespeichert',
                          content=Label(text="Neues Gebrauchsmaterial\nwurde gespeichert!"),
                          size_hint=(None, None), size=(200, 100))
        popup.open()


class TableBox(BoxLayout):
    def __init__(self, data, columns, **kwargs):
        self.table_data = data
        self.columns = columns
        super().__init__(**kwargs)


class Table(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.columns: int = 0
        self.table_data: list = []
        self.popupWindow: Popup or None = None

        self.createTableData(control.getData())

    def createTableData(self, data: dict[str, dict[int, str]]):
        column_titles = [x for x in data.keys()]
        rows_length = len(data[column_titles[0]])
        self.columns = len(column_titles)

        self.table_data = []

        for y in column_titles:
            self.table_data.append(
                {'text': str(y), 'size_hint_y': None, 'height': 30, 'bcolor': (1.0, .31, 0.0, 1)})
        for z in range(rows_length):
            for y in column_titles:
                self.table_data.append(
                    {'text': str(data[y][z]), 'size_hint_y': None, 'height': 20, 'bcolor': (.06, .25, .50, 1)})

    def callback_suche(self, text: str):
        self.createTableData(control.getData())
        self.createTable()

    def createTable(self):
        self.clear_widgets(self.children[:1])
        self.add_widget(TableBox(self.table_data, self.columns))

    def filter(self):
        show = Popups(popup_close=self.popup_close)
        self.popupWindow = Popup(title="Filter", title_align="center",
                                 content=show, auto_dismiss=True,
                                 size_hint=(None, None), size=(300, 400))
        self.popupWindow.open()

    def add_GG(self):
        show = Popup_add_GG(popup_add_GG_close=self.popup_add_GG_close)
        self.popupWindow_add_GG = Popup(title="Gebrauchsgegenstand hinzufügen", title_align="center",
                                 content=show, auto_dismiss=True,
                                 size_hint=(None, None), size=(300, 400))
        self.popupWindow_add_GG.open()

    def popup_add_GG_close(self):
        self.popupWindow_add_GG.dismiss()

    def popup_close(self):
        self.popupWindow.dismiss()


class UIApp(App):
    """
    Basis der UI
    """

    def build(self):
        Window.size = (800, 600)
        self.sManage = ScreenManager()
        self.sManage.add_widget(AddInv(name='addInv'))
        self.sManage.add_widget(AddConsum(name='addConsum'))
        self.sManage.add_widget(AddUses(name='addUses'))
        self.sManage.add_widget(ShowAll(name='showAll'))
        self.sManage.add_widget(Einzelansicht(name='einzelansicht'))
        self.sManage.current = 'showAll'
        return self.sManage


if __name__ == '__main__':
    # Für tests am View
    UIApp().run()
