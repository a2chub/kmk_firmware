import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()
# debug_enabled = True にするとデバッグログが表示される
keyboard.debug_enabled = True

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# レイヤーモジュールを組み込み
layers_mod = Layers()
keyboard.modules = [layers_mod]

RAISE = KC.MO(1)
# 通常の文字列送信は send_string で実行できるはずだが、あらかじめ KC.A 等初期化しておかないと
# エラーになるので simple_key_sequence を使用
MACRO_BASE = simple_key_sequence((KC.A, KC.B, KC.C, KC.D,, KC.E, KC.F,))
MACRO_RAISE = simple_key_sequence((KC.N0, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,))

keyboard.keymap = [
    [  #Base
        RAISE, KC.A, KC.LED_TOG, MACRO_BASE, KC.B, KC_D
    ],
    [  #RAISE
        _______, KC.N0, _______, MACRO_RAISE, KC.E, KC.F
    ]
]

if __name__ == '__main__':
    keyboard.go()