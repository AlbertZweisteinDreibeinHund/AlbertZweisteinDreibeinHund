import arcade
import random

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        self.spielfeld = {(0, 0): "", (1, 0): "", (2, 0): "",(0, 1): "", (1, 1): "", (2, 1): "",(0, 2): "", (1, 2): "", (2, 2): ""}

        self.player = "X"

    def gewinnprüfung(self):
        if self.spielfeld[(0, 0)] == self.spielfeld[(1, 0)] == self.spielfeld[(2, 0)] != "":
            return True
        if self.spielfeld[(0, 1)] == self.spielfeld[(1, 1)] == self.spielfeld[(2, 1)] != "":
            return True
        if self.spielfeld[(0, 2)] == self.spielfeld[(1, 2)] == self.spielfeld[(2, 2)] != "":
            return True
        if self.spielfeld[(0, 0)] == self.spielfeld[(0, 1)] == self.spielfeld[(0, 2)] != "":
            return True
        if self.spielfeld[(1, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(1, 2)] != "":
            return True
        if self.spielfeld[(2, 0)] == self.spielfeld[(2, 1)] == self.spielfeld[(2, 2)] != "":
            return True
        if self.spielfeld[(0, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(2, 2)] != "":
            return True
        if self.spielfeld[(2, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(0, 2)] != "":
            return True



    def on_draw(self):
        self.clear()
        arcade.draw_line(25, 200, 575, 200, arcade.color.WHITE, 12)
        arcade.draw_line(25, 400, 575, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 25, 200, 575, arcade.color.WHITE, 12)
        arcade.draw_line(400, 25, 400, 575, arcade.color.WHITE, 12)

        for koordinaten in self.spielfeld:
            symbol = self.spielfeld[koordinaten]
            pos_x = 200 * koordinaten[0] + 100 
            pos_y = 200 * koordinaten[1] + 100 
            arcade.draw_text(symbol, pos_x, pos_y,arcade.color.WHITE, 150,anchor_x="center", anchor_y="center", )



    def change_player(self, player):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            x_cord = round((x - 100) / 200)
            y_cord = round((y - 100) / 200)
            if self.check((x_cord, y_cord)) == True:
                self.computers_turn()
                pass
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.__init__()
        elif symbol == arcade.key.Q:
            arcade.close_window()

          
    def check(self, kords):
        if self.spielfeld[kords] == "" :
            self.spielfeld[kords] = self.player
            self.change_player("")
            return True
        else:
            return False



    def computers_turn(self):
        while 1 == 1:
            if self.check((random.randint(0, 2),random.randint(0, 2))) == True:
                self.win_check()
 
             
             


TTT()
arcade.run()
 

