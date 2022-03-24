#!usr/env/bin python

def main():
	arr = [4,5,6,8,7,2,1,5,6,4,5,1]

	busca_valor = int(input("Qual o valor que deseja buscar? "))
	encontrado = False	
	
	for x in range(len(arr)):
		if busca_valor == arr[x]:
			print(f'valor encontrado na posicao {x}')
			encontrado = True
			break

	if not encontrado:
		print('Valor nao foi encontrado')

if __name__ == '__main__':
	main()