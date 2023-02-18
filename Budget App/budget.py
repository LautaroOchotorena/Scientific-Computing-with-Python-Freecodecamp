import math
class Category: #Clase
	cat=''  #category
	deposit_ = 0   #Total deposit
	withdraw_ = 0  #Total withdraw
	def __init__(self, type1):	#Constructor
		self.cat = type1
		self.ledger = list()
	def deposit(self,amount,description=''):  #deposit method
		dic = dict()
		dic["description"] = description
		dic["amount"] = amount
		self.deposit_ = self.deposit_ + amount
		self.ledger.append(dic)
	def withdraw(self,amount,description=""):  #withdraw method
		dic = dict()
		if self.check_funds(amount)==True:
			dic["description"] = description
			dic["amount"] = -amount
			self.withdraw_ = self.withdraw_ + amount
			self.ledger.append(dic)
			return(True)
		else: 
			return(False)
	def get_balance(self):  #get_balance method
		return(self.deposit_-self.withdraw_)
	def transfer(self,amount,type1):  #transfer method
		if (self.check_funds(amount)==True):
			type1.deposit(amount,'Transfer from ' + self.cat)
			self.withdraw(amount,'Transfer to ' + type1.cat)
			return(True)
		else: 
			return(False)
	def check_funds(self,amount):  #Check_funds method
		if (self.deposit_-self.withdraw_<amount):
			return(False)
		else: return(True)
	def __str__(self):  #diplay categories
		text = '*'*(int((30-len(self.cat))/2))+self.cat+'*'*(int((30-len(self.cat))/2))+'\n'
		for desc_money in self.ledger:
			if len(str(desc_money["amount"]))<=7:
				desc_money["amount"]=("{:.2f}".format(desc_money["amount"]))
			text = text + str(desc_money["description"][:23:1]) + ' '*(30-len(desc_money["description"][:23:1])-len(str(desc_money["amount"]))) + str(desc_money["amount"]) + '\n'
		text = text + 'Total: ' + str(self.get_balance())
		return(text)
def create_spend_chart(list1):  #graphic
	total_spend = 0    #total_spend between all the categories 
	per = [-1]*5
	i = 1
	maxi=0  #maximum lenght of categories
	for category in list1:
		total_spend += category.withdraw_
		if maxi<len(category.cat):
			maxi = len(category.cat)
	for category in list1:
		per[i] = math.floor((category.withdraw_/total_spend)*10)*10
		i+=1
	text = 'Percentage spent by category\n'
	for i in reversed(range(11)):
		if 0<i<10:
			text = text + ' ' + str(10*i) + "| "
		elif i==10:
			text = text + str(10*i) + "| "
		elif i==0:
			text = text + '  ' + str(10*i) + "| "
		for j in range(1,len(list1)+1):
			if per[j]>=10*i:
				text+='o  '
			else:
				text+='   '
		text += '\n'
	text+='    '+'-'*(3*len(list1)+1)+'\n'
	for k in range(maxi):
		text+=' '*5
		for category in list1:
			if k<len(category.cat):
				text+=category.cat[k]+' '*2
			else:
				text+=' '*3
		if k<maxi-1:
			text+='\n'
	return(text)