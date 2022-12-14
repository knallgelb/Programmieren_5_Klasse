# Variablen

Variablen speichern Werte und haben den Vorteil, dass man sie anschließend an derer Stelle wiederverwenden kann.

Ihr kennt wahrscheinlich Variablen aus der Mathematik.

Dort werden die Variablennamen **"x, y, z, ..."** verwendet.

Beim Programmieren verwendet man sprechende Namen für Variablen!

Beispiele dafür sind:
* vorname
* nachname
* klasse
* strasse
* lieblings_essen
* weihnachts_wuensche
* etc.

## Einer Variablen einen Wert zuweisen

Einer Variablen weist man über ein `=` einen Wert zu.

Dabei steht die Variable `links` dann ein `=` und rechts der Wert bzw. was man machen möchte.

### Beispiele

```python
vorname = "Maxime"
nachname = "Musterfrau"
lieblings_essen = "Salzbuger Nockerl"
letzte_schulnote_deutsch = 3
```

## Variablen an anderer Stelle wiederverwenden

### Beispiele

```python
vorname = "Maxime"
nachname = "Musterfrau"
lieblings_essen = "Salzbuger Nockerl"
letzte_schulnote_deutsch = 3

# Ausgabe am Bildschirm
print(f"{vorname} {nachname} isst gerne {lieblings_essen}.")

laenge = 3
breite = 7
flaeche = laenge * breite

print(f"Ein Rechteck mit der Länge {laenge} und der Breite {breite} hat eine Fläche von {flaeche}.")

schularbeitsnoten_mathematik = [3, 2, 4, 2, 5, 2]

print(f"Die beste Mathematiknote von {vorname} war {min(schularbeitsnoten_mathematik)}.")

print(f"Die schlechteste Mathematiknote von {vorname} war {max(schularbeitsnoten_mathematik)}.")

print(f"{vorname} hat an {len(schularbeitsnoten_mathematik)} Mathematikschularbeiten teilgenommen.")

print(f"Die Summe aller Mathematiknoten war {sum(schularbeitsnoten_mathematik)}.")

print(f"Der Druchschnitt aller Mathematiknoten von {vorname} war {sum(schularbeitsnoten_mathematik) / len(schularbeitsnoten_mathematik)}.")
```