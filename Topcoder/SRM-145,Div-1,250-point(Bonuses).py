class Bonuses:
	def getDivision(self,points):
		total=0
		bonus=[]
		pts=[]
		for i in points:
			total+=i
		left=100
		total = float(total)
		for i in xrange(len(points)):
			bonus.append({"position":i,"bonus":int(points[i]/float(total)*100),"points":points[i]})
			left-=int(points[i]/total*100)
		sorted_list=sorted(bonus, key=lambda k: (k['points'],-k['position']))
		i=len(bonus)-1
		while(left!=0):
			sorted_list[i]["bonus"]+=1
			left-=1
			i-=1
		return [i["bonus"] for i in bonus]