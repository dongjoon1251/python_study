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
		self.eqn_list = []
	def make_list(self):
		if not len(self.eqn.split('(')) == len(self.eqn.split(')')) :
			return "paren number error"
		start = self.eqn.find('(')
		end = -1
		if not start == -1: 
			result = 1
			for i in range(len(self.eqn)):
				if self.eqn[i]=='(' and not i==start:
					result+=1
				elif self.eqn[i]==')':
					result-=1
				if result ==0 and end == -1:
					end = i
			if not start == 0: 
				if not self.eqn[:start-1] == '':
					self.eqn_list.append(self.eqn[:start-1])
				self.eqn_list.append(self.eqn[start-1:end+1])	
				
			else:
				self.eqn_list.append(self.eqn[start+1:end])	
			if not (end+1) == len(self.eqn):
				self.eqn_list.append(self.eqn[end+1:]) 
			else:
				if self.eqn[:start-1] == '': 
					if self.eqn[0]=='-' and self.eqn[2]=='-':
						self.eqn_list[0]='+'+self.eqn_list[0][3:-1]
					elif (self.eqn[0]=='-' or self.eqn[2]=='-') and not self.eqn[2].isdigit():
						self.eqn_list[0]='-'+self.eqn_list[0][3:-1]
						#print self.eqn
					elif self.eqn[0]=='+' and self.eqn[2]=='+':
						self.eqn_list[0]='+'+self.eqn_list[0][3:-1]
					elif self.eqn[0] == '-':
						self.eqn_list.append('*'+self.eqn_list[0][1:]) 
						self.eqn_list[0]= '-1'
					elif self.eqn[0] =='+':
						self.eqn_list.append('+'+self.eqn_list[0][1:]) 
						self.eqn_list[0]= '0'
					
			#print self.eqn_list
		else:
			start = self.eqn[0:].find('+')
			#print self.eqn
			if self.eqn[0]=='+':
				start = self.eqn[1:].find('+')
			start_sub= self.eqn[0:].find('-')
			if self.eqn[0]=='-':
				start_sub = self.eqn[1:].find('-')+1 
			start_mul= self.eqn[0:].find('*')
			if self.eqn[0]=='*':
				start_mul = self.eqn[1:].find('*')+1
			start_div= self.eqn[0:].find('/')
			if self.eqn[0]=='/':
				start_div = self.eqn[1:].find('/') +1
			
			if not start == -1:  
				if not self.eqn[:start] == '':
					self.eqn_list.append(self.eqn[:start])
				self.eqn_list.append(self.eqn[start:])
			elif not start_sub == -1:  
				if not self.eqn[:start_sub] == '':
					self.eqn_list.append(self.eqn[:start_sub])
				self.eqn_list.append(self.eqn[start_sub:])
				#print self.eqn_list
			elif not start_mul == -1:  
				if not self.eqn[:start_mul] == '':
					self.eqn_list.append(self.eqn[:start_mul])
				self.eqn_list.append(self.eqn[start_mul:])
			elif not start_div == -1:  
				if not self.eqn[:start_div] == '':
					self.eqn_list.append(self.eqn[:start_div])
				self.eqn_list.append(self.eqn[start_div:])
			else:
				self.eqn_list.append(self.eqn) 
		return self.eqn_list
	
	def calculate(self): 
		if self.make_list() == "paren number error":
			print "paren number error"
			return None 
		if len(self.eqn_list) ==1: 
			if self.eqn_list[0][0:].isdigit() or self.eqn_list[0][1:].isdigit():
				return int(self.eqn_list[0])
		result =0
		if self.eqn_list[0][0] == '+': 
			result = Equation(self.eqn_list[0][1:]).calculate()
		elif  self.eqn_list[0][0] == '-': 
			result = -1*Equation(self.eqn_list[0][1:]).calculate()
		else:
			result = Equation(self.eqn_list[0]).calculate()	
		 
		for i in range(len(self.eqn_list)-1):
			oper_type = self.eqn_list[i+1][0]
			if oper_type == '-':
				next_eqn = Equation(self.eqn_list[i+1][:]).calculate()
				result = add(result,next_eqn)
			else:
				next_eqn = Equation(self.eqn_list[i+1][1:]).calculate()
			if oper_type=='+':
				result = add(result, next_eqn) 
			if oper_type=='*':
				result = mul(result, next_eqn)
			if oper_type=='/':
				result = div(result, next_eqn)
		
		return result
	
def testParen():
	assertTrue(Equation('1+(4+3)*5').make_list()[1]=='+(4+3)')
	assertTrue(Equation('((4+3)*5)').make_list()[0]=='(4+3)*5')	
	assertTrue(Equation('(4+3)*(5-2)').make_list()[0]=='4+3')	
	assertTrue(Equation('(4+3)*(5-2)').make_list()[1]=='*(5-2)')
	assertTrue(Equation('-(-1)+(4-3)').make_list()[0]=='-(-1)')
	assertTrue(Equation('1+(4-3)').make_list()[1]=='+(4-3)')
	assertTrue(Equation('-(-1)').make_list()[0]=='+1')
	assertTrue(Equation('+(-1)').make_list()[0]=='-1')
	assertTrue(Equation('-(+1)').make_list()[0]=='-1')
	assertTrue(Equation('+(+1)').make_list()[0]=='+1')
	
	assertTrue(Equation('-(+1)').calculate() == -1)
def testMul():
	assertTrue(Equation('2*3').calculate() == 6)
	assertTrue(Equation('1+2*3').calculate() == 7)
	assertTrue(0==Equation('1-(-1+3)*3+5').calculate())
	print Equation('1-(-1+3)*3+5').make_list()
	assertTrue(9==Equation('1-(-1)*3+5').calculate())
	print Equation('1-(-1)*3+5').calculate()
	assertTrue(-19==Equation('2-3*(4+3)').calculate())
	assertTrue(7==Equation('-(-1)*(4+3)').calculate())
	assertTrue(-7==Equation('-1*(4+3)').calculate())
	assertTrue(-12==Equation('+(4*3)*(-1)').calculate()) 
	assertTrue(12==Equation('+(4*3)').calculate())
	
	 
def testAdd(): 
	assertTrue(4==Equation('1+3').calculate())
	assertFalse(4==Equation('1+4').calculate())
	assertTrue(10==Equation('1-(-1)+3+5').calculate())
	assertTrue(8==Equation('-(-1)+(4+3)').calculate())
	assertTrue(8==Equation('+(4+3)-(-1)').calculate()) 
	assertTrue(7==Equation('+(4+3)').calculate())
  
def testSub():
	assertFalse(3==Equation('3-1').calculate())
	assertTrue(3==Equation('4-1').calculate())
	assertTrue('-3'==Equation('-3-1').make_list()[0])
	assertTrue(-6==Equation('-3-1-2').calculate())
	assertTrue(-8==Equation('-1-(-1)-3-5').calculate())
	assertTrue(0==Equation('-(-1)-(4-3)').calculate())
	#print Equation('-(-1)-(4-3)').make_list()
	assertTrue(0==Equation('-(4-3)-(-1)').calculate()) 
	assertTrue(-1==Equation('-(4-3)').calculate())
	#print Equation('-(4-3)').make_list()

#testAdd()
#testSub()
#testParen()
#testMul()