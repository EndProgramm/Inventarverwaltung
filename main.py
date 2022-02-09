# -*- coding: utf-8 -*-
# Controller für die Inventarverwaltung

from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()


if __name__ == '__main__':
    # Für tests des Controllers (Achtung greift natürlich trotzdem auf die anderen Teile zu!)
    pass
