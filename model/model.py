import sqlite3

class Model():
    def __init__(self):
        self.verbindung = sqlite3.connect("inventar.db")
        self.zeiger = self.verbindung.cursor()

    def getInventory(self):
        sql = 'SELECT * FROM Material;'
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def filterInventory(self,column,search): #Suche nach Suchbegriff in Beliebiger Spalte
        sql = "SELECT * FROM Material WHERE {}".format(column) +" LIKE '%"+search+"%'"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def searchInventory(self,search): #Suche nur in Namen und Bemerkungen
        sql = "SELECT * FROM Material WHERE Name OR Bemerkung LIKE '%"+search+"%'"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]

