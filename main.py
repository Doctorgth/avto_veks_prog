from help import *

import keyboard


def on_cl(key):
    if key.name=="p":
        k.next()
    if key.name=="o":
        k.prev()

window=create_window()
k=text(marsh(),50,50)
keyboard.on_press(on_cl)
window.mainloop()