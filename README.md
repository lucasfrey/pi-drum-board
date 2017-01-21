Pi Drum Board
=======

Based on the [Curses soundboard program for Raspberry PI](https://github.com/dalethatcher/piboard)

Pi Drum Board is a Python based program that best runs on [Raspberry Pi](https://www.raspberrypi.org/).
It allows you to play a sound each time you press a key. To run the program, simply launch the ./run.sh
 
Works perfectly with the [Makey Makey Classic](http://www.makeymakey.com). 
By default, the keys Up, Down, Left, Right, W, S, D, F and G are setup to play a sound, like in the makey makey standard kit.

The A key is set up to change the drumset.

Drum set folder
--------
There are two default drum set folders, arabic and japanese.

Feel free to implement a drum set yourself by adding a folder in the root directory and updating board.py
 
`drumset = ['arabic', 'japanese', 'your-new-drumset']`

and adding a .wav file corresponding to each key.

