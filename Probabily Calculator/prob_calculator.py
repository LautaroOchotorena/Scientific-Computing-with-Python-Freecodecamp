import copy
import random
class Hat:
	def __init__(self, **colors):
		self.contents = list()
		for (color,value) in colors.items():
			for t in range(value):
				self.contents.append(color)
	def draw(self,number):
		list2 = list()
		if (number<=len(self.contents)):
			for k in range(number):
				x=random.choice(self.contents)
				list2.append(x)
				self.contents.remove(x)
		else:
			list2 = self.contents
			self.contents = list()
		return(list2)
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
	count=0
	for k in range(num_experiments):
		hat1 = copy.deepcopy(hat)
		list1 = hat1.draw(num_balls_drawn)
		leng_list1 = len(list1)
		total_balls_ext=0
		for t in expected_balls.keys():
			for j in range(expected_balls[t]):
				total_balls_ext+=1
				if t in list1:
					list1.remove(t)
		if len(list1)+total_balls_ext==leng_list1:
			count+=1
	return(count/num_experiments)


random.seed(95)
hat=Hat(red=3,blue=2)
print(hat.contents)
hat=Hat(red=5,blue=2)
print(hat.contents)
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print("Probability:", probability)

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print("Probability:", probability)
