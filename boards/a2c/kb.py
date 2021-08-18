import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP17, board.GP18, board.GP19)
    col_pins = (board.GP20, board.GP21)
    diode_orientation = DiodeOrientation.COLUMNS
    led_pin = board.GP25