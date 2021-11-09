# as variáveis de texto possuem um pouco mais de funcionalidade do que mostramos na última aula

nome = "Pedro Fadel"

# na verdade, toda variável de texto é também uma lista, com cada elemento sendo um caracter, ou uma letra
# sendo assim, podemos acessar os índices específicos como podemos numa lista

print(nome[0]) # P
print(nome[1]) # e
print(nome[2]) # d
print(nome[3]) # r
print(nome[4]) # o
print(nome[5]) # ' '

# podemos iterar sobre ela em loops assim como em listas
for letra in nome:
	print(letra)

# a função 'len' retorna o tamanho da variável de texto
print(len(nome))  # 11

# além disso, a string ( variável de texto ) em si possui diversas funções internas do python que podem ser chamadas

# a função 'split' separa a variável dado um caracter, criando uma lista com um elemento para cada parte
print(nome.split(' '))  # ["Pedro", "Fadel"]
nome = "Thiago Alves De Souza"
print(nome.split(' '))  # ["Thiago", "Alves", "De", "Souza"]

# caso o caracter do split não exista, a lista criada possui um só elemento, que é a variável completa
print(nome.split('W'))  # ["Pedro Fadel"]


# a função 'find' retorna o índice da primeira ocorrência dado um caracter
print(nome.find('F'))  # 6

# caso o caracter não exista, é retornado -1
print(nome.find('W'))  # -1


# a função 'replace' substitui caracteres da variável por outro
print(nome.replace('e', 'j'))  # Pjdro Fadjl

