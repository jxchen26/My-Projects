import turtle as t
from tetromino import *


class Tetris(t.Turtle):

	#game constants
	screen_width = 800
	screen_height = 960
	board_w = 10
	board_h = 24
	square_w = int(int(screen_width/2)/board_w)
	square_h = int(screen_height/board_h)
	upper_left_corner = {
		"x":-int(screen_width/2),
		"y":int(screen_height/2)
	}
	print(upper_left_corner["x"],upper_left_corner["y"])
	print("the square width: ", square_w, "the sqaure height:",square_h)

	init_xoffset = 120

	def __init__(self):
		super().__init__() # part of the turtle class 
		self.board = [0 for i in range(self.board_w * self.board_h)]
		self.piece = None
		self.pointer = {
		"x":self.upper_left_corner["x"]+self.init_xoffset, 
		"y":self.upper_left_corner["y"]
		} #upper left corner 
		print("BOARD:",self.board)

	def create_board():
		board = []
		for i in range(self.board_w*self.board_h)

	def draw_square(self, block):

		if block == 0:
			self.pencolor(190,190,190)
			self.fillcolor("white")
		elif block == "#":
			self.pencolor(190,190,190)
			self.fillcolor("blue")
		else:
			self.pencolor(190,190,190)
			self.fillcolor("blue")




		self.begin_fill()
		for i in range(2):
			self.forward(self.square_w)
			self.right(90)
			self.forward(self.square_h)
			self.right(90)
		self.end_fill()

	def draw_screen(self):

		#move pen to upper left corner 
		self.penup()
		self.goto(self.upper_left_corner["x"], self.upper_left_corner["y"]) 
		self.pendown()
		self.pensize(2)


		y = self.upper_left_corner["y"]
		for s in range(len(self.board)): #10
			self.draw_square(self.board[s])
			self.setx(self.xcor()+self.square_w) # increase pen's x position
			if (s+1)%10 == 0:
				# after every row, move pen down 1 row and reset x
				y -= self.square_h
				self.penup()
				self.goto(self.upper_left_corner["x"], y)
				self.pendown()

	def load_tetromino(self):
		from tetromino import Tetromino
		self.piece = Tetromino()


	def draw_tetromino(self):
		#get pointer position
		x = self.pointer["x"]
		y= self.pointer["y"] 


		for row in range(5):
			self.penup()
			self.goto(x,y)
			self.pendown()
			for col in range(5):
				if self.piece.orientation[(row*self.piece.w)+col] == "#":
					self.fillcolor("red")
					self.begin_fill()
					for i in range(2):
						self.forward(self.square_w)
						self.right(90)
						self.forward(self.square_h)
						self.right(90)
					self.end_fill()

				#move right one square 
				x += self.square_w
				self.setx(x)
			#reset x and move pointer down 1 row 
			x = self.pointer["x"]
			y -= self.square_h

	def move_down(self):
		self.pointer["y"] -= self.square_h

		if self.pointer["y"] <= -int(self.screen_height/2):
			self.pointer["y"] = int(self.screen_height/2)

	def left_arrow_press(self):
		self.piece.rotate_left()

	def right_arrow_press(self):
		self.piece.rotate_right()

	def move_up(self):
		self.pointer["y"]+= self.square_h

	def move_left(self):
		print("a pressed self.pointer[0]:",self.pointer["x"])
		self.pointer["x"] -= self.square_w

	def move_right(self):
		print("d pressed self.pointer[0]:",self.pointer["x"])
		self.pointer["x"] += self.square_w
		
	def set_piece(self):
		x_index = int((self.pointer["x"]+400)/self.square_w) 
		y_index = int(-1*(self.pointer["y"]-480)/self.square_h)
		print("x_i:", x_index, "y_i", y_index)
		board_index = y_index*self.board_w+x_index
		print("the pointer's  is at:", board_index)

		#has to be 2 for loops for i in range of 5 to iterate the tetromino
		for row in range(5):
			for col in range(5):
				if self.piece.orientation[(row*self.piece.w)+col] != "#" and self.board[board_index+col] ==0 : # ignore all empty spot 
					continue
				elif self.piece.orientation[(row*self.piece.w)+col] == "#" and self.board[board_index+col] !=0 : # theres collision 
					print("Collision!")
					return 
			board_index += 10
			print("updated board index:", board_index)

		board_index = y_index*self.board_w+x_index
		for row in range(5):
			for col in range(5):
				if self.piece.orientation[(row*self.piece.w)+col] != "#" and self.board[board_index+col] ==0 : # ignore all empty spot 
					continue
				self.board[board_index+col] = "#"
			 # skip one row on the board 
			board_index += 10

		print("NEW BOARD:", self.board)


				



game = Tetris()

# #settings
screen = t.Screen()
screen.setup(game.screen_width,game.screen_height) 
screen.colormode(255)
screen.tracer(0)

game.load_tetromino()

screen.onkey(game.left_arrow_press, "Left")
screen.onkey(game.right_arrow_press, "Right")
screen.onkey(game.move_down,"Down")
screen.onkey(game.move_up,"w")
screen.onkey(game.move_left, "a")
screen.onkey(game.move_right,"d")
screen.onkey(game.set_piece, "s")
screen.listen()
game.hideturtle()


# pen_x = t.goto(-int(screen_width/2)+4*40, int(screen_height/2)-2.5)
# t.dot(10)
# #random piece
# piece = Tetromino()


# #translate piece onto the board 
# def draw_piece():
# 	passs

	


while 1 :
	game.clear()

	# game.move_down()

	game.draw_screen()
	game.draw_tetromino()


	screen.update()

screen.mainloop()