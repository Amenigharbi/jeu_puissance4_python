import pygame

# Constants for the game
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
CELL_SIZE = 100
MARGIN = 1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (69, 69, 69)
RED = (255, 0, 0)


# Initialize pygame
pygame.init()

# Set the window size
screen = pygame.display.set_mode([(CELL_SIZE * BOARD_WIDTH) + (MARGIN * (BOARD_WIDTH + 1)),
                                  (CELL_SIZE * BOARD_HEIGHT) + (MARGIN * (BOARD_HEIGHT + 1))])

# Set the window title
pygame.display.set_caption("Puissance 4")

#############################################################################################################

# Class for the game board
class Board:
    def __init__(self):
        # Initialize the board
        self.board = [[0 for j in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]
        # Initialize the current player
        self.current_player = 1

    def check_move(self, column):
        # Check if the column is full
        if self.board[0][column] != 0:
               return False
        # Return True if the move is valid
        return True

    def make_move(self, column):
        # Find the first empty cell in the column
        for i in range(BOARD_HEIGHT):
            if self.board[i][column] == 0:
                # Make the move and switch players
                self.board[i][column] = self.current_player
                self.current_player = 1 if self.current_player == 2 else 2
                return

    def check_win(self):
        # Check for a horizontal win
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH - 3):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] and self.board[i][j] != 0:
                    return self.board[i][j]
        # Check for a vertical win
        for i in range(BOARD_HEIGHT - 3):
            for j in range(BOARD_WIDTH):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] and self.board[i][j] != 0:
                    return self.board[i][j]
        # Check for a diagonal win (top left to bottom right)
        for i in range(BOARD_HEIGHT - 3):
            for j in range(BOARD_WIDTH - 3):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] and self.board[i][j] != 0:
                    return self.board[i][j]
        # Check for a diagonal win (top right to bottom left)
        for i in range(BOARD_HEIGHT - 3):
            for j in range(3, BOARD_WIDTH):
                if self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] and self.board[i][j] != 0:
                    return self.board[i][j]
        # Check for a draw
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if self.board[i][j] == 0:
                    return 0
        # Return -1 if the game is a draw
        return -1
##############################################################################################################################################################

# Class for the graphical interface
class GUI:
    def __init__(self):
        # Initialize the font
        self.font = pygame.font.SysFont('Arial', 36)

    def draw_board(self, board):
        # Clear the screen
        screen.fill(BLACK)
        # Draw the cells
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                color = GREY
                if board.board[i][j] == 1:
                    color = BLACK
                elif board.board[i][j] == 2:
                    color = WHITE
                pygame.draw.rect(screen, color, [(MARGIN + CELL_SIZE) * j + MARGIN,
                                                 (MARGIN + CELL_SIZE) * i + MARGIN,
                                                 CELL_SIZE,
                                                 CELL_SIZE])
        # Update the display
        pygame.display.update()

    def get_move(self):
        # Wait for the user to make a move
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the column where the user clicked
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (CELL_SIZE + MARGIN)
                    waiting = False
        # Return the column where the user clicked
        return column

    def show_message(self, message):
        # Render the message
        text = self.font.render(message, True, RED)
        # Get the size of the message
        text_rect = text.get_rect()
        # Set the position of the message
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        # Draw the message
        screen.blit(text, text_rect)
        # Update the display
        pygame.display.update()