# TESTE DE NÚMERO PRIMO
def verificar_numero_primo(numero: int):
    # Se o número for negativo ou nulo, retornará a mensagem
    if numero <= 0:
        return "Válido somente números inteiros positivos e não nulos"
    
    # Se o número for 2, o único primo que é par, então retornará que é primo e encerra a função
    if numero == 2:
        return f"{numero} é primo!"

    # Se o número for maior que 2, a função irá verificar se o número é par ou não
    if numero > 2:
        # Caso seja par, retorna imediatamente que não é primo.
        if numero % 2 == 0:
            return f"{numero} não é primo!"
        else: # Caso contrário então verificamos se existe algum número impar no intervalo de [3, (numero/2) + 1] que divide o número inserido
            for i in range(3, int(1 + numero/2), 2):
                # Se existir, retornamos que não é primo e encerramos o loop
                if numero % i == 0:
                    return f"{numero} não é primo"
                    break
            # Se depois do loop não existir nenhum número no intervalo que divida o número inserido, então o número é primo
            return f"{numero} é primo!"
    else: # Caso o número inserido seja 1 ou qualquer outro número menor que dois, então ele não é primo
        return f"{numero} não é primo"

numero_input = int(input("Digite um número inteiro positivo e não nulo: "))
print(verificar_numero_primo(numero_input))

# TESTES REALIZADOS
'''
print(verificar_numero_primo(31))
print(verificar_numero_primo(100))
print(verificar_numero_primo(4))
print(verificar_numero_primo(23))
print(verificar_numero_primo(53))
print(verificar_numero_primo(51))
'''

