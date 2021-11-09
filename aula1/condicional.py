idade_fadel = 27
altura_fadel = 1.68

ja_teve_cabelo_azul = True
tem_casa_propria = False

altura_thiago = 1.85
idade_thiago = 27
idade_lorena = 27
altura_lorena = 1.55

# 'if' recebe uma condição, se for verdade, executa o que estiver 'dentro' do 'if'
if altura_fadel > altura_lorena:
	print("O Fadel é mais alto que a Lorena")

# todo 'if' pode ter um 'else' que é executado caso a condição do 'if' não seja verdadeira
if altura_fadel > altura_thiago:
	print("O Fadel é mais alto que o Thiago")
else:
	print("O Thiago é mais alto que o Fadel")

# é possível usar uma variável 'boolean' na condição do 'if'
if ja_teve_cabelo_azul is True:
	print("O Fadel já teve cabelo azul")
else:
	print("O Fadel não teve cabelo azul")

# é possível negar uma condição usando o operador 'not'
if tem_casa_propria is not True:
	print("O Fadel ainda nao tem uma casa própria")
else:
	print("O Fadel tem uma casa própria")

# no caso de teste de igualdade, sempre usamos dois sinais de iguais '=='
if idade_fadel == idade_thiago:
	print("O Fadel e o Thiago tem a mesma idade")
else:
	print("O Fadel e o Thiago não tem a mesma idade")

# é possível usar '>=' para maior ou igual, e '<=' para menor ou igual
if idade_fadel >= idade_lorena:
	print("A idade do Fadel é maior ou igual à idade da Lorena")
else:
	print("A idade do Fadel é menor que a idade da Lorena")
