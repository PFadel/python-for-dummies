# listas de variáveis de texto
alunos = ["lorena", "thiago"]
# listas de variáveis inteiras
numeros_primos = [2, 3, 5, 7, 11]
# listas podem ter variáveis de vários tipos misturados (não recomendado)
lista_mista = ["banana", 42, False, 3.14]

# por causa do erro de 'index out of range' é perigoso acessar listas pelo índice diretamente
# ao invés disso, podemos passar ( ou iterar ) sobre as listas usando a estrutura de repetição 'for'
# existem diferentes formas de se fazer isso

# a mais simples:
for i in range(0, len(alunos)):  # nesse exemplo len(alunos) = 2
	print(alunos[i]) # a primeira vez que o loop passar aqui exibirá 'lorena', e depois 'thiago'

# a mais 'elegante(?)', costuma ser mais eficiente também:
for aluno in alunos: # nesse exemplo, se cria uma variável 'aluno' que só existe dentro do 'for'
	print(aluno)


# é possível iterar na lista com 'while', mas normalmente não é muito prático
i = 0
while i < len(alunos):
	print(alunos[i])
	i += 1  # quando se coloca += significa que estamos pegando o valor antigo da variável e acrescentando algum valor