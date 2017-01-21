import pygame
import time
import curses

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

## Init
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
## Drumset index
i = 0
screen.clear()

## Screen display
while True:
	## Update the song folder to the selected drum set
	drumset = ['arabic', 'japanese']

	screen.addstr(1, 0, "Ready to play sounds or press a to change the set of drums or q to quit!")
	screen.addstr(2, 0, "Current drum set is : " + drumset[i])
	screen.addstr(3, 0, "To get to a new console press Alt-F2")

	up = pygame.mixer.Sound(currentDrumset + '/up.wav')
	down = pygame.mixer.Sound(currentDrumset + '/down.wav')
	left = pygame.mixer.Sound(currentDrumset + '/left.wav')
	right = pygame.mixer.Sound(currentDrumset + '/right.wav')
	w = pygame.mixer.Sound(currentDrumset + '/w.wav')
	s = pygame.mixer.Sound(currentDrumset + '/s.wav')
	d = pygame.mixer.Sound(currentDrumset + '/d.wav')
	f = pygame.mixer.Sound(currentDrumset + '/f.wav')
	g = pygame.mixer.Sound(currentDrumset + '/g.wav')

	event = screen.getch()

	screen.clear()

	if event == ord('q'):
		break
	elif event == curses.KEY_UP:
		screen.addstr(0, 0, "You pressed up!")
		up.play()
	elif event == curses.KEY_DOWN:
		screen.clear()
		screen.addstr(0, 0, "You pressed down!")
		down.play()
	elif event == curses.KEY_LEFT:
		screen.clear()
		screen.addstr(0, 0, "You pressed left!")
		left.play()
	elif event == curses.KEY_RIGHT:
		screen.clear()
		screen.addstr(0, 0, "You pressed right!")
		right.play()
	elif event == ord('w'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w!")
		w.play()
	elif event == ord('s'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w!")
		s.play()
	elif event == ord('d'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w!")
		d.play()
	elif event == ord('g'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w!")
		g.play()
	elif event == ord('f'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w!")
		f.play()
	elif event == ord('a'):
		screen.clear()

		if i > len(drumset):
			i = i + 1
		else:
			i = 0
	else:
		screen.clear()
		screen.addstr(0, 0, "That key doesn't do anything!")

curses.endwin()
