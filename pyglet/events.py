#!/usr/bin/env python

from __future__ import print_function

import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()


@window.event
def on_key_press(symbol, modifiers):
    print("key %s was pressed" % symbol)
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')


@window.event
def on_mouse_press(x, y, button, modifiers):
    print("location: (%s, %s), button: %s" % (x, y, button))
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')


@window.event
def on_draw():
    window.clear()


pyglet.app.run()
