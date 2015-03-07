class PowerOutage:
	def estimateTimeOut(self,u=(),v=(),cost=()):
		self.tree={}
		for i in xrange(len(u)):
			self.tree[u[i]]=self.tree.get(u[i],[])+[(v[i],cost[i])]
		#Returning one way cost because that's what needed
		return self.traverse()[0]

	def traverse(self,node=0):
		if not self.tree.get(node):
			return (0,0)
		child_cost=[]
		max=-1
		one_way_cost=0
		return_cost=0
		for child in self.tree[node]:
			#Recursively finding return and one way cost of nodes.
			cost = self.traverse(child[0])
			#Finding return cost and one way cost of this node + child node's costs
			cost = (cost[0]+child[1],cost[1]+child[1]*2)
			if cost[1]>max:max=cost[1]
			child_cost.append(cost)
		#Finding costliest route below this node.
		for cost in child_cost:
			if cost[1]==max:
				max=-1
				one_way_cost+=cost[0]
				return_cost+=cost[1]
			else:
				one_way_cost+=cost[1]
				return_cost+=cost[1]
		return (one_way_cost,return_cost)