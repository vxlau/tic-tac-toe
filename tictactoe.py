import random

'''
Tic tac toe game

6-30-14
'''


game_over  = False
win = False
lost = False

board = [ ['' for x in range(3)] for x in range(3)] #2d arrary empty board


#maps board positions to 2d matrix positions
#returns string type in row , col format
def map_pos(pos):
	pos_dic = {1:'0,0', 2:'0,1', 3:'0,2', 4:'1,0', 5:'1,1', 6:'1,2', 7:'2,0', 8:'2,1', 9:'2,2'}
	return pos_dic[int(pos)]
	

#function prints snapshot of board
def print_board():
	for row in range(0,3):
		for col in range(0,3):
			print board[row][col],
			if col != 2: 
				print '|',	
		print ''

def print_instr():
	print 'Tic Tac Toe'
	print 'First person to get 3 in a row wins!'
	print 'You are X'
	print 'Rules: Enter numbers 1-9 to place a piece on the board'
	print ' 1|2|3 '
	print ' 4|5|6 '
	print ' 7|8|9 ' 

#checks if user's move is valid.
#if valid, inputs X into array
#else returns false
def user_move(pos):
	global board

	board_pos = map_pos(pos)
	input_row = int( board_pos.split(',')[0][0] )
	input_col = int( board_pos.split(',')[1] )

	if board[input_row][input_col] == '':
		board[input_row][input_col] = 'X'
	
	else:
		return False	

#randomly checks if a position is taken
#if not, place mark in board		
def ai_move():
	#got string in row , col format; need to parse for each
	ai_row_map = map_pos(random.randint(1,9) )
	ai_col_map = map_pos( random.randint(1,9) )
		
	ai_row = int( ai_row_map.split(',')[0][0])
	ai_col = int( ai_col_map.split(',')[1] )

	while board[ai_row][ai_col] != '':
		ai_row_map = map_pos(random.randint(1,9) )
	        ai_col_map = map_pos( random.randint(1,9) )
		ai_row = int( ai_row_map.split(',')[0][0])
	        ai_col = int( ai_col_map.split(',')[1] )

	board[ai_row][ai_col] = 'O'

def smart_ai_move():
	#did not finish
	return 'hi' 

#check if end condition is reached
def check_end():
	for i in range(0,3):
		#check horizontal and vertical win conditions
		if board[i][0] == board[i][1] == board[i][2] != '' \
		or board[0][i] == board[1][i] == board[2][i] != '' :
			print 'Game Over across'
			return True
		#check diagonal win conditions	
		if board[0][0] == board[1][1] == board[2][2] != '' \
		or board[0][2] == board[1][1] == board[2][0] != '':
			print 'Game Over diagonal'
			return True
		#check draw condition
		if '' not in board[0] and '' not in board[1] and '' not in board[2]:
			print 'Game Over draw'
			return True
	return False

print_instr()
print 'Current board'
print_board()		
while game_over != True:
	print 'It is your turn '
	
	try:
		move = int( raw_input('Place piece on: ') )
		if move <= 9 and move >= 1:
			valid = user_move(move) #user makes move if valid 
			if valid == False:
				print 'Invalid: Position is alreay taken'
				print_board()
				continue
			else:   #----------------------can't differienate draw  -------
				print 'The current board is: '
				print_board()
				game_over= check_end()
				if game_over == True:
					print 'Congrats, you won!'
					break

				#AI makes a move
				print 'Now it is AI turn'
				ai_move()
				print 'The current board is: '
				print_board()
				game_over=check_end()
				if game_over == True:
					print 'Sorry, you lost'
					break
			
		else:
			print('You need to eneter an integer between 1-9')		
	except ValueError:
		print ('You need to enter a valid interger')
		continue
	
			
