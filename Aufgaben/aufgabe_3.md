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

Folgende Fragen sollen wie folgt beantwortet werden:

* Wenn die Anzahl der Buchstaben von `mein_name` länger als 8 Zeichen ist, dann gib `Was für ein langer Name.` aus. In
  allen anderen Fällen `dein Name hat weniger als 8 Zeichen`. **Hinweis**: über `len(variablenname)` kann man die Länge
  eines Strings herausfinden.
* Wenn dein `alter`
    * kleiner als 14 ist, dann gib `Ich darf in Wien zwischen 5 und 23h unterwegs sein.`
    * größer als 14 und kleiner als 16 ist, dann
      gib `Ich darf laut Jugendschutzgesetz in Wien schon bis 1h Nachts unterwegs sein.`
    * größer als 16 ist, dann gib `Ich darf in Wien so lange ich will unterwegs sein.`
* Wenn deine `party_freunde_anzahl`
    * kleiner 5 ist, dann gib `Wird eine überschaubare Party. Es kommen {party_freunde_anzahl} Freunde von mir.` aus.
    * größer als 5, dann gib `Die Party ist schon größer.` aus.
    * größer 20, dann gib `Wird eine mächtige Party.` aus.
* Wenn `klasse_mitglieder_letztes_jahr` größer als `klasse_mitglieder_dieses_jahr` ist, dann
  gib `Dieses Schuljahr haben *klasse_mitglieder_dieses_jahr - klasse_mitglieder_letztes_jahr*  Freunde die Klasse verlassen.`.
  * In allen anderen Fällen gib `Wir sind noch immer gleich viele SchülerInnen in der Klasse.` aus.
* Wenn `9 - anzahl_schuljahre` kleiner gleich 0 sind, dann gib `Ich habe meine Schulpflicht schon erfüllt.` aus.
  * In allen anderen Fällen gib `Ich habe noch {9 - anzahl_schuljahre} bis ich die Schulpflicht erreicht habe.` aus.
* Wenn dein `geschlecht`
    * gleich `f` ist, dann gib `Ich bin mein_name und bin weiblich.` aus.
    * gleich `m` ist, dann gib `Ich bin mein_name und bin männlich.` aus.
    * In allen anderen Fällen (sonst), dann gib `Ich bin mein_name, ich bin weder männlich noch weiblich.` aus.
* Wenn `ort` gleich `Wien` ist, dann gib `Ich wohne in der Bundeshauptstadt von Österreich.` aus.
    * in allen anderen Fällen gib `Ich wohne nicht in Wien.`
* Wenn dein `betriebssystem` gleich `Windows` oder `Mac` ist, dann gib `Ich benutze {betriebssystem}.` aus.
    * in allen anderen Fällen gib `Ich benutze {betriebssystem}. Wahrscheinlich ist es Linux.` aus.
* Wenn die `tage_seit_letzter_aktivitaet` größer gleich 3 ist, dann
  gib `Heute werde ich wieder {lieblings_hobby} machen :).` aus.