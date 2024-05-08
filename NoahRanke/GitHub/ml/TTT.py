import arcade

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        spielfeld = {(0, 0): "", (1, 0): "", (2, 0): "",(0, 1): "", (1, 1): "", (2, 1): "",(0, 2): "", (1, 2): "", (2, 2): ""}

    def on_draw(self):
        self.clear()

        arcade.draw_line(25, 200, 575, 200, arcade.color.WHITE, 12)
        arcade.draw_line(25, 400, 575, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 25, 200, 575, arcade.color.WHITE, 12)
        arcade.draw_line(400, 25, 400, 575, arcade.color.WHITE, 12)

        for koordinaten in self.spielfeld:


TTT()
arcade.run()
 

