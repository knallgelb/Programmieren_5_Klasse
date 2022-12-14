# Abfragen

Für Entscheidungen verwendet man in Python `IF-Abfragen`.

D.h. man stellt eine Frage und reagiert anschließend darauf.

Die funktionieren wie folgt:

```
Wenn Bedingung erfüllt:
    mach was
[Wenn andere Bedingung erfüllt:]
    auch was machen
[sonst]
    mach in allen anderen Fällen was anderes
```

[...] sind optionale Angaben.

## Bedingungen

Das Ergebnis von einer Abfrage ist immer ein `Boolscher Wert`. D.h. es kommt entweder True (Wahr) oder False (Falsch)
heraus.

### Vergleichsoperatoren
```
== gleich

!= ungleich

< kleiner

<= kleiner gleich

> größer

>= größer gleich
```

Bedingungen können auch verknüpft werden. Das funktioniert dann über `and` bzw. `or`.

## Abfragen über Einrückung strukturieren

Damit Python weiß, was wohin gehört, verwendet es Einrückungen.

Passt die Einrückung nicht, dann bekommt man eine Fehlermeldung. Hier hilft lesen, um das Problem schnell zu lösen.

## Beispiele

```python
if 6 < 5:
    print("JA")

print(6 < 5)
print(5 < 6)

result = 5 < 6
if result:
    print("5 ist kleiner als 6")
```

```python
alter_text = input("Wie alt bist du? ")

alter_zahl = int(alter_text)

if alter_zahl >= 14:
    print("Du darfst in allen Bundesländern, bis auf Oberösterreich, bis mindestens 1h ausgehen")
else:
    print("Du darfst nur zwischen 5 und 23 Uhr unterwegs sein.")

```