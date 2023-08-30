# Esta função receberá um número inteiro como input e retornará uma lista de divisores desse número
def get_divisores(numero: int):
    divisores = []
    
    if numero == 0:
        divisores.append("Todos os números inteiros exceto 0")
    
    if numero == 1:
        divisores.append(1)
    
    if numero > 1:
        i = 1
        while i < numero + 1:
            if numero % i == 0:
                divisores.append(i)
            i += 1
    
    return divisores

# TESTES REALIZADOS
'''
print(get_divisores(2))
print(get_divisores(1))
print(get_divisores(0))
print(get_divisores(78))
'''

# Outra maneira de verificar números primos:
# Números primos são diferentes de 1 e divisíveis apenas por 1 e ele mesmo
# A função abaixo recebe um número inteiro como input e verifica o tamanho da lista de divisores desse número.
# Caso o tamanho da lista de divisores seja 2, então o número é primo, caso contrário, o número não é primo.
def verificar_primo(numero):
    lista_de_divisores = get_divisores(numero)
    print("-"*50)
    if len(lista_de_divisores) == 2:
        print(f"{numero} é primo\nSeus divisores são: {lista_de_divisores}")
    else:
        print(f"{numero} é não é primo\nSeus divisores são: {lista_de_divisores}")
    print("-"*50)

# TESTES REALIZADOS
'''
verificar_primo(30)
verificar_primo(101)
verificar_primo(23)
verificar_primo(64)
verificar_primo(33)
verificar_primo(94)
verificar_primo(0)
verificar_primo(1)
'''

# Função principal
def main():
    print("-=VERIFICADOR DE NÚMERO PRIMO=-")
    numero = int(input("Digite um número inteiro: "))
    verificar_primo(numero)

if __name__ == "__main__":
    main()
