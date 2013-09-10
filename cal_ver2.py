def assertTrue(bool):
	print bool

def assertFalse(bool):
	print not bool
	
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b

#eval
	
class Equation:
	def __init__(self, eqn):
		self.eqn = eqn 
		self.div_sub = False
		self.mul_sub = False
	def is_pair(self):	 
		result = 0
		for i in range(len(self.eqn)):
			if self.eqn[i]=='('  :
				result+=1
			elif self.eqn[i]==')':
				result-=1 
		return result==0	 
	def find_end_paren(self, start):
		result = 0
		end = -1
		for i in range(start, len(self.eqn)):
			if self.eqn[i]=='('  :
				result+=1
			elif self.eqn[i]==')':
				result-=1 
			if result == 0 and end==-1:
				end = i
		return end
	def in_paren(self): 
		return self.eqn.find('(')!=-1 and self.eqn.find(')')!=-1
	def in_mul_div(self):
		return self.eqn.find('*')!=-1 or self.eqn.find('/')!=-1
	def in_add_sub(self):
		return self.eqn.find('+')!=-1  or self.eqn.find('-')!=-1
	def get_front_eq(self, start):
		add_end = self.eqn[:start].rfind('+')
		sub_end = self.eqn[:start].rfind('-')
		mul_end = self.eqn[:start].rfind('*')
		div_end = self.eqn[:start].rfind('/')
		
		temp_end_list=[]
		temp_end_list.append(add_end)
		temp_end_list.append(sub_end)
		temp_end_list.append(mul_end)
		temp_end_list.append(div_end)
		"""
		for end in temp_end_list:
			if end==(start-1):
				print "no parameter"
		"""
		start_list = []
		if add_end!=-1 and add_end!=0:
			start_list.append(add_end)
		if sub_end!=-1 and sub_end!=0:
			start_list.append(sub_end) 
		if len(start_list)==0:
			return 0,self.eqn[:start]
		else:
			return  max(start_list)+1,self.eqn[ max(start_list)+1:start]
		return ''
	def get_back_eq(self, start):
		add_start = self.eqn[start+1:].find('+')
		sub_start = self.eqn[start+1:].find('-')
		mul_start = self.eqn[start+1:].find('*')
		div_start = self.eqn[start+1:].find('/')
		
		temp_start_list=[]
		temp_start_list.append(add_start)
		temp_start_list.append(sub_start)
		temp_start_list.append(mul_start)
		temp_start_list.append(div_start)
		
		"""
		for temp_start in temp_start_list:
			if temp_start==(start+1):
				print "no parameter"
		"""
		 
		if sub_start == 0 and self.div_sub:
			sub_start = self.eqn[start+2:].find('-')
			if sub_start != -1:
				sub_start += 1
			self.div_sub = False
		 
		if sub_start == 0 and self.mul_sub:
			sub_start = self.eqn[start+2:].find('-')
			if sub_start != -1:
				sub_start += 1
			self.mul_sub = False
		
		start_list = []
		if add_start!=-1:
			start_list.append(add_start)
		if sub_start!=-1:
			start_list.append(sub_start) 
			
			
		if mul_start!=-1:
			start_list.append(mul_start)
		if div_start!=-1:
			start_list.append(div_start)
		if len(start_list) ==0:
			return len(self.eqn), self.eqn[start+1:]
		else:	 
			return start+1+min(start_list), self.eqn[start+1:start+1+min(start_list)]
		
		return ''
	def calculate(self):
		if not self.is_pair():
			print 'not good pair'
			return self.eqn
		#while True: 
		while True:
			
			if self.eqn[1:].isdigit() or self.eqn.isdigit():
				#print self.eqn
				return str(int(self.eqn))
			
			if self.in_paren(): 
				start_paren = self.eqn.find('(')
				end_paren = self.find_end_paren(start_paren)
				new_eqn = self.eqn[start_paren+1:end_paren]
				new_eqn = Equation(new_eqn).calculate()
				front_eqn = self.eqn[:start_paren]
				if front_eqn!='' and new_eqn[0]=='-':
					if front_eqn[-1]=='+':
						front_eqn = front_eqn[:-1]
					elif front_eqn[-1]=='-':
						front_eqn = front_eqn[:-1]+'+'
						new_eqn = new_eqn[1:] 
					elif front_eqn[-1]=='/':
						self.div_sub = True
					elif front_eqn[-1]=='*':
						self.mul_sub = True
				self.eqn = front_eqn+new_eqn+self.eqn[end_paren+1:]
				#operated = True
				#print self.eqn
			elif self.in_mul_div():
				start_mul = self.eqn.find('*')
				start_div = self.eqn.find('/')
				start_list = []
				if start_mul !=-1:
					start_list.append(start_mul)
				if start_div != -1:
					start_list.append(start_div)
				start = min(start_list) 
				#print start, start_mul, start_div
				front_idx, front_eq = self.get_front_eq(start)
				back_idx, back_eq = self.get_back_eq(start) 
				front_rest = ''
				back_rest = ''
				if front_idx!=0:
					front_rest = self.eqn[:front_idx]
				if back_idx !=len(self.eqn):
					back_rest = self.eqn[back_idx:] 
				new_eqn = ''
				if self.eqn[start] =='*':
					new_eqn = str(mul(int(front_eq), int(back_eq) )) 
				elif self.eqn[start]=='/':
					new_eqn = str(div(int(front_eq), int(back_eq) )) 
				
				if front_rest!='' and new_eqn[0]=='-':
					if front_rest[-1]=='+':
						front_rest = front_rest[:-1]
					elif front_eqn[-1]=='-':
						front_rest = front_rest[:-1]+'+'
						new_eqn = new_eqn[1:] 
				self.eqn = front_rest + new_eqn +back_rest		
				#operated = True
			
			elif self.in_add_sub() :
				#pass
				#print self.eqn
				 
				start_add = self.eqn.find('+')
				start_sub = self.eqn.find('-')
				start_list = []
				if start_add == 0:
					start_add = self.eqn[1:].find('+')
					if start_add!=-1:
						start_add+=1
				if start_sub == 0:
					start_sub = self.eqn[1:].find('-')
					if start_sub!=-1:
						start_sub+=1
								
				if start_add !=-1 and start_add!=0:
					start_list.append(start_add)
				if start_sub != -1 and start_sub!=0:
					start_list.append(start_sub)
				start = min(start_list) 
				#print start, start_mul, start_div
				front_idx, front_eq = self.get_front_eq(start)
				back_idx, back_eq = self.get_back_eq(start) 
				front_rest = ''
				back_rest = ''
				if front_idx!=0:
					front_rest = self.eqn[:front_idx]
				if back_idx !=len(self.eqn):
					back_rest = self.eqn[back_idx:]
				if self.eqn[start] =='+':
					self.eqn = front_rest+ str(add(int(front_eq), int(back_eq) ))+back_rest
				elif self.eqn[start]=='-':
					self.eqn = front_rest + str(sub(int(front_eq), int(back_eq) ))+back_rest
			"""
			if self.eqn[1:].isdigit() or self.eqn.isdigit():
				print self.eqn
				return str(int(self.eqn))
			"""
			#print self.eqn	
				#break 
		return self.eqn

assertTrue( Equation('(1+5*(3+(-4)*4)-2/3)').calculate() == '-64' )
assertTrue( Equation('4*3').calculate()=='12')
assertTrue( Equation('(1*5*(3/(-4)*4)*2/3)').calculate() == '-14' )
assertTrue( Equation('(1-5+(3-(-4)+4)-2+3)').calculate() == '8' )
assertTrue(Equation('(3/4*4)').calculate() == '0')
assertTrue(Equation('3+4*2').calculate() == '11')
assertTrue(Equation('(4+3)*5').calculate() =='35')
assertTrue(Equation('-(-3)').calculate() == '3')
assertTrue(Equation('+(-3)').calculate() == '-3')
assertTrue(Equation('-4-2').calculate() == '-6')
assertTrue(Equation('+4+2').calculate() == '6')

#Equation('3+*4').calculate()
	