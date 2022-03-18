import sqlite3

class Model():
    def __init__(self):
        self.verbindung = sqlite3.connect("model/inventar.db")
        self.zeiger = self.verbindung.cursor()

    def getInventory(self): #Ausgabe aller Datensätze
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
    
    def addInventory(self, name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung): #Einfügen eines Datensatzes(Values as String with Value, Empty → None)
        self.zeiger.execute('INSERT INTO "Material" (Name, Typ, Kategorie, Raum, Ausgeliehen, Status, Anzahl, Bemerkung) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung))
        mID = self.zeiger.lastrowid
        self.verbindung.commit()
        return(mID)
    
    def deleteInventory(self, mID):#Löschen eines Datensatzes
        sql = "DELETE FROM Material WHERE mID='"+mID+"';"
        self.zeiger.execute(sql)
        self.verbindung.commit()
        
    def updateInventory(self,mID, name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung): #Updaten eines Datensatzes (Values as String with Value, Empty → None)
        self.zeiger.execute('UPDATE "Material" SET Name = ?, Typ = ?, Kategorie = ?, Raum = ?, Ausgeliehen = ?, Status = ?, Anzahl = ?, Bemerkung = ? WHERE mID = ?;', (name,typ,kategorie,raum,ausgeliehen,status,anzahl,bemerkung,mID))
        self.verbindung.commit()
        
    def altsortInventory(self, column, direction): #Sortieren, dass keine Suche und Filterung berücksichtigt
        sql = "SELECT * from Material ORDER BY {}".format(column)+" "+direction+""
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def sortInventory(self, search, direction, sortcolumn = "mID", filtercolumn = None): #Sortieren, welches Suche und Filterung berücksichtigt
        sql = "SELECT * from Material"
        if filtercolumn != None:
            sql += " WHERE {}".format(filtercolumn)
        else:
            sql += " WHERE Name OR Bemerkung"
        sql += " LIKE '%"+search+"%' ORDER BY {}".format(sortcolumn)+" "+direction+""
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def getColumns(self): #Ausgabe aller Spaltennamen
        sql = "select name FROM pragma_table_info('Material') as tblInfo"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def getKategorien(self):# Ausgabe aller vorhandenen Kategorien
        sql = "SELECT Kategorie FROM Material group by Kategorie"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def checkInventory(self,name,typ,kategorie,raum,mID="%%"):#Überprüfung anhand Name Typ Kategorie und Raum ob ein Datensatz bereits vorhanden ist
        self.zeiger.execute('SELECT * FROM "Material" WHERE Name = ? And Typ = ? AND Kategorie = ? AND Raum = ? and mID LIKE ?;', (name,typ,kategorie,raum,mID))
        if self.zeiger.fetchall()!=[]:
            return True
        return False
    
    def getData(self,mID): #Ausgabe eines Datensatzes mittels ID(ID als "String")
        sql = "SELECT * FROM Material WHERE mID = '"+str(mID)+"';"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    def idData(self,mID):  #Gibt Datensatz mit gewählter ID aus, falls nicht vorhanden None
        self.zeiger.execute('SELECT * FROM "Material" WHERE mID = ?', [mID])
        fetched_data = self.zeiger.fetchall()
        if fetched_data == []:
            return None
        return fetched_data[0]
    
    def filterAll(self,mID,search,typ,kategorie,raum,ausgeliehen,status,min,max,sort,direction): #empty as %; search as search without %; Anzahl bei GG egal
        ausgeliehenisnull = ""
        if ausgeliehen == "%":
            ausgeliehenisnull = " OR Ausgeliehen IS NULL "
        statusisnull = ""        
        if status == "%":
            statusisnull = ''' OR Status IS NULL '''
        if min == "%":
            min = 0
        if max == "%":
            max = 2147483647
        if mID != "":
            mID = f'AND mID = {mID} '            
        sql = f'SELECT * FROM "Material" WHERE (Name LIKE "%{search}%" OR Bemerkung LIKE "%{search}%") AND Typ LIKE "{typ}" AND Kategorie LIKE "{kategorie}" AND Raum LIKE "{raum}" AND (Ausgeliehen LIKE "{ausgeliehen}"{ausgeliehenisnull}) AND (Status LIKE "{status}"{statusisnull}) {mID}AND Anzahl >= {min} AND Anzahl <= {max}  ORDER BY "{sort}" {direction}'
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]


if __name__ == '__main__':
    # Für tests
    pass
