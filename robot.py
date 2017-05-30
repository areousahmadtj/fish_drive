import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensor import distance

def init()
	gpio.setmode(gpio.BOARD)
	gpio.setup(7 , gpio.OUT)	# Number of GPIO pin RB Pi where motor will be conected
	gpio.setup(11 , gpio.OUT)
	gpio.setup(13 , gpio.OUT)
	gpio.setup(15 , gpio.OUT)
	
def forward(tf):
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, False)
	time.sleep(tf)
	gpio.cleanup()
	
def reverse(tf)
	gpio.output(7, True)
	gpio.output(11, False)
	gpio.output(13, False)
	gpio.output(15, True)
	time.sleep(tf)
	gpio.cleanup()
	
def turn_left(tf)
	gpio.output(7, True)
	gpio.output(11, True)
	gpio.output(13, True)
	gpio.output(15, False)
	time.sleep(tf)
	gpio.cleanup()
	
def turn_right(tf)
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, False)
	gpio.output(15, False)
	time.sleep(tf)
	gpio.cleanup()
	
def pivot_left(tf)
	gpio.output(7, True)
	gpio.output(11, False)
	gpio.output(13, True)
	gpio.output(15, False)
	time.sleep(tf)
	gpio.cleanup()
	
def pivot_right(tf)
	gpio.output(7, False)
	gpio.output(11, True)
	gpio.output(13, False)
	gpio.output(15, True)
	time.sleep(tf)
	gpio.cleanup()
	
def key_input(event):
	init()
	print 'Key:', event.char
	key_press = event.char
	sleep_time = 0.1
	
	if key_press.lower() == 'w' or key_press.upper() =='W':
		forward(sleep_time)
	elif key_press.lower() == 's' or key_press.upper() =='S':
		reverse(sleep_time)
	elif key_press.lower() == 'a' or key_press.upper() =='A':
		turn_left(sleep_time)
	elif key_press.lower() == 'd' or key_press.upper() =='D':
		turn_right(sleep_time)
	elif key_press.lower() == 'q' or key_press.upper() =='Q':
		pivot_left(sleep_time)
	elif key_press.lower() == 'e' or key_press.upper() =='E':
		pivot_right(sleep_time)
	else:
		pass
		
	curDis = distance('cm') #current distance of object from sensor
	if curDis < 25:
		init()
		reverse(2)
		
command = tk.TK()
command.bind('<KeyPress>', key_input)
command.mainloop()