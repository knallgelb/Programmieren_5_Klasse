# Aufgaben 4 - Listen

Wie du eine Liste anlegst, findest du hier: [Listen.md](../listen.md)

Hier sind mehrere Teilaufgaben zu lösen. Diese sind jeweils in einer eigenen Datei abzugeben. Siehe den Unterpunkten.

## 4.1 Listen abarbeiten

Erstelle die Datei `einkaufen.py`.

Lege die folgende Variablen an:

* einkaufsliste_gegenstaende (Liste von Strings | was du so einkaufst; mindestens 7 Dinge)
* vorname (String | dein Vorname)

Schreibe eine For-Schleife die für jedes Element in der Liste folgenden Text
ausgibt: `Heute kaufe ich, {vorname}, {den_gegenstand} ein.`

## 4.2 Listen miteinander verschränken

Erstelle die Datei `erweiterung_einkaufen.py`.

Kopiere die Variablen aus `einkaufen.py` in die neue Datei.

Erweitere die Variablen um:

* einkaufsliste_anzahl (Liste an Integers | gleiche Anzahl wie einkaufsliste_gegenstaende)

Beide Listen sind miteinander verschränkt. D.h. Wenn das erste Element in `einkaufsliste_gegenstaende` `Milch`ist, dann
soll das erste Element in `einkaufliste_anzahl` die Anzahl der Packungen darstellen. z.B. 3.

### Beispiel

```python
einkaufsliste_gegenstaende = ["Milch", "Paprika"]
einkaufsliste_anzahl = [3, 2]
```

Erstelle eine neue Variable `einkaufsliste` und weise das Produkt der Funktion `zip` der beiden
Listen, `einkaufsliste_gegenstaende` und `einkaufsliste_anzahl` zu. In [Listen.md](../listen.md) findest du ganz unten
ein Beispiel dazu.

Arbeite anschließend die Variable `einkaufsliste` mit eier For-Schleife ab und gib für jeden Gegenstand folgenden Text
aus: `Ich soll heute {anzahl}x {gegenstand} einkaufen gehen.`.
