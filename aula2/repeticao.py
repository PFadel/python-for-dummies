# existem dois tipos de estruturas de repetição

# a primeira é o 'for'
# usamos 'for' para uma quantidade *conhecida* de repetições

# neste exemplo, repetimos de 0 a 9, 10 NÃO é exibido
# começamos do 0 e vamos até 10-1, incrementando i de 1 em 1
for i in range(0, 10):  # a variável 'i' só existe dentro do 'for'
	print(f"Neste momento a variável 'i' vale: {i}")

# ATENÇÃO NA IDENTAÇÃO ( espaço em branco nas linhas após o 'for' ) pois define o que será executado

print('')

# se desejar fazer de forma regressiva, podemos fazer da forma abaixo, neste exemplo o 0 NÃO é exibido
# começamos do 10 e vamos até 0+1, decrementando i de 1 em 1
for i in range(10, 0, -1):
	print(f"Neste momento a variável 'i' vale: {i}")

# a segunda estrutura de repetição é o 'while'
# usamos 'while' para uma quantidade *desconhecida* de repetições

# nesse exemplo, pedimos para o usuário entrar com uma senha até que seja a correta
senha = ''
while senha != 'Th14g0_L0r3n4':
	senha = input("Entre com a senha:")
print("Senha correta!")
# ATENÇÃO NA IDENTAÇÃO


# diferente do 'for', a condição do 'while' é um 'bool'
# o exemplo acima poderia ser reescrito assim:

# nesse exemplo usamos um 'if' dentro do 'while', respeitando a identação de cada um deles
senha = 'Th14g0_L0r3n4'
senha_correta = False
while senha_correta is False:
	senha_input = input("Entre com a senha:")
	if senha_input == senha:
		senha_correta = True
print("Senha correta!")
