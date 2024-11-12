def converter_cpf(cpf):
   
    return [int(digito) for digito in cpf if digito.isdigit()]

def validar_tamanho(cpf_numeros):
 
    return len(cpf_numeros) == 11

def negar_numeros_iguais(cpf_numeros):
    
    return all(digito == cpf_numeros[0] for digito in cpf_numeros)

def calcular_primeiro_digito(cpf_numeros):
 
    soma = sum(cpf_numeros[i] * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    return digito1 == cpf_numeros[9]

def calcular_segundo_digito(cpf_numeros):
    
    soma = sum(cpf_numeros[i] * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    return digito2 == cpf_numeros[10]


cpf = input("Informe seu CPF: ").replace('.', '').replace('-', '')
cpf_numeros = converter_cpf(cpf)

if not validar_tamanho(cpf_numeros):
    print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
elif negar_numeros_iguais(cpf_numeros):
    print("CPF inválido. Não pode conter todos os números iguais.")
elif calcular_primeiro_digito(cpf_numeros) and calcular_segundo_digito(cpf_numeros):
    print("CPF é válido")
else:
    print("CPF é inválido")
