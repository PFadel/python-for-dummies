nome = "Pedro"
sobrenome = "Fadel"
idade = 27
altura = 1.68

# subtração e soma de variáveis inteiras
idade_luma = idade - 2
idade_bernardo = idade_luma + 3

print(f"A Luma tem {idade_luma} anos e o irmão dela tem {idade_bernardo} anos")

# um sinal de divisão faz uma divisão exata, resultando num número real
idade_quebrada_duzias = idade / 12

# dois sinais de divisão fazem uma divisão inteira, resultando num número inteiro e um resto
idade_duzias = idade // 12
# o resto da divisão é conseguido usando o operador '%'
resto_idade_duzias = idade % 12

print(f"O Pedro tem {idade_quebrada_duzias} dúzias de idade, ou seja, {idade_duzias} dúzias e {resto_idade_duzias} anos de idade")

# multiplicação de variáveis inteiras
idade_em_meses = idade * 12

print(f"Meu nome é {nome}, tenho {idade_em_meses} meses de idade e {altura} de altura")

# potência
dois_ao_quadrado = pow(2, 2) # 2 elevado à 2
tres_ao_quadrado = pow(3, 2) # 3 elevado à 2
dois_ao_cubo = pow(2, 3) # 2 elevado à 3
tres_ao_cubo = pow(3, 3) # 3 elevado à 3

print(f"Dois ao quadrado é {dois_ao_quadrado}")
print(f"Três ao quadrado é {tres_ao_quadrado}")
print(f"Dois ao cubo é {dois_ao_cubo}")
print(f"Três ao cubo é {tres_ao_cubo}")

#
# Raiz quadrada é mais complicado pra explicar como fazer então fica pra próxima aula (:
#

# multiplicação de variáveis reais
altura_em_cm = altura * 100

print(f"Meu nome é {nome}, tenho {idade_em_meses} meses de idade e {altura_em_cm} centímetros de altura")

# soma de texto ? junta um texto no outro
nome_inteiro = nome + " " + sobrenome

print(f"Meu nome inteiro é {nome_inteiro}, tenho {idade} anos e {altura} de altura")
