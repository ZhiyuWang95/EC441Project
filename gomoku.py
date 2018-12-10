from board import Board
from player import Player

class Gomoku:
	def __init__(self):
		self.player1 = Player(1)
		self.player2 = Player(2)
		self.board = Board()

	def input(self):
		print("in")
		turn_x_y = raw_input("Player 1 turn: ")
		turns = turn_x_y.split(',')
		return (turns[0], turns[1])

	#self is object itself (in this case gomoku)
	#capitalize objects and classes
	def play(self, move, player):
		#while True:
		if(player == 1):
			turn_x_y = move#raw_input("Player 1 turn: ")
			turns = turn_x_y.split(',')
			turn_x = turns[0]
			turn_y = turns[1]
			
			if not (self.player1.check_legal(self.board,int(turn_x),int(turn_y))):
				return 0
				'''
				turn_x_y = raw_input("Player 1 turn: ")
				turns = turn_x_y.split(',')
				turn_x = turns[0]
				turn_y = turns[1]
				'''
			self.player1.move(self.board,int(turn_x),int(turn_y))
			
			if self.player1.win(self.board,int(turn_x),int(turn_y)):
				print("Player 1 wins")
				return 1

		elif(player == 2):
			turn_x_y = move#raw_input("Player 2 turn: ")
			turns = turn_x_y.split(',')
			turn_x = turns[0]
			turn_y = turns[1]

			if not (self.player2.check_legal(self.board,int(turn_x),int(turn_y))):
				return 0
				'''
				turn_x_y = raw_input("Player 2 turn: ")
				turns = turn_x_y.split(',')
				turn_x = turns[0]
				turn_y = turns[1]
				'''
			self.player2.move(self.board,int(turn_x),int(turn_y))
			
			if self.player2.win(self.board,int(turn_x),int(turn_y)):
				print("Player 2 wins")
				return 1

#game = Gomoku()
#game.play()

