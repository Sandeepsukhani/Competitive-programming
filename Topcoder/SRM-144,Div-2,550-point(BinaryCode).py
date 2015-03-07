class BinaryCode:
	def decode(self,message):
		if len(message)==1:
			if message=="0":return ("0","NONE")
			return ("NONE","1")
		x=self.process("0",message)
		y=self.process("1",message)
		return (x,y)
	
	def process(self,P_0,message):
		output=[P_0]*len(message)
		output[1]=str(int(message[0])-int(P_0))
		i=2
		while(i<len(message)):
			#Finding original sequence by subtracting i-1th and i-2nd element of original sequence(Found earlier) from ith element of encrypted sequence 
			P_i=int(message[i-1])-int(output[i-1])-int(output[i-2])
			#If P_i is greater than 1, that means its invalid
			if P_i>1:return "NONE"
			output[i]=str(P_i)
			i+=1
		if int(message[len(message)-1])==(int(output[len(output)-1])+int(output[len(output)-2])):
			return "".join(output)
		return "NONE"