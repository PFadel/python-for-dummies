# uma função é um bloco de código que pode ser executado várias vezes apenas chamando pelo seu nome
def soma(a, b):
	resultado = a + b
	return resultado

# ela tem argumentos e retorna alguma informação
def subtrai(a, b):
	resultado = a - b
	return resultado

# podemos converter o input de texto para uma variávei inteira chamando 'int'
a = int(input("Entre com o primeiro número:"))

# se o input não for um número inteiro, isso vai dar erro
b = int(input("Entre com o segundo número:"))

resultado = soma(a, b)
print(f"A soma de {a} e {b} é {resultado}")

# repetindo nomes de variáveis aqui fazem elas terem seus valores sobreescritos
a = int(input("Entre com o primeiro número:"))

b = int(input("Entre com o segundo número:"))

resultado = subtrai(a, b)
print(f"A subtração de {a} e {b} é {resultado}")