import os # operating system
products = []
if os.path.isfile('products.txt'):
	print('yeah!找到档案了')
	with open('products.txt', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品, 价格' in line:
				continue		
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products) 
else:
	pring('找不到档案......')

#让使用者输入
while True:
	name = input('请输入商品名称：')
	if name == 'q': 
		break
	price = input('请输入商品价格：')
	price = int(price)
print(products)

#印出所有购买记录
for p in products:
	print(p[0], '的价格', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

#写入档案
with open('products.txt', 'w', encoding = 'utf-8') as f:
	f. write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # ‘\n’ 换行








