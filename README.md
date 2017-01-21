Pi Drum Board
=======

Based on the [Curses soundboard program for Raspberry PI](https://github.com/dalethatcher/piboard)

Pi Drum Board is a Python based program that best run on [Raspberry Pi](https://www.raspberrypi.org/)
It allows you to play a sound each time you hit the keyboard. To run the program, simply launch the ./run.sh
 
Works perfectly with the [Makey Makey Classic](http://www.makeymakey.com), the key set up are the same the standard kit
Up, Down, Left, Right, W, S, D, F and G

the A key is set up to change the drumset

Drum set folder
--------
There is two default drum set folder, arabic and japanese.

Feel free to implement a drum set yourself by adding a folder in the root directory and updating board.py
 
`drumset = ['arabic', 'japanese', 'your-new-drumset']`

and adding a file corresponding to each key.

