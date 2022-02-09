# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from model.datenbank import DB
from view.ui import UIApp


class Controller:
    def __init__(self):
        self.model = DB()
        self.view = UIApp()

        # Code hier

        self.view.run()


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    pass
