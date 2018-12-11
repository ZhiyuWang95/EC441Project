class Board:

	
	def __init__(self):
		self.config = [[0 for x in range(15)] for x in range(15)]

	def toString(self):
		edge = "  |"
		for m in range(15):
			edge = edge + str(m%10) + '|'
		print(edge)
		rtn="-------------------------------"
		for j in range(15):
			if j < 10:
				rtn+="\n"+ str(0) + str(j) +"|" 
			else:
				rtn+="\n"+ str(j) +"|"
			for i in range(15):
				pos = self.config[i][j]
				if pos==0:
					pos=" "

				rtn+=str(pos)+"|"
		rtn+="\n-------------------------------"
		return rtn
