class MyClass:
	name = "BILL"

	def __init__(self):
		print("构造函数被调用")
		self.value = 20

	@staticmethod
	def run():
		print('*', MyClass.name, '*')
		print("call static method")
	
	@classmethod

	def do(self):
		print('[', self.name, ']')
		print("in class method , call static method")

		self.run()

	def do1(self):
		print(self.value)
		print('<', self.name,'>')
		print(self)

MyClass.run()
c = MyClass()
c.do()

print('MyClass.name=', MyClass.name)
c.do1()
