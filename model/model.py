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
    
    def addInventory(self, name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung): #Values as String with Value, Empty → None
        self.zeiger.execute('INSERT INTO "Material" (Name, Typ, Kategorie, Raum, Ausgeliehen, Status, Anzahl, Bemerkung) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung))
        id = self.zeiger.lastrowid
        self.verbindung.commit()
        return(id)
    
    def deleteInventory(self, mId):
        sql = "DELETE FROM Material WHERE id='"+mId+"';"
        self.zeiger.execute(sql)
        self.verbindung.commit()
        
    def updateInventory(self,id, name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung): #Values as String with Value, Empty → None
        self.zeiger.execute('UPDATE "Material" SET Name = ?, Typ = ?, Kategorie = ?, Raum = ?, Ausgeliehen = ?, Status = ?, Anzahl = ?, Bemerkung = ? WHERE MID = ?;', (name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung,id))
        self.verbindung.commit()
        
    def altsortInventory(self, column, direction):
        sql = "SELECT * from Material ORDER BY {}".format(column)+" "+direction+""
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def sortInventory(self, search, direction, sortcolumn = "MID", filtercolumn = None):
        sql = "SELECT * from Material"
        if filtercolumn != None:
            sql += " WHERE {}".format(filtercolumn)
        else:
            sql += " WHERE Name OR Bemerkung"
        sql += " LIKE '%"+search+"%' ORDER BY {}".format(sortcolumn)+" "+direction+""
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def getColumns(self):
        sql = "select name FROM pragma_table_info('Material') as tblInfo"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def getKategorien(self):
        sql = "SELECT Kategorie FROM Material group by Kategorie"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def data_check(self,name,typ,kategorie,raum,id="%%"):
        self.zeiger.execute('SELECT * FROM "Material" WHERE Name = ? And Typ = ? AND Kategorie = ? AND Raum = ? and MID LIKE ?;', (name,typ,kategorie,raum,id))
        if self.zeiger.fetchall()!=[]:
            return True
        return False
    
    def id_data(self,id):
        self.zeiger.execute('SELECT * FROM "Material" WHERE MID = ?;', (id))
        return(self.zeiger.fetchall())[0]


if __name__ == '__main__':
    # Für tests
    pass

