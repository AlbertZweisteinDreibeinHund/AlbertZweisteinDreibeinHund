import arcade

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        self.spielfeld = {(0, 0): "X", (1, 0): "", (2, 0): "",(0, 1): "", (1, 1): "", (2, 1): "",(0, 2): "", (1, 2): "", (2, 2): ""}

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)
        if x < 300 and y < 300:
            self.spielfeld[(0,0)]= "0";



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


TTT()
arcade.run()
 

