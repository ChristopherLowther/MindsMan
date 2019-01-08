class Piece: #this is the base class for all game pieces, including the player
	def setup(window): #sets up variables needed for all pieces
		Piece.window=window #all pieces will share the same window
		Piece.pieces=[] #all the pieces will be stored in this list
		
	def play(): #move all the pieces
		for i in Piece.pieces:
			i.move()
	
	def __init__(self):
		Piece.pieces.append(self) #add each new piece to list
	
	def move(self): #basic movement
		self.x+=self.xv
		self.y+=self.yv
		self.window.canvas.move(self.graphic,self.xv,self.yv)
	
	def touch(self,other): #run a check to see if two pieces are touching (returns True or False)
		return (self.x-other.x)**2+(self.y-other.y)**2<=(self.width+other.width)**2  and not other is self
