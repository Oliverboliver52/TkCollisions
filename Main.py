
class collisions:
	def check(shapeA, shapeToCheck,canvas):
		pos = canvas.coords(shapeA)
		collisions = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
		if shapeToCheck in collisions:
			return True
		else:
			return False
	def getCol(shape,canvas):
		pos = canvas.coords(shape)
		return canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
	def flappyScore(bird,*pipes,canvas):
		for i in pipes:
			if canvas.coords(bird)[2] >= canvas.coords(i)[0] and canvas.coords(bird)[2] <= canvas.coords[i][0] + 4:
				return True
		return False
