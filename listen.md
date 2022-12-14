# Listen
Können mehrere Werte aufnehmen. Siehe [datentypen](datentypen.md).

## Listen abarbeiten
Um für jeden Wert in einer Liste eine bestimmte Aktion durchzuführen, kann man eine `For-Schleife` verwenden.

### For-Schleife
Z.B. möchte man für jeden Wert in der Liste *Wünsche* seinen Eltern anschreiben.

### Beispiel
```python
meine_wuensche = ["ein neues Computerspiel", "einen Urlaub", "eine Husky Schlittenfahrt"]

vorname = input("Wer wünscht sich was? ")
wunsch_fuer_ereignis = input("Weihnachten, Geburtstag, ... was darf es sein? ")

for wunsch in meine_wuensche:
    print(f"""Liebe Mama, Lieber Papa,
        Ich wünsche mir dieses Jahr zu {wunsch_fuer_ereignis} {wunsch}.
        Ich hab euch ganz doll lieb.
        Dickes Bussi --{vorname}--
        """)
```

## Abfragen: Elemente in der Liste vorhanden?
Es gibt die Möglichkeit nachzufragen, ob ein Element in der Liste vorhanden bzw. nicht vorhanden ist.

Das funktioniert über das Wort `in`.

Verneinen kann man das mit `not`.

### Beispiel

```python
noten = [2,1,4,3,2,5,2]

if 5 in noten:
    print("Dieses Jahr war leider ein Fünfer dabei. Mach es nächstes Jahr besser!")

namen = ["Max", "Heinz", "Bubi", "Flora", "Vali", "Marianne"]

if "Rainer" not in namen:
    print("Bei euch gibt es keinen Rainer.")
```

## Minimum / Maximum / Summe
In Python kann man über die Funktionen
* `min(liste)` das Minimum der Liste
* `max(liste)` das Maximum der Liste
* `sum(liste)` die Summe der Liste

herausfinden.

### Beispiele

Siehe auch [Variablen](variablen.md).

```python
noten = [2,1,4,3,2,5,2]
minimum = min(noten)
maximum = max(noten)
summe = sum(noten)
```