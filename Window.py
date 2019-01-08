import tkinter as tk

class Window: #creates a full-screen window (F11 toggles full-screen)
	def __init__(self):
		self.root=tk.Tk()
		self.width=self.root.winfo_screenwidth()
		self.height=self.root.winfo_screenheight()
		self.root.attributes('-zoomed',True)
		self.frame=tk.Frame(self.root)
		self.frame.pack()
		self.root.bind("<Escape>", exit) #exit when escape is pressed
		self.root.attributes("-fullscreen",True)
		self.canvas=tk.Canvas(self.root,bg="black",width=self.width,height=self.height)
		self.canvas.pack(side="top",fill="both",expand=True)

	def run(self):
		self.root.mainloop()


if __name__=='__main__':
	w=Window()
	w.run()
