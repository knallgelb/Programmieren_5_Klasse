from time import sleep

name = input("Bitte verrate mir deinen Name: ")
lehrer = "Rainer Amler"

greetings = f"""
Hallo liebe/r {name}. Es ist schön, dass du heute da bist.

Du hast vermutlich gerade dein erstes Python-Programm gestartet. Ich hoffe die gefällt das Programmieren.

Was ich dir jetzt schon verraten kann ist, dass es ganz viele Jobs in der Informatik gibt.

Das sind jetzt nicht nur ProgrammiererInnen, da gibt es noch ProjektmanagerInnen, DesignerInnen, etc.

Viel Spaß in meinem Unterricht.

Alles Liebe,
{lehrer}
"""

for line in greetings.split():
    print(line)
    sleep(0.4)
