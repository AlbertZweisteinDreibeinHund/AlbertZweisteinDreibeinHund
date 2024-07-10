import arcade, random

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        self.spielfeld = {(0, 0): "", (1, 0): "", (2, 0): "", (0, 1): "", (1, 1): "", (2, 1): "", (0, 2): "", (1, 2): "", (2, 2): ""}

        self.spieler = "X"

    # Gibt True zurück, falls ein Spieler gewonnen hat, ansonsten False
    def gewinnprüfung(self):
        # Untere Zeile
        if self.spielfeld[(0, 0)] == self.spielfeld[(1, 0)] == self.spielfeld[(2, 0)] != "":
            return True
        # Mittlere Zeile
        if self.spielfeld[(0, 1)] == self.spielfeld[(1, 1)] == self.spielfeld[(2, 1)] != "":
            return True
        # Obere Zeile
        if self.spielfeld[(0, 2)] == self.spielfeld[(1, 2)] == self.spielfeld[(2, 2)] != "":
            return True
        # Linke Spalte
        if self.spielfeld[(0, 0)] == self.spielfeld[(0, 1)] == self.spielfeld[(0, 2)] != "":
            return True
        # Mittlere Spalte
        if self.spielfeld[(1, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(1, 2)] != "":
            return True
        # Rechte Spalte
        if self.spielfeld[(2, 0)] == self.spielfeld[(2, 1)] == self.spielfeld[(2, 2)] != "":
            return True
        # Diagonale von unten links nach oben rechts
        if self.spielfeld[(0, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(2, 2)] != "":
            return True
        # Diagonale von unten rechts nach oben links
        if self.spielfeld[(2, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(0, 2)] != "":
            return True
        return False

    # Gibt eine Liste mit den Positionen aller freien Felder zurück
    def freie_felder(self):
        felder_liste = []
        for i in range(3):
            for j in range(3):
                if self.spielfeld[(i, j)] == "":
                    felder_liste.append((i, j))
        return felder_liste

    # Gibt True zurück, wenn das Spiel unentschieden ausgegangen ist, ansonsten False
    def unentschieden(self):
        if len(self.freie_felder()) == 0 and self.gewinnprüfung() == False:
            return True
        else:
            return False
        
    # Wird automatisch immer dann ausgeführt, wenn der Spieler mit der Maus klickt
    # (x, y) ist die Position des Mausklicks
    def on_mouse_press(self, x, y, button, modifiers):
        if self.spieler == "X":
            # Umrechnen der Position des Mausklicks im Fenster in die entsprechende Position in self.spielfeld
            if 0 <= x < 200:
                x_spielfeld = 0
            if 0 <= y < 200:
                y_spielfeld = 0
            if 200 <= x < 400:
                x_spielfeld = 1
            if 200 <= y < 400:
                y_spielfeld = 1
            if 400 <= x < 600:
                x_spielfeld = 2
            if 400 <= y < 600:
                y_spielfeld = 2
            if self.spielfeld[(x_spielfeld, y_spielfeld)] == "" and self.gewinnprüfung() == False:
                # Das Symbol des aktuellen Spielers wird auf die Position im Spielfeld gesetzt
                self.spielfeld[(x_spielfeld, y_spielfeld)] = self.spieler
                # Der Spieler wird gewechselt
                if self.spieler == "X":
                    self.spieler = "O"
                else:
                    self.spieler = "X"

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.R:
            self.__init__()
        elif symbol == arcade.key.Q:
            arcade.close_window()

    def random_zug(self):
        freie_felder_liste = self.freie_felder()
        return random.choice(freie_felder_liste)

    # Falls der Computer unmittelbar gewinnen kann, wird das Feld zurückgegeben, über der er dies kann
    # Falls nicht, aber der menschliche Spieler gewinnen kann, wird das Feld zurückgegeben, über der er dies kann
    # Falls nicht, wird ein zufälliges freies Feld zurückgegeben
    def mittelschlauer_zug(self):
        # Liste mit allen freien Feldern anlegen
        freie_felder_liste = self.freie_felder()

        # Probehalber setzen und prüfen, ob man gewinnen kann
        for feld in freie_felder_liste:
            self.spielfeld[feld] = "O"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        # Probehalber setzen und prüfen, ob man verlieren kann
        for feld in freie_felder_liste:
            self.spielfeld[feld] = "X"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        return self.random_zug()
    
    def schlauer_zug(self):
        # Liste mit allen freien Feldern anlegen
        freie_felder_liste = self.freie_felder()
     #   if self.spielfeld[(0, 0)] != "" or self.spielfeld[(0, 2)] != "" or self.spielfeld[(2, 0)] != "" or self.spielfeld[(2, 2)] != "":
           # return (1, 1)

        # Probehalber setzen und prüfen, ob man gewinnen kann
        for feld in freie_felder_liste:
            self.spielfeld[feld] = "O"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        # Probehalber setzen und prüfen, ob man verlieren kann
        for feld in freie_felder_liste:
            self.spielfeld[feld] = "X"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        if len(freie_felder_liste) == 9:
            return (1, 1)
        elif len(freie_felder_liste) == 8 and self.spielfeld[(1, 1)] == "X":
            ...

    # Kümmert sich darum, dass der Computerspieler setzt
    def on_update(self, delta_time):
        if self.spieler == "O" and not self.gewinnprüfung() and not len(self.freie_felder()) == 0:
            feld = self.mittelschlauer_zug()
            self.spielfeld[feld] = "O"
            self.spieler = "X"

    def on_draw(self):
        self.clear()

        arcade.draw_line(20, 200, 580, 200, arcade.color.WHITE, 12)
        arcade.draw_line(20, 400, 580, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 20, 200, 580, arcade.color.WHITE, 12)
        arcade.draw_line(400, 20, 400, 580, arcade.color.WHITE, 12)

        for koordinaten in self.spielfeld:
            # Das Symbol im Spielfeld an den aktuellen Koordinaten
            symbol = self.spielfeld[koordinaten]
            # Die Position in der internen Darstellung des Spielfelds wird umgerechnet in die Position in der grafischen Darstellung im Fenster
            pos_x = 200 * koordinaten[0] + 100
            pos_y = 200 * koordinaten[1] + 100
            # Wir zeichnen das Symbol ("". "X" oder "O") an die Stelle (pos_x, pos_y) in der Schriftgröße 100 und so, dass die angegebene Position den Mittelpunk
            # des Textes angibt, statt wie standardmäßig dessen Anfangspunkt
            arcade.draw_text(symbol, pos_x, pos_y, font_size=108, anchor_x="center", anchor_y="center")

        # TODO auf 26.06.2024: Die beiden nachfolgenden Zeichenbefehle gut verstehen (welcher Parameter tut was?)
        if self.gewinnprüfung() == True:
            arcade.draw_rectangle_filled(300, 300, 600, 600, arcade.make_transparent_color(arcade.color.BLACK, 190))
            arcade.draw_text(("X" if self.spieler == "O" else "O") + " hat gewonnen!", 0, 322.275, arcade.color.AQUA, font_size=80, width=600, align="center")
        if self.unentschieden() == True:
            arcade.draw_rectangle_filled(300, 300, 600, 600, arcade.make_transparent_color(arcade.color.BLACK, 190))
            arcade.draw_text("Unentschieden!", 0, 275, arcade.color.CANARY_YELLOW, font_size=60, width=600, align="center")


    

TTT()
arcade.run()

# (0, 0) -> (100, 100)
# (1, 0) -> (300, 100)
# (2, 0) -> (500, 100)
# (0, 1) -> (100, 300)
# (1, 1) -> (300, 300)
# (2, 1) -> (500, 300)
# (0, 2) -> (100, 500)
# (1, 2) -> (300, 500)
# (2, 2) -> (500, 500)
# (x, y) -> (200 * x + 100, 200 * y + 100)