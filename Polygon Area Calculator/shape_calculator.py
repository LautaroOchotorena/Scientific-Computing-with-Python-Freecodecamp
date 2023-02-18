#Rectangle Class
class Rectangle:
	def __init__(self, wid, heig):	#Constructor
		self.width = wid
		self.height = heig
	def set_width(self,wid):
		self.width = wid
	def set_height(self,heig):
		self.height = heig
	def get_area(self):
		return(self.height*self.width)
	def get_perimeter(self):
		return(2*self.height+2*self.width)
	def get_diagonal(self):
		return((self.width ** 2 + self.height ** 2) ** .5)
	def get_picture(self):  #it prints the rectangle
		if(self.height<=50 and self.width<=50):
			text=''
			for k in range(1,self.height+1):
				text+='*'*self.width+'\n'
			return(text)
		else:
			return("Too big for picture.")
	def get_amount_inside(self,shape):  #how many amount of shapes fit into the rectangle
		heig=self.height
		wid=self.width
		count=0
		while(shape.height<=heig and shape.width<=wid):
			count+=1
			heig1=heig-shape.height
			while(shape.height<=heig1):
				count+=1
				heig1-=shape.height
			wid1=wid-shape.width
			while(shape.width<=wid1):
				count+=1
				wid1-=shape.width
			wid-=shape.width
			heig-=shape.height
		return(count)
	def __str__(self):
		return('Rectangle(width='+str(self.width)+', height='+str(self.height)+')')

#Square Class
class Square(Rectangle):
	def __init__(self, side):
		self.height=side
		self.width=side
	def set_side(self,side):
		self.height=side
		self.width=side
	def __str__(self):
		return('Square(side='+str(self.width)+')')