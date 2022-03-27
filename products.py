import os

#Load the file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products		



#Let user input
def input_newproduct(products):
	while True:
		name = input('請輸入商品名稱')
		if name == 'q':
			break
		price = input('請輸入商品價格')
		products.append([name, price])
	return products

#列出購買紀錄
def print_products(products):
	for p in products:
		print(p)

#write the file
def put_in(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('找到檔案惹')
		products = read_file(filename)
	else:
		print('找不到檔案QQ')
		products = []
	
	products = input_newproduct(products)
	put_in(filename, products)
	print_products(products)


main()