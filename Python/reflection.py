class Cat(object):
	def __init__(self, name="kitty"):
		self.name = name
	
	def sayHi(self):
		print(self.name, "say Hi")

kit = Cat()
print("name is:", kit.name)
kit.sayHi()

print(dir(kit))
print(dir(Cat))

# 判断是否方法或属性是否存在
print(hasattr(kit,'sayHi'))
print(hasattr(kit,'name'))

# 设置 name 属性
setattr(kit, 'name', 'xiaohei')
print("name is:", kit.name)

# 通过反射的方式调用 sayHi 方法
func = getattr(kit, 'sayHi')
func()

# 删除属性
delattr(kit, name)
print("name is:", kit.name)
