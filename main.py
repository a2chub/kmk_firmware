import board
from board import *
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence

from kmk.extensions.display import OLED

keyboard = KMKKeyboard()
# debug_enabled = True にするとデバッグログが表示される
keyboard.debug_enabled = False

# レイヤーモジュールを組み込み
layers_mod = Layers()
keyboard.modules = [layers_mod]

# エクステンションを読み込み
oled_ext = OLED(scl = GP15, sda = GP14, addr = 0x3c, freq = 400_000)
keyboard.extensions = [oled_ext]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

RAISE = KC.MO(1)

keyboard.keymap = [
    [  #Base
        RAISE,      KC.N0, \
        KC.A,       KC.B,  \
        KC.C,       KC.D,
    ],
    [  #RAISE
        _______,    KC.N0, \
        KC.N1,      KC.N2, \
        KC.N3,      KC.N4, 
    ]
]

if __name__ == '__main__':
    keyboard.go()
    
