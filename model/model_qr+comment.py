import sqlite3
import qrcode
from kivy.uix.image import Image
from time import strftime
import cv2

class Model():
    
    #stellt Verbindung zur Datenbank her
    def __init__(self): 
        self.verbindung = sqlite3.connect("model\inventar.db")
        self.zeiger = self.verbindung.cursor()

    #Ausgabe aller Datensätze
    def getInventory(self):
        sql = 'SELECT * FROM Material;' 
        self.zeiger.execute(sql) #Ausführen der SQL-Anfrage
        return [dsatz for dsatz in self.zeiger] #Formatierung
    
    #Suche nach Suchbegriff in Beliebiger Spalte
    def filterInventory(self,column,search): 
        sql = "SELECT * FROM Material WHERE {}".format(column) +" LIKE '%"+str(search)+"%'"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Suche nur in Namen und Bemerkungen
    def searchInventory(self,search): 
        sql = "SELECT * FROM Material WHERE Name OR Bemerkung LIKE '%"+str(search)+"%'"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Einfügen eines Datensatzes(Empty → None)
    def addInventory(self, name,typ,kategorie,raum,ausgeliehen,zustand,anzahl,bemerkung): #Rückgabe → ID as Integer
        self.zeiger.execute('INSERT INTO "Material" (Name, Typ, Kategorie, Raum, Ausgeliehen, Zustand, Anzahl, Bemerkung) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (name,typ,kategorie,raum,ausgeliehen,zustand,anzahl,bemerkung))
        mID = self.zeiger.lastrowid #Nimmt die zuletzt geschriebene ID
        self.verbindung.commit() #Änderungen schreiben
        return(mID)
    
    #Löschen eines Datensatzes
    def deleteInventory(self, mID):
        sql = "DELETE FROM Material WHERE mID='"+str(mID)+"';"
        self.zeiger.execute(sql)
        self.verbindung.commit()
        
    #Updaten eines Datensatzes (Angabe des Datensatzes über ID, Empty → None)
    def updateInventory(self,mID, name,typ,kategorie,raum,ausgeliehen,zustand,anzahl,bemerkung): 
        self.zeiger.execute('UPDATE "Material" SET Name = ?, Typ = ?, Kategorie = ?, Raum = ?, Ausgeliehen = ?, Zustand = ?, Anzahl = ?, Bemerkung = ? WHERE mID = ?;', (name,typ,kategorie,raum,ausgeliehen,zustand,anzahl,bemerkung,mID))
        self.verbindung.commit()
    
    #Sortieren, welches keine Suche und Filterung berücksichtigt(direction als "asc" oder "desc")
    def altsortInventory(self, column, direction): 
        sql = "SELECT * from Material ORDER BY {}".format(column)+" "+direction+""
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Sortieren, welches Suche und Filterung berücksichtigt(filtercolumn = Spalte, nach der gefiltert wird; sortcolumn = Spalte, nach der sortiert wird; direction als "asc" oder "desc")
    def sortInventory(self, search, direction, sortcolumn = "mID", filtercolumn = None): 
        sql = "SELECT * from Material"
        if filtercolumn != None: #Überprüfen nach Filterung
            sql += " WHERE {}".format(filtercolumn)
        else:
            sql += " WHERE Name OR Bemerkung"
        sql += " LIKE '%"+search+"%' ORDER BY {}".format(sortcolumn)+" "+direction+""
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Ausgabe aller Spaltennamen
    def getColumns(self): 
        sql = "select name FROM pragma_table_info('Material') as tblInfo"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Ausgabe aller vorhandenen Kategorien
    def getKategorien(self):
        sql = "SELECT Kategorie FROM Material group by Kategorie"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Überprüfung anhand Name, Typ, Kategorie und Raum, ob ein Datensatz bereits vorhanden ist
    def checkInventory(self,name,typ,kategorie,raum,mID="%%"):
        self.zeiger.execute('SELECT * FROM "Material" WHERE Name = ? And Typ = ? AND Kategorie = ? AND Raum = ? and mID LIKE ?;', (name,typ,kategorie,raum,mID))
        if self.zeiger.fetchall()!=[]: #Überprüfen, ob Ergebnis vorhanden ist
            return True
        return False
    
    #Ausgabe eines Datensatzes mittels ID
    def getData(self,mID): 
        sql = "SELECT * FROM Material WHERE mID = '"+str(mID)+"';"
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #Gibt Datensatz mit gewählter ID aus, falls nicht vorhanden None
    def idData(self,mID):  
        self.zeiger.execute('SELECT * FROM "Material" WHERE mID = ?', [mID])
        fetched_data = self.zeiger.fetchall()
        if fetched_data == []: #Überprüfen, ob leer
            return None
        return fetched_data[0] #Ausgabe als Tupel (maximal ein Datensatz)
    
    #Filterfunktion mit allen Filtereinstellungen, sowie Sortierfuktion (mID empty als "", sonst empty als "%")
    def filterAll(self,mID,search,typ,kategorie,raum,ausgeliehen,zustand,min,max,sort,direction): 
        ausgeliehenisnull = ""
        if ausgeliehen == "%": #testen ob ausgelliehen leer
            ausgeliehenisnull = " OR Ausgeliehen IS NULL "
        zustandisnull = ""   #testen ob zustand leer
        if zustand == "%":
            zustandisnull = ''' OR Zustand IS NULL '''
        if min == "%":   #Defaultwert = 0
            min = 0
        if max == "%":  #Defaultwert = 2^63
            max = 9223372036854775808
        if mID != "":   #testen ob Id leer ist
            mID = f'AND mID = {mID} '
        #sql-Anfrage, mit allen Filteroptionen in einer Anfrage (Suche,Filter aller Kategorien,Sortieren) unter berücksichtigung der Datenbankstruktur
        sql = f'SELECT * FROM "Material" WHERE (Name LIKE "%{search}%" OR Bemerkung LIKE "%{search}%") AND Typ LIKE "{typ}" AND Kategorie LIKE "{kategorie}" AND Raum LIKE "{raum}" AND (Ausgeliehen LIKE "{ausgeliehen}"{ausgeliehenisnull}) AND (Zustand LIKE "{zustand}"{zustandisnull}) {mID}AND Anzahl >= {min} AND Anzahl <= {max}  ORDER BY "{sort}" {direction}'
        self.zeiger.execute(sql)
        return [dsatz for dsatz in self.zeiger]
    
    #erstellt QR-Code mit Inhalt "inhalt" mit nahmen "qrcode.png"
    def qrCode(self,inhalt): 
        qr = qrcode.QRCode()
        qr.add_data(inhalt)
        qr.make(fit=True)        
        img = qr.make_image(fill_color="black", back_color="white")
        qrCodeName= "qrcode.png"
        img.save(qrCodeName)
        
    #liest QR-Code aus filename aus und gibt Daten falls möglich zurück
    def qrDecode(self,filename):
        img = cv2.imread(filename)
        det = cv2.QRCodeDetector()
        data,x,y = det.detectAndDecode(img)
        if x is not None:
            return(data)
        else:
            return("error")

if __name__ == '__main__':
    # Für tests
    pass
