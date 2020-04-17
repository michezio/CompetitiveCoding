'''
not an optimal solution, more complex than necessary
but still sufficiently fast and clean
'''

class Solution:
	def checkValidString(self, s):
		s = list(s)
		if len(s) == 0:
			return True
		if s[0] == ')' or s[-1] == '(':
			return False
		stat = [0]
		st = []
		for i in range(len(s)):
			c = s[i]
			if c == '(':
				stat.append(stat[-1] + 1)
			elif c == ')':
				stat.append(stat[-1] - 1)
			elif c == '*':
				stat.append(stat[-1])
				st.append(i)
			if stat[-1] < 0:
				if len(st) == 0:
					return False
				else:
					for k in range(st.pop(),len(stat)):
						stat[k] += 1
		if stat[-1] == 0:
			return True
		if stat[-1] > len(st):
			return False
		else:
			while(stat[-1] > 0):
				for k in range(st.pop(),len(stat)):
						stat[k] -= 1
						if stat[k] < 0:
							return False
			return True
