def calcular_quadrado(numero):
    resultados = []
    potencia = 1
    while 16 ** potencia < numero:
        valor = 16 ** potencia
        resultados.append(valor)
        potencia += 1
    return resultados

# Obter o número escolhido pelo usuário
numero_escolhido = float(input("Digite um número: "))

# Chamar a função para calcular o quadrado para várias potências e exibir os resultados
resultados = calcular_quadrado(numero_escolhido)

for potencia, resultado in enumerate(resultados, start=1):
    print(f"O número {numero_escolhido} elevado a {potencia}ª potência é {resultado}")
    #resutado = numero_escolhido * 