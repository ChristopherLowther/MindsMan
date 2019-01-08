import os
from Piece import Piece
from Snack import Snack
from sound import sound

class Snacker(Piece): #The player will control one of these
	def __init__(self):
		super(Snacker,self).__init__()
		self.x=Piece.window.width/16
		self.y=Piece.window.height/2
		self.width=Piece.window.height/32 #size of Snacker
		self.open=45 #how wide the mouth is opened
		self.xv=0 #velocity
		self.yv=0
		self.score=0
		Piece.window.root.bind("<Up>",self.up) #set keys to move Snacker
		Piece.window.root.bind("<Down>",self.down)
		Piece.window.root.bind("<KeyRelease>",self.stop)
		
		coord=self.x-self.width,self.y-self.width,self.x+self.width,self.y+self.width
		self.graphic=Piece.window.canvas.create_arc(coord,start=self.open,extent=360-self.open*2,fill="#00ff00")
		
		
	def up(self,event=None): #change velocity (called on keypress)
		self.yv=-self.width/4
	def down(self,event=None):
		self.yv=self.width/4
	def stop(self,event=None):
		if event.keysym=='Up' and self.yv<0:
			self.yv=0
		elif event.keysym=='Down' and self.yv>0:
			self.yv=0
	
	def move(self):
		super(Snacker,self).move()
		for i in Piece.pieces: #eat any snack you come into contact with
			if i.touch(self): 
				if type(i)==Snack:
					self.bite()
					self.score+=i.points
					if i.points>=0:
						sound('chomp.wav')
					else:
						sound('chomp2.wav')

	def bite(self): #animate mouth moving
		self.open=self.open-4
		if self.open<=0:
			self.open=45
		else:
			Piece.window.root.after(17,self.bite)
		
		self.window.canvas.itemconfig(self.graphic,start=self.open,extent=360-self.open*2)
