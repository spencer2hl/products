products = []
while True:
	name = input('请输入商品名称：')
	if name == 'q': 
		break
	price = input('请输入商品价格：')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的价格', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.txt', 'w', encoding = 'utf-8') as f:
	f. write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # ‘\n’ 换行








