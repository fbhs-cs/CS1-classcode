class NumChanger:
	def __init__(self, l):
    		self.nums = l
	def add_to(self, x):
    		for i in range(0,len(self.nums)):
        		self.nums[i] = self.nums[i]+x
	def mult_to(self, x):
    		for i in range(0,len(self.nums)):
        		self.nums[i] = self.nums[i]*x
	def remove_from(self, x):
    		if x in self.nums:
        		self.nums.remove(x)
        		return True
    		else:
        		return False
	def get_sum(self):
    		return sum(self.nums)
	def average(self):
    		return sum(self.nums) / len(self.nums)
	def mode(self):
    		cm = (0,0)
    		for n in self.nums:
        		if self.nums.count(n)>cm[1]:
            		cm = (n,self.nums.count(n))
    				return cm[0]
	def __str__(self):
    		out = ' '
    	for num in self.nums:
        	out = out + str(num) + ' '
    		return out
def main():
	test = NumChanger([10, 3, 8, 7, 6, 5, 4, 8, 2, 8])
	print(test)
	test.add_to(4)
	print(test)
	print(test.remove_from(10))
	print(test)
	print(test.get_sum())
	print(test.average())
	print(test.mode())
	test2 = NumChanger([1, 5, 7, 7, 12, 3, 4])
	print(test2)
	test2.mult_to(2)
	print(test2.remove_from(5))
	print(test2)
	print(test2.get_sum())
	print(test2.average())
	print(test2.mode())
if __name__ == "__main__":
	main()
