def initialize_board():
    """
    Creates a 3x3 Tic-Tac-Toe board initialized with empty spaces.

    Returns
    -------
    list of list of str
        A 3x3 game board with all spaces initialized to ' ' (empty).
    """
    return [[' ' for _ in range(3)] for _ in range(3)]


def make_move(board, row, col, player):
    """
    Places the player's symbol ('X' or 'O') on the board at the specified position.

    Parameters
    ----------
    board : list of list of str
        The current game board.
    row : int
        The row index (0-based).
    col : int
        The column index (0-based).
    player : str
        The player's symbol ('X' or 'O').

    Returns
    -------
    bool
        True if the move was successful, False otherwise.
    """
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def check_winner(board):
    """
    Checks the current board for a winner.

    Parameters
    ----------
    board : list of list of str
        The current game board.

    Returns
    -------
    str or None
        'X' or 'O' if there is a winner, 'Draw' if it's a draw, or None if the game is ongoing.
    """
    # Check rows, columns, and diagonals
    lines = board + list(zip(*board))  # Rows and columns
    lines.append([board[i][i] for i in range(3)])  # Main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # Anti-diagonal

    for line in lines:
        if all(cell == 'X' for cell in line):
            return 'X'
        if all(cell == 'O' for cell in line):
            return 'O'

    # Check for draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'

    return None


def reset_game():
    """
    Resets the game by reinitializing the board.

    Returns
    -------
    list of list of str
        A new 3x3 game board with all spaces initialized to ' ' (empty).
    """
    return initialize_board()
