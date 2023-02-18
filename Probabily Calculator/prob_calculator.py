import copy
import random
class Hat:
	def __init__(self, **colors):
		self.contents=list()
		for (color,value) in colors.items():
			for t in range(value):
				self.contents.append(color)
	def draw(self,number):   #Remove balls
		list2 = list()
		if (number<=len(self.contents)):
			for k in range(number):
				x=random.choice(self.contents)
				list2.append(x)
				self.contents.remove(x)
		else:
			list2 = self.contents
		return(list2)
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):  #Calculate the prob
	count=0
	hat1 = Hat(**expected_balls)
	for k in range(num_experiments):  #Use the class
		hat2 = copy.deepcopy(hat)
		list = hat2.draw(num_balls_drawn)
		for color in hat1.contents:  #I wanna remove the whole hat1.contest from list
			try:
				list.remove(color)
        #if it posible continue removing
			except:
        #If it isn't possible
				count-=1
				break
		count+=1
	return(count/num_experiments)