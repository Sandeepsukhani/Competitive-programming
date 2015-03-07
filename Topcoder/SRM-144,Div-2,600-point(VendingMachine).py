class VendingMachine:
	def motorUse(self,price,purchases):
		if type(price)==str:
			price=[price]
		else:
			price=list(price)
		total_cols=len(price[0].split(" "))
		total_price=[0]*total_cols
		time=0
		for i in xrange(len(price)):
			price[i]=price[i].split(" ")
			for j in xrange(len(price[i])):
				price[i][j]=int(price[i][j])
				total_price[j]+=price[i][j]
		current_index=0
		move_to=self.findMax(total_price)
		time+=self.find_move_cost(current_index,move_to,total_cols)
		prev_purchase_index=0
		current_index=move_to
		for i in xrange(len(purchases)):
			if int(purchases[i].split(":")[1])-int(purchases[prev_purchase_index].split(":")[1])>=5:
				move_to=self.findMax(total_price)
				time+=self.find_move_cost(current_index,move_to,total_cols)
				current_index=move_to
			purchase=purchases[i]
			r,c=[int(j) for j in purchase.split(":")[0].split(",")]
			if price[r][c]==-1:
				return -1
			time+=self.find_move_cost(current_index,c,total_cols)
			total_price[c]-=price[r][c]
			price[r][c]=-1
			prev_purchase_index=i
			current_index=c
		move_to=self.findMax(total_price)
		time+=self.find_move_cost(current_index,move_to,total_cols)
		return time

	def findMax(self,total_prices):
		max=total_prices[0]
		index=0
		for i in xrange(len(total_prices)):
			if total_prices[i]>max:
				max=total_prices[i]
				index=i
		return index

	def find_move_cost(self,current_index,move_to,total_cols):
		return (abs(move_to-current_index) if abs(move_to-current_index)<(total_cols-abs(move_to-current_index)) else (total_cols-abs(move_to-current_index)))