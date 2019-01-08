import os

if os.name=='posix': #Linux
	def sound(name):
		os.system('aplay '+name+'&')
elif os.name=='mac': #MacOS
	def sound(name):
		os.system('afplay '+name+'&')

elif os.name=='nt':#windows
	import  winsound
	def sound(name):
		winsound.PlaySound(name, winsound.SND_ASYNC)





if __name__=='__main__':
	import time
	sound('chomp.wav')
	time.sleep(1)
