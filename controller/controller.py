# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from model.datenbank import DB


class Controller:
    def __init__(self):
        self.model = DB()

    def getData(self) -> dict[dict]:
        return None

    def saveUses(self) -> bool:
        pass


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    c = Controller()
