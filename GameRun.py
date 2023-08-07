import GameBoard
import pygame

class Game:
    def __init__(self) :
       
     # Initialize the game board and GUI
     self.board = GameBoard.Board()
     self.gui = GameBoard.GUI()
    def round(self):
    # Main game loop
     while True:
        # Draw the board
        self.gui.draw_board(self.board)
        # Get the user's move
        column = self.gui.get_move()
        # Make the move
        self.board.make_move(column)
        # Check if the game is over
        result = self.board.check_win()
        if result == 1:
            # Show a message if player 1 wins
            self.gui.show_message("Player 1 wins!")
            break
        elif result == 2:
            # Show a message if player 2 wins
            self.gui.show_message("Player 2 wins!")
            break
        elif result == -1:
            # Show a message if the game is a draw
            self.gui.show_message("It's a draw!")
            break

class main():
    def __init__(self) :
        
     # Run the game
     self.game=Game()

    # Wait for the user to close the window
    def run(self):
        self.game.round()
        while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    

m=main()
m.run()