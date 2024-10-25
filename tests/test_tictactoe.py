import pytest
from tictactoe_cz2842.tictactoe import initialize_board, make_move, check_winner, reset_game

# 1.a
def test_initialize_board():
    board = initialize_board()
    
    # Verify that the board is 3x3
    assert len(board) == 3
    assert all(len(row) == 3 for row in board)
    
    # Verify that all cells are initialized with empty spaces
    assert all(cell == ' ' for row in board for cell in row)


# 1.b
def test_make_move_valid():
    # Start with a pre-specified board configuration
    board = [
        ['X', ' ', 'O'],
        [' ', ' ', ' '],
        [' ', 'X', ' ']
    ]
    
    # Test player 'X' making a valid move
    result_x = make_move(board, 1, 1, 'X')  # Place 'X' in the center (row 1, col 1)
    assert result_x == True
    assert board[1][1] == 'X'
    
    # Test player 'O' making a valid move
    result_o = make_move(board, 0, 1, 'O')  # Place 'O' in the top-middle (row 0, col 1)
    assert result_o == True
    assert board[0][1] == 'O'


# 1.c
def test_make_move_invalid():
    # Start with a pre-specified board configuration
    board = [
        ['X', 'O', 'X'],
        [' ', 'O', ' '],
        [' ', 'X', 'O']
    ]
    
    # Attempt to place 'X' in an already occupied cell (0, 0)
    result_x = make_move(board, 0, 0, 'X')
    assert result_x == False  # The move should be rejected
    assert board[0][0] == 'X'  # Board should remain unchanged at (0, 0)
    
    # Attempt to place 'O' in an already occupied cell (1, 1)
    result_o = make_move(board, 1, 1, 'O')
    assert result_o == False  # The move should be rejected
    assert board[1][1] == 'O'  # Board should remain unchanged at (1, 1)

# 1.d
def test_game_integration():
    # Initialize the board
    board = initialize_board()
    assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    # Player X makes a move
    assert make_move(board, 0, 0, 'X') == True
    assert board[0][0] == 'X'
    
    # Player O makes a move
    assert make_move(board, 1, 1, 'O') == True
    assert board[1][1] == 'O'
    
    # Player X makes a move
    assert make_move(board, 0, 1, 'X') == True
    assert board[0][1] == 'X'
    
    # Player O makes a move
    assert make_move(board, 2, 2, 'O') == True
    assert board[2][2] == 'O'
    
    # Player X makes a move to win the game (row 0)
    assert make_move(board, 0, 2, 'X') == True
    assert board[0][2] == 'X'
    
    # Check if Player X is the winner
    assert check_winner(board) == 'X'
    
    # Reset the game
    board = reset_game()
    assert board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    # Verify no winner after reset
    assert check_winner(board) == None

# 1.e
# shown in Jupyter Notebook


# 2.a
@pytest.mark.parametrize("initial_board, row, col, player, expected_result, expected_board", [
    # Case 1: Existing board where player 'X' already occupies the top-left corner
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 1, 'O', True, [['X', 'O', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
    
    # Case 2: Trying to place 'O' in an already occupied spot (top-left corner)
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'O', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),

    # Case 3: Valid move by 'O' in a different row
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 1, 1, 'O', True, [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]),

    # Case 4: Out-of-bounds move (row 3, column 1)
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 3, 1, 'X', False, [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]),
])
def test_make_move(initial_board, row, col, player, expected_result, expected_board):
    try:
        result = make_move(initial_board, row, col, player)
    except IndexError:
        result = False  # Handle out-of-bounds moves as False
    
    # Verify if the move was successful
    assert result == expected_result
    
    # Verify if the board state is as expected after the move
    assert initial_board == expected_board



# 2.b
# Define a pytest fixture to provide a fresh game board before each test
@pytest.fixture
def fresh_board():
    """Fixture to initialize a new game board before each test."""
    return initialize_board()


# Use the fixture in the test functions
def test_make_move_valid_with_fixture(fresh_board):
    # Using the fresh_board fixture to test a valid move
    result = make_move(fresh_board, 0, 0, 'X')
    assert result == True
    assert fresh_board[0][0] == 'X'


def test_make_move_invalid_with_fixture(fresh_board):
    # Make a valid move first
    make_move(fresh_board, 0, 0, 'X')
    
    # Try to overwrite the move (should fail)
    result = make_move(fresh_board, 0, 0, 'O')
    assert result == False
    assert fresh_board[0][0] == 'X'  # Board should remain unchanged


def test_winner_with_fixture(fresh_board):
    # Simulate a winning condition for player 'X'
    make_move(fresh_board, 0, 0, 'X')
    make_move(fresh_board, 0, 1, 'X')
    make_move(fresh_board, 0, 2, 'X')
    
    # Check if 'X' is the winner
    winner = check_winner(fresh_board)
    assert winner == 'X'
    
