import random
from Piece import Piece
class Snack(Piece): #kind of like Skittles
	def __init__(self):
		super(Snack,self).__init__()
		self.r=random.randrange(64,256) #the color will be chosen at random
		self.g=random.randrange(64,256)
		self.b=random.randrange(64,256)
		self.points=-self.r*3+self.g+self.b*2 #red is bad for you (deducts points)
		self.r='{:02x}'.format(self.r)
		self.g='{:02x}'.format(self.g)
		self.b='{:02x}'.format(self.b)
		self.x=Piece.window.width*1.1 #starts just to the right outside the window
		self.y=random.uniform(0,Piece.window.height) #height is randomized
		self.xv=-(random.randrange(0,int(Piece.window.width/100))+int(Piece.window.width/100)) #move left at random speed
		self.yv=0
		self.width=Piece.window.height/128 #snacks are bitesized
		coord=self.x-self.width,self.y-self.width,self.x+self.width,self.y+self.width
		self.graphic=Piece.window.canvas.create_oval(coord,fill="#"+self.r+self.g+self.b)
		
	def move(self):
		super(Snack,self).move()
		if self.x<0: #vanishes when it goes off screen
			Piece.window.canvas.delete(self.graphic)
			Piece.pieces.remove(self)

	def touch(self,other): #if it's touched it gets eaten
		if super(Snack,self).touch(other):
			Piece.window.canvas.delete(self.graphic)
			Piece.pieces.remove(self)
			return True
		else: return False

