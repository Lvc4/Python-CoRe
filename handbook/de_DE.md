# CoRe Schnelleinstieg

## Was ist CoRe

CoRe ist ein Brettspiel, indem es darum geht möglichst viele Steine selbst auf das Brett zu bekommen,
dabei können unter gewissen umständen Steine des Gegners "umgedreht" werden,
um diese zu seinem eigen zu machen.

Dabei spielt man allerdings nicht Mensch-gegen-Mensch, sondern man programmiert eine KI,
mit der aufgabe das Spiel zu meistern. Dafür wird hauptsächlich die Python Programmiersprache genutzt,
allerdings werden unter Umständen andere Sprachen wie AntLang in kommenden Versionen unterstützt
(vielleicht sind diese zum Zeitpunkt des Lesens schon implementiert).

## Die Spielregeln

### Wichtige Fakten

Jeder Spieler hat eine unlimitierte Anzahl an Steinen,
das Brett ist ein 8-mal-8 Schachbrett, es wird auf den Feldern gespielt,
nicht auf den Schnittpunkten.
Eine Regelkomform gespielte Partie besteht aus insgesamt 64 Zügen.

### Grundlegendes Platzieren

Die spielregeln sind sehr simpel: die KIs sind abwechselnd am Zug,
jede platziert einen Stein auf ein freies feld im Brett.
Sind alle felder belegt wird gezählt welcher Spieler mehr Steine auf dem Brett hat;
dieser darf sich dann Sieger nennen.

### Steine Entfernen

Wird ein stein auf eine Vertikale und/oder Horizontale gespielt,
auf der bereits ein Stein der eigenen farbe liegt,
wird jeder gegnerische Stein bis zu den eigenen umgedreht, das heißt zur eigenen farbe gewandelt.

### Corner Kills

Außerdem gibt es die sonderregel, dass ein Eckstein des gegners umgedreht werden kann,
wenn man selbst einen Stein ein Feld diagonal zur Ecke platziert.
Diese technik wird als "Corner Kill" bezeichnet (englisch: Eck-Tötung),
wobei der Eckstein als "Corner Stone" und der diagonal anligende als "Killing Stone" bezeichnet werden.

## Die API

Diese simplen Spielregeln ermöglichen es auf einfachste weise eine KI zu schreiben.

Eine der einfachsten möglichen KIs ist die folgende:

```python
import random

def turn(board, symbol):
	while 1:
		x = random.choice(range(8))
		y = random.choice(range(8))
		if board[y][x] == '#': return (x,y)

```

Diese AI wird oft als "crazy" (englisch: Verrückt) bezeichnet, da sie keiner logischen Struktur folgt.

Sie definiert eine funktion "turn" (englisch: Spielzug), die das Board, also Brett als Matrix
und das Spielersymbol, also "X" oder "O" erhält und ein Koordinaten-Tupel zurückgibt.

Die X und Y Koordinaten werden solange zufällig ermittelt, bis sie auf ein leeres Feld zeigen.

Ein Feld kann die folgende Form haben:

| Wert | Bedeutung   |
|------|-------------|
| X    | Spieler X   |
| O    | Spieler O   |
| #    | Leeres Feld |

## Ein Spiel Simulieren

Um ein Spiel zu simulieren werden zwei KIs benötigt, die gegeneinander Antreten.
Es ist möglich die selbe KI gegen die selbe spielen zu lassen.
Dies geht wie folgt:

```sh
% ./core meine_ki.py meine_ki.py
# Allgemein:
% ./core ki_1 ki_2
```

## Was kommt als nächstes?

Wenn du dir die Grundlagen verinnerlicht hast, steht als nächstes das Entwickeln einer Turnier-KI an.
Nimm an Wettbewerben teil, sammle Gewinne und werde ein Erfolgreicher CoRe spieler.
