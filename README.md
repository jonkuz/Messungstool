# Messungstool
Das vorliegende Skript beinhaltet die Implementierung von insgesamt acht Abfragen, vier für die OLTP- und vier für die OLAP-Umgebung.
Die Abfragen können bis zu 30-mal aufgerufen werden, wobei die jeweiligen Zeiten gespeichert werden. Im Anschluss erfolgt die Berechnung und Ausgabe von Median, Mittelwert und Standardabweichung.
Schließlich werden die Daten in Form eines Boxplots visualisiert.

## Voraussetzungen
- Python Version 3.11.0 installiert
- Python Package requests installiert
- Python Package pandas installiert
- Python Package matplotlib installiert
- Python Package seaborn installiert

## Aufsetzen der Umgebung
- Falls noch nicht installiert: Installation von [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- Klonen des Source-Codes von [github](https://github.com/jonkuz/Messungstool.git)
```
git clone https://github.com/jonkuz/Messungstool.git
```
- Einstellen des Python Interpreter (In Pycharm unten rechts)
- Installieren der Pakete requests, httpx und ClickHouse connect funktioniert in PyCharm auch über den Package Manager. 
  - [requests](https://pypi.org/project/requests/)
  - [pandas](https://pandas.pydata.org/)
  - [matplotlib](https://matplotlib.org/)
  - [seaborn](https://seaborn.pydata.org/index.html)

## Ausführen des Skriptes
Um die API auszuführen, muss in der main-Methode die gewünschte Abfrage angegeben werden.
Die Methoden sind bereits importiert.
Im Anschluss werden Median, Mittelwert und Standardabweichung auf der Konsole ausgegeben.
Das Boxplot wird in einem separaten Tab generiert. 
Mit einem Rechtsklick auf die Vorschau kann das Bild als Datei gespeichert werden.



