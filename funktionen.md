# Funktionen

Mittels Funktionen kann man Code wiederverwenden. Funktionen sind extrem praktisch und sollten sooft es geht verwendet
werden.

Jede Funktion beginnt dabei mit dem Schlüsselwort `def`. Danach folgt der Funktionsname und dann in Klammern die
Parameter. Diese sind allerdings optional.

Danach wird der Code eingerückt, damit weiß Python welcher Code wohin gehört.

Funktionen sollten dabei immer so wenig wie möglich tun.

D.h. sollte eine Funktion zu komplex werden, dann ist es wahrscheinlich ratsamer sie in mehrere Funktionen aufzuteilen.

## Beispiel

```python
def add(a: int, b: int) -> int:
    return a + b


ergebnis = add(2, 3)
print(ergebnis)
```