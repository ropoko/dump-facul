#!usr/env/bin python

def main():
	arr = [4,5,6,8,7,2,1,5,6,4,5,1]

	print(arr)	
	
	for i in range(len(arr)):	
		menor = i
		
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[menor]:
				menor = j

		arr[menor], arr[i] = arr[i], arr[menor]

	print(arr)

if __name__ == '__main__':
	main()