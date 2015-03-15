class RectangularGrid:
	def countRectangles(self,width,height):
		if width>height:
			width,height=height,width
		i=1
		total=0
		#Finding blocks vertically and horizontally.
		while i<=width:
			j=i+1
			while j<=height:
				column_wise_fit=height-j+1
				row_wise_fit=width-i+1
				total+=column_wise_fit*row_wise_fit
				if j<=width and i<=height:
					column_wise_fit=height-i+1
					row_wise_fit=width-j+1
					total+=column_wise_fit*row_wise_fit
				j+=1
			i+=1
		
		return total