from Window import Window
import tkinter as tk
from sound import sound
from Piece import Piece
from Snacker import Snacker
from Snack import Snack		
import random

class Game:
	def __init__(self):
		self.window=Window()
		self.window.root.after(17,self.play) #update game about 60 times per second
		self.window.root.after(30*1000,self.end) #game ends in thirty seconds
		Piece.setup(self.window) #run setup, give player a character, and start the game
		self.snackman=Snacker()
		self.window.root.mainloop()
	
	def play(self): #the main game loop
		if random.randrange(0,10)==0: #throw a snack every few frames
			Snack()

		Piece.play() #move all the pieces
		self.window.root.after(17,self.play) #play again after about 1/60th of a second
	
	def end(self): #print score and exit program
		print('\n'*50,'Score:',self.snackman.score)
		exit()

game=Game()
