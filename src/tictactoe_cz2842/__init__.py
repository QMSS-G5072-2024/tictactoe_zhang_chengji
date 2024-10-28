# read version from installed package
from importlib.metadata import version
__version__ = version("tictactoe_cz2842")

from .tictactoe import initialize_board, make_move, check_winner, reset_game
