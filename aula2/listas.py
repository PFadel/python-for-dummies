# listas de variáveis de texto
alunos = ["lorena", "thiago"]
# listas de variáveis inteiras
numeros_primos = [2, 3, 5, 7, 11]
# listas podem ter variáveis de vários tipos misturados (não recomendado)
lista_mista = ["banana", 42, False, 3.14]

# podemos acessar o elemento na lista usando '[i]'' onde 'i' é o índice da lista
# toda lista começa com índice no 0

print(alunos[0]) # lorena
print(alunos[1]) # thiago

print(numeros_primos[0]) # 2
print(numeros_primos[1]) # 3
print(numeros_primos[2]) # 5
print(numeros_primos[3]) # 7
print(numeros_primos[4]) # 11

print(lista_mista[0]) # banana
print(lista_mista[1]) # 42
print(lista_mista[2]) # False
print(lista_mista[3]) # 3.14

# se tentarmos acessar um índice que não existe na lista, vamos receber um erro do python
# o erro é 'list index out of range', que significa que essa lista não possui esse índice
# -> print(alunos[2])

# depois que uma lista é definida, podemos adicionar elementos nela usando a função 'append' 
alunos.append("Luma")  # queria ):
print(alunos)  # ["lorena", "thiago", "Luma"]

# para remover elementos, existem duas formas

# removendo pelo elemento diretamente
# caso o elemento não exista na lista, será retornado um erro do Python 'list.remove(x): x not in list'
alunos.remove("Luma")  # </3
print(alunos)  # ["lorena", "thiago"]

# removendo pelo índice do elemento
# caso o índice não exista na lista, será retornado um erro do Python 'pop index out of range'
alunos.pop(1)

# podemos também verificar se um elemento existe em uma lista
if "lorena" in alunos:
	print("Lorena está aprendendo Python!")

# existe uma função básica do python que te retorna o tamanho da lista
# você chama ela escrenvendo 'len(<lista>)'
print(len(alunos)) # 2
print(len(numeros_primos)) # 5
print(len(lista_mista)) # 4

# podemos usar uma variável como uma cópia da variável da lista sem alterá-la, exemplo:
melhor_aluno = alunos[0]
print(f"O melhor aluno da turma é {melhor_aluno}")

melhor_aluno = "Luma"
print(f"Na verdade o melhor aluno da turma é {melhor_aluno}")

# se acessarmos a lista vamos ver que a variável no índice não foi alterada
print(alunos[0]) # lorena
