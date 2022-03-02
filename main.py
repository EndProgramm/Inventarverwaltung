# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

"""
Beschreibung: \n
Basis der UI, implementiert mit UIApp
"""

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
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from controller.controller import Controller

control = Controller()


class AddInv(Screen):
    pass


class AddConsum(Screen):
    def saveInv(self):
        popup = Popup(title='Gespeichert',
                      content=Label(text="Neues Verbrauchsmaterial\nwurde gespeichert!"),
                      size_hint=(None, None), size=(200, 100))
        popup.open()


class Popups(FloatLayout):
    popup_close = ObjectProperty(None)
    typ_spinner=ObjectProperty()
    kategorie_spinner=ObjectProperty()
    raum_ent=ObjectProperty()
    zustand_spinner=ObjectProperty()
    anzahl_von_ent=ObjectProperty()
    anzahl_bis_ent=ObjectProperty()
    ausleihbar_spinner = ObjectProperty()
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
        print(dict)


class ShowAll(Screen):
    pass


class AddUses(Screen):
    def saveInv(self):
        if control.saveObejct():  # Hier ist der Callback
            popup = Popup(title='Gespeichert',
                          content=Label(text="Neues Gebrauchsmaterial\nwurde gespeichert!"),
                          size_hint=(None, None), size=(200, 100))
        popup.open()


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)

        abfage = control.getData()
        self.data = {int(key): {spalte: str(wert) for spalte, wert in enumerate(inhalt)} for key, inhalt in
                     enumerate(abfage)}


class Table(BoxLayout):
    def __init__(self, table='', **kwargs):
        super().__init__(**kwargs)

        data = control.getData()

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

        # self.ids.table_floor_layout.cols = self.columns   # define value of cols to the value of self.columns
        # self.ids.table_floor.data = self.table_data       # add self.table_data to data value

    def callback_suche(self, text):
        print(text)

    def filter(self):
        show = Popups(popup_close=self.popup_close)
        self.popupWindow = Popup(title="Filter", title_align="center",
                                 content=show, auto_dismiss=True,
                                 size_hint=(None, None), size=(300, 400))
        self.popupWindow.open()

    def popup_close(self):
        self.popupWindow.dismiss()




class UIApp(App):
    """
    Basis der UI
    """

    def build(self):
        Window.size = (800, 600)
        sManage = ScreenManager()
        sManage.add_widget(AddInv(name='addInv'))
        sManage.add_widget(AddConsum(name='addConsum'))
        sManage.add_widget(AddUses(name='addUses'))
        sManage.add_widget(ShowAll(name='showAll'))
        sManage.current = 'showAll'
        return sManage


if __name__ == '__main__':
    # Für tests am View
    UIApp().run()
