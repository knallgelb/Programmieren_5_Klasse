# Aufgabe 3 - Abfragen

Alle notwendigen Informationen findest du unter [Abfragen.md](../abfragen.md).

Erstelle die Datei `entscheidungen.py`.

Lege die folgenden Variablen an und weise ihnen Werte zu:

* mein_name (String)
* alter (Integer)
* party_freunde_anzahl (Integer)
* klasse_mitglieder_dieses_jahr (Integer)
* klasse_mitglieder_letztes_jahr (Integer)
* anzahl_schuljahre (Integer)
* geschlecht (String m oder f)
* ort (String)
* betriebssystem (String)
* tage_seit_letzter_aktivitaet (Integer)
* lieblings_hobby (String)

Folgende Fragen sollen wie folgt beantwortet werden, gib den Text aus der nach dem `|` steht:

* Wenn dein `alter`
    * kleiner als 14 ist | `Ich darf in Wien zwischen 5 und 23h unterwegs sein.`
    * größer gleich als 14 und kleiner gleich als 16 ist | `Ich darf in Wien schon bis 1h Nachts unterwegs sein.`
    * größer als 16 ist | `Ich darf in Wien so lange ich will unterwegs sein.`
* Wenn die Anzahl der Buchstaben von `mein_name` länger als 8 Zeichen
  ist | `Mein Name {mein_name} hat mehr als 8 Zeichen.`
    * In allen anderen Fällen | `Mein Name {mein_name} hat weniger als 8 Zeichen.`
    * **Hinweis**: über `len(variablenname)` kann man die Länge eines Strings herausfinden.
* Wenn deine `party_freunde_anzahl`
    * kleiner 5 ist | `Wird eine überschaubare Party. Es kommen {party_freunde_anzahl} Freunde von mir.`
    * größer als 5 | `Die Party ist schon größer.`
    * größer 20 | `Wird eine mächtige Party.`
* Wenn `klasse_mitglieder_letztes_jahr` größer als `klasse_mitglieder_dieses_jahr`
  ist | `Dieses Schuljahr haben {klasse_mitglieder_letztes_jahr - klasse_mitglieder_dieses_jahr} Freunde die Klasse verlassen.`.
    * In allen anderen Fällen | `Wir sind noch immer gleich viele SchülerInnen in der Klasse.`
* Wenn `9 - anzahl_schuljahre` kleiner 0 ist | `Ich habe meine Schulpflicht schon erfüllt.`
    * In allen anderen Fällen | `Ich habe noch {9 - anzahl_schuljahre} bis ich die Schulpflicht erreicht habe.`
* Wenn dein `geschlecht`
    * gleich `f` ist | `Ich bin {mein_name} und bin weiblich.`
    * gleich `m` ist | `Ich bin {mein_name} und bin männlich.`
    * In allen anderen Fällen | `Ich bin mein_name, ich bin weder männlich noch weiblich.`
* Wenn `ort` gleich `Wien` ist | `Ich wohne in der Bundeshauptstadt von Österreich.`
    * in allen anderen Fällen | `Ich wohne nicht in Wien.`
* Wenn dein `betriebssystem` gleich `Windows` oder `Mac` ist | `Ich benutze {betriebssystem}.`
    * in allen anderen Fällen | `Ich benutze {betriebssystem}. Wahrscheinlich ist es Linux.`
* Wenn die `tage_seit_letzter_aktivitaet` größer gleich 3 ist | `Heute werde ich wieder {lieblings_hobby} machen :).`