# User Input

In Python Programmen kann man auch direkt den User Input abfragen.

Das funktioniert über `input()` Methode.

Daten, die man über `input()` erhält, sind immer Strings. D.h. möchte man damit rechnen, dann müssen diese umgewandelt
werden.

## Beispiel

```python
vorname = input("Wie lautet dein Vorname? ")
lieblings_essen = input("Wie lautet dein Lieblingsessen? ")
alter = input("Wie alt bist du? ")

bis_ich_18_bin = 18 - int(alter)

print(f"{vorname} wird in {bis_ich_18_bin} Jahren 18. Jahre alt und isst am liebsten {lieblings_essen}.")



```