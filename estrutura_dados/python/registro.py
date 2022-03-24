#!usr/env/bin python

def main():
	registro = []

	print('Faca o cadastro de 4 pessoas: ')

	for i in range(1):
		nome = str(input('Digite seu nome: '))
		idade = int(input('Digite sua idade: '))
		telefone = str(input('Digite o numero de telefone: '))
		cod_area = int(input('Digite o codigo de area: '))
		registro.append({ "nome": nome, "idade": idade, "telefone": telefone, "cod_area": cod_area })
		
	resposta = str(input('deseja exibir o relatório? s/n: '))

	if resposta.lower() == 's':
		cod_area_desejado = int(input('Para qual area? '))

		print('Exibindo pessoas registradas \n')

		for pessoa in registro:
			if pessoa['cod_area'] == cod_area_desejado:
				print(f"nome: {pessoa['nome']}")
				print(f"idade: {pessoa['idade']}")
				print('----------\n')

if __name__ == '__main__':
	main()
