class Tetromino():

	#each tetris piece is represented by a each line string
	pieces = [

	['-','-','#','-','-',
	 '-','-','#','-','-',
	 '-','-','#','-','-',
	 '-','-','#','-','-',
	 '-','-','-','-','-'],

	['-','-','-','-','-',
	 '-','-','#','-','-',
	 '-','#','#','#','-',
	 '-','-','-','-','-',
	 '-','-','-','-','-']


	]

	w = 5

	def __init__(self):
		from random import randint
		self.orientation = self.pieces[randint(0,1)]
		print("piece:",self.orientation)


	def rotate_right(self):
		"""right roatation translation"""
		prev_orientation = self.orientation.copy()
		for row in range(self.w):
			for col in range(self.w):
				self.orientation[row*self.w+col] = prev_orientation[20+row-(5*col)]

	def rotate_left(self):
		prev_orientation = self.orientation.copy()
		for row in range(self.w):
			for col in range(self.w):
				self.orientation[row*self.w+col] = prev_orientation[(-row)+4+(5*col)] 

	def print_piece(self):
	#each piece is representeda as a 5 by 5 2d grid
		for i in range(self.w):
			print(''.join(self.orientation[i*self.w:(i*self.w)+5]))


	

