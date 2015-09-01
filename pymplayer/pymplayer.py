#!/usr/bin/env python2

# -*- coding: UTF-8 -*-

import subprocess
import time


def main():
    player = subprocess.Popen(["mplayer", "-loop", "0", "pay.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    time.sleep(10)

    player.stdin.write("q")


if __name__ == "__main__":
    main()
