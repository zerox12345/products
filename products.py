import os

#Load the file
products = []
if os.path.isfile('products.csv'):
	print('找到檔案惹')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	for i in products:
		print(i)
else:
	print('找不到檔案QQ')


#Let user input
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
			break
	price = input('請輸入商品價格')
	products.append([name, price])
print(products)

#列出購買紀錄
for p in products:
	print(p)

#write the file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')