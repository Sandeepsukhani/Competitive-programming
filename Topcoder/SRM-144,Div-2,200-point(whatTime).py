class Time:
	def whatTime(self,sec):
		if sec==0:
			return "0:0:0"
		#Finding how many hours fits in given seconds
		h=sec/3600
		sec%=3600
		#Finding how many mins fits from what is left
		m=sec/60
		sec%=60
		return str(h)+":"+str(m)+":"+str(sec)